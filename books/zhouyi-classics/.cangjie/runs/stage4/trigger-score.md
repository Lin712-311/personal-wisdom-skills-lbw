# 触发评测判分 — zhouyi-classics

- runs: 24（TP 19 / FP 0 / FN 0 / TN 5）
- precision 1.000 / recall 1.000 / **F1 1.000**
- 兄弟混淆率: 0.000（0/2）

| case | expected | selected | 判定 |
|---|---|---|---|
| tr-source#r1 | should_trigger | zhouyi-classics | TP |
| tr-layered#r1 | should_trigger | zhouyi-classics | TP |
| tr-position#r1 | should_trigger | zhouyi-classics | TP |
| tr-bridge#r1 | should_trigger | zhouyi-classics | TP |
| tr-judgment#r1 | should_trigger | zhouyi-classics | TP |
| tr-symbol#r1 | should_trigger | zhouyi-classics | TP |
| tr-conflict#r1 | should_trigger | zhouyi-classics | TP |
| tr-values#r1 | should_trigger | zhouyi-classics | TP |
| tr-recast#r1 | should_trigger | zhouyi-classics | TP |
| tr-safety#r1 | should_trigger | zhouyi-classics | TP |
| edge-quote#r1 | should_trigger | zhouyi-classics | TP |
| edge-no-line#r1 | should_trigger | zhouyi-classics | TP |
| edge-score#r1 | should_trigger | zhouyi-classics | TP |
| edge-najia#r1 | sibling | zengshan-buyi | OK |
| edge-image#r1 | should_trigger | zhouyi-classics | TP |
| edge-variant#r1 | should_trigger | zhouyi-classics | TP |
| edge-five#r1 | should_trigger | zhouyi-classics | TP |
| edge-new-fact#r1 | should_trigger | zhouyi-classics | TP |
| edge-counterfeit#r1 | should_trigger | zhouyi-classics | TP |
| edge-history#r1 | should_trigger | zhouyi-classics | TP |
| no-python#r1 | should_not_trigger | none | TN |
| no-weather#r1 | should_not_trigger | none | TN |
| sibling-cast#r1 | sibling | traditional-divination-skill | OK |
| no-tarot#r1 | should_not_trigger | none | TN |

> 本报告只给原始配对计数与比率；统计非劣需预注册界值 + McNemar/配对 Bootstrap（§10.3），不在此自动宣布。
