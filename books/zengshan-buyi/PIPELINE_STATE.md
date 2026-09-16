# 《增刪卜易》cangjie-skill 流水线状态

## 当前状态

- **当前阶段**：Stage 5 — 已完成
- **执行状态**：**用户已确认推荐的 pack；产物已编译、验证并安装**
- **阶段门**：全部通过；后续更新仍须保留 pack 路由策略、安全边界和可审计来源，不得静默覆盖本地人工修改。
- **最近更新**：2026-09-16（Australia/Sydney）

## Stage 0 输入与校验

- 来源清单：`source/source-manifest.json`
- 原始文本：`source/raw-wikitext.txt`
- manifest 页面数：34
- 原始文本：6,056 行；422,123 bytes
- SHA-256：`377f1f4280dd528000825300f83337a859645c34912d11ff979242b864aa4592`
- 校验结果：与 manifest 的 `sha256` 一致
- 版本警告：维基总页标记 Textquality 25%，多数子页标记 50%；文件包含古籍主体、李文辉增删、李我平评议、现代录入/原剑补料和维基模板，后续必须保留来源层标签。

## 全文处理范围

| 范围 | 章节/材料 | 状态 |
|---|---|---|
| `L1-L236` | 总页、现代录入者言、原剑增订、目录及卷一转引 | 已读 |
| `L237-L2066` | 卷二，章 27–35 | 已读 |
| `L2067-L3410` | 卷三，章 36–68 | 已读 |
| `L3411-L4512` | 卷四，章 69–130 | 已读 |
| `L4513-L4573` | 序 | 已读 |
| `L4574-L4795` | 卷一章 1–3（含录入者疑似增补） | 已读 |
| `L4796-L5039` | 八宫六十四卦全图 | 已读 |
| `L5040-L5507` | 卷一章 4–16 | 已读 |
| `L5508-L5956` | 卷一章 17–26 | 已读 |
| `L5957-L6056` | 生旺墓绝、题头总注、应期总注、归魂游魂 | 已读至 EOF |

初次分块输出中出现截断的范围 `L3240-L3260`、`L3750-L3780`、`L4177-L4355`、`L5776-L5827` 已单独补读。连续覆盖证据为 `L1-L6056`，无已知物理行缺口。

## Stage 0 产出

- [x] 创建 `BOOK_OVERVIEW.md`
- [x] 一句话主旨
- [x] 5 个一级结构及关系
- [x] 关键术语、核心命题与论证链
- [x] 区分古籍主体、李文辉增删、李我平评议、现代录入/镜像层
- [x] 批判时代局限、立场盲点、未证明假设与最强反对意见
- [x] 区分可执行候选、历史参考与不得 active 化的高风险内容
- [x] 建立带 task_id、来源位置、预期交付物、重要性依据和缺口的关键任务表
- [x] 用户已确认 Stage 0（2026-09-16 16:40:40 +10:00，回复“继续”）

## Stage 0 已确认的 3 个关键点

1. **版本与归属**：接受当前“野鶴主体 / 李文辉觉子增删 / 李我平评议 / 原剑及录入者现代补料”的四层划分；未署名段落和原刊年份仍等待更可靠的影印本或校勘本核对。
2. **蒸馏目标**：以后续“历史规则的可复现重建 + 批判性检验”为主，不把六爻输出包装成现实预测或专业建议。
3. **安全边界**：医疗、法律、财务、生育、死亡、犯罪和灾害等内容只能进入 reference/needs_review，不能编译为会给出现实决策结论的 active 能力。

## 下一步门禁

- 用户于 2026-09-16 17:47:00 +10:00 回复“继续”，确认 Stage 1.5 的四类分流并允许进入下一阶段。
- 用户于 2026-09-16 回复“按照推荐吧”，确认 Stage 5 使用 `pack`。
- 安装门已解除并完成；当前没有待确认的流水线门禁。
- 持续禁止：把 reference/needs-review 升为 active，或把内部历史规则描述成科学预测及医疗、法律、财务等专业结论。

## Stage 1 候选产出

- `candidates/frameworks.md`：17 条
- `candidates/principles.md`：110 条
- `candidates/cases.md`：24 条代表性案例
- `candidates/counter-examples.md`：19 条
- `candidates/glossary.md`：23 条核心术语
- 合计：193 条原始候选；允许跨提取器重复，Stage 1.5 负责合并和路由。
- 覆盖：五路结果均覆盖 `ZSBY-T01`–`ZSBY-T09`；所有候选均保留原文位置与来源层。

## Stage 1.5 最终审计产出

- `verified.md`：10 个最终 canonical；只表示历史系统内部可复现或安全审计，不表示现实预测效力。
- `references.md`：26 个最终 reference canonical；完整映射 24 cases、23 glossary、12 个领域原则 reference 与 15 个 framework/counter reference。
- `needs-review.md`：7 个关键缺口 canonical。
- `rejected/by-source-id.md`：84 个 source-level rejected 全部按最终 canonical 去重映射；canonical 层 rejected 为 0。
- `coverage-audit.md`：完成 `ZSBY-T01`–`ZSBY-T09` 的原文位置 → 原候选 → 最终 decision → 交付路径 → 缺口链路。

### 数量口径

| 口径 | verified | reference | needs_review | rejected | 合计 |
|---|---:|---:|---:|---:|---:|
| 193 个 source candidate（分区原判定） | 21 | 74 | 14 | 84 | 193 |
| 跨分区最终 canonical | 10 | 26 | 7 | 0 | 43 |

跨分区 canonical 数较少是因为同一方法在 framework/principle/counter/case/glossary 中重复出现；source-level rejected 表示去重或错误归因，不是删除证据。原则分区曾判 verified 的复占协议最终转入 needs_review：现代预注册和次数上限不能替代原书缺失的停止条件。

### 阻断 Stage 1.6 的主要缺口

1. 端到端纳甲底本、序数/编码、异常输入与字段 schema 未完成。
2. 用神两现、伏神法与复占法缺稳定仲裁。
3. 原书复占“明/恍惚”、最大次数、合断与停止条件不可检验。
4. 规则权重、同强冲突和多候选应期排序/失败定义缺失。
5. 当前镜像 Textquality 低，纳甲等处有疑似异文；未取得影印/校勘本。

## Stage 1.6 晋级门结论

- 评审文件：`promotion-gate.md`
- 10 个 verified canonical 全部保留为来源路由入口 `zengshan-buyi` 的内部能力卡；没有拆出新的独立 Skill。
- 原因：这些单元主要是同一条六爻解释链的内部步骤、来源审计或安全门，用户通常以“六爻占问/《增删卜易》解释”进入；拆分会与已安装的 `traditional-divination-skill` 抢触发。
- 可发现入口预算：实际 1 / 软预算 8；没有能力失联。

## Stage 2–4 完成情况

- Capability Bundle：`.cangjie/capabilities/verified.yaml`，10 个 active router 能力。
- RIA++ 卡片：`.cangjie/capabilities/cards/` 共 10 张，均含 R/I/A1/A2/E/B。
- Zettelkasten：`also_read` 与卡片关系已回填；23 个术语已生成 `GLOSSARY.md` 和随包副本。
- Stage 4 独立盲测：三个干净子代理处理 24 个路由用例和 20 个实际输出用例。
- 最终路由：precision 1.000、recall 1.000、F1 1.000；兄弟混淆 0/2。
- 实际输出：20/20 完成，20/20 用例的全部机械断言通过。
- 测试修订：初始 edge taxonomy 与标点敏感断言的修订理由已记录，未修改盲测输出。

## Stage 5 编译与安装

- `DIGEST.md`：5,423 字符，覆盖核心方法、反例、材料局限与全部能力链接。
- auto purpose=`workflow` 推荐 `pack`。
- 推荐产物：1 个来源路由入口 + 0 个晋级 Skill，共 1 个可发现入口；备选 `single` 同为 1 个入口并携带 10 张内部能力卡。
- 用户已采用推荐方案；成功构建 run：`run-20260916-181254-65f060`。
- 编译目录：`dist/zengshan-buyi`；安装目录：`D:\Codex\skills\zengshan-buyi`。
- 编译产物和安装副本各 15 个文件，逐文件 SHA-256 差异为 0；两侧 `SKILL.md` SHA-256 均为 `C692C5DA398B7576B4B9137600EAA7B42CACA490D917406BD4BAE3EDD27C370E`。
- 编译目录及安装目录分别通过 pack 校验：0 errors、0 warnings；安全关键词扫描无命中。
- 首次编译因 Windows 默认 GBK 解码校验日志失败，未发布不完整产物；切换 Python UTF-8 模式后重新完整编译成功，两次 run 的决策记录均保留用于审计。
- 新安装 Skill 将在下一轮对话的技能发现刷新后可自动触发。
