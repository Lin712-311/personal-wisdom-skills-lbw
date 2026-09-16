# 触发评测判分 — zengshan-buyi

- runs: 24（TP 18 / FP 0 / FN 0 / TN 6）
- precision 1.000 / recall 1.000 / **F1 1.000**
- 兄弟混淆率: 0.000（0/2）

| case | expected | selected | 判定 |
|---|---|---|---|
| tr-provenance#r1 | should_trigger | zengshan-buyi | TP |
| tr-question#r1 | should_trigger | zengshan-buyi | TP |
| tr-encoding#r1 | should_trigger | zengshan-buyi | TP |
| tr-lookup#r1 | should_trigger | zengshan-buyi | TP |
| edge-unknown-author#r1 | should_trigger | zengshan-buyi | TP |
| edge-subject#r1 | should_trigger | zengshan-buyi | TP |
| edge-five-lines#r1 | sibling | traditional-divination-skill | OK |
| no-python#r1 | should_not_trigger | none | TN |
| tr-focus#r1 | should_trigger | zengshan-buyi | TP |
| tr-ledger#r1 | should_trigger | zengshan-buyi | TP |
| tr-rule#r1 | should_trigger | zengshan-buyi | TP |
| tr-timing#r1 | should_trigger | zengshan-buyi | TP |
| edge-najia#r1 | should_trigger | zengshan-buyi | TP |
| edge-two-focus#r1 | should_trigger | zengshan-buyi | TP |
| edge-conflict#r1 | should_trigger | zengshan-buyi | TP |
| edge-proof#r1 | should_trigger | zengshan-buyi | TP |
| tr-domain#r1 | should_trigger | zengshan-buyi | TP |
| tr-safety#r1 | should_trigger | zengshan-buyi | TP |
| edge-health-route#r1 | should_trigger | zengshan-buyi | TP |
| edge-history-only#r1 | should_trigger | zengshan-buyi | TP |
| edge-hit-date#r1 | should_not_trigger | none | TN |
| no-weather#r1 | should_not_trigger | none | TN |
| sibling-cast#r1 | sibling | traditional-divination-skill | OK |
| no-tarot#r1 | should_not_trigger | none | TN |

> 本报告只给原始配对计数与比率；统计非劣需预注册界值 + McNemar/配对 Bootstrap（§10.3），不在此自动宣布。
