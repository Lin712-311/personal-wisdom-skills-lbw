# Project handoff — traditional divination v1

- **Handoff ID**: `TDV1-20260916-COMPLETE`
- **Updated**: 2026-09-17 (Australia/Sydney)
- **Repository**: `C:\Users\19364\Documents\Codex\personal-wisdom-skills-lbw` (local-only path)
- **Remote**: `https://github.com/Lin712-311/personal-wisdom-skills-lbw.git`
- **Branch**: `feature/traditional-divination-v1`
- **Goal**: build an automatically discoverable, source-audited traditional six-line divination skill and teach the GitHub workflow through reviewable commits.

## Authority and scope

- User approved creating and installing a personal traditional-divination agent/Skill and using Cangjie to distill books.
- Version 1 is limited to six-line coin casting and 《增删卜易》 as the first book source.
- Traditional interpretation is cultural reflection, not scientific prediction or professional medical, legal, or investment advice.
- Personal questions and birth data are not committed.

## Completed and verified

- Empty GitHub repository bootstrapped; `main` contains the initial skeleton.
- `traditional-divination-skill` created with implicit invocation, deterministic hexagram engine, one-shot secure random casting, references, and eval cases.
- 17 unit tests pass; skill format validation passes; security scan is clean.
- Installed at `D:\Codex\skills\traditional-divination-skill` (local-only path); source and installed `SKILL.md` hashes matched at installation.
- Wikisource snapshot contains 34 pages in reading order, SHA-256 `377f1f4280dd528000825300f83337a859645c34912d11ff979242b864aa4592`.
- Cangjie Stage 0 read the complete source (`L1–L6056/EOF`) and produced `books/zengshan-buyi/BOOK_OVERVIEW.md` plus `PIPELINE_STATE.md`; the user confirmed its three scope decisions.
- Stage 1 extracted 193 independently sourced candidates: 17 frameworks, 110 principles, 24 cases, 19 counter-examples and 23 glossary terms.
- Stage 1.5 completed three independent validation passes and a cross-partition consolidation. Every source candidate has a recorded disposition.
- Source-level disposition: 21 verified, 74 reference, 14 needs-review and 84 rejected-as-duplicate-or-misattributed (193 total).
- Canonical disposition after deduplication: 10 verified, 26 reference, 7 needs-review and 0 unsupported canonical rejections.
- Final audit artifacts are `verified.md`, `references.md`, `needs-review.md`, `rejected/by-source-id.md` and `coverage-audit.md` under `books/zengshan-buyi/`.
- User confirmed Stage 1.5 at 2026-09-16 17:47:00 +10:00.
- Stage 1.6 retained all 10 verified canonical units as router-served capabilities; no duplicate independent skill was promoted.
- Stage 2 produced 10 complete RIA++ cards and a schema-readable Capability Bundle.
- Stage 3 produced a 23-term glossary, linked cards and book overview.
- Stage 4 independent blind evaluation completed: routing 24/24 with F1 1.000 and sibling confusion 0/2; output tasks 20/20 completed with all configured assertions passing.
- Stage 5 produced a 5,423-character `DIGEST.md`; compile preview recommends `pack` for workflow purpose, yielding one source router and zero promoted skills.
- User confirmed the recommended `pack`; Cangjie run `run-20260916-181254-65f060` compiled it successfully.
- The companion was installed at `D:\Codex\skills\zengshan-buyi`: source and installed copies each contain 15 files, with zero per-file SHA-256 differences.
- Both compiled and installed packs pass validation with 0 errors and 0 warnings; the installed `SKILL.md` SHA-256 is `C692C5DA398B7576B4B9137600EAA7B42CACA490D917406BD4BAE3EDD27C370E`.
- `BOOK_ROADMAP.md` classifies follow-on books without mixing medicine, economic history or fraud studies into divination rules.
- 《周易》经传与《周易正义》已蒸馏并安装为 `zhouyi-classics`，作为卦爻辞和注疏辅助层。
- 纳甲排盘升级已安装：固定 `yaomancy/liuyao-engine` 提交 `53291663a4c733c4cbdfa174a8d3075475c07fd3`，并安装 `sxtwl 2.0.7`、`lunar-python 1.4.8`、`najia 2.0.1`。
- 上游完整开发测试为 22 passed、64 subtests passed；仓库测试现为 28 passed，包含全部 64 卦名称、悉尼 AEST/AEDT 和已记录考试卦的端到端纳甲回归测试。
- `derive_liuyao_chart.py` 现在接受六个爻值、实际时间、IANA 时区、类别和问题，输出带引擎提交号的结构化盘面。

## Delivery state

- No pipeline confirmation remains pending. The recommended pack has been compiled, validated and installed.
- A normal request such as “给我算一卦” or “用六爻看看” routes to `traditional-divination-skill`.
- An explicit request such as “按《增删卜易》解释” or “核对这条古籍规则” routes to the `zengshan-buyi` companion.
- 提供实际起卦时间和时区后，主 Skill 会运行 `derive_liuyao_chart.py`，再把排盘事实交给 `zengshan-buyi` 和 `zhouyi-classics` 分层解释。
- The newly installed companion becomes discoverable from the next conversation turn after the host refreshes its skill catalog.

## Future update path

1. Preserve the pack strategy, source-layer labels and high-risk stop card when revising this companion.
2. Re-run Cangjie validation and both routing boundary tests before replacing the installed copy.
3. Distill the next approved book as a separate source companion; do not silently merge medicine, economic history or fraud studies into divination logic.

## Known boundary

The primary skill now supports deterministic original/moving/changed hexagrams plus time-aware 纳甲、月建、日辰、旬空、六神、世应、六亲 and limited 旺衰 facts. Seven interpretive needs-review gaps remain, especially 用神两现、伏神分歧、规则权重 and precise 应期, so the system must preserve unresolved results rather than claim one complete universal method. Divination output remains cultural reflection rather than evidence for medical, legal, financial, fertility, death, crime or disaster decisions.
