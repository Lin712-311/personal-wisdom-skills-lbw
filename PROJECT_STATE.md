# Project handoff — traditional divination v1

- **Handoff ID**: `TDV1-20260916-STAGE0`
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
- Cangjie Stage 0 read the complete source (`L1–L6056/EOF`) and produced `books/zengshan-buyi/BOOK_OVERVIEW.md` plus `PIPELINE_STATE.md`.
- Feature branch pushed to GitHub through commit `2bfe872`.

## Pending user decision (hard gate)

Cangjie Stage 1 must not begin until the user confirms the Stage 0 overview. The concise confirmation is:

> 接受当前来源分层；继续把它做成“有来源、可复核、有安全边界的传统文化占问”，不包装成科学预测，高风险领域不输出决策结论。

If the user disagrees, update `BOOK_OVERVIEW.md` and `PIPELINE_STATE.md` before extraction.

## Next executable step after confirmation

1. Record the confirmation time in `BOOK_OVERVIEW.md` and mark Stage 0 approved in `PIPELINE_STATE.md`.
2. Run the five Cangjie Stage 1 extraction roles with independent outputs.
3. Perform Stage 1.5 triple verification and stop for the next required user confirmation.
4. Acceptance: candidates are source-located, coverage-audited, and routed to `verified`, `reference`, `needs_review`, or `rejected` without creating active capability cards early.

## Known boundary

The installed primary skill is usable now for question normalization, casting, and deterministic original/moving/changed hexagram calculation. Until the Cangjie companion is compiled and installed, it must label interpretation as simplified and must not claim full 纳甲、月建、日辰、旬空、六神、世应、六亲、用神、旺衰 or 应期 support.
