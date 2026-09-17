# 《周易》经传与《周易正义》cangjie-skill 流水线状态

## 当前状态

- **当前阶段**：Stage 5 — 已完成
- **执行状态**：用户已确认推荐的一入口方案；产物已蒸馏、盲测、编译、验证并安装
- **目标形态**：一个 `zhouyi-classics` 来源 companion，作为现有六爻 Skill 的经传/义理辅助层，不新建相互抢触发的“周易”和“易经”两个入口
- **最近更新**：2026-09-17（Australia/Sydney）

## Stage 0 输入与校验

| 来源 | 角色 | 页数 | 物理规模 | SHA-256 | 校验 |
|---|---|---:|---:|---|---|
| `source/zhouyi/raw-wikitext.txt` | 六十四卦经文及彖、象、文言、系辞、说卦、序卦、杂卦 | 74 | 3,854 行；176,183 bytes | `da52c7fd9308122d153a3d4823034b0013cbf90b0cf1bc8a1694a83361d085c3` | 与子 manifest 一致 |
| `source/zhouyi-zhengyi/raw-wikitext.txt` | 王弼/韩康伯注、孔颖达疏 | 100 | 7,270 行；903,203 bytes | `a3b125ba3cb90f1f14e7c275b6dbb67c5a384328ebc254e016f5b4613472435d` | 与子 manifest 一致 |

## 已确认的来源问题

1. 《周易》总页的 `Textquality` 为 50%；当前镜像可用于建立可追溯语料，但不是校勘定本。
2. 《小象》聚合页有明显录入错误，后续引文须优先按单卦页与《周易正义》交叉核对。
3. 《周易正义》同时抓到 `02隨` 与 `03隨`，总目录指向后者；二者作为重复/异文，不重复计数。
4. 经、传、王弼/韩康伯注、孔颖达疏及现代整理说明必须分层，不能混写成“《易经》原文说”。
5. 传统的伏羲、文王、周公、孔子作者说只能标为传统归属；skill 不把它写成无争议的现代史实。

## Stage 0 产出

- [x] 归档两套来源及各自 manifest
- [x] 校验页数、物理规模与 SHA-256
- [x] 按文王卦序重排六十四卦，并把十翼类材料置后
- [x] 建立经 / 传 / 注 / 疏 / 现代整理五层来源模型
- [x] 形成一句话主旨与 6 个一级结构
- [x] 建立关键术语、核心命题、批判边界和任务覆盖表
- [x] 明确与纳甲六爻的接口和禁止倒灌项
- [x] 向用户展示并取得 Stage 0 确认（2026-09-17 01:22:34 +10:00，用户回复“jixu”）

## 阶段门与用户确认

- Stage 0：用户于 2026-09-17 回复“jixu”，确认继续整书提炼。
- Stage 1.5：用户于 2026-09-17 回复“易经 你也帮我提炼进去先”，确认采用推荐的单一 `zhouyi-classics` 来源入口并继续编译安装。
- 当前没有待确认门禁。后续更新不得把 reference / needs-review 静默提升为 active，也不得把传统占筮包装成科学预测。

## Stage 1 / 1.5 数量

- frameworks：30
- principles：60
- cases：14
- counter-examples / external boundaries：16
- glossary：30
- source candidates 合计：150
- 最终 canonical：verified 10 / reference 18 / needs_review 6

## Stage 2–3 能力构建

- Capability Bundle：`.cangjie/capabilities/verified.yaml`，10 个 active router 能力。
- RIA++ 能力卡：`.cangjie/capabilities/cards/` 共 10 张，覆盖来源分层、全卦与爻层解释、时位应比、变卦桥接、判断辞、取象边界、注疏冲突、6789 编码、同题不重占和高风险判停。
- Zettelkasten：`also_read` 和卡片关系已回填；30 个术语形成 `GLOSSARY.md` 与随包 glossary。
- `DIGEST.md`：5,302 字符，覆盖方法、反例、材料局限及全部能力链接。

## Stage 4 压力测试

- 三名独立盲测代理先完成 24 条路由提示与第一批 10 条输出；第四名独立代理完成第二批 10 条输出。
- 最终路由：precision 1.000、recall 1.000、F1 1.000；兄弟混淆 0/2。
- 实际输出：20/20 用例通过，42/42 机械断言通过。
- 首轮发现“纳甲”边界被转给 `traditional-divination-skill`；修订后明确三层职责并由独立代理复测为 `sibling:zengshan-buyi`。
- 原始盲测与评分记录：`.cangjie/runs/stage4/`。

## Stage 5 编译与安装

- 输出策略：`single`；共 1 个可发现 Skill、10 个内部能力、16 个文件。
- 最终构建 run：`run-20260917-142025-6640be`。
- 编译目录：`books/zhouyi-classics/dist`。
- 安装目录：`D:\Codex\skills\zhouyi-classics`。
- 安装校验：0 errors、0 warnings；编译与安装均为 16 个文件，逐文件 SHA-256 差异为 0。
- `SKILL.md` SHA-256：`C520EF1F2AE2CD209F52C985DD04447629356118B6A061CCD60DA364D705852C`。
- 新开对话后技能发现会重新扫描，届时可自动路由；本线程的静态技能列表可能直到下一轮刷新才显示新安装项。
