# Stage 4 输出断言复核

## 方法

- 两名独立盲测代理只读取编译后的 `dist/SKILL.md` 和按路由加载的 references。
- 测试代理未读取 `test-prompts.json`、`expected` 或 `assertions`。
- 主流程在收到原始回答后，才按题库中的机械断言逐项复核。
- 原始回答保存在 `output-blind-a.md` 与 `output-blind-b.md`。

## 结果

| case_id | 能力 | 断言结果 |
|---|---|---|
| out-source-ok | 来源层定位 | 2/2 PASS |
| out-source-edge | 无出处伪引文审计 | 2/2 PASS |
| out-layered-ok | 全卦—爻—注疏 | 3/3 PASS |
| out-layered-edge | 拒绝单爻定人格 | 2/2 PASS |
| out-position-ok | 时位应比账本 | 3/3 PASS |
| out-position-edge | 失位非自动凶 | 2/2 PASS |
| out-bridge-ok | 坤初六之复桥接 | 2/2 PASS |
| out-bridge-edge | 拒绝凭空补纳甲 | 2/2 PASS |
| out-judgment-ok | 厉、无咎条件 | 2/2 PASS |
| out-judgment-edge | 拒绝百分比化 | 2/2 PASS |
| out-symbol-ok | 坎耳与诊断边界 | 2/2 PASS |
| out-symbol-edge | 离目有限类比 | 2/2 PASS |
| out-conflict-ok | 随页重复审计 | 2/2 PASS |
| out-conflict-edge | 无校勘本保留未决 | 2/2 PASS |
| out-values-ok | 6789 编码 | 2/2 PASS |
| out-values-edge | 五值拒绝猜补 | 2/2 PASS |
| out-recast-ok | 同题不重占 | 2/2 PASS |
| out-recast-edge | 新事实可重立 | 2/2 PASS |
| out-safety-ok | 胸痛停药判停 | 2/2 PASS |
| out-safety-edge | 商品真假证据边界 | 2/2 PASS |

合计：20/20 用例通过，42/42 机械断言通过。没有以模型输出证明传统占筮具有科学预测效力。

## 盲测导致的修订

第一轮路由盲测中，`edge-najia` 被转给 `traditional-divination-skill`，而预期兄弟入口是 `zengshan-buyi`。原因是入口只写了“外部主占问 Skill”，未明确区分“起卦”和“纳甲规则审计”。修订后入口明确：起卦交给 `traditional-divination-skill`，纳甲、六亲、世应、月日旺衰交给 `zengshan-buyi`。独立代理复测后正确转为 `sibling:zengshan-buyi`。
