# 《周易》经传与《周易正义》Stage 1.5 覆盖审计

## 数量口径

- Stage 1 source candidate：框架/流程 30、原则/规则 60、案例 14、反例/边界 16、术语 30，合计 **150**。
- 跨分区最终 canonical：verified 10、reference 18、needs_review 6；source-level 重复和细碎项由 `rejected/by-source-id.md` 映射。
- canonical 数量小于 source candidate，是因为同一方法在框架、原则、反例、案例和术语中重复出现；重复不能冒充独立证据。

## ZY-T01–T09 链路

| task_id | Stage 1 主要候选 | 最终 decision / 去向 | 关键缺口 |
|---|---|---|---|
| ZY-T01 原典定位 | `f02, f27, P005, P060, g01-g11` | VC-01/02/07 verified；术语 reference | 校勘本与异文 NR-01 |
| ZY-T02 彖象文言解释 | `f01-f04, P005, P042-P049` | VC-02 verified；大象表 REF-MAP-01 | 《小象》录入风险 NR-01 |
| ZY-T03 象辞变占方法 | `f05-f17, P002-P035, g11-g30` | VC-03/04/05/08/09；术语 reference | 关系权重 NR-04；完整蓍法 NR-05 |
| ZY-T04 八卦取象 | `f18-f19, f29, P036-P041, ce02` | VC-06；REF-MAP-02 | 不得字面化或无限联想 |
| ZY-T05 卦序与比较 | `f20-f21, P057-P059` | REF-SEQ-01；VC-07 审计 | 卦序叙事不是历史因果 |
| ZY-T06 时位中应比 | `f01-f08, P031-P034, ce03-ce06` | VC-02/03/05 | 无统一优先级 NR-04 |
| ZY-T07 注疏比较 | `f27-f28, P060, c01/c14` | VC-01/07；案例 reference | 其他易学传统 NR-03 |
| ZY-T08 六爻桥接 | `f30, P003/P050, ce01, eb01-eb04` | VC-04/08/09/10 | 纳甲仍由外部 Skill；应期 NR-06 |
| ZY-T09 安全与真实性 | `f07/f27/f28, ce01-ce12, eb01-eb04` | VC-01/07/09/10；边界 reference | 现代实证综述未做 |

## 覆盖结论

- `ZY-T01`–`ZY-T09` 全部具有“原文 → candidate → decision → 去向”链路。
- 只验证了经典查询、解释流程、结构账本、有限爻值编码和安全审计；没有验证占筮预测准确率。
- 版本、作者层、完整蓍法、解释权重和精确时间仍是显式缺口，未被现代常识静默补齐。

## Stage 2–5 交付审计

- Capability Bundle：`.cangjie/capabilities/verified.yaml`，共 10 个 active router 能力；全部保留在一个 `zhouyi-classics` 入口内，未拆成相互抢触发的“周易”和“易经”。
- RIA++ 卡：`.cangjie/capabilities/cards/` 共 10 张，均含原文依据、方法骨架、正例、触发场景、执行步骤、边界与关联能力。
- 术语与摘要：`GLOSSARY.md` 收录 30 个术语；`DIGEST.md` 为 5,302 字符并链接全部核心能力卡。
- Stage 4 路由盲测：24 条，最终 precision 1.000、recall 1.000、F1 1.000，兄弟入口混淆 0/2。
- Stage 4 输出盲测：20/20 用例通过，42/42 机械断言通过。测试只证明路由与输出契约，不证明占筮预测效力。
- 盲测修订：首次把纳甲边界路由到了通用起卦入口；现已明确改为“起卦 → `traditional-divination-skill`，纳甲规则 → `zengshan-buyi`，经传注疏 → `zhouyi-classics`”，复测通过。
- Stage 5：编译为 single 形态，1 个 Skill、10 个内部能力、16 个文件；安装到 `D:\Codex\skills\zhouyi-classics`。
