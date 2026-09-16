- id: P001
  title: 现代增补的装卦顺序
  type: checklist
  source_chapter: 现代增补·原剑增订说明（raw-wikitext L26-L67）
  source_quote: "定地支、定世应、装六亲、装六兽。"
  summary: 按地支、世应、六亲、六神的顺序装卦；这是现代录入者整理的便查法，不是古籍主体原文。
  tags: [modern-editorial, casting, najia, provenance]
  task_ids: [ZSBY-T02, ZSBY-T09]

- id: P002
  title: 现代增补的旬空取余法
  type: calculation
  source_chapter: 现代增补·旬空快速算法（raw-wikitext L80-L88）
  source_quote: "旬空公式：空亡=(地支+11-天干)%12，所得的余数就是空亡开始的位置"
  summary: 用干支序数取模求旬空起点；该公式属于现代增补，原文未完整交代序数编码与跨界约定。
  tags: [modern-editorial, formula, void, provenance]
  task_ids: [ZSBY-T02, ZSBY-T06, ZSBY-T09]
  inputs: [天干序数, 地支序数]
  formula: "(地支序数 + 11 - 天干序数) mod 12"
  units: 十二地支序位
  output: 旬空开始的地支位置
  missing_conditions: 原文未明示天干、地支从0还是从1编码，也未单列余数0的映射。

- id: P003
  title: 现代增补的干支合法性校验
  type: calculation
  source_chapter: 现代增补·干支有效性（raw-wikitext L90-L93）
  source_quote: "天干数-地支数=奇数，错误；天干数-地支数=偶数，正确。"
  summary: 以干支序数差的奇偶检查干支组合是否合法；属于现代录入者补充。
  tags: [modern-editorial, validation, formula, provenance]
  task_ids: [ZSBY-T02, ZSBY-T05, ZSBY-T09]
  inputs: [天干序数, 地支序数]
  formula: "若(天干序数-地支序数) mod 2 = 0则有效，否则无效"
  units: 序数奇偶
  output: 干支组合有效或错误
  missing_conditions: 序数表需先固定；只能校验阴阳配对，不能独立证明纪日数据正确。

- id: P004
  title: 现代增补的常用神煞查表
  type: calculation
  source_chapter: 现代增补·神煞（raw-wikitext L94-L113）
  source_quote: "华盖：寅午戌年日见戌；申子辰年日见辰；亥卯未年日见未；巳酉丑年日见丑。"
  summary: 依年支、日支或日干查华盖、驿马、禄神、月德、天德、羊刃、国印、将星、文昌等；本表是现代增补且仅宜作为辅助信息。
  tags: [modern-editorial, lookup-table, stars, provenance]
  task_ids: [ZSBY-T04, ZSBY-T09]
  inputs: [年支, 月支, 日干, 日支, 所查神煞]
  formula: 按原文各神煞对应表逐项映射
  units: 干支类别
  output: 对应神煞所在干支
  missing_conditions: 部分神煞按年或日、按月或日的优先级未说明，且未提供经验有效性依据。

- id: P005
  title: 现代增补的占问边界
  type: maxim
  source_chapter: 现代增补·录入者说明（raw-wikitext L121-L124）
  source_quote: "不疑何卜。生病了应该找医生，事业不顺，应该努力工作，不应该依赖卜筮。"
  summary: 仅在确有疑难时占问；疾病、事业等现实问题应先采用医学或行动方案。这是现代录入者的安全性增补。
  tags: [modern-editorial, safety, scope, provenance]
  task_ids: [ZSBY-T01, ZSBY-T07, ZSBY-T09]

- id: P006
  title: 一事一问且不追问同题
  type: rule
  source_chapter: 现代增补·录入者说明（raw-wikitext L121-L124）
  source_quote: "一天只能占一次，一个事情只能占一次，不可再三占卜，只能在两难之间犹豫的时候占卜。"
  summary: 同一事项只起一问，不以反复起卦追逐偏好答案；次数限制来自现代增补，古籍另有“卦不明再占”的条件性例外。
  tags: [modern-editorial, question-contract, recast, provenance]
  task_ids: [ZSBY-T01, ZSBY-T07, ZSBY-T09]

- id: P007
  title: 月破的判定与解除
  type: rule
  source_chapter: 古籍主体·月破章（raw-wikitext L241-L251）
  source_quote: "月建所冲之爻谓之月破……今日虽破，出月不破；今日虽破，逢合之日不破。"
  summary: 月建所冲为月破；动爻、变爻仍可能作用，出月、填实或逢合后可解除，静而无援者才按真破处理。
  tags: [ancient-core, month-break, conditions, timing]
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06]

- id: P008
  title: 伏神可用条件清单
  type: checklist
  source_chapter: 古籍主体·飞伏神章（raw-wikitext L311-L348）
  source_quote: "伏神得日月生者一也；伏神旺相者二也；伏神得飞神生者三也；伏神得动爻生者四也；伏神得逢日月动爻冲克飞神者五也。"
  summary: 用神不现时查伏神；伏神得日月、旺相、飞神、动爻扶助，或飞神被冲克时，列为可出伏候选。
  tags: [ancient-core, hidden-line, checklist, use-god]
  task_ids: [ZSBY-T03, ZSBY-T04]

- id: P009
  title: 伏神不可用条件清单
  type: checklist
  source_chapter: 古籍主体·飞伏神章（raw-wikitext L311-L348）
  source_quote: "伏神休囚无气者一也；伏神被日月冲克者二也；伏神被旺相之飞神克害者三也；伏神墓绝于日月飞爻者四也；伏神休囚值旬空月破者五也。"
  summary: 伏神休囚、受冲克、被旺飞神克、墓绝或又值空破时，不作为可用伏神。
  tags: [ancient-core, hidden-line, invalidation, checklist]
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T05]

- id: P010
  title: 用神不现时重占
  type: rule
  source_chapter: 古籍主体·飞伏神章（raw-wikitext L370-L378）
  source_quote: "予得验者，伏神有用者六，伏神终不得出者五……不若再占一卦，用神出现而无疑也。"
  summary: 若伏神条件仍含混，作者偏好重新起卦取得显现用神；这是一项不明时的升级规则，而非清晰答案下的重问。
  tags: [ancient-core, recast, ambiguity, escalation]
  task_ids: [ZSBY-T03, ZSBY-T05, ZSBY-T07]

- id: P011
  title: 进神退神固定配对
  type: calculation
  source_chapter: 古籍主体·进神退神章（raw-wikitext L431-L441）
  source_quote: "亥化子、寅化卯、巳化午、申化酉、丑化辰、辰化未、未化戌、戌化丑，皆为化进神；反此者为退神。"
  summary: 以十二地支的固定变爻配对判定化进或化退，不能仅按一般序数增减判断。
  tags: [ancient-core, transformation, lookup-table, progression]
  task_ids: [ZSBY-T02, ZSBY-T04, ZSBY-T06]
  inputs: [动爻地支, 变爻地支]
  formula: "进神集合={(亥,子),(寅,卯),(巳,午),(申,酉),(丑,辰),(辰,未),(未,戌),(戌,丑)}；逆向为退神"
  units: 地支有序对
  output: 进神、退神或均非
  missing_conditions: 吉凶与应期还须结合旺衰、空破、日月与是否有用。

- id: P012
  title: 进退神须满足有效条件
  type: rule
  source_chapter: 古籍主体·进神退神章（raw-wikitext L665-L675）
  source_quote: "动旺相而化旺相，乘势而进，一也；动休囚而化休囚，待时而进，二也；动爻变爻有一而值休囚，亦待旺相之日而进，三也；动爻变爻有一而值空破，待填实之日而进，四也。"
  summary: 进退不能只看配对；还要分当下乘势、待旺、待填实等状态，并据此决定何时发生。
  tags: [ancient-core, progression, conditions, timing]
  task_ids: [ZSBY-T04, ZSBY-T06]

- id: P013
  title: 随鬼入墓须先验强弱
  type: rule
  source_chapter: 古籍主体·随鬼入墓章（raw-wikitext L687-L739）
  source_quote: "世用休囚被克而入墓，始以凶推；旺相有扶者，虽入墓而无害。"
  summary: “随鬼入墓”只在世爻或用神休囚受克时按凶看；旺相有扶不成立，墓被冲开、冲破也要重新判断。
  tags: [ancient-core, grave, correction, strength]
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T08]

- id: P014
  title: 独发独静不可替代用神
  type: rule
  source_chapter: 古籍主体·独发章（raw-wikitext L757-L759）
  source_quote: "独发独静，亦不可舍用神而断，乃事后应验之机耳。"
  summary: 单一动爻或静爻只能作为事后应象线索，不能越过已确定的用神直接裁决。
  tags: [ancient-core, use-god, audit, evidence-order]
  task_ids: [ZSBY-T03, ZSBY-T05]

- id: P015
  title: 两现用神的条件选择
  type: rule
  source_chapter: 古籍主体·两现章（raw-wikitext L830-L867）
  source_quote: "用神两现者，古法舍其月破而用不破，舍其旬空而用不空……予屡试之，旺相者不验，反应旬空月破之爻。"
  summary: 两个同类用神出现时，旧法偏取不空不破者；作者以实例提出条件性反例，要求结合前占、发动与实际应期，不机械舍空破。
  tags: [ancient-core, use-selection, conflict, audit]
  task_ids: [ZSBY-T03, ZSBY-T05, ZSBY-T07]

- id: P016
  title: 神煞只能附看
  type: rule
  source_chapter: 古籍主体·星煞章（raw-wikitext L870-L900）
  source_quote: "卦之吉凶，全在五行生克制化，神煞无关也……贵人、禄神、驿马、天喜，亦须得用神旺相，方可为吉。"
  summary: 吉凶先由五行、用神和旺衰决定；神煞即使保留，也必须依附旺相用神，不得独立裁决。
  tags: [ancient-core, stars, evidence-priority, correction]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P017
  title: 生扶与克墓的数量不代替根气
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L903-L911）
  source_quote: "用神多者，须墓库以收藏；用神少者，宜生扶而有根。"
  summary: 同类爻过多时考察墓库收束，过少时考察生扶；但被扶者必须有根，不能只数支持项。
  tags: [ancient-core, aggregation, root, checklist]
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T05]

- id: P018
  title: 岁君只用于重大长程事项
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L917-L923）
  source_quote: "岁君只可占朝廷大事、年运久远之谋，家宅琐屑之事，不必用也。"
  summary: 年太岁只纳入国家、年运或长期事项；日常家庭小事不应强行引入。
  tags: [ancient-core, scope, annual-marker, relevance]
  task_ids: [ZSBY-T01, ZSBY-T04, ZSBY-T05]

- id: P019
  title: 舍卦身而取世爻
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L930-L936）
  source_quote: "古以卦身为我身，予试之不验，凡遇身者，即以世爻为主。"
  summary: 作者否定卦身作为主体指标，统一以世爻承担“我方/自身”角色。
  tags: [ancient-core, correction, subject, world-line]
  task_ids: [ZSBY-T02, ZSBY-T05]

- id: P020
  title: 世应只在双方事项中映射主客
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L938-L949）
  source_quote: "凡占彼此相干之事，以世为我，应为彼；若非彼此相干，不可拘泥。"
  summary: 只有确有对方参与的事项才把世、应解释为我方与对方；单方事项不得硬套。
  tags: [ancient-core, subject-object, scope, mapping]
  task_ids: [ZSBY-T01, ZSBY-T02, ZSBY-T08]

- id: P021
  title: 动爻为始变爻为终
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L951-L955）
  source_quote: "动为事之始，变为事之终。"
  summary: 解释过程顺序时，将动爻视为起始状态，变爻视为后续或结果状态，再检查生克冲合。
  tags: [ancient-core, sequence, transformation, interpretation]
  task_ids: [ZSBY-T04, ZSBY-T06]

- id: P022
  title: 多爻乱动时升级重占
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L957-L963）
  source_quote: "卦有乱动，事必纷纭……不若再占一卦。"
  summary: 多爻发动导致主线无法区分时，标记为信息冲突并重占；不是因为答案不合意而重占。
  tags: [ancient-core, conflict, recast, escalation]
  task_ids: [ZSBY-T05, ZSBY-T07]

- id: P023
  title: 用神有气且无阻才判可成
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L965-L967）
  source_quote: "用神有气无他故者，所求遂意；用神无气或受伤者，谋望难成。"
  summary: 先验用神是否有气，再审空破、受克、墓绝等阻碍；支持与阻碍必须同时结算。
  tags: [ancient-core, use-god, strength, blockers]
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T05]

- id: P024
  title: 空爻逢冲或填实后再作用
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L969-L975）
  source_quote: "空逢冲则实，动不为空；动而化空，亦待冲空填实之日应之。"
  summary: 旬空不是永久无效；静空、动空和化空分别等待冲、值或填实，必须把状态与时间分开。
  tags: [ancient-core, void, timing, state-transition]
  task_ids: [ZSBY-T04, ZSBY-T06]

- id: P025
  title: 合住之爻待冲开
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L971-L981）
  source_quote: "动而逢合，绊住不能动，待冲开之日月而应。"
  summary: 动爻被合时暂缓作用，至冲开时再应；爻与爻成合通常要求双方发动，不能仅凭静态邻接成立。
  tags: [ancient-core, combination, timing, conditions]
  task_ids: [ZSBY-T04, ZSBY-T06]

- id: P026
  title: 入墓须以冲开与根气复核
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L994-L1096）
  source_quote: "旺相者墓而不墓，衰弱者实为入墓；墓逢日月冲开，则出墓而有用。"
  summary: 入墓的有效性由旺衰根气决定，墓被日月冲开后状态改变；不得见“墓”即定死局。
  tags: [ancient-core, grave, strength, state-transition]
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06]

- id: P027
  title: 日月对爻的作用不对称
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1077-L1083）
  source_quote: "日月能克卦中之爻，卦中之爻不能克日月。"
  summary: 在本书内部模型中，月建与日辰是外部强条件，可作用于卦爻；不能反向以卦爻“克掉”日月。
  tags: [ancient-core, hierarchy, day-month, audit]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P028
  title: 官鬼持世须按事项分支
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1105-L1113）
  source_quote: "官鬼持世，非占功名官事，不可概以吉论；占忧疑疾病，又当以忧患推之。"
  summary: 同一结构在求官、诉讼、疾病、忧疑等不同领域含义相反，必须先完成问题分类。
  tags: [ancient-core, domain-routing, official-ghost, branch]
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T08]

- id: P029
  title: 不采用日德天干配六亲
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1133-L1146）
  source_quote: "古以日干配六亲，又以日德论吉凶，予试之不验，悉宜删去。"
  summary: 作者明确排除以日干另配六亲、以日德独断吉凶的方法，避免并行体系造成冲突。
  tags: [ancient-core, rejected-rule, consistency, audit]
  task_ids: [ZSBY-T02, ZSBY-T05]

- id: P030
  title: 忌神持世不是无条件失败
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1148-L1172）
  source_quote: "忌神持世，固多阻滞；若得日月制伏，或动而化生化合，仍有可成。"
  summary: 忌神持世先标为阻碍，再检查日月制伏、化生、化合等救应；不能以单一命中项盖过全局。
  tags: [ancient-core, hostile-god, exceptions, aggregation]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P031
  title: 不以旬空规避现实伤害
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1174-L1187）
  source_quote: "古有避凶之法，谓忌神旬空则可逃避，予试之不验。"
  summary: 作者否定把忌神旬空当成普遍避险方案；安全决策不得仅靠空亡解除。
  tags: [ancient-core, rejected-rule, safety, void]
  task_ids: [ZSBY-T05, ZSBY-T08]

- id: P032
  title: 化墓化绝化空先看本爻强弱
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1215-L1219）
  source_quote: "用神旺相，化墓化绝化空，未可便以凶断；衰弱受伤而又化凶，方为不利。"
  summary: 变爻状态必须与动爻本身旺衰、受伤与扶助合并判断，不能把状态标签独立当结论。
  tags: [ancient-core, transformation, strength, audit]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P033
  title: 不采用用神化同类即无用
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1219-L1223）
  source_quote: "古云用化用无用，予试之不验。"
  summary: 用神变成同一六亲不能自动判为无用，仍须按生克、旺衰、空破和事项判断。
  tags: [ancient-core, rejected-rule, transformation, correction]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P034
  title: 十二长生只取生旺墓绝
  type: rule
  source_chapter: 古籍主体·生旺墓绝章（raw-wikitext L1225-L1227）
  source_quote: "长生十二神，予只验长生、帝旺、墓、绝四者，其余不验。"
  summary: 本书内部只保留长生、帝旺、墓、绝四个状态，排除沐浴、冠带、临官等其余阶段。
  tags: [ancient-core, state-model, rejected-rule, simplification]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P035
  title: 变官鬼按强弱分支
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1229-L1240）
  source_quote: "用神旺相化鬼，鬼不能伤；用神休囚化鬼，灾祸易侵。"
  summary: 变出官鬼不是固定凶象；先检查用神旺衰和回头生克，再进入不同分支。
  tags: [ancient-core, transformation, branch, strength]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P036
  title: 回头克优先列为强阻碍
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1249-L1255）
  source_quote: "动而化回头克者，祸尤速。"
  summary: 变爻反克本动爻时，列为高优先级阻碍；仍需与日月、根气、空破及领域风险共同审计。
  tags: [ancient-core, return-overcoming, blocker, priority]
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06]

- id: P037
  title: 克用动爻须有力才成害
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1257-L1260）
  source_quote: "克用之爻虽动，若休囚无气，或被日月制伏，不能为害。"
  summary: 敌对动爻是否有效，取决于其自身旺衰、日月扶制和目标抗力；“动”本身不是充分条件。
  tags: [ancient-core, hostile-line, strength, causal-chain]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P038
  title: 同类过多以墓库收束
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1261-L1283）
  source_quote: "用神重叠太多，须看墓库收藏，冲开墓库之时乃应。"
  summary: 多个同类目标同时出现时，用墓库作为收束条件，并把冲开时点作为候选应期。
  tags: [ancient-core, duplicates, grave, timing]
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T06]

- id: P039
  title: 间爻只用于双方中介
  type: rule
  source_chapter: 古籍主体·间爻章（raw-wikitext L1285-L1286）
  source_quote: "间爻者，世应中间之爻也，惟占彼此相干之事，方可以中人论。"
  summary: 仅在双方互动问题中把世应之间的爻解释为中间人；无中介结构时不作此映射。
  tags: [ancient-core, intermediary, scope, mapping]
  task_ids: [ZSBY-T01, ZSBY-T08]

- id: P040
  title: 世爻静空与动空分开处理
  type: rule
  source_chapter: 古籍主体·世空章（raw-wikitext L1287-L1289）
  source_quote: "世空无故者，多主退悔；若世爻发动，空而不空，须待填实。"
  summary: 无其他原因的静态世空可作退意信号；世爻发动则保留作用并等待填实，不能同判。
  tags: [ancient-core, world-line, void, branch]
  task_ids: [ZSBY-T04, ZSBY-T06]

- id: P041
  title: 不以阴阳爻断过去未来
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1291-L1293）
  source_quote: "古以阳爻为过去，阴爻为未来，予试之不验。"
  summary: 作者排除以爻的阴阳直接映射过去或未来的时间法。
  tags: [ancient-core, rejected-rule, timing, audit]
  task_ids: [ZSBY-T05, ZSBY-T06]

- id: P042
  title: 用神克世只在特定领域成立
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1304-L1312）
  source_quote: "用神克世，惟占财、行人、医药有取，余占不可概论。"
  summary: “用神克世”的解释被限制在求财、行人、医药等指定问题，其他领域不得迁移套用。
  tags: [ancient-core, domain-boundary, use-god, scope]
  task_ids: [ZSBY-T05, ZSBY-T08]

- id: P043
  title: 合住与衰弱的应期恢复规则
  type: rule
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1327-L1331）
  source_quote: "合住者待冲，衰弱者待旺。"
  summary: 合住造成的延迟以冲开为候选恢复点；衰弱造成的延迟以得生、得旺为候选恢复点。
  tags: [ancient-core, timing, recovery, condition]
  task_ids: [ZSBY-T04, ZSBY-T06]

- id: P044
  title: 只追踪与所问有关的爻
  type: maxim
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1333-L1335）
  source_quote: "占此事，只看此事之用神；卦中虽有奇异之爻，与所问无涉，不可旁推。"
  summary: 分析范围由问题契约和用神限定；不因出现显眼符号而扩张到未问事项。
  tags: [ancient-core, relevance, question-contract, anti-overreach]
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T05]

- id: P045
  title: 六神不得越过五行主线
  type: rule
  source_chapter: 古籍主体·六神章（raw-wikitext L1337-L1343）
  source_quote: "六神不过附和之神，吉凶全在五行生克，不可舍五行而专用六神。"
  summary: 六神仅补充事物性质或形态，不得替代用神、旺衰和生克制化。
  tags: [ancient-core, six-spirits, evidence-priority, audit]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P046
  title: 长期判断追查根源
  type: principle
  source_chapter: 古籍主体·黄金策总断千金赋（raw-wikitext L1345-L1362）
  source_quote: "欲知久远，须察根源；根深者久，根浅者暂。"
  summary: 长期问题不只看当前强弱，还要追查支持链是否有根、阻碍是否真正清除。
  tags: [ancient-core, root-cause, long-horizon, audit]
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06]

- id: P047
  title: 学全规则但只用相关规则
  type: maxim
  source_chapter: 古籍主体·千金赋评释结语（raw-wikitext L1463-L1469）
  source_quote: "法须全学，用贵变通，不可执一。"
  summary: 规则库要完整学习，实际应用却只能选择与当前问题、条件和证据相符的规则。
  tags: [ancient-core, adaptability, relevance, anti-rigidity]
  task_ids: [ZSBY-T01, ZSBY-T05, ZSBY-T08]

- id: P048
  title: 一念一事并直陈所问
  type: checklist
  source_chapter: 古籍主体·卜筮正宗与用神分类章（raw-wikitext L1467-L1547）
  source_quote: "一念之诚，可格天地……占者须将所问之事直告，不可隐讳。"
  summary: 起卦前固定单一事项、真实意图与明确措辞；自己的事项原则上由自己起卦，代问时记录实际发问者。
  tags: [ancient-core, question-contract, intent, provenance]
  task_ids: [ZSBY-T01, ZSBY-T09]

- id: P049
  title: 天气占问必须限定现象与地点
  type: checklist
  source_chapter: 古籍主体·天时章（raw-wikitext L1628-L1660）
  source_quote: "占天时，须分欲晴、欲雨、欲风、欲雪，并须指定地方。"
  summary: 天气问题先确定要预测的现象、地理范围与时间范围，避免用一个模糊问题覆盖多种结果。
  tags: [ancient-core, weather, question-contract, domain]
  task_ids: [ZSBY-T01, ZSBY-T08]

- id: P050
  title: 天气用神映射
  type: calculation
  source_chapter: 古籍主体·天时章（raw-wikitext L1636-L1740）
  source_quote: "子孙为日月，主晴；父母为雨雪；兄弟为风云；官鬼为雷电阴雾；妻财为晴之元神。"
  summary: 按所问天气类型选取六亲并结合发动、旺衰与制化；映射只属于该历史术数体系。
  tags: [ancient-core, weather, use-selection, historical-divination]
  task_ids: [ZSBY-T03, ZSBY-T08]
  inputs: [所问天气类型, 六亲分布, 动静, 旺衰]
  formula: "晴→子孙（妻财为元神）；雨雪→父母；风云→兄弟；雷电阴雾→官鬼"
  units: 天气类别与六亲类别
  output: 天气问题的主用神及辅助神
  missing_conditions: 不具现代气象学验证；地点、季节、时间范围和多爻冲突必须另行处理。

- id: P051
  title: 天气动变按先后解释
  type: rule
  source_chapter: 古籍主体·天时章（raw-wikitext L1742-L1752）
  source_quote: "动爻为先，变爻为后；如父动化子，先雨后晴；子动化父，先晴后雨。"
  summary: 天气转换以动爻表示前段、变爻表示后段，形成可检验的顺序预测。
  tags: [ancient-core, weather, sequence, transformation]
  task_ids: [ZSBY-T06, ZSBY-T08]

- id: P052
  title: 天气应期按动静空破分支
  type: rule
  source_chapter: 古籍主体·天时章（raw-wikitext L1845-L1870）
  source_quote: "动而逢合逢值，静而逢值逢冲；旬空待填冲，月破待填合。"
  summary: 天气用神发动时看逢值或逢合，静止时看逢值或逢冲；旬空、月破另等填实、冲开或合起。
  tags: [ancient-core, weather, timing, branch]
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T08]

- id: P053
  title: 不用四时旺衰替代天气用神
  type: rule
  source_chapter: 古籍主体·天时章（raw-wikitext L1703-L1714）
  source_quote: "古以四时旺衰断晴雨，又以子孙为雪，予试之不验。"
  summary: 作者排除仅按季节旺衰断晴雨和把子孙直接当雪的旧法，要求仍回到所问天气与用神。
  tags: [ancient-core, weather, rejected-rule, audit]
  task_ids: [ZSBY-T05, ZSBY-T08]

- id: P054
  title: 终身类问题拆分领域
  type: checklist
  source_chapter: 古籍主体·身命章（raw-wikitext L2073-L2083）
  source_quote: "占终身者，财、官、寿、父母、兄弟、妻子，须各分占，不可一卦包断。"
  summary: 把终身总问拆成财富、事业、寿命、父母、手足、婚姻、子女等可独立验证的子问题。
  tags: [ancient-core, decomposition, life-reading, question-contract]
  task_ids: [ZSBY-T01, ZSBY-T07, ZSBY-T08]

- id: P055
  title: 终身财福分看世财子
  type: checklist
  source_chapter: 古籍主体·终身财福章（raw-wikitext L2081-L2160）
  source_quote: "占终身财福，先看世爻，再看财爻，又看子孙；三者各有旺衰生克，不可只凭一爻。"
  summary: 终身财务问题同时检查主体承受力、财爻资源和子孙源头，并处理六合、六冲、空破的条件性影响。
  tags: [ancient-core, finance, checklist, aggregation]
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T08]

- id: P056
  title: 世弱世空不直接推出贫夭
  type: rule
  source_chapter: 古籍主体·终身财福章（raw-wikitext L2090-L2155）
  source_quote: "世爻衰弱，不可即断贫夭；得日月生扶，或财福旺而相生，仍为有济。"
  summary: 世爻弱、空、遇冲合都须与日月、财福、根气合并判断，拒绝单指标决定终身结果。
  tags: [ancient-core, life-reading, correction, aggregation]
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T08]

- id: P057
  title: 寿命只取世爻且不用固定年轮
  type: rule
  source_chapter: 古籍主体·寿元章（raw-wikitext L2347-L2373）
  source_quote: "占寿只以世爻为用……古以六爻每爻管五年，予试之不验。"
  summary: 寿命占以世爻为主，并明确排除“每爻固定管五年”的机械换算；属高风险历史规则，不可作医学或寿命决策。
  tags: [ancient-core, longevity, rejected-rule, high-risk]
  task_ids: [ZSBY-T05, ZSBY-T08]

- id: P058
  title: 亲属问题先指定具体对象
  type: checklist
  source_chapter: 古籍主体·父母兄弟妻子章（raw-wikitext L2561-L2705）
  source_quote: "父母须分占父与母，兄弟多人须指明所问何人，妻妾亦不可混占。"
  summary: 同一六亲类别包含多人时，先写明父或母、哪位手足、哪位伴侣，避免结果无法对应。
  tags: [ancient-core, relatives, disambiguation, question-contract]
  task_ids: [ZSBY-T01, ZSBY-T08]

- id: P059
  title: 子女问题区分过去现在未来
  type: rule
  source_chapter: 古籍主体·子嗣章（raw-wikitext L2695-L2710）
  source_quote: "问子须分已生、现在有孕、将来求子；将来之占，不可以过去之事混断。"
  summary: 子女问题按已发生、当前妊娠、未来计划拆分，时间框架不同则用神与可验证结果也不同。
  tags: [ancient-core, children, time-scope, decomposition]
  task_ids: [ZSBY-T01, ZSBY-T06, ZSBY-T08]

- id: P060
  title: 代占亲属先查代占者风险
  type: rule
  source_chapter: 古籍主体·代占六亲章（raw-wikitext L2755-L2764）
  source_quote: "代占六亲，先看世爻有无受伤；世若大凶，须防占者自身。"
  summary: 代问他人时保留世爻作为发问者检查项，再看被问亲属；属于历史体系中的双层安全审计。
  tags: [ancient-core, proxy-question, safety-check, relatives]
  task_ids: [ZSBY-T04, ZSBY-T08, ZSBY-T09]

- id: P061
  title: 对具体文本或方位直接起问
  type: rule
  source_chapter: 古籍主体·学业与求名章（raw-wikitext L2769-L2785）
  source_quote: "欲习何经何书，即指其书而占，不必以五行分经史子集。"
  summary: 面对具体书、职业或目的地，直接指定对象起问；不先用宽泛五行类比替代真实对象。
  tags: [ancient-core, direct-question, rejected-mapping, specificity]
  task_ids: [ZSBY-T01, ZSBY-T05, ZSBY-T08]

- id: P062
  title: 考试按阶段分别占问
  type: checklist
  source_chapter: 古籍主体·考试章（raw-wikitext L2843-L2920）
  source_quote: "童试、乡试、会试、殿试，各有日期，各宜分占；不可一卦统问。"
  summary: 把资格、各轮考试、录取和名次拆成独立事项，并为每项记录应期；成绩判断再核父母、官鬼与世爻。
  tags: [ancient-core, education, decomposition, checklist]
  task_ids: [ZSBY-T01, ZSBY-T06, ZSBY-T08]

- id: P063
  title: 事项结果与发生时间分开判
  type: work_template
  source_chapter: 古籍主体·考试与求名诸章（raw-wikitext L2921-L2934）
  source_quote: "先定成败，再推应期；吉凶未明，不可先拘某日。"
  summary: 先完成能否发生的状态判断，再用值、冲、合、填实等规则生成时间候选，避免时间规则反向决定结果。
  tags: [ancient-core, outcome-first, timing, workflow]
  task_ids: [ZSBY-T04, ZSBY-T06]

- id: P064
  title: 求官先核资格与职位对象
  type: checklist
  source_chapter: 古籍主体·求仕章（raw-wikitext L3090-L3135）
  source_quote: "求官须问有无资格、何官何任、已得候补或初求，各宜分别。"
  summary: 求职求官先固定资格、目标职位、阶段与地点，再选择官鬼、父母、世爻等指标；不可把所有职业问题归成一问。
  tags: [ancient-core, career, prerequisites, decomposition]
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T08]

- id: P065
  title: 高风险诉求遇严重阻碍即停止
  type: rule
  source_chapter: 古籍主体·上书叩阍章（raw-wikitext L3200-L3230）
  source_quote: "若世用受重克、入墓绝而无救，不可妄进；为公为民者，亦须卦象明白方可行。"
  summary: 请愿、诉讼、军事等高风险行动遇多重无救阻碍时应停止；即使自称公益，也要要求证据清晰并转交现实专业程序。
  tags: [ancient-core, high-risk, stop-rule, public-interest]
  task_ids: [ZSBY-T05, ZSBY-T07, ZSBY-T08]

- id: P066
  title: 库存买卖按强弱与根气决策
  type: rule
  source_chapter: 古籍主体·囤货卖货章（raw-wikitext L3468-L3483）
  source_quote: "财旺宜卖，财衰有根可守可买；财衰无根者，不宜收存。"
  summary: 在本书历史模型中，财旺对应出售候选，财弱但有根可等待，财弱无根则不继续囤积。
  tags: [ancient-core, commerce, inventory, historical-divination]
  task_ids: [ZSBY-T04, ZSBY-T08]

- id: P067
  title: 商品须先区分期限
  type: checklist
  source_chapter: 古籍主体·囤货卖货章（raw-wikitext L3485-L3493）
  source_quote: "货有时限者与无时限者不同，先问何时须售，方可定迟速。"
  summary: 商品决策先记录保质、交割或资金期限；有期限与可长期持有的商品不能共用同一等待策略。
  tags: [ancient-core, commerce, horizon, question-contract]
  task_ids: [ZSBY-T01, ZSBY-T06, ZSBY-T08]

- id: P068
  title: 商品应期按旺衰空破恢复
  type: rule
  source_chapter: 古籍主体·卖货宜守章（raw-wikitext L3493-L3505）
  source_quote: "旺者逢墓冲，衰者逢生旺，空者逢填冲，破者逢填合，皆为可售之期。"
  summary: 先识别财爻当前阻碍，再以对应的状态解除点作为出售时机候选。
  tags: [ancient-core, commerce, timing, state-transition]
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T08]

- id: P069
  title: 买卖地点与方向须明确
  type: checklist
  source_chapter: 古籍主体·卖货往何方章（raw-wikitext L3524-L3543）
  source_quote: "在本地卖、往外地卖、往何方卖，须各指明而占。"
  summary: 把本地、外地和具体方向写进问题，不凭事后结果再改变地点解释。
  tags: [ancient-core, commerce, location, specificity]
  task_ids: [ZSBY-T01, ZSBY-T08]

- id: P070
  title: 借贷区分求财与偿还能力
  type: checklist
  source_chapter: 古籍主体·借贷放债章（raw-wikitext L3569-L3595）
  source_quote: "借贷者，占其能借否；放债者，占彼能还否，世应财爻各有所主。"
  summary: 借入与贷出是不同问题：前者问能否获得资金，后者还要审查对方与偿还；不得共用一个财爻结论。
  tags: [ancient-core, lending, counterparty, decomposition]
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T08]

- id: P071
  title: 不为悖德牟利提供占断
  type: maxim
  source_chapter: 古籍主体·赌博与谋财章（raw-wikitext L3605-L3632）
  source_quote: "惠迪吉，从逆凶，何须问卜。"
  summary: 对赌博、欺诈、侵害他人等悖德求利，不进入术数优化流程，直接以现实法律与伦理边界停止。
  tags: [ancient-core, ethics, stop-rule, finance]
  task_ids: [ZSBY-T07, ZSBY-T08]

- id: P072
  title: 婚姻基础与父母干预分开问
  type: checklist
  source_chapter: 古籍主体·婚姻章（raw-wikitext L3635-L3754）
  source_quote: "婚姻先占夫妇本身，再占父母允否；不可将二事混为一断。"
  summary: 先固定双方意愿与关系本身，再把父母同意、财礼、日期等外部条件拆开；书中也反对强成不愿之婚。
  tags: [ancient-core, marriage, consent, decomposition]
  task_ids: [ZSBY-T01, ZSBY-T07, ZSBY-T08]

- id: P073
  title: 妊娠问题先安全后其他属性
  type: checklist
  source_chapter: 古籍主体·胎孕章（raw-wikitext L3756-L3800）
  source_quote: "临产危急，只宜占母子安危，不可先问男女。"
  summary: 将是否怀孕、母体安全、胎儿安全、分娩时间分开；紧急情况只处理安全并立即转医疗系统。
  tags: [ancient-core, pregnancy, high-risk, safety]
  task_ids: [ZSBY-T01, ZSBY-T07, ZSBY-T08]

- id: P074
  title: 古籍胎儿性别推断式
  type: calculation
  source_chapter: 古籍主体·胎孕章（raw-wikitext L3760-L3771）
  source_quote: "以子孙爻之阴阳、卦宫阴阳等推男女，须兼看旺衰动变。"
  summary: 记录古籍内部的胎儿性别推断候选，仅供文献忠实性；不可替代医学检查，也不应支持性别选择。
  tags: [ancient-core, pregnancy, historical-divination, unsafe-inference]
  task_ids: [ZSBY-T04, ZSBY-T08, ZSBY-T09]
  inputs: [子孙爻阴阳, 卦宫阴阳, 旺衰, 动变]
  formula: 原文以阴阳组合及动变作男女分支，非单一数值公式
  units: 阴阳类别
  output: 古籍声称的男女判断
  missing_conditions: 缺乏医学与统计验证；不适用于临床、伦理或生育决策。

- id: P075
  title: 出行目的地与归期分开
  type: checklist
  source_chapter: 古籍主体·出行行人章（raw-wikitext L3805-L3846）
  source_quote: "占出行先看世爻，占彼处看应爻；问归期与问安危，各宜分占。"
  summary: 出行问题先审自身，再审目的地；是否安全、能否到达、何时返回是不同任务，不应互相替代。
  tags: [ancient-core, travel, decomposition, subject-object]
  task_ids: [ZSBY-T01, ZSBY-T06, ZSBY-T08]

- id: P076
  title: 疾病必须转医疗且不得以祭祀代治
  type: rule
  source_chapter: 古籍主体与现代增补·疾病鬼神章（raw-wikitext L3945-L4020, L121-L124）
  source_quote: "切不可听信祭鬼而不服药，误人性命。"
  summary: 古籍主体已警告不可用祭祀取代服药；现代录入者进一步明确“生病应该找医生”。所有疾病规则只作历史材料。
  tags: [ancient-core, modern-editorial, medical-safety, provenance]
  task_ids: [ZSBY-T07, ZSBY-T08, ZSBY-T09]

- id: P077
  title: 不由卦象开药或定针灸
  type: rule
  source_chapter: 古籍主体·医药章（raw-wikitext L4145-L4155）
  source_quote: "以卦定药之寒热、定针灸穴道，予试之不验，且恐误人。"
  summary: 作者排除从卦象推药性、剂量、穴位或治疗方案；治疗必须交由合格医疗人员。
  tags: [ancient-core, rejected-rule, medical-safety, stop-rule]
  task_ids: [ZSBY-T05, ZSBY-T07, ZSBY-T08]

- id: P078
  title: 家宅问题按家庭成员分占
  type: checklist
  source_chapter: 古籍主体·家宅章（raw-wikitext L4158-L4223）
  source_quote: "一卦不可统断一家吉凶，父母、兄弟、妻子，各宜另占。"
  summary: 房屋状态与每位家庭成员的健康、迁入适应等拆开记录，避免一卦给整家人贴同一结论。
  tags: [ancient-core, housing, household, decomposition]
  task_ids: [ZSBY-T01, ZSBY-T07, ZSBY-T08]

- id: P079
  title: 六畜按物种分别问
  type: checklist
  source_chapter: 古籍主体·六畜章（raw-wikitext L4227-L4242）
  source_quote: "牛马猪羊鸡犬，不可一卦混占，须指明何畜。"
  summary: 不同牲畜分别建问题与用神记录，防止用一个模糊类别事后任意对应。
  tags: [ancient-core, livestock, specificity, decomposition]
  task_ids: [ZSBY-T01, ZSBY-T08]

- id: P080
  title: 宅墓问题先写明具体疑因
  type: work_template
  source_chapter: 古籍主体·旧宅与坟墓章（raw-wikitext L4244-L4495）
  source_quote: "疑是何处何故，即指其事而占；修后欲知已除否，再占为法。"
  summary: 先记录怀疑的具体位置、原因和拟采取的修复；修复后的验证另起一问，不用原卦循环解释。
  tags: [ancient-core, housing, grave, verification]
  task_ids: [ZSBY-T01, ZSBY-T06, ZSBY-T07, ZSBY-T08]

- id: P081
  title: 禁止盗葬侵地
  type: maxim
  source_chapter: 古籍主体·坟茔章（raw-wikitext L4465-L4475）
  source_quote: "盗葬他人之地，损人利己，天理不容，何必占之。"
  summary: 对侵占他人土地或盗葬的请求直接停止，不提供择时、方位或规避方案。
  tags: [ancient-core, ethics, stop-rule, land]
  task_ids: [ZSBY-T07, ZSBY-T08]

- id: P082
  title: 初学者四步最小流程
  type: work_template
  source_chapter: 古籍主体·增删卜易评释要领（raw-wikitext L4697-L4721）
  source_quote: "先装卦，次取用神，三看日月动变生克，四定吉凶应期。"
  summary: 以装卦、取用、聚合条件、输出结论与应期构成最小可执行流程；每步保留前提和冲突记录。
  tags: [ancient-core, workflow, novice, checklist]
  task_ids: [ZSBY-T02, ZSBY-T03, ZSBY-T04, ZSBY-T06]

- id: P083
  title: 现代增补的铜钱起卦编码
  type: calculation
  source_chapter: 现代增补·摇卦法（raw-wikitext L4602-L4692）
  source_quote: "三枚钱共掷六次，第一次为初爻，自下而上；三字为老阴，三背为老阳，一背二字为少阳，二背一字为少阴。"
  summary: 六次投掷自下而上记录本卦，老阴老阳作为动爻生成变卦；该段被文本明确标为疑似录入者增补。
  tags: [modern-editorial, casting, formula, provenance]
  task_ids: [ZSBY-T02, ZSBY-T09]
  inputs: [每次三枚钱的正反面, 六次投掷顺序]
  formula: "三字→老阴(动)；三背→老阳(动)；一背二字→少阳；二背一字→少阴；第1次置初爻"
  units: 六次三枚钱结果
  output: 六爻本卦、动爻与变卦
  missing_conditions: 字/背对应哪一面由版本约定；概率公平性和异常投掷重来规则未说明。

- id: P084
  title: 四来源强弱聚合
  type: calculation
  source_chapter: 古籍主体·用神元神忌神仇神章（raw-wikitext L4734-L4756）
  source_quote: "月建、日辰、动爻、变爻，四处皆来生扶为吉；三处克而一处生，须看一处有力无力；两生两克，较量旺衰。"
  summary: 把月、日、动爻、变爻作为四类外部作用源，先计方向再比强弱；票数相等或少数强源时不得机械多数决。
  tags: [ancient-core, aggregation, calculation, conflict]
  task_ids: [ZSBY-T04, ZSBY-T05]
  inputs: [月建对用神作用, 日辰对用神作用, 动爻对用神作用, 变爻对本爻作用, 各源旺衰有效性]
  formula: "4扶→强支持；3扶1克→偏支持；2扶2克→比较强弱；3克1扶→仅在扶源强而有效时可救；4克→强阻碍"
  units: 有效作用源数量与强度等级
  output: 支持、冲突、阻碍及需复核条件
  missing_conditions: 强弱没有统一数值刻度；空破、合绊、墓绝、根气会改变每一作用源是否有效。

- id: P085
  title: 六亲由宫五行与爻五行计算
  type: calculation
  source_chapter: 古籍主体·安六亲章（raw-wikitext L5076-L5102）
  source_quote: "生我者父母，我生者子孙，克我者官鬼，我克者妻财，比和者兄弟。"
  summary: 以所属卦宫五行为“我”，比较每爻五行的生克比和，得到六亲角色。
  tags: [ancient-core, six-relations, formula, casting]
  task_ids: [ZSBY-T02]
  inputs: [卦宫五行, 各爻地支五行]
  formula: "爻生宫→父母；宫生爻→子孙；爻克宫→官鬼；宫克爻→妻财；同五行→兄弟"
  units: 五行关系类别
  output: 各爻六亲
  missing_conditions: 必须先正确确定卦宫和纳甲地支；现代增补L5097仅为解释性复述。

- id: P086
  title: 纳甲装支查表
  type: calculation
  source_chapter: 古籍主体·装卦纳甲章（raw-wikitext L5045-L5070）
  source_quote: "乾内卦子寅辰，外卦午申戌；坤内卦未巳卯，外卦丑亥酉。"
  summary: 按八经卦及内外卦位置查六爻地支，再据地支定五行；必须保留原版本表，不擅自修正文句。
  tags: [ancient-core, najia, lookup-table, casting]
  task_ids: [ZSBY-T02, ZSBY-T05, ZSBY-T09]
  inputs: [上卦, 下卦, 爻位]
  formula: 按原文八经卦内外纳支表映射
  units: 卦名与爻位
  output: 每爻所纳地支及五行
  missing_conditions: 原始文本可能含异文或录入误字；需以source_quote和版本来源保留可追溯性。

- id: P087
  title: 世应位置查表
  type: calculation
  source_chapter: 古籍主体·安世应章（raw-wikitext L5106-L5117）
  source_quote: "八纯卦世在六爻，应在三爻；一世卦世在初，应在四；二世卦世在二，应在五；三世卦世在三，应在六。"
  summary: 先判定八宫序位，再按世位与相隔三爻确定应位；游魂、归魂使用各自表项。
  tags: [ancient-core, world-response, formula, casting]
  task_ids: [ZSBY-T02]
  inputs: [所属八宫, 宫内序位]
  formula: "八纯世6应3；一世世1应4；二世世2应5；三世世3应6；四世世4应1；五世世5应2；游魂世4应1；归魂世3应6"
  units: 六爻位次
  output: 世爻位与应爻位
  missing_conditions: 必须先正确识别宫内序位；不同版本的游魂归魂口诀需核对。

- id: P088
  title: 动爻阴阳反转生成变卦
  type: calculation
  source_chapter: 古籍主体·变卦章（raw-wikitext L5123-L5163）
  source_quote: "老阴变少阳，老阳变少阴；不动之爻仍旧。"
  summary: 仅反转发动爻的阴阳，其他爻保持不变，由六个新爻组成变卦，再装变爻地支与六亲。
  tags: [ancient-core, transformation, formula, casting]
  task_ids: [ZSBY-T02]
  inputs: [本卦六爻阴阳, 动爻集合]
  formula: "动阴→阳；动阳→阴；静爻不变"
  units: 六个爻位的二元状态
  output: 变卦与各动爻对应变爻
  missing_conditions: 需先有可靠动爻记录；变爻的作用范围另受本爻关系限制。

- id: P089
  title: 用元忌仇的关系链
  type: calculation
  source_chapter: 古籍主体·用神元神忌神仇神章（raw-wikitext L5165-L5192）
  source_quote: "生用神者为元神，克用神者为忌神，生忌神而克元神者为仇神。"
  summary: 选定用神后，按生克链派生元神、忌神与仇神，所有角色都随用神变化而变化。
  tags: [ancient-core, four-gods, formula, use-selection]
  task_ids: [ZSBY-T03, ZSBY-T04]
  inputs: [用神五行, 其余爻五行]
  formula: "生用→元神；克用→忌神；生忌且克元→仇神"
  units: 五行关系类别
  output: 每爻相对于用神的功能角色
  missing_conditions: 角色只表示方向，实际有效性还需旺衰、动静、空破、合墓等条件。

- id: P090
  title: 元神忌神有效性清单
  type: checklist
  source_chapter: 古籍主体·元神忌神衰旺章（raw-wikitext L5207-L5232）
  source_quote: "元神旺相或临日月、发动化回头生、长生帝旺者有力；休囚空破、被克、化绝墓退者无力。"
  summary: 元神与忌神都先经过有效性门槛，再进入聚合；名称为“元”不保证能生，名称为“忌”不保证能克。
  tags: [ancient-core, four-gods, validation, checklist]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P091
  title: 五行生克固定映射
  type: calculation
  source_chapter: 古籍主体·五行相生相克章（raw-wikitext L5247-L5282）
  source_quote: "金生水，水生木，木生火，火生土，土生金；金克木，木克土，土克水，水克火，火克金。"
  summary: 以固定五行有向图计算生与克，作为六亲、用元忌仇和作用链的底层映射。
  tags: [ancient-core, five-elements, formula, foundation]
  task_ids: [ZSBY-T02, ZSBY-T04]
  inputs: [作用者五行, 受作用者五行]
  formula: "生环=金→水→木→火→土→金；克环=金→木→土→水→火→金"
  units: 五行类别
  output: 生、克或比和
  missing_conditions: 只给关系方向，不含旺衰、距离、动静与日月权重。

- id: P092
  title: 受克但得生时合并评估
  type: rule
  source_chapter: 古籍主体·克处逢生章（raw-wikitext L5308-L5324）
  source_quote: "用神受克，若又得日月动爻来生，谓之克处逢生，不可即以凶断。"
  summary: 目标同时受克与得生时标记冲突，比较两边有效性与根气，不允许先见受克就停止。
  tags: [ancient-core, conflict, aggregation, recovery]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P093
  title: 变爻只作用于本动爻
  type: rule
  source_chapter: 古籍主体·动变生克章（raw-wikitext L5367-L5380）
  source_quote: "变爻只能生克冲合本位动爻，不能越位生克旁爻；日月则可作用诸爻。"
  summary: 变爻的直接作用范围局限于产生它的动爻；日辰、月建才是全局作用源。
  tags: [ancient-core, transformation, locality, causal-scope]
  task_ids: [ZSBY-T02, ZSBY-T04, ZSBY-T05]

- id: P094
  title: 四时旺相休囚查表
  type: calculation
  source_chapter: 古籍主体·四时旺相章（raw-wikitext L5393-L5412）
  source_quote: "春木旺火相水休金囚土死；夏火旺土相木休水囚金死；秋金旺水相土休火囚木死；冬水旺木相金休土囚火死。"
  summary: 按季节为五行赋旺、相、休、囚、死状态，作为强弱的一项输入而非单独结论。
  tags: [ancient-core, season, strength, lookup-table]
  task_ids: [ZSBY-T04]
  inputs: [季节或月令, 目标五行]
  formula: 按春夏秋冬五行旺相休囚死表映射
  units: 五级状态类别
  output: 目标五行的季节状态
  missing_conditions: 月建、日辰、动变、空破、墓绝和根气仍可能改变综合强弱。

- id: P095
  title: 月建为当月全局权重
  type: rule
  source_chapter: 古籍主体·月将章（raw-wikitext L5417-L5481）
  source_quote: "月建能生克冲合卦中诸爻，月内司权；出月则权移，月破之爻亦可填实。"
  summary: 月建作用于全部爻，在当月权重最高；出月后需重新结算，尤其不能把月破永久化。
  tags: [ancient-core, month, global-effect, timing]
  task_ids: [ZSBY-T04, ZSBY-T06]

- id: P096
  title: 日辰为全程全局条件
  type: rule
  source_chapter: 古籍主体·日辰章（raw-wikitext L5507-L5524）
  source_quote: "日辰为六爻之主宰，能生克冲合诸爻，自始至终有权。"
  summary: 日辰对全卦各爻提供生、克、冲、合和暗动条件；仍要区分其具体作用而非只记吉凶标签。
  tags: [ancient-core, day, global-effect, timing]
  task_ids: [ZSBY-T04, ZSBY-T06]

- id: P097
  title: 六神按日干顺排
  type: calculation
  source_chapter: 古籍主体·六神章（raw-wikitext L5549-L5572）
  source_quote: "甲乙日起青龙，丙丁日起朱雀，戊日起勾陈，己日起腾蛇，庚辛日起白虎，壬癸日起玄武，自初爻顺排。"
  summary: 依据日干确定初爻六神，再按固定次序逐爻上排；六神只作辅助描述。
  tags: [ancient-core, six-spirits, formula, auxiliary]
  task_ids: [ZSBY-T02, ZSBY-T04]
  inputs: [日干, 爻位]
  formula: "起点：甲乙青龙、丙丁朱雀、戊勾陈、己腾蛇、庚辛白虎、壬癸玄武；序列青龙→朱雀→勾陈→腾蛇→白虎→玄武"
  units: 六爻位次
  output: 每爻六神
  missing_conditions: 六神不独立决定吉凶，必须服从用神与五行主线。

- id: P098
  title: 六合分六种来源
  type: checklist
  source_chapter: 古籍主体·六合章（raw-wikitext L5597-L5608）
  source_quote: "有月合、日合、动爻合、动化合、卦逢六合、六冲变六合，须分其所从来。"
  summary: 记录合的来源和对象；不同来源影响作用范围、是否绊住以及何时被冲开。
  tags: [ancient-core, combination, taxonomy, timing]
  task_ids: [ZSBY-T04, ZSBY-T06]

- id: P099
  title: 三合局的组成与成局条件
  type: calculation
  source_chapter: 古籍主体·三合章（raw-wikitext L5644-L5653）
  source_quote: "申子辰合水局，亥卯未合木局，寅午戌合火局，巳酉丑合金局；三字须具，且有发动者方成。"
  summary: 三个地支必须凑齐指定组合，并满足发动等条件才建立三合局；缺一项不能直接按局论。
  tags: [ancient-core, triple-combination, formula, validation]
  task_ids: [ZSBY-T04, ZSBY-T05]
  inputs: [卦中及日月的地支集合, 各爻动静]
  formula: "{申,子,辰}→水；{亥,卯,未}→木；{寅,午,戌}→火；{巳,酉,丑}→金"
  units: 三地支集合
  output: 是否成局及局五行
  missing_conditions: 原文不同情形对日月补字、静爻和变爻能否成局有细分，需保留来源逐项核验。

- id: P100
  title: 六冲固定配对
  type: calculation
  source_chapter: 古籍主体·六冲章（raw-wikitext L5670-L5681）
  source_quote: "子午冲、丑未冲、寅申冲、卯酉冲、辰戌冲、巳亥冲。"
  summary: 用固定地支配对识别冲，再按月冲、日冲、爻冲、卦冲及动静决定作用。
  tags: [ancient-core, clash, formula, state-change]
  task_ids: [ZSBY-T04, ZSBY-T06]
  inputs: [两个地支]
  formula: "冲集合={{子,午},{丑,未},{寅,申},{卯,酉},{辰,戌},{巳,亥}}"
  units: 地支无序对
  output: 是否相冲
  missing_conditions: 相冲的后果依旺衰、动静、空破和是冲散还是冲起而变。

- id: P101
  title: 三刑只在弱而受伤时采纳
  type: rule
  source_chapter: 古籍主体·三刑章（raw-wikitext L5744-L5754）
  source_quote: "寅巳申、丑戌未为三刑，子卯相刑；用神旺相者刑而不伤，休囚受制者方为害。"
  summary: 先识别刑的组合，再以目标是否休囚受制作为伤害门槛；不把“见刑”直接当结果。
  tags: [ancient-core, punishment, strength, condition]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P102
  title: 日冲静旺爻可成暗动
  type: rule
  source_chapter: 古籍主体·暗动章（raw-wikitext L5765-L5777）
  source_quote: "静爻旺相而被日辰冲者为暗动；休囚被冲者为日破。"
  summary: 同样受日冲，旺相静爻进入暗动，休囚静爻则偏向破损；强弱是分支条件。
  tags: [ancient-core, hidden-movement, day-clash, branch]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P103
  title: 不采用动爻自动冲散
  type: rule
  source_chapter: 古籍主体·动散章（raw-wikitext L5789-L5799）
  source_quote: "古以动爻逢冲为散，予试之，旺相有气者冲而愈动，休囚无气者方散。"
  summary: 动爻被冲后的结果取决于旺衰；旺者可能被激活，弱者才可能冲散。
  tags: [ancient-core, rejected-rule, movement, strength]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P104
  title: 六爻全变须回到用神
  type: rule
  source_chapter: 古籍主体·卦变章（raw-wikitext L5811-L5828）
  source_quote: "六爻全动，虽卦变其名，仍须以用神旺衰生克为主。"
  summary: 整卦变化带来高度不稳定信号，但不能只按卦名之变裁决，仍需用神与作用链。
  tags: [ancient-core, all-lines-moving, use-god, audit]
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T05]

- id: P105
  title: 反吟伏吟只作条件信号
  type: rule
  source_chapter: 古籍主体·反吟伏吟章（raw-wikitext L5831-L5882）
  source_quote: "反吟主反复，伏吟主呻吟不进，然亦须看用神，不可舍用神执卦名而断。"
  summary: 反吟、伏吟描述反复或停滞倾向，只能在用神与全局条件支持时采用。
  tags: [ancient-core, repetition, auxiliary, evidence-priority]
  task_ids: [ZSBY-T04, ZSBY-T05]

- id: P106
  title: 旬空表与填冲规则
  type: calculation
  source_chapter: 古籍主体·旬空章（raw-wikitext L5887-L5905）
  source_quote: "甲子旬戌亥空，甲戌旬申酉空，甲申旬午未空，甲午旬辰巳空，甲辰旬寅卯空，甲寅旬子丑空。"
  summary: 以六旬查两空支；静空待填或冲，动空与化空保留条件性作用，不能统一当无效。
  tags: [ancient-core, void, lookup-table, timing]
  task_ids: [ZSBY-T04, ZSBY-T06]
  inputs: [日柱所属旬]
  formula: "甲子旬→戌亥；甲戌旬→申酉；甲申旬→午未；甲午旬→辰巳；甲辰旬→寅卯；甲寅旬→子丑"
  units: 旬与地支对
  output: 当旬两个空亡地支
  missing_conditions: 实际作用还需区分真空、假空、动空、化空及填实或冲实时间。

- id: P107
  title: 生旺墓绝查表
  type: calculation
  source_chapter: 古籍主体·生旺墓绝章（raw-wikitext L5958-L5992）
  source_quote: "水土长生在申、旺在子、墓在辰、绝在巳；木长生亥、旺卯、墓未、绝申；火长生寅、旺午、墓戌、绝亥；金长生巳、旺酉、墓丑、绝寅。"
  summary: 依五行与所临地支查长生、帝旺、墓、绝；状态是否造成结果仍由目标旺衰和冲合决定。
  tags: [ancient-core, life-stages, lookup-table, strength]
  task_ids: [ZSBY-T04]
  inputs: [目标五行, 所临地支]
  formula: "水土:生申旺子墓辰绝巳；木:生亥旺卯墓未绝申；火:生寅旺午墓戌绝亥；金:生巳旺酉墓丑绝寅"
  units: 五行与地支类别
  output: 长生、帝旺、墓、绝或非四状态
  missing_conditions: 本书排除其余八阶段；入墓、逢绝的效力必须再看有无根气、生扶和冲开。

- id: P108
  title: 各门类应期总表
  type: calculation
  source_chapter: 古籍主体·各门类应期总注章（raw-wikitext L6017-L6035）
  source_quote: "静而逢值逢冲，动而逢合逢值；太旺逢墓逢冲，衰绝遇生遇旺，入墓喜冲开，六合宜相击，月破喜填，旬空爱填冲。"
  summary: 先识别主事爻所处状态，再按状态的解除或触发条件生成应期候选；远事用年月、近事用日时。
  tags: [ancient-core, timing, formula, state-transition]
  task_ids: [ZSBY-T04, ZSBY-T06]
  inputs: [主事爻动静, 旺衰, 合冲, 墓, 月破, 旬空, 进退, 事件远近]
  formula: "静→值/冲；动→合/值；过旺→墓/冲；衰绝→生/旺；墓→冲开；合→冲开；月破→填/合；旬空→填/冲；远→年月；近→日时"
  units: 月、日、时或干支触发条件
  output: 一个或多个候选应期及触发理由
  missing_conditions: 原文承认占远应近、占近应远等例外；候选冲突时没有统一数值排序法。

- id: P109
  title: 卦意不明才允许再占
  type: rule
  source_chapter: 古籍主体·各门类应期总注章（raw-wikitext L6032-L6035）
  source_quote: "倘遇卦之不明，再占是一法。卦有恍惚者，再占一卦，不可妄断。"
  summary: 只有信息含混、规则冲突而无法形成结论时才升级重占；应记录触发原因，并与现代“一事不再三占”共同执行。
  tags: [ancient-core, ambiguity, recast, conflict]
  task_ids: [ZSBY-T05, ZSBY-T07, ZSBY-T09]

- id: P110
  title: 游魂归魂不得替代用神
  type: rule
  source_chapter: 古籍主体·归魂游魂章（raw-wikitext L6045-L6055）
  source_quote: "须以用神为主，然后以此参之，若舍用神执此而断者，谬也。"
  summary: 游魂可作变动不定、归魂可作拘滞的辅助倾向，但都必须服从用神与生克主线。
  tags: [ancient-core, wandering-spirit, returning-spirit, evidence-priority]
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T05]
