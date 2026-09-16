# Project handoff — traditional divination v1

- **Handoff ID**: `TDV1-20260916-STAGE5-PREVIEW`
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
- User confirmed Stage 1.5 at 2026-09-16 17:47:00 +10:00.
- Stage 1.6 retained all 10 verified canonical units as router-served capabilities; no duplicate independent skill was promoted.
- Stage 2 produced 10 complete RIA++ cards and a schema-readable Capability Bundle.
- Stage 3 produced a 23-term glossary, linked cards and book overview.
- Stage 4 independent blind evaluation completed: routing 24/24 with F1 1.000 and sibling confusion 0/2; output tasks 20/20 completed with all configured assertions passing.
- Stage 5 produced a 5,423-character `DIGEST.md`; compile preview recommends `pack` for workflow purpose, yielding one source router and zero promoted skills.
- `BOOK_ROADMAP.md` classifies follow-on books without mixing medicine, economic history or fraud studies into divination rules.

## Pending user decision (hard gate)

The deterministic compile preview recommends `pack` because the purpose is workflow. In this bundle, pack contains one `zengshan-buyi` source router and no promoted siblings, so it keeps one discoverable entry and all 10 internal cards.

Required response: `按推荐` / `改成 single` / `改成 pack`.

## Next executable step after confirmation

1. Run `cangjie.py compile ... --output auto --purpose workflow --yes` for “按推荐”, or the explicit selected output mode.
2. Validate the compiled artifact, install it to `D:\Codex\skills\zengshan-buyi`, and run one source-router smoke test plus one sibling-boundary smoke test.
3. Update `PIPELINE_STATE.md` to complete, commit and push the final artifacts and handoff state.

## Known boundary

The installed primary skill is usable now for question normalization, casting, and deterministic original/moving/changed hexagram calculation. Until the Cangjie companion is compiled and installed, it must label interpretation as simplified and must not claim full 纳甲、月建、日辰、旬空、六神、世应、六亲、用神、旺衰 or 应期 support.
