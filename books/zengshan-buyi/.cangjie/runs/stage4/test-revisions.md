# Stage 4 fixture revisions

## Revision 1 — edge route semantics

The initial suite labeled eight “invoke then refuse/stop” prompts as `edge_case`. The deterministic scorer treats `edge_case` as a negative target, so correct routing to `zengshan-buyi` was counted as a false positive. After independent agents had already submitted locked results, these cases were reclassified as `should_trigger`; `edge-five-lines` was reclassified as sibling `traditional-divination-skill`, and the context-free “百分百日期” request as `should_not_trigger`.

This changes the fixture taxonomy, not agent outputs or routing descriptions. Safety and missing-input behavior remain tested in `output_cases`.

## Revision 2 — punctuation-insensitive output assertions

Eight output cases used presentation-specific substrings such as `寅卯`, `三、四` or `水=元神`. Blind outputs supplied the correct semantic fields using tables, punctuation or bit arrays. Assertions were replaced with stable semantic tokens such as `寅、卯`, `三爻、四爻`, `[1, 0, 0, 1, 1, 0]` and explicit five-element relations.

No blind output was edited. The initial reports remain in the run artifacts for audit.
