# 《周易》经传与《周易正义》cangjie-skill 流水线状态

## 当前状态

- **当前阶段**：Stage 1.5 — 三重验证已完成，等待用户轻确认
- **执行状态**：150 个 source candidate 已完成来源、可执行性与任务增益审计；尚未进入 Capability Bundle 编译
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

## 下一步门禁

请用户确认 Stage 1.5 的四类分流：10 个 verified canonical、18 个 reference canonical、6 个 needs-review，以及 source-level 去重映射。确认后进入 Stage 1.6；推荐仍为 1 个 `zhouyi-classics` 来源入口，不拆成多个抢触发的 Skill。

## Stage 1 / 1.5 数量

- frameworks：30
- principles：60
- cases：14
- counter-examples / external boundaries：16
- glossary：30
- source candidates 合计：150
- 最终 canonical：verified 10 / reference 18 / needs_review 6
