# Traditional Divination Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bootstrap the user's GitHub repository, build and validate a source-audited first version of `traditional-divination-skill`, install it into Codex, and teach the Git workflow through small commits.

**Architecture:** The public GitHub repository is the editable source of truth. `traditional-divination-skill` handles natural-language routing, question normalization, reproducible coin casting, and deterministic base/changing hexagram calculation. Cangjie artifacts for 《增删卜易》 remain under `books/` and compile into a narrowly described companion source skill; both validated skills are installed in `D:\Codex\skills`, while generic “算命” prompts route through the primary skill.

**Tech Stack:** Git/GitHub, Python 3.11 standard library, `unittest`, Agent Skills `SKILL.md`, `agents/openai.yaml`, Cangjie Skill v2.5.

## Global Constraints

- Remote repository: `https://github.com/Lin712-311/personal-wisdom-skills-lbw.git`.
- Local repository: `C:\Users\19364\Documents\Codex\personal-wisdom-skills-lbw`.
- Installed skill: `D:\Codex\skills\traditional-divination-skill`.
- Installed source companion: `D:\Codex\skills\zengshan-buyi-skill`.
- Version 1 uses only 《增删卜易》 as its book-derived interpretation source.
- User confirmation is required after Cangjie Stage 0, Stage 1.5, and before the final compile mode.
- Version 1 computes original hexagram, moving lines, and changed hexagram; it does not claim complete 纳甲、月建、日辰、旬空、六神 or 应期 calculation.
- Personal birth data, question histories, paid books, `.env` files, tokens, and private chats must never be committed.
- Fortune-telling output is traditional cultural interpretation, not scientific prediction, medical diagnosis, legal advice, or an investment guarantee.

---

### Task 1: Bootstrap the Empty GitHub Repository

**Files:**
- Create: `README.md`
- Create: `.gitignore`
- Create: `docs/designs/2026-09-16-traditional-divination-skill-design.md`
- Create: `docs/superpowers/plans/2026-09-16-traditional-divination-skill.md`

**Interfaces:**
- Consumes: empty public repository at the configured remote URL.
- Produces: a `main` branch with a safe project skeleton and an `origin` remote.

- [ ] **Step 1: Clone the empty repository using an explicit local directory**

```powershell
git clone https://github.com/Lin712-311/personal-wisdom-skills-lbw.git C:\Users\19364\Documents\Codex\personal-wisdom-skills-lbw
Set-Location C:\Users\19364\Documents\Codex\personal-wisdom-skills-lbw
```

Expected: Git warns that the repository is empty; the local directory contains `.git`.

- [ ] **Step 2: Create the initial project documentation**

`README.md` must contain:

```markdown
# Personal Wisdom Skills

个人可调用知识与传统文化 Skills 仓库。第一阶段构建一个以《增删卜易》为来源、能够自动触发的六爻占问 Skill。

## Repository layout

- `books/` — Cangjie source audits and capability bundles
- `skills/` — installable Agent Skills
- `tests/` — repository-level tests
- `docs/` — designs, plans, and learning notes

## Safety

Do not commit personal birth data, private questions, API keys, paid ebooks, or chat exports. Traditional divination is presented as cultural interpretation and reflection, not scientific prediction.
```

`.gitignore` must contain:

```gitignore
.env
.env.*
*.key
*.pem
__pycache__/
*.py[cod]
.venv/
venv/
.pytest_cache/
cache/
private/
personal-data/
question-history/
*.log
dist/
```

Copy the approved design and this plan into the exact documentation paths listed above.

- [ ] **Step 3: Verify repository state**

Run:

```powershell
git status --short
git remote -v
git config user.name
git config user.email
```

Expected: four new files; `origin` points to `Lin712-311/personal-wisdom-skills-lbw`; author name and email are nonempty. If either identity value is missing, stop and ask the user which GitHub name/email to configure for this repository—never invent an email.

- [ ] **Step 4: Create and push the initial commit**

```powershell
git add README.md .gitignore docs
git commit -m "chore: initialize personal wisdom skills repository"
git branch -M main
git push -u origin main
```

Expected: GitHub displays the README and `main` becomes the default branch.

- [ ] **Step 5: Create the feature branch**

```powershell
git switch -c feature/traditional-divination-v1
```

Expected: current branch is `feature/traditional-divination-v1`.

---

### Task 2: Add a Reproducible Public-Domain Source Fetcher

**Files:**
- Create: `scripts/__init__.py`
- Create: `scripts/fetch_wikisource.py`
- Create: `tests/test_fetch_wikisource.py`
- Create at runtime: `books/zengshan-buyi/source/raw-wikitext.txt`
- Create at runtime: `books/zengshan-buyi/source/source-manifest.json`

**Interfaces:**
- Consumes: MediaWiki API base URL, main title `增刪卜易`, and subpage prefix `增刪卜易/`.
- Produces: `fetch_book(api_base: str, title: str, output_dir: Path) -> dict[str, object]` and a SHA-256 source manifest.

- [ ] **Step 1: Write failing unit tests with mocked HTTP responses**

```python
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.fetch_wikisource import fetch_book, sha256_text


class FetchWikisourceTests(unittest.TestCase):
    def test_sha256_is_stable(self):
        self.assertEqual(
            sha256_text("abc"),
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        )

    @patch("scripts.fetch_wikisource.api_json")
    def test_fetch_book_orders_main_page_before_subpages(self, api_json):
        api_json.side_effect = [
            {"query": {"allpages": [{"title": "增刪卜易/2"}, {"title": "增刪卜易/1"}]}},
            {"parse": {"wikitext": {"*": "MAIN"}}},
            {"parse": {"wikitext": {"*": "ONE"}}},
            {"parse": {"wikitext": {"*": "TWO"}}},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            manifest = fetch_book("https://example.invalid/w/api.php", "增刪卜易", Path(tmp))
            text = (Path(tmp) / "raw-wikitext.txt").read_text(encoding="utf-8")
            self.assertLess(text.index("MAIN"), text.index("ONE"))
            self.assertLess(text.index("ONE"), text.index("TWO"))
            self.assertEqual(manifest["page_count"], 3)
            self.assertEqual(json.loads((Path(tmp) / "source-manifest.json").read_text(encoding="utf-8"))["sha256"], manifest["sha256"])
```

- [ ] **Step 2: Run the test to verify it fails**

Run:

```powershell
python -m unittest tests.test_fetch_wikisource -v
```

Expected: FAIL because `scripts.fetch_wikisource` does not exist.

- [ ] **Step 3: Implement the minimal fetcher**

```python
from __future__ import annotations

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def api_json(api_base: str, params: dict[str, str]) -> dict[str, Any]:
    url = f"{api_base}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "personal-wisdom-skills/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fetch_book(api_base: str, title: str, output_dir: Path) -> dict[str, object]:
    listing = api_json(api_base, {
        "action": "query", "list": "allpages", "apprefix": f"{title}/",
        "apnamespace": "0", "aplimit": "max", "format": "json",
    })
    pages = [title] + sorted(item["title"] for item in listing["query"]["allpages"])
    sections: list[str] = []
    for page in pages:
        parsed = api_json(api_base, {
            "action": "parse", "page": page, "prop": "wikitext", "format": "json",
        })
        sections.append(f"\n===== {page} =====\n{parsed['parse']['wikitext']['*'].strip()}\n")
    combined = "".join(sections)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "raw-wikitext.txt").write_text(combined, encoding="utf-8", newline="\n")
    manifest: dict[str, object] = {
        "title": title,
        "source_url": "https://zh.wikisource.org/wiki/增刪卜易",
        "api_base": api_base,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "page_count": len(pages),
        "pages": pages,
        "sha256": sha256_text(combined),
    }
    (output_dir / "source-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(fetch_book("https://zh.wikisource.org/w/api.php", "增刪卜易", args.output), ensure_ascii=False, indent=2))
```

- [ ] **Step 4: Run unit tests and fetch the real source**

```powershell
python -m unittest tests.test_fetch_wikisource -v
python scripts/fetch_wikisource.py --output books/zengshan-buyi/source
```

Expected: tests PASS; manifest has a nonzero `page_count` and a 64-character SHA-256.

- [ ] **Step 5: Commit source tooling and the public-domain snapshot**

```powershell
git add scripts/__init__.py scripts/fetch_wikisource.py tests/test_fetch_wikisource.py books/zengshan-buyi/source
git commit -m "feat: add auditable Zengshan Buyi source snapshot"
```

---

### Task 3: Complete Cangjie Stage 0 and Stop for the Required User Review

**Files:**
- Create: `books/zengshan-buyi/PIPELINE_STATE.md`
- Create: `books/zengshan-buyi/BOOK_OVERVIEW.md`

**Interfaces:**
- Consumes: `books/zengshan-buyi/source/raw-wikitext.txt` and `source-manifest.json`.
- Produces: Adler structural, interpretive, critical, and applicability analysis plus a source-located key-task table.

- [ ] **Step 1: Read the entire source in bounded chunks**

Use chapter markers (`===== title =====`) as chunk boundaries. Record every processed page title in `PIPELINE_STATE.md`; do not claim whole-book coverage until all manifest pages are accounted for.

- [ ] **Step 2: Write `BOOK_OVERVIEW.md` using the Cangjie template**

The document must include:

```markdown
# 《增删卜易》整书理解

## 元信息与版本
## 一句话主旨
## 3–7 个一级结构及其关系
## 原书术语及原文位置
## 核心命题与论证方式
## 时代局限、未证明假设与最强反对意见
## 可执行能力候选与不适合 Skill 化的内容
## 原书关键任务清单
```

Every key-task row must contain `task_id`, task, source page/section, expected output, importance, and rationale.

- [ ] **Step 3: Record the Stage 0 checkpoint**

`PIPELINE_STATE.md` must state that Stage 0 is complete but unapproved, and that Stage 1 is prohibited until the user confirms the displayed skeleton.

- [ ] **Step 4: Run the Stage 0 quality scan**

```powershell
rg -n "一句话主旨|一级结构|关键术语|时代局限|未证明|关键任务" books/zengshan-buyi/BOOK_OVERVIEW.md
rg -n "待确认|Stage 1" books/zengshan-buyi/PIPELINE_STATE.md
```

Expected: every required section is present; status is explicitly awaiting user confirmation.

- [ ] **Step 5: Commit and present the checkpoint**

```powershell
git add books/zengshan-buyi/BOOK_OVERVIEW.md books/zengshan-buyi/PIPELINE_STATE.md
git commit -m "docs: complete Zengshan Buyi stage zero analysis"
git push -u origin feature/traditional-divination-v1
```

Stop implementation and ask the user to approve or correct the book skeleton.

---

### Task 4: Build the Deterministic Hexagram Engine with TDD

**Files:**
- Create: `skills/traditional-divination-skill/scripts/hexagrams.py`
- Create: `skills/traditional-divination-skill/scripts/cast_coins.py`
- Create: `skills/traditional-divination-skill/scripts/derive_hexagram.py`
- Create: `tests/test_hexagrams.py`

**Interfaces:**
- Consumes: six integers in `{6, 7, 8, 9}`, ordered bottom line to top line.
- Produces: `derive(values: list[int]) -> dict[str, object]` with original, moving-line, and changed-hexagram data.

- [ ] **Step 1: Write failing engine tests**

```python
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "skills" / "traditional-divination-skill" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from hexagrams import derive


class HexagramTests(unittest.TestCase):
    def test_all_young_yang_is_qian_without_change(self):
        result = derive([7, 7, 7, 7, 7, 7])
        self.assertEqual(result["original"]["number"], 1)
        self.assertEqual(result["changed"]["number"], 1)
        self.assertEqual(result["moving_lines"], [])

    def test_all_old_yin_changes_kun_to_qian(self):
        result = derive([6, 6, 6, 6, 6, 6])
        self.assertEqual(result["original"]["number"], 2)
        self.assertEqual(result["changed"]["number"], 1)
        self.assertEqual(result["moving_lines"], [1, 2, 3, 4, 5, 6])

    def test_bottom_yang_rest_yin_is_returning(self):
        self.assertEqual(derive([7, 8, 8, 8, 8, 8])["original"]["number"], 24)

    def test_rejects_wrong_length(self):
        with self.assertRaisesRegex(ValueError, "exactly six"):
            derive([7, 8])

    def test_rejects_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "6, 7, 8, or 9"):
            derive([7, 7, 7, 7, 7, 5])
```

- [ ] **Step 2: Run tests to verify failure**

```powershell
python -m unittest tests.test_hexagrams -v
```

Expected: FAIL because the engine does not exist.

- [ ] **Step 3: Implement trigram and King Wen lookup data**

Use bottom-to-top bit strings:

```python
TRIGRAMS = {
    "111": "乾", "110": "兑", "101": "离", "100": "震",
    "011": "巽", "010": "坎", "001": "艮", "000": "坤",
}

KING_WEN = {
    "乾": {"乾": 1, "兑": 10, "离": 13, "震": 25, "巽": 44, "坎": 6, "艮": 33, "坤": 12},
    "兑": {"乾": 43, "兑": 58, "离": 49, "震": 17, "巽": 28, "坎": 47, "艮": 31, "坤": 45},
    "离": {"乾": 14, "兑": 38, "离": 30, "震": 21, "巽": 50, "坎": 64, "艮": 56, "坤": 35},
    "震": {"乾": 34, "兑": 54, "离": 55, "震": 51, "巽": 32, "坎": 40, "艮": 62, "坤": 16},
    "巽": {"乾": 9, "兑": 61, "离": 37, "震": 42, "巽": 57, "坎": 59, "艮": 53, "坤": 20},
    "坎": {"乾": 5, "兑": 60, "离": 63, "震": 3, "巽": 48, "坎": 29, "艮": 39, "坤": 8},
    "艮": {"乾": 26, "兑": 41, "离": 22, "震": 27, "巽": 18, "坎": 4, "艮": 52, "坤": 23},
    "坤": {"乾": 11, "兑": 19, "离": 36, "震": 24, "巽": 46, "坎": 7, "艮": 15, "坤": 2},
}

HEXAGRAM_NAMES = {
    1: "乾", 2: "坤", 3: "屯", 4: "蒙", 5: "需", 6: "讼", 7: "师", 8: "比",
    9: "小畜", 10: "履", 11: "泰", 12: "否", 13: "同人", 14: "大有", 15: "谦", 16: "豫",
    17: "随", 18: "蛊", 19: "临", 20: "观", 21: "噬嗑", 22: "贲", 23: "剥", 24: "复",
    25: "无妄", 26: "大畜", 27: "颐", 28: "大过", 29: "坎", 30: "离", 31: "咸", 32: "恒",
    33: "遁", 34: "大壮", 35: "晋", 36: "明夷", 37: "家人", 38: "睽", 39: "蹇", 40: "解",
    41: "损", 42: "益", 43: "夬", 44: "姤", 45: "萃", 46: "升", 47: "困", 48: "井",
    49: "革", 50: "鼎", 51: "震", 52: "艮", 53: "渐", 54: "归妹", 55: "丰", 56: "旅",
    57: "巽", 58: "兑", 59: "涣", 60: "节", 61: "中孚", 62: "小过", 63: "既济", 64: "未济",
}
```

The first dictionary key in `KING_WEN` is the upper trigram; the nested key is the lower trigram.

- [ ] **Step 4: Implement `derive` and CLI JSON output**

Line conversion is fixed:

```python
ORIGINAL_BIT = {6: 0, 7: 1, 8: 0, 9: 1}
CHANGED_BIT = {6: 1, 7: 1, 8: 0, 9: 0}
```

`derive_hexagram.py` must parse six positional integers and print UTF-8 JSON with `ensure_ascii=False`.

- [ ] **Step 5: Implement one-shot secure coin casting**

`cast_coins.py` must use `secrets.randbelow(2)` for 18 independent coin results, encode heads as 3 and tails as 2, and print all raw coins plus six line totals. It must cast exactly once per process invocation and never retry based on interpretation.

- [ ] **Step 6: Run tests and manual examples**

```powershell
python -m unittest tests.test_hexagrams -v
python skills/traditional-divination-skill/scripts/derive_hexagram.py 7 7 7 7 7 7
python skills/traditional-divination-skill/scripts/cast_coins.py
```

Expected: tests PASS; first CLI result is hexagram 1 with no moving lines; cast output contains six lines and 18 recorded coins.

- [ ] **Step 7: Commit the deterministic engine**

```powershell
git add skills/traditional-divination-skill/scripts tests/test_hexagrams.py
git commit -m "feat: add reproducible hexagram calculation"
```

---

### Task 5: Complete Cangjie Stages 1–4 After Stage 0 Approval

**Files:**
- Create: `books/zengshan-buyi/candidates/*.md`
- Create: `books/zengshan-buyi/verified.md`
- Create: `books/zengshan-buyi/coverage-audit.md`
- Create: `books/zengshan-buyi/references.md`
- Create: `books/zengshan-buyi/needs-review.md`
- Create: `books/zengshan-buyi/rejected/*.md`
- Create: `books/zengshan-buyi/GLOSSARY.md`
- Create: `books/zengshan-buyi/.cangjie/capabilities/verified.yaml`
- Create: `books/zengshan-buyi/.cangjie/capabilities/cards/*.md`
- Create: `books/zengshan-buyi/.cangjie/capabilities/destinations.json`

**Interfaces:**
- Consumes: user-approved Stage 0 overview and complete source snapshot.
- Produces: a validated Capability Bundle with source-located, executable, bounded capabilities.

- [ ] **Step 1: Run five independent extraction roles**

Use the exact Cangjie prompts for framework, principle, case, counter-example, and glossary extraction. With four total agent slots, run them in two waves while preserving independent outputs. Do not allow one extractor to rewrite another's file.

- [ ] **Step 2: Perform triple verification**

For every candidate, record V1 source sufficiency, V2 executability, and V3 task gain. Route each item to exactly one of `verified`, `reference`, `needs_review`, or `rejected`. Update `coverage-audit.md` against the independent Stage 0 key-task list.

- [ ] **Step 3: Stop for the required Stage 1.5 user confirmation**

Present the four routing groups and every important coverage gap. Do not create active capability cards until the user confirms.

- [ ] **Step 4: Apply the promotion gate and write RIA++ cards**

Each active card must have R, I, A1, A2, E, and B sections; every original quotation must stay within the Cangjie quotation limit. Synthetic exercises must be labeled as synthetic.

- [ ] **Step 5: Test trigger, router reachability, and representative outputs**

Record actual answer outputs rather than only prompt lists. Fail any capability that invents missing calendrical data, produces a bare good/bad verdict, or makes scientific certainty claims.

- [ ] **Step 6: Commit the bundle and audit trail**

Before committing, preview the compiler's single-first recommendation:

```powershell
python D:\Codex\skills\cangjie-skill\scripts\cangjie.py compile `
  --bundle books\zengshan-buyi\.cangjie\capabilities `
  --out dist\zengshan-buyi-skill `
  --output auto `
  --purpose workflow
```

Show the decision report to the user. After the user confirms the recommended mode, compile with `--yes`. The bundle entry name must be `zengshan-buyi-skill`, and its description must target book-specific/source-method questions rather than generic “算命” prompts, preventing competition with the primary skill.

```powershell
python D:\Codex\skills\cangjie-skill\scripts\cangjie.py compile `
  --bundle books\zengshan-buyi\.cangjie\capabilities `
  --out dist\zengshan-buyi-skill `
  --output auto `
  --purpose workflow `
  --yes
```

Then commit the Bundle and audit trail; `dist/` remains ignored because it is reproducible build output.

```powershell
git add books/zengshan-buyi
git commit -m "feat: distill validated Zengshan Buyi capabilities"
```

---

### Task 6: Build the Installable Skill Entry Point

**Files:**
- Create: `skills/traditional-divination-skill/SKILL.md`
- Create: `skills/traditional-divination-skill/agents/openai.yaml`
- Create: `skills/traditional-divination-skill/references/interaction-flow.md`
- Create: `skills/traditional-divination-skill/references/interpretation-format.md`
- Create: `skills/traditional-divination-skill/references/safety-and-uncertainty.md`
- Create: `skills/traditional-divination-skill/references/source-audit.md`
- Create: `skills/traditional-divination-skill/evals/traditional-divination.eval.md`

**Interfaces:**
- Consumes: deterministic engine plus validated Cangjie capability bundle.
- Produces: a discoverable Agent Skill with implicit invocation enabled.

- [ ] **Step 1: Complete the skill directory created by the tested scripts**

```powershell
New-Item -ItemType Directory -Force skills\traditional-divination-skill\references | Out-Null
New-Item -ItemType Directory -Force skills\traditional-divination-skill\assets | Out-Null
New-Item -ItemType Directory -Force skills\traditional-divination-skill\evals | Out-Null
```

Do not run `init_skill.py` here: Task 4 already created the directory and tested scripts, and the initializer must not overwrite them. Create and edit files with `apply_patch`.

- [ ] **Step 2: Write discriminating SKILL.md frontmatter**

```yaml
---
name: traditional-divination-skill
description: >-
  使用可复核的六爻起卦结果和《增删卜易》来源边界处理传统占问。用户说算命、起卦、六爻、问感情事业考试，或提供六次硬币结果时使用。仅解释《周易》文本、请求八字紫微、咨询医疗法律、要求投资保证或普通随机数时不要使用。
---
```

The body must route through: question normalization → user-cast or explicitly authorized random cast → deterministic script → source-bounded interpretation → practical action → uncertainty and high-risk boundary.

- [ ] **Step 3: Generate `agents/openai.yaml`**

```powershell
python D:\Codex\skills\.system\skill-creator\scripts\generate_openai_yaml.py skills/traditional-divination-skill `
  --interface display_name="传统六爻顾问" `
  --interface short_description="自然语言起卦、复核卦象并给出有边界的传统解释" `
  --interface default_prompt='使用 $traditional-divination-skill 帮我把一个具体问题整理后起卦分析。'
```

Verify that `policy.allow_implicit_invocation` is `true`.

- [ ] **Step 4: Write references and eval cases**

The references must contain the stable output contract, privacy rules, retry prohibition, source manifest hash, and explicit limits of Version 1. Eval cases must include at least:

- Trigger: “帮我算一下未来三个月的求职情况。”
- Trigger: “我摇出了 7 8 8 8 8 8，从下往上。”
- Do not trigger: “解释一下《周易》乾卦的文学含义。”
- Do not trigger: “我胸口疼，能不能起卦看看是不是心脏病？”
- Do not trigger: “根据我的生日排八字。”
- Failure case: five line values only.

- [ ] **Step 5: Commit the skill entry point**

```powershell
git add skills/traditional-divination-skill
git commit -m "feat: add implicitly invoked traditional divination skill"
```

---

### Task 7: Validate, Install, and Test Discovery

**Files:**
- Modify only if validation finds issues: `skills/traditional-divination-skill/**`
- Create at runtime: `D:\Codex\skills\traditional-divination-skill`
- Create at runtime: `D:\Codex\skills\zengshan-buyi-skill`

**Interfaces:**
- Consumes: complete skill source directory.
- Produces: validated installed skill and evidence of natural-language discoverability.

- [ ] **Step 1: Run all deterministic tests**

```powershell
python -m unittest discover -s tests -v
```

Expected: all tests PASS with zero errors and zero failures.

- [ ] **Step 2: Run skill validation**

```powershell
python D:\Codex\skills\.system\skill-creator\scripts\quick_validate.py skills/traditional-divination-skill
```

Expected: valid frontmatter, valid name, and no structural errors.

- [ ] **Step 3: Run the agent-skill security scan**

```powershell
python D:\Codex\skills\agent-skill-creator\scripts\security_scan.py skills/traditional-divination-skill
```

Expected: no hardcoded secrets, `.env`, prompt injection payloads, or unsafe shell construction.

- [ ] **Step 4: Install from the repository source**

Before replacing any existing path, verify the resolved source and destination. If the destination does not exist, copy the directory. If it exists, compare hashes and stop rather than silently overwrite user edits.

```powershell
Copy-Item -Recurse -LiteralPath skills\traditional-divination-skill -Destination D:\Codex\skills\traditional-divination-skill
Copy-Item -Recurse -LiteralPath dist\zengshan-buyi-skill -Destination D:\Codex\skills\zengshan-buyi-skill
```

- [ ] **Step 5: Verify the installed copy**

```powershell
python D:\Codex\skills\.system\skill-creator\scripts\quick_validate.py D:\Codex\skills\traditional-divination-skill
python D:\Codex\skills\cangjie-skill\scripts\validate_skill_pack.py D:\Codex\skills\zengshan-buyi-skill
Get-FileHash skills\traditional-divination-skill\SKILL.md, D:\Codex\skills\traditional-divination-skill\SKILL.md
```

Expected: validation passes and both hashes match.

- [ ] **Step 6: Verify natural-language behavior in a new Codex session**

Positive prompt: “帮我算一下最近的感情，我不懂六爻，你一步一步问我。”  
Expected: the skill asks for a specific question/time range and offers user-cast or authorized random casting.

Negative prompt: “帮我解释《周易》乾卦第一爻。”  
Expected: no automatic fortune-telling workflow.

---

### Task 8: Finish GitHub Integration and Learning Notes

**Files:**
- Create: `docs/github-learning-log.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: verified feature branch and installed artifact.
- Produces: reviewable Git history, a merged `main`, and a short bilingual Git learning record.

- [ ] **Step 1: Document the actual Git commands used**

`docs/github-learning-log.md` must explain `clone`, `status`, `add`, `commit`, `branch`, `merge`, `push`, `pull`, and `origin`, using the actual repository commands from this run.

- [ ] **Step 2: Update README with installation and invocation examples**

Include the installed path and an example natural-language request, but no personal question history.

- [ ] **Step 3: Commit and push the finished feature branch**

```powershell
git add README.md docs/github-learning-log.md
git commit -m "docs: add Git workflow and skill usage guide"
git push
```

- [ ] **Step 4: Review the feature diff before merge**

```powershell
git diff --stat main...feature/traditional-divination-v1
git log --oneline --decorate --graph --all
```

Expected: only project files, public-domain source material, tests, and documentation appear; no secrets or personal data.

- [ ] **Step 5: Merge and push main**

```powershell
git switch main
git merge --no-ff feature/traditional-divination-v1 -m "feat: release traditional divination skill v1"
git push origin main
```

- [ ] **Step 6: Final repository verification**

```powershell
git status --short
git log -5 --oneline
git remote -v
```

Expected: clean working tree, recent merge commit on `main`, and correct `origin` URLs.
