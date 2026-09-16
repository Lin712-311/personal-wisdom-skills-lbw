# Project handoff — traditional divination v1

- **Handoff ID**: `TDV1-20260916-STAGE1.5`
- **Updated**: 2026-09-16 (Australia/Sydney)
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
- Feature branch has been pushed through the Stage 1 extraction commit `3991038`; the Stage 1.5 audit commit follows this handoff update.

## Pending user decision (hard gate)

Cangjie Stage 1.6 must not begin until the user reviews and lightly confirms the Stage 1.5 four-way disposition. The concise confirmation is:

> 确认 Stage 1.5 的 verified / reference / needs_review / rejected 范围，进入下一阶段。

If the user disagrees, revise the Stage 1.5 audit files and `PIPELINE_STATE.md` before promotion work.

## Next executable step after confirmation

1. Record the Stage 1.5 confirmation in `PIPELINE_STATE.md`.
2. Read and execute the Cangjie Stage 1.6 promotion gate.
3. Create only the capability cards supported by the 10 verified canonical items; keep references and unresolved gaps inactive.
4. Continue the required pressure tests and compilation stages before installing the 《增删卜易》 companion Skill.

## Known boundary

The installed primary skill is usable now for question normalization, casting, and deterministic original/moving/changed hexagram calculation. Until the Cangjie companion is compiled and installed, it must label interpretation as simplified and must not claim full 纳甲、月建、日辰、旬空、六神、世应、六亲、用神、旺衰 or 应期 support.
