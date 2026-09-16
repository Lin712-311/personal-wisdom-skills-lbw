# 《增刪卜易》Stage 1.5 覆盖审计

> 链路：原文位置 → Stage 1 source candidate → 最终 canonical/decision → 最终交付路径 → 剩余缺口。Stage 2–4 已创建并盲测 Capability Bundle；下表保留 Stage 1.5 原始路径，文末登记实际交付路径。

## 数量与口径

### 193 个 source candidate（分区原判定口径）

| 类别 | framework + counter（36） | principles（110） | cases + glossary（47） | 合计 |
|---|---:|---:|---:|---:|
| verified | 12 | 9 | 0 | **21** |
| reference | 15 | 12 | 47 | **74** |
| needs_review | 4 | 10 | 0 | **14** |
| rejected | 5 | 79 | 0 | **84** |
| **总计** | **36** | **110** | **47** | **193** |

### 跨分区最终 canonical 口径

| 类别 | 数量 | 去向 |
|---|---:|---|
| verified | **10** | `verified.md`；仅有资格进入 Stage 1.6 |
| reference | **26** | `references.md`：9 案例组 + 15 术语组 + 1 领域矩阵 + 1 现代批判/边界 |
| needs_review | **7** | `needs-review.md` |
| rejected | **0** | canonical 层无额外淘汰；84 个 source-level rejected 在 `rejected/by-source-id.md` 去重映射 |
| **总计** | **43** | 跨分区产品单元 |

数量变化原因：source 口径允许跨 extractor 重复，并把被完整覆盖的细碎候选计为 rejected；final canonical 口径把同一方法、术语和案例组跨分区合并。原则分区的复占协议因现代护栏不能替代原书停止条件，最终转入 `ZSBY-NR-04`。

## ZSBY-T01–T09 端到端覆盖

| task_id | 原文位置 → 原候选 | 最终 canonical / decision | 最终交付路径 | 关键缺口 |
|---|---|---|---|---|
| ZSBY-T01 问题合同 | `L4553-L4570, L1465-L1580, L2075-L2078, L3635-L3637` → FW-003, FW-016, P048 及领域实例 P018/P020/P039/P044/P049/P054/P058/P059/P061/P062/P064/P067/P069/P070/P072/P075/P078/P079/P080；案例 c12-c14/c18/c21/c24 | VC-02 verified；VC-09 verified；VC-10 verified 安全门；REF-CASE-05/09 reference | `verified.md#VC-02/#VC-09/#VC-10`；未来 `book/overview.md#问题范围案例` | 原书无现代风险分流、隐私/同意和专业转交细则；这些只能显式外加 |
| ZSBY-T02 排卦结构 | `L4574-L5161`，现代段 `L4602-L4692` → FW-002/FW-004, P001-P003/P082-P088, c01, g02/g03/g07 | VC-01/03/04 verified（局部）；NR-01、NR-07 needs_review；REF-CASE-01、REF-TERM-02/04 reference | `verified.md#VC-01/#VC-03/#VC-04`；`needs-review.md#NR-01/#NR-07`；未来 glossary/overview | 纳甲异文、序数基准、异常投掷、干支日期与全字段 schema 未解决；不能称端到端完成 |
| ZSBY-T03 取用与四神 | `L5165-L5243, L830-L867, L309-L420` 及分门章节 → FW-005/FW-006/FW-012/FW-013, P008-P010/P019/P038/P089, g01-g06/g17/g23，多项案例 | VC-05 verified；VC-02/09 支撑；NR-02 两现、NR-03 伏神/复占；相关术语/案例 reference | `verified.md#VC-05`；`needs-review.md#NR-02/#NR-03`；未来 `book/glossary.md` | 代占、两现、伏神/复占与“占此应彼”没有唯一仲裁，只能保留分支 |
| ZSBY-T04 作用账本 | `L5202-L5955, L4736-L4758` → FW-006-FW-009, P013/P017/P023/P027/P030/P032/P035-P037/P084/P090-P107，g04-g20，大量案例 | VC-04/05/06 verified；VC-07 审计；NR-05 needs_review；术语/案例 reference | `verified.md#VC-04/#VC-05/#VC-06/#VC-07`；`needs-review.md#NR-05`；未来 glossary | 无统一量化权重、同强冲突或跨章例外排序；只能输出账本/分支 |
| ZSBY-T05 辨误与例外 | `L237-L2065, L5546-L5881` → FW-010/FW-011, P015/P029/P033/P034/P041/P045/P053/P101/P103-P105/P110，ce04-ce09，c09/c17/c19/c24 | VC-07 verified；VC-06 支撑；NR-05/06/07；REF-CASE-04/06/07/09 与现代批判 reference | `verified.md#VC-07`；`needs-review.md#NR-05/#NR-06/#NR-07`；未来 `book/overview.md#证据限制` | 缺完整失败分母、盲法、基准率、前瞻登记和独立核验；书内删改不等于科学验证 |
| ZSBY-T06 应期 | `L6010-L6035, L5412-L5543` 及领域案例 → FW-015, P007/P012/P021/P024-P026/P043/P063/P098/P108, g08-g21，c02-c11/c15-c20/c23 | VC-08 verified（未排序候选）；NR-06 needs_review；REF-CASE-03/04 与 REF-TERM-13 | `verified.md#VC-08`；`needs-review.md#NR-06`；未来 `book/glossary.md#应期` | 无候选优先级、概率、容错窗口、截止和失败定义；P063 引文不实 |
| ZSBY-T07 分占/复占/停止 | `L4553-L4570, L376-L409, L4715-L4719, L5884-L5954, L6033` → FW-003/FW-010/FW-012-FW-014, P006/P010/P022/P109, g17/g22/g23，c02/c04/c10/c11/c16/c22/c23 | VC-02/07/10 verified（拆题、审计、安全）；NR-02/03/04 needs_review；REF-CASE-02/TERM-14 reference | `verified.md#VC-02/#VC-07/#VC-10`；`needs-review.md#NR-02/#NR-03/#NR-04` | “明/恍惚”、最大次数、合断准则和判停均未定义；现代预注册协议不能冒充原书规则 |
| ZSBY-T08 领域路由 | 卷二至卷四 `L237-L4512` → FW-016/FW-017，P028/P042/P050-P081，c04-c24，g01-g03/g22 | VC-09 路由、VC-02 合同、VC-10 安全门 verified；REF-DOMAIN-01、案例组 reference | `verified.md#VC-09/#VC-10`；`references.md#领域历史矩阵`；未来 overview/Boundary | 古代制度大多失效；医疗、法律、财务、生育、死亡、犯罪、灾害、人格断语禁止 active |
| ZSBY-T09 版本真实性 | `L3-L124, L237-L243, L4602-L4692, L5097/L5199/L5331` → FW-001, P001-P004/P083/P086，ce15，所有候选 source_layer | VC-01 verified；NR-01/07 needs_review；REF-BOUNDARY-01 reference | `verified.md#VC-01`；`needs-review.md#NR-01/#NR-07`；未来 `book/overview.md#版本与归属` | 无初刻/可靠影印/校勘本；未署名归属、原刊年份和现代补入边界待考 |

## 覆盖结论

- `ZSBY-T01`–`T09` 均有“位置—候选—decision—去向”链路；没有因未通过而静默消失。
- T02/T03/T04/T05/T06/T07/T09 仍有实质缺口，因此只能声明“限定能力完成”，不能声明整套术数算法完整或有效。
- 所有 `verified` 均受统一边界约束：历史系统内部可复现或安全审计，不代表现实预测效力。

## Stage 2–5 实际交付路径

| canonical | 能力卡 |
|---|---|
| VC-01 | `.cangjie/capabilities/cards/provenance-audit.md` |
| VC-02 | `.cangjie/capabilities/cards/question-contract.md` |
| VC-03 | `.cangjie/capabilities/cards/line-encoding.md` |
| VC-04 | `.cangjie/capabilities/cards/lookup-transform.md` |
| VC-05 | `.cangjie/capabilities/cards/focus-relations.md` |
| VC-06 | `.cangjie/capabilities/cards/evidence-ledger.md` |
| VC-07 | `.cangjie/capabilities/cards/rule-audit.md` |
| VC-08 | `.cangjie/capabilities/cards/timing-candidates.md` |
| VC-09 | `.cangjie/capabilities/cards/domain-router.md` |
| VC-10 | `.cangjie/capabilities/cards/high-risk-stop.md` |

- 23 个术语已落实到 `GLOSSARY.md` 和 `.cangjie/capabilities/book/glossary.md`。
- 案例组、领域矩阵、证据限制和版本边界已落实到 `.cangjie/capabilities/book/overview.md`。
- 读者版精华已落实到 `DIGEST.md`。
- Stage 4 独立盲测：24/24 路由判断完成，F1 1.000，兄弟混淆 0/2；20/20 实际输出完成且全部机械断言通过。初始 fixture 修订记录见 `.cangjie/runs/stage4/test-revisions.md`。
- `destinations.json` 为 10 个 active 能力登记唯一 `served_by: zengshan-buyi` 去向，没有能力失联。
