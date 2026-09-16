# Stage 1 候选：原则、规则、清单与计算口径

> 本文件只做全量候选提取，不代表筛选、认可或现代事实判断。`经 / 传 / 注 / 疏` 均单独标层；涉及占筮、鬼神、知来等内容只记录为文本内部主张。

- id: P001
  title: 卦名与取象不可用单一类型穷尽
  type: rule
  source_chapter: 孔疏·乾卦（zhouyi-zhengyi raw-wikitext L146）
  source_quote: "物有万象，人有万事……不可一例求之，不可一类取之。"
  summary: 孔疏认为卦名有的取物象、有的取作用、有的取人事；解释时不得把所有卦强压成一种命名或取象规则。
  tags: [疏, interpretation, anti-rigidity, naming]
  task_ids: [ZY-T06, ZY-T07]

- id: P002
  title: 六爻三才位置映射
  type: calculation
  source_chapter: 孔疏·乾卦（zhouyi-zhengyi raw-wikitext L152-L154）
  source_quote: "一、二为地道，三、四为人道，五、上为天道。"
  summary: 孔疏采用两爻一组的三才位置口径；这是注疏解释模型，不是可经验验证的自然分类。
  tags: [疏, line-position, three-powers, mapping]
  task_ids: [ZY-T03, ZY-T06]
  inputs: [爻位1至6]
  formula: "1至2映射地道；3至4映射人道；5至6映射天道"
  units: 爻位
  output: 三才层级
  missing_conditions: 只给位置层级，不能单独推出吉凶；须结合卦、时、应、比与辞。

- id: P003
  title: 九六为变爻而七八为不变爻
  type: calculation
  source_chapter: 孔疏·乾卦（zhouyi-zhengyi raw-wikitext L150）
  source_quote: "老阳数九，老阴数六……七为少阳，八为少阴，质而不变。"
  summary: 注疏所存蓍法口径以九、六标老阳老阴并取其变，以七、八标少阳少阴而不变。
  tags: [疏, casting, moving-line, numeric-mapping]
  task_ids: [ZY-T03, ZY-T08]
  inputs: [单爻蓍数结果]
  formula: "9=老阳/动；6=老阴/动；7=少阳/静；8=少阴/静"
  units: 蓍数爻值
  output: 阴阳画与动静状态
  missing_conditions: 原段并未独立给出现代随机程序如何生成6/7/8/9；不得由此补造概率。

- id: P004
  title: 不以月份机械固定乾卦六爻
  type: rule
  source_chapter: 孔疏·乾卦（zhouyi-zhengyi raw-wikitext L154）
  source_quote: "诸儒以为九二当太蔟之月……于理稍乖。"
  summary: 孔疏反对把乾卦各爻机械配成固定月份，提示“时”首先是情境阶段，不等于现代日历应期。
  tags: [疏, timing, correction, anti-literal]
  task_ids: [ZY-T06, ZY-T07, ZY-T09]

- id: P005
  title: 彖看全卦而爻看变化
  type: rule
  source_chapter: 易传·系辞上第三章（zhouyi raw-wikitext L3535；正义 L5799-L5817）
  source_quote: "彖者，言乎象者也。爻者，言乎变者也。"
  summary: 解读顺序应区分全卦层与爻变层：彖统摄一卦之象，爻辞呈现具体位置与变化，二者不可互相替代。
  tags: [传, interpretation, hexagram, moving-line]
  task_ids: [ZY-T02, ZY-T03, ZY-T08]

- id: P006
  title: 吉凶悔吝无咎的分级口径
  type: calculation
  source_chapter: 易传·系辞上第二、三章（zhouyi raw-wikitext L3532-L3535）
  source_quote: "吉凶者，言乎其失得也。悔吝者，言乎其小疵也。无咎者，善补过也。"
  summary: 文本把吉凶对应得失，把悔吝视为较小过失或忧虞，把无咎解释为善于补过；无咎不等于大吉。
  tags: [传, judgement-scale, terminology, mapping]
  task_ids: [ZY-T01, ZY-T03, ZY-T08]
  inputs: [卦爻辞中的判断词]
  formula: "吉/凶→得/失；悔/吝→小疵或忧虞；无咎→经补过而免咎"
  units: 传统判断类别
  output: 分级解释标签
  missing_conditions: 仍须结合该卦爻的条件句；这些不是统计概率。

- id: P007
  title: 未明写吉凶不等于中性
  type: rule
  source_chapter: 孔疏·系辞上第二章（zhouyi-zhengyi raw-wikitext L5761）
  source_quote: "或吉凶据文可知……亦有爻处吉凶之际，吉凶未定。"
  summary: 孔疏列出不写吉凶的多种原因：文义已明、结果未定、取决于行为或用其他判断词表达；不得把“无吉凶字样”自动判成中性。
  tags: [疏, judgement, missing-label, conditions]
  task_ids: [ZY-T03, ZY-T06, ZY-T07]

- id: P008
  title: 无咎须核验补过条件
  type: rule
  source_chapter: 孔疏·系辞上第三章（zhouyi-zhengyi raw-wikitext L5807-L5809）
  source_quote: "无咎者，即此卦爻能补其过。若不能补过，则有咎也。"
  summary: 注疏把多数“无咎”理解为满足补过或善应之后免咎；输出必须说明达成条件，不可直接译作幸运。
  tags: [疏, no-blame, condition, correction]
  task_ids: [ZY-T03, ZY-T06, ZY-T08]

- id: P009
  title: 不以一爻立固定通例
  type: rule
  source_chapter: 孔疏·系辞上第二章（zhouyi-zhengyi raw-wikitext L5761）
  source_quote: "不可以一爻为例，义有变通也。"
  summary: 一条爻辞或一个卦例不能直接升级为普遍断语；须比较同卦结构、他卦反例和注疏条件。
  tags: [疏, anti-overgeneralization, evidence, audit]
  task_ids: [ZY-T06, ZY-T07, ZY-T09]

- id: P010
  title: 静态读象辞动态读变占
  type: rule
  source_chapter: 易传·系辞上第二章（zhouyi raw-wikitext L3532；正义 L5783-L5785）
  source_quote: "居则观其象而玩其辞，动则观其变而玩其占。"
  summary: 文本给出两种使用方式：平居学习重象与辞，准备行动时重变化与占；这属于传统文本内部方法，不证明占能预知未来。
  tags: [传, usage, interpretation, divination-claim]
  task_ids: [ZY-T03, ZY-T08, ZY-T09]

- id: P011
  title: 先比拟再发言先议定再行动
  type: maxim
  source_chapter: 易传·系辞上第八章（zhouyi raw-wikitext L3550）
  source_quote: "拟之而后言，议之而后动，拟议以成其变化。"
  summary: 面对复杂变化先建立恰当类比并讨论核验，再形成表达与行动，避免未经审查便下结论。
  tags: [传, deliberation, action, communication]
  task_ids: [ZY-T03, ZY-T09]

- id: P012
  title: 言行影响须审慎
  type: maxim
  source_chapter: 易传·系辞上第八章（zhouyi raw-wikitext L3552）
  source_quote: "言行，君子之枢机……可不慎乎！"
  summary: 把语言和行动视为荣辱与远近影响的枢纽，要求在公开表达和采取行动前审慎评估外溢影响。
  tags: [传, speech, conduct, caution]
  task_ids: [ZY-T03, ZY-T09]

- id: P013
  title: 薄物也可承载极慎程序
  type: principle
  source_chapter: 易传·系辞上第八章（zhouyi raw-wikitext L3554）
  source_quote: "夫茅之为物薄而用可重也，慎斯术也以往，其无所失矣。"
  summary: 即便事项看似轻微，也可通过额外的承垫与核验表达慎重；重点是程序性谨慎而非把白茅字面化。
  tags: [传, caution, procedure, analogy]
  task_ids: [ZY-T02, ZY-T09]

- id: P014
  title: 有功而不自伐
  type: maxim
  source_chapter: 易传·系辞上第八章（zhouyi raw-wikitext L3556）
  source_quote: "劳而不伐，有功而不德……谦也者，致恭以存其位者也。"
  summary: 完成工作后不自夸、不把功劳变成支配他人的资本，以谦恭维持关系与位置。
  tags: [传, humility, achievement, conduct]
  task_ids: [ZY-T02, ZY-T03]

- id: P015
  title: 机密事项控制言语出口
  type: rule
  source_chapter: 易传·系辞上第八章（zhouyi raw-wikitext L3560）
  source_quote: "几事不密则害成；是以君子慎密而不出也。"
  summary: 事情尚在关键未成阶段时应控制敏感信息披露；这是古代政治伦理语境下的谨慎原则，现代使用仍须服从法律与安全义务。
  tags: [传, confidentiality, timing, boundary]
  task_ids: [ZY-T03, ZY-T09]

- id: P016
  title: 大衍蓍法单轮操作
  type: calculation
  source_chapter: 易传·系辞上第九章（zhouyi raw-wikitext L3565；正义约 L6050-L6170）
  source_quote: "大衍之数五十，其用四十有九，分而为二……揲之以四……再扐而后挂。"
  summary: 文本给出以五十为名数、实际使用四十九策，经分二、挂一、揲四、归奇、再扐形成一次营变的传统程序。
  tags: [传, yarrow, calculation, casting]
  task_ids: [ZY-T03, ZY-T08]
  inputs: [蓍策50根]
  formula: "取49策→任分两组→从一组挂1→两组各按4揲数→余策归扐；按文本重复扐挂程序"
  units: 蓍策根数
  output: 一次营变后的策数状态
  missing_conditions: 此短段未把每次余数处理、三变如何映射6/7/8/9全部展开；实现必须另按已校核蓍法规范，不凭常识补齐。

- id: P017
  title: 乾坤策数与总策数口径
  type: calculation
  source_chapter: 易传·系辞上第九章（zhouyi raw-wikitext L3567）
  source_quote: "乾之策二百一十有六，坤之策百四十有四，凡三百有六十。"
  summary: 易传给出乾216策、坤144策、合计360策，并将上下篇总策说为11520；这是文本的象数口径，不等于现代概率模型。
  tags: [传, yarrow, numeric, symbolic-count]
  task_ids: [ZY-T03, ZY-T07]
  inputs: [乾卦6个老阳策数, 坤卦6个老阴策数]
  formula: "乾=6×36=216；坤=6×24=144；合计=360；二篇总策=11520"
  units: 策
  output: 传统象数总量
  missing_conditions: “二篇之策”逐卦计数细则未在该句展开；象征配数不可当作经验测量。

- id: P018
  title: 四营一变十八变成六爻卦
  type: calculation
  source_chapter: 易传·系辞上第九章（zhouyi raw-wikitext L3567；孔疏 L7025-L7027）
  source_quote: "四营而成易，十有八变而成卦。"
  summary: 注疏把分二、挂一、揲四、归奇概括为四营；三变定一爻，六爻共十八变成一卦。
  tags: [传, 疏, yarrow, casting-sequence]
  task_ids: [ZY-T03, ZY-T08]
  inputs: [每变的蓍策操作结果]
  formula: "4项操作=1营变；3变=1爻；6爻=18变"
  units: 营、变、爻
  output: 六爻卦及各爻数值
  missing_conditions: 仍需明确从下往上记录爻位及余数映射；原句未给现代随机替代规则。

- id: P019
  title: 《易》的四类用途分流
  type: checklist
  source_chapter: 易传·系辞上第十章（zhouyi raw-wikitext L3570）
  source_quote: "以言者尚其辞，以动者尚其变，以制器者尚其象，以卜筮者尚其占。"
  summary: 文本将使用者需求分为辞、变、象、占四路；不能把整部《周易》缩成单一预测工具。
  tags: [传, routing, text, change, image, divination]
  task_ids: [ZY-T03, ZY-T08, ZY-T09]

- id: P020
  title: 象辞变通的解释链
  type: template
  source_chapter: 易传·系辞上第十二章（zhouyi raw-wikitext L3586-L3588）
  source_quote: "立象以尽意，设卦以尽情伪，系辞以尽其言，变而通之以尽利。"
  summary: 可执行的分层模板是：先辨象，再定位卦情，再核对卦爻辞，最后观察变化如何转成可行行动；任何一步都不应被一句吉凶替代。
  tags: [传, interpretation-chain, template, provenance]
  task_ids: [ZY-T02, ZY-T03, ZY-T08]

- id: P021
  title: 穷则变变则通通则久
  type: maxim
  source_chapter: 易传·系辞下第二章（zhouyi raw-wikitext L3602）
  source_quote: "穷则变，变则通，通则久。"
  summary: 当既有方式走到尽头时调整，调整须建立新的通路，能通行后才谈持续；这是变化哲学原则，不是保证转变必然成功。
  tags: [传, adaptation, change, sustainability]
  task_ids: [ZY-T03, ZY-T09]

- id: P022
  title: 藏器待时而动
  type: rule
  source_chapter: 易传·系辞下第四章（zhouyi raw-wikitext L3621）
  source_quote: "君子藏器于身，待时而动。"
  summary: 先形成能力和工具，再等待条件成熟采取行动；“待时”须由现实条件核验，不由卦象单独宣布。
  tags: [传, readiness, timing, action]
  task_ids: [ZY-T03, ZY-T09]

- id: P023
  title: 善恶由小处累积
  type: principle
  source_chapter: 易传·系辞下第四章（zhouyi raw-wikitext L3623）
  source_quote: "善不积不足以成名，恶不积不足以灭身。"
  summary: 不因善小而不做，也不因恶小而不改；文本把长期结果理解为小行为累积。
  tags: [传, accumulation, conduct, feedback]
  task_ids: [ZY-T03]

- id: P024
  title: 安存治时仍预想危亡乱
  type: checklist
  source_chapter: 易传·系辞下第四章（zhouyi raw-wikitext L3625）
  source_quote: "安而不忘危，存而不忘亡，治而不忘乱。"
  summary: 在稳定、存续、治理正常时分别检查潜在危险、消亡和失序风险，作为事前风险清单。
  tags: [传, risk, prevention, checklist]
  task_ids: [ZY-T03, ZY-T09]

- id: P025
  title: 能力与责任必须匹配
  type: rule
  source_chapter: 易传·系辞下第四章（zhouyi raw-wikitext L3627）
  source_quote: "德薄而位尊，知小而谋大，力小而任重，鲜不及矣。"
  summary: 在承担高位、大谋或重任前，分别核验品德、认知和资源能力是否足以承载，避免角色超过能力边界。
  tags: [传, capacity, responsibility, risk]
  task_ids: [ZY-T03, ZY-T09]

- id: P026
  title: 见微知著及时行动
  type: rule
  source_chapter: 易传·系辞下第四章（zhouyi raw-wikitext L3629）
  source_quote: "几者，动之微，吉之先见者也。君子见几而作，不俟终日。"
  summary: 识别早期信号后及时采取可逆行动，不等问题完全显现；不得把任意巧合事后包装成“先见”。
  tags: [传, weak-signal, timing, action]
  task_ids: [ZY-T03, ZY-T09]

- id: P027
  title: 发现错误后不重复
  type: maxim
  source_chapter: 易传·系辞下第四章（zhouyi raw-wikitext L3631）
  source_quote: "有不善，未尝不知；知之，未尝复行也。"
  summary: 建立“察觉—承认—停止复发”的纠错闭环，而不是只表达后悔。
  tags: [传, correction, learning, conduct]
  task_ids: [ZY-T03, ZY-T09]

- id: P028
  title: 行动言语求助的三项前置条件
  type: checklist
  source_chapter: 易传·系辞下第四章（zhouyi raw-wikitext L3633）
  source_quote: "安其身而后动，易其心而后语，定其交而后求。"
  summary: 行动前先确保自身立足，沟通前先使心态平和，向人求助前先确认关系；原文的政治伦理语境不妨碍把它用作沟通检查表。
  tags: [传, preparation, communication, relationship]
  task_ids: [ZY-T03, ZY-T09]

- id: P029
  title: 九卦修德用途表
  type: checklist
  source_chapter: 易传·系辞下第六章（zhouyi raw-wikitext L3639-L3642）
  source_quote: "履以和行，谦以制礼，复以自知，恒以一德，损以远害，益以兴利。"
  summary: 文本把履、谦、复、恒、损、益、困、井、巽分别配到和行、制礼、自知、一德、远害、兴利、寡怨、辨义、行权，形成学习与自省清单。
  tags: [传, nine-hexagrams, cultivation, checklist]
  task_ids: [ZY-T02, ZY-T03]

- id: P030
  title: 解释不可立死板定准
  type: rule
  source_chapter: 易传·系辞下第七章（zhouyi raw-wikitext L3645；孔疏·乾 L146）
  source_quote: "上下无常，刚柔相易，不可为典要，唯变所适。"
  summary: 爻位与刚柔随具体卦情而变，规则只能作为可审计起点，不能脱离时、位和对象机械套用。
  tags: [传, anti-rigidity, change, boundary]
  task_ids: [ZY-T03, ZY-T06, ZY-T09]

- id: P031
  title: 六爻解释先后与重点位置
  type: template
  source_chapter: 易传·系辞下第七章（zhouyi raw-wikitext L3647）
  source_quote: "原始要终……其初难知，其上易知……辨是与非，则非其中爻不备。"
  summary: 分析六爻时记录初爻的起因难辨、上爻的结果较明，并用中间爻补足过程与是非；不能只看最醒目的一爻。
  tags: [传, line-sequence, template, process]
  task_ids: [ZY-T02, ZY-T06, ZY-T08]

- id: P032
  title: 二四三五位置倾向不是绝对吉凶
  type: calculation
  source_chapter: 易传·系辞下第八章（zhouyi raw-wikitext L3650；正义约 L6889-L6933）
  source_quote: "二多誉，四多惧……三多凶，五多功。"
  summary: 文本总结二、四虽同功但二多誉四多惧，三、五虽同功但三多凶五多功；“多”表示倾向，不能机械当作每卦必然结果。
  tags: [传, line-position, tendency, calculation]
  task_ids: [ZY-T03, ZY-T06]
  inputs: [爻位2至5, 阴阳刚柔, 是否得中, 与尊位距离]
  formula: "2→多誉；4→多惧；3→多凶；5→多功，仅作先验倾向后再按具体卦校正"
  units: 爻位倾向
  output: 初步位置风险标签
  missing_conditions: 必须结合得中、得位、应比和卦时；原文用“多”而非“皆”。

- id: P033
  title: 始终保持忧惧以求无咎
  type: maxim
  source_chapter: 易传·系辞下第八章（zhouyi raw-wikitext L3654；正义 L6931-L6933）
  source_quote: "懼以终始，其要无咎。"
  summary: 从开始到结束持续进行风险意识与复核，其目标是避免可归责的过失，而不是承诺必得吉利。
  tags: [传, risk, no-blame, audit]
  task_ids: [ZY-T03, ZY-T09]

- id: P034
  title: 近爻不相得须检查外应与时
  type: rule
  source_chapter: 易传·系辞下第九章（zhouyi raw-wikitext L3659；王注孔疏 L6979-L6989）
  source_quote: "相违而无患者，得其应也；相顺而皆凶者，乖于时也。"
  summary: 相邻爻不相得不自动等于凶；有外应可缓解。表面相顺也不自动吉，若违背卦时仍可凶。
  tags: [传, 注, 疏, adjacency, response, timing]
  task_ids: [ZY-T06, ZY-T07, ZY-T08]

- id: P035
  title: 三才成六画的结构口径
  type: calculation
  source_chapter: 易传·说卦第二章（zhouyi raw-wikitext L3670；正义 L7053-L7055）
  source_quote: "兼三才而两之，故易六画而成卦。"
  summary: 天、地、人三层各用两画展开而成六爻；孔疏另记王弼体系以二四为阴位、三五为阳位，初上无固定阴阳位。
  tags: [传, 疏, six-lines, structure]
  task_ids: [ZY-T03, ZY-T06]
  inputs: [天道, 地道, 人道]
  formula: "3个层级×每层2爻=6爻；王系位置阴阳：2/4阴，3/5阳，初/上未定"
  units: 爻位
  output: 六位结构及位置阴阳标签
  missing_conditions: 位置阴阳是王弼—韩康伯解释体系，不等于爻本身阴阳，也非所有学派唯一口径。

- id: P036
  title: 八卦核心德性映射
  type: calculation
  source_chapter: 易传·说卦第七章（zhouyi raw-wikitext L3700；正义 L7137）
  source_quote: "乾健，坤顺，震动，巽入，坎陷，离丽，艮止，兑说。"
  summary: 将八卦映射为健、顺、动、入、陷、丽、止、说，供义理检索；它是传统类比表，不是人格或事件的科学分类器。
  tags: [传, trigram, lookup-table, boundary]
  task_ids: [ZY-T04, ZY-T09]
  inputs: [八卦名]
  formula: "乾→健；坤→顺；震→动；巽→入；坎→陷；离→丽；艮→止；兑→说"
  units: 卦德类别
  output: 核心取象关键词
  missing_conditions: 必须结合上下卦、爻辞和问题语境；不可单独推出诊断或事实。

- id: P037
  title: 后天八卦方位与过程映射
  type: calculation
  source_chapter: 易传·说卦第五章（zhouyi raw-wikitext L3679-L3687；正义 L7101-L7105）
  source_quote: "出乎震，齐乎巽，相见乎离，致役乎坤，说言乎兑，战乎乾，劳乎坎，成言乎艮。"
  summary: 说卦将震巽离坤兑乾坎艮配为东、东南、南、地/养、西、西北、北、东北，并串成出、齐、见、役、说、战、劳、成的过程。
  tags: [传, trigram, direction, process-map]
  task_ids: [ZY-T04, ZY-T07]
  inputs: [八卦名]
  formula: "震→东/出；巽→东南/齐；离→南/见；坤→养/役；兑→西/说；乾→西北/战；坎→北/劳；艮→东北/成终始"
  units: 传统方位与阶段
  output: 方位及过程关键词
  missing_conditions: 坤在该段不专配一方；不能直接转成现代地理定位或应期。

- id: P038
  title: 八卦动物取象表
  type: calculation
  source_chapter: 易传·说卦第八章（zhouyi raw-wikitext L3703）
  source_quote: "乾为马，坤为牛，震为龙，巽为鸡，坎为豕，离为雉，艮为狗，兑为羊。"
  summary: 保存八卦—动物的原典映射，供原文检索，不把动物象自动解释为现实人物特征。
  tags: [传, trigram, animal, lookup-table]
  task_ids: [ZY-T04, ZY-T09]
  inputs: [八卦名]
  formula: "乾马、坤牛、震龙、巽鸡、坎豕、离雉、艮狗、兑羊"
  units: 传统物象类别
  output: 动物象
  missing_conditions: 只有类比映射，没有给出现代预测使用的判定规则。

- id: P039
  title: 八卦身体取象表
  type: calculation
  source_chapter: 易传·说卦第九章（zhouyi raw-wikitext L3706）
  source_quote: "乾为首，坤为腹，震为足，巽为股，坎为耳，离为目，艮为手，兑为口。"
  summary: 保存八卦—身体部位的传统映射；只可用于文本解释，不得据此诊断疾病或替代医疗检查。
  tags: [传, trigram, body, safety]
  task_ids: [ZY-T04, ZY-T09]
  inputs: [八卦名]
  formula: "乾首、坤腹、震足、巽股、坎耳、离目、艮手、兑口"
  units: 身体部位象
  output: 传统身体取象
  missing_conditions: 无症状、病因、概率或诊断标准；必须禁止医学断言。

- id: P040
  title: 八卦家庭角色取象表
  type: calculation
  source_chapter: 易传·说卦第十章（zhouyi raw-wikitext L3709-L3712）
  source_quote: "乾天故称父，坤地故称母……震长男、巽长女、坎中男、离中女、艮少男、兑少女。"
  summary: 保存父母与三男三女的传统角色映射；现代使用必须标明其前现代父系与二元性别语境。
  tags: [传, trigram, family, historical-context]
  task_ids: [ZY-T04, ZY-T09]
  inputs: [八卦名]
  formula: "乾父、坤母、震长男、巽长女、坎中男、离中女、艮少男、兑少女"
  units: 传统家庭角色
  output: 家庭角色象
  missing_conditions: 不可用于推断现实人物性别、排行、性格或权力正当性。

- id: P041
  title: 八卦扩展物象查表
  type: calculation
  source_chapter: 易传·说卦第十一章（zhouyi raw-wikitext L3715-L3743；正义 L7197-L7217）
  source_quote: "乾为天、为圜、为君、为父、为玉、为金……坤为地、为母、为布、为釜……"
  summary: 乾坤震巽坎离艮兑各有物质、人物、动物、器物和性质清单；调用时须返回具体出处和候选象，禁止无限联想。
  tags: [传, trigram, extended-images, lookup-table]
  task_ids: [ZY-T04, ZY-T07, ZY-T09]
  inputs: [八卦名, 所需物象类别]
  formula: 按L3715-L3743逐卦逐类查询，不跨类自行扩写
  units: 传统类比类别
  output: 原典列明的一个或多个物象
  missing_conditions: 镜像可能有异文；身体、疾病、人物类只能作文本说明，不能当事实识别器。

- id: P042
  title: 大象行动映射一（乾至比）
  type: checklist
  source_chapter: 易传·大象聚合页（zhouyi raw-wikitext L2432-L2439）
  source_quote: "乾：自强不息；坤：厚德载物；屯：经纶；蒙：果行育德。"
  summary: 前八卦行动词依次为自强不息、厚德载物、经纶、果行育德、饮食宴乐、作事谋始、容民畜众、建国亲侯；须按卦返回，不混成通用预测。
  tags: [传, great-image, action-map, checklist]
  task_ids: [ZY-T02, ZY-T08]

- id: P043
  title: 大象行动映射二（小畜至豫）
  type: checklist
  source_chapter: 易传·大象聚合页（zhouyi raw-wikitext L2440-L2447）
  source_quote: "小畜懿文德，履辨上下，泰辅相天地，否俭德辟难。"
  summary: 小畜至豫依次为懿文德、辨上下定民志、辅相天地、俭德辟难、类族辨物、遏恶扬善、裒多益寡、作乐崇德。
  tags: [传, great-image, action-map, checklist]
  task_ids: [ZY-T02, ZY-T08]

- id: P044
  title: 大象行动映射三（随至复）
  type: checklist
  source_chapter: 易传·大象聚合页（zhouyi raw-wikitext L2448-L2455）
  source_quote: "随向晦宴息，蛊振民育德，临教思无穷，观省方观民设教。"
  summary: 随至复依次为向晦宴息、振民育德、教思容保、省方设教、明罚敕法、明庶政而慎断狱、厚下安宅、闭关休整。
  tags: [传, great-image, action-map, checklist]
  task_ids: [ZY-T02, ZY-T08]

- id: P045
  title: 大象行动映射四（无妄至咸）
  type: checklist
  source_chapter: 易传·大象聚合页（zhouyi raw-wikitext L2456-L2462）
  source_quote: "大畜多识前言往行以畜德；颐慎言语节饮食；咸虚受人。"
  summary: 无妄至咸依次为对时育物、识前言往行以畜德、慎言节食、独立不惧、常德习教、继明照四方、虚心受人。
  tags: [传, great-image, action-map, checklist]
  task_ids: [ZY-T02, ZY-T08]

- id: P046
  title: 大象行动映射五（恒至解）
  type: checklist
  source_chapter: 易传·大象聚合页（zhouyi raw-wikitext L2463-L2471）
  source_quote: "恒立不易方，遯远小人不恶而严，大壮非礼弗履。"
  summary: 恒至解依次为立定方向、疏远而不憎恶、非礼不履、自昭明德、用晦而明、言有物行有恒、同中存异、反身修德、赦过宥罪。
  tags: [传, great-image, action-map, checklist]
  task_ids: [ZY-T02, ZY-T08]

- id: P047
  title: 大象行动映射六（损至革）
  type: checklist
  source_chapter: 易传·大象聚合页（zhouyi raw-wikitext L2472-L2480）
  source_quote: "损惩忿窒欲，益见善则迁有过则改，萃戒不虞，升积小以高大。"
  summary: 损至革依次为惩忿窒欲、迁善改过、施禄忌居德、申命四方、备械防不虞、积小成大、遂志、劳民劝相、治历明时。
  tags: [传, great-image, action-map, checklist]
  task_ids: [ZY-T02, ZY-T08]

- id: P048
  title: 大象行动映射七（鼎至涣）
  type: checklist
  source_chapter: 易传·大象聚合页（zhouyi raw-wikitext L2481-L2490）
  source_quote: "震恐惧修省，艮思不出其位，归妹永终知敝，旅明慎用刑。"
  summary: 鼎至涣依次为正位凝命、恐惧修省、思不出位、居贤德善俗、永终知敝、折狱致刑、明慎用刑、申命行事、朋友讲习、立庙祭享。
  tags: [传, great-image, action-map, checklist]
  task_ids: [ZY-T02, ZY-T08]

- id: P049
  title: 大象行动映射八（节至未济）
  type: checklist
  source_chapter: 易传·大象聚合页（zhouyi raw-wikitext L2491-L2495）
  source_quote: "节制数度议德行；中孚议狱缓死；既济思患预防；未济慎辨物居方。"
  summary: 节至未济依次为制数度议德行、议狱缓死、恭哀俭可稍过、预想祸患并预防、谨慎辨物定位。
  tags: [传, great-image, action-map, checklist]
  task_ids: [ZY-T02, ZY-T08, ZY-T09]

- id: P050
  title: 蒙卦一问原则
  type: rule
  source_chapter: 经与彖·蒙卦（zhouyi raw-wikitext L355-L368）
  source_quote: "初筮告，再三渎，渎则不告。"
  summary: 同一疑问以首次正式占问为准，反复追问被视为亵渎而不再作答；实际系统应记录首卦，避免挑选满意结果。
  tags: [经, question-contract, recast, audit]
  task_ids: [ZY-T01, ZY-T08, ZY-T09]

- id: P051
  title: 诉讼争端不宜拖到终局
  type: rule
  source_chapter: 经与彖·讼卦（zhouyi raw-wikitext L419-L432）
  source_quote: "中吉，终凶……讼不可成也。"
  summary: 争端应在中途寻求澄清或裁断，不把持续对抗本身当成成功；这是古典行动劝诫，不是法律意见。
  tags: [经, 传, dispute, de-escalation]
  task_ids: [ZY-T01, ZY-T02, ZY-T09]

- id: P052
  title: 谦卦调多补寡
  type: principle
  source_chapter: 彖与大象·谦卦（zhouyi raw-wikitext L716-L719）
  source_quote: "裒多益寡，称物平施。"
  summary: 对过多与不足进行调节，按对象实际情况公平施予；不可脱离资源与权利条件只讲服从。
  tags: [传, balance, distribution, conduct]
  task_ids: [ZY-T02, ZY-T09]

- id: P053
  title: 损益必须与时同行
  type: rule
  source_chapter: 彖·损益卦（zhouyi raw-wikitext L1551, L1583）
  source_quote: "损刚益柔有时，损益盈虚，与时偕行。凡益之道，与时偕行。"
  summary: 增减不按“增加必吉、减少必凶”判断，而须核验对象、盈虚和时机。
  tags: [传, increase, decrease, timing]
  task_ids: [ZY-T02, ZY-T06, ZY-T08]

- id: P054
  title: 节制不可走向苦节
  type: rule
  source_chapter: 经与彖·节卦（zhouyi raw-wikitext L2150-L2159）
  source_quote: "苦节不可贞，其道穷也……不伤财，不害民。"
  summary: 制度与节制应可持续，并以不伤资源、不害人为边界；过度严苛的节制不可长期坚持。
  tags: [经, 传, moderation, sustainability]
  task_ids: [ZY-T01, ZY-T02, ZY-T09]

- id: P055
  title: 小过只宜小事不宜大事
  type: rule
  source_chapter: 经与彖·小过卦（zhouyi raw-wikitext L2214-L2223）
  source_quote: "可小事，不可大事……不宜上宜下。"
  summary: 小有越常只适合低风险、局部事务，不据此发动重大行动；宜收敛向下而非向上扩张。
  tags: [经, 传, scope, small-step]
  task_ids: [ZY-T01, ZY-T02, ZY-T08]

- id: P056
  title: 完成之后仍要预防风险
  type: maxim
  source_chapter: 大象·既济卦（zhouyi raw-wikitext L2258）
  source_quote: "君子以思患而豫防之。"
  summary: 即使事情进入“既济”状态，也要列出潜在失稳因素和预防措施，不把阶段性完成视为永久安全。
  tags: [传, post-success, risk, prevention]
  task_ids: [ZY-T02, ZY-T09]

- id: P057
  title: 序卦只能作托象关系链
  type: rule
  source_chapter: 韩注孔疏·序卦（zhouyi-zhengyi raw-wikitext L7235）
  source_quote: "序卦之所明，非易之蕴也。盖因卦之次，托象以明义。"
  summary: 韩康伯与孔疏不把《序卦》的前后因果当作《易》的唯一深层本质；使用时只作为卦序叙事和比较线索。
  tags: [注, 疏, sequence, boundary]
  task_ids: [ZY-T05, ZY-T07, ZY-T09]

- id: P058
  title: 序卦六类关系检索
  type: calculation
  source_chapter: 孔疏·序卦（zhouyi-zhengyi raw-wikitext L7235）
  source_quote: "第一天道门，第二人事门，第三相因门，第四相反门，第五相须门，第六相病门。"
  summary: 孔疏记录周氏把卦序关系分成天道、人事、相因、相反、相须、相病六类，但随后并未采纳为唯一解释。
  tags: [疏, sequence, classification, disputed]
  task_ids: [ZY-T05, ZY-T07]
  inputs: [相邻卦对]
  formula: "候选分类∈{天道,人事,相因,相反,相须,相病}"
  units: 卦序关系类别
  output: 周氏分类候选与孔疏保留意见
  missing_conditions: 孔疏明确不采用此说为总解释；不得把分类当成固定因果律。

- id: P059
  title: 六十四卦两两成对的覆变检查
  type: calculation
  source_chapter: 孔疏·序卦（zhouyi-zhengyi raw-wikitext L7235）
  source_quote: "六十四卦，二二相耦，非覆即变。"
  summary: 按孔疏，文王卦序可逐对检查：多数上下翻覆成对；翻覆仍同卦者则以阴阳全变配对。
  tags: [疏, sequence, paired-hexagrams, calculation]
  task_ids: [ZY-T05, ZY-T07]
  inputs: [文王序相邻奇偶位卦, 六爻阴阳序列]
  formula: "若A上下倒置=B则标覆；否则检查A六爻阴阳全反=B并标变"
  units: 六爻二进制结构
  output: 覆卦对或变卦对
  missing_conditions: 这是卦序结构观察，不足以证明《序卦》叙事或历史成因。

- id: P060
  title: 注疏异说必须并列保留
  type: rule
  source_chapter: 《周易正义》总说明（zhouyi-zhengyi raw-wikitext L17）
  source_quote: "始专崇王注而众说皆废……如斯之类，皆显然偏袒。"
  summary: 镜像总说明指出《正义》偏向王弼；抽取结论时必须显示王韩注、孔疏裁断及其所驳异说，不把《正义》伪装成无立场共识。
  tags: [editorial, provenance, commentary-bias, conflict]
  task_ids: [ZY-T07, ZY-T09]

## 覆盖说明

- 《周易》`L192-L2295`：逐卦扫描卦辞、爻辞、彖与象；规范性高密度内容以卦级规则及八组《大象》清单归档，未把每个情境爻辞都错误提升为普遍原则。
- 《周易》`L2297-L3520`：与单卦页交叉核对彖、大象、小象、文言；聚合《小象》存在录入错误，原则引用优先采用单卦页或无争议总纲。
- 《周易》`L3522-L3661`：完整覆盖系辞上下的象、辞、变、占、蓍法、位置倾向、行动箴言和解释纪律。
- 《周易》`L3663-L3854`：覆盖说卦全部映射、序卦关系与杂卦对举；映射均加传统类比与现代安全边界。
- 《周易正义》`L1-L5668`：扫描六十四卦注疏，提取跨卦可执行的命名、爻位、动静数值、时位和反机械规则；个案论证留给 case/framework extractor。
- 《周易正义》`L5669-L6998`：覆盖系辞正义对吉凶省略、无咎、爻位、应比、蓍法和“义有变通”的细化。
- 《周易正义》`L6999-L7270`：覆盖说卦、序卦、杂卦正义；包括王系位置口径、方位物象解释、覆变卦对和序卦六类异说。
- 合计候选 **60 条**：rule 20、calculation 16、checklist 12、maxim 7、principle 3、template 2。所有预测性、鬼神性和自然—人事类比均只标作文本内部模型，没有写成现代已证事实。
