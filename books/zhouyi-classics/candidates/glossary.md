# 《周易》经传与《周易正义》关键术语候选

> Stage 1 glossary extractor 产物。定义按“经／传／王韩注／孔疏”分层；`chunk_id` 用于回溯预筛文本，`source_lines` 指向归档原文。这里的“作者定义”是相应文本层的内部用法，不代表现代学术共识，也不把后世纳甲六爻术语倒写进原典。

```yaml
- id: g01
  term: 卦
  type: term
  source_chapter: 周易正义·乾
  author_definition: |
    孔疏引《易纬》释“卦者挂也”，即悬挂物象以示人；又说三画足以象八类基本物象，重为六画以展开变化。卦因此是由六爻构成、统摄一个处境及其变化关系的整体单位。
  key_distinction: |
    ≠ 单独一个吉凶标签。
    ≠ 后世八宫、纳甲、六亲、世应的总称。
    = 先作为全卦整体读，再进入具体爻位。
  why_it_matters: |
    下游若把“卦”当成一句断语，会跳过全卦结构；若把八宫纳甲当作经文本义，又会造成时代倒置。
  source_layer: 孔颖达疏（引《易纬》并作解释）
  source_lines: [zhouyi-zhengyi:L146]
  chunk_id: [ck-9162a2e78e03]
  tags: [term, core-concept, structure, source-layer]
  task_ids: [ZY-T01, ZY-T06, ZY-T07, ZY-T08]

- id: g02
  term: 爻
  type: term
  source_chapter: 系辞下；周易正义·乾
  author_definition: |
    《系辞》说“爻也者，效天下之动者也”；孔疏据此解释爻为仿效万物之象、表现处境内部变化的画与爻辞单位。
  key_distinction: |
    ≠ 脱离本卦即可独立使用的签诗。
    ≠ 后世六爻排盘中包含六亲、地支、六神等整行信息。
    = 卦中一个位置、阴阳画及其对应辞义，重点在“动”和阶段。
  why_it_matters: |
    这是读取动爻的基本单位；必须同时知道本卦、爻位和文本层，不能只抽取一个关键词断事。
  source_layer: 易传；孔颖达疏
  source_lines: [zhouyi:L3612, zhouyi-zhengyi:L150]
  chunk_id: [ck-81f12ddb0aa9, ck-9162a2e78e03]
  tags: [term, core-concept, moving-line, source-layer]
  task_ids: [ZY-T01, ZY-T02, ZY-T06, ZY-T08]

- id: g03
  term: 初／上／九／六
  type: notation
  source_chapter: 周易正义·乾；系辞下
  author_definition: |
    “初”标第一位，“上”标第六位；孔疏以阳爻称九、阴爻称六，并保存“老阳九、老阴六为变”的解释。系辞以初为事端未著、上为事情终极已显。
  key_distinction: |
    初、上是位置；九、六是爻性/传统蓍数记号，二者不能混作顺序号。
    “九六为变”是注疏保存的传统筮法解释，不自动等于任何现代随机算法。
  why_it_matters: |
    可防止把“初九”误读为第九爻，也让起卦引擎的数字输出能正确接到经文爻位。
  source_layer: 易传；孔颖达疏所存旧说
  source_lines: [zhouyi:L3647, zhouyi-zhengyi:L150, zhouyi-zhengyi:L6879-L6881]
  chunk_id: [ck-81f12ddb0aa9, ck-9162a2e78e03, ck-9d6754d54e1b]
  tags: [term, notation, line-position, casting]
  task_ids: [ZY-T01, ZY-T06, ZY-T08]

- id: g04
  term: 八卦
  type: term
  source_chapter: 系辞上；说卦
  author_definition: |
    乾、坤、震、巽、坎、离、艮、兑八个三画卦；经传以其德、象、方位等形成基础分类，并“因而重之”形成六画卦。
  key_distinction: |
    ≠ 六十四卦。
    ≠ 后世八宫卦序。
    说卦物象是类比资源，不是现实对象之间已证实的因果表。
  why_it_matters: |
    下游会用上下卦解释结构和取象；必须限制类比，尤其不得凭身体象诊断疾病或凭家庭象断定人物身份。
  source_layer: 易传
  source_lines: [zhouyi:L3581, zhouyi:L3663-L3744]
  chunk_id: [ck-81f12ddb0aa9, ck-bbe02fd37700]
  tags: [term, trigram, imagery, boundary]
  task_ids: [ZY-T04, ZY-T08, ZY-T09]

- id: g05
  term: 六十四卦
  type: term
  source_chapter: 周易六十四卦单页
  author_definition: |
    八卦相重所得的六画卦系统；每卦以卦辞统摄整体，并以六个爻位展开处境的始终与阶段差异。
  key_distinction: |
    ≠ 64 个彼此孤立的固定预言。
    = 一套由卦体、卦辞、爻辞及传文共同组成的处境词汇。
  why_it_matters: |
    决定资料组织必须是一套可检索体系，而不是拆成 64 个互相抢触发的 Skill。
  source_layer: 经；易传；镜像目录仅作索引
  source_lines: [zhouyi:L192-L2295, zhouyi:L3595]
  chunk_id: [ck-f47bfc9bf4f9, ck-81f12ddb0aa9]
  tags: [term, corpus-structure, hexagram]
  task_ids: [ZY-T01, ZY-T05, ZY-T08]

- id: g06
  term: 三才／三极
  type: term
  source_chapter: 系辞上；说卦
  author_definition: |
    天、地、人三层结构；说卦称“兼三才而两之”，于是六画成卦，系辞称六爻之动为“三极之道”。孔疏亦以一二为地、三四为人、五上为天说明六位。
  key_distinction: |
    = 六爻位置的一种经典结构解释。
    ≠ 自然科学分类，也不是六亲或三类现实人物的固定映射。
  why_it_matters: |
    能解释为何六画分成三组成对位置，同时阻止把天地人字面化成具体对象。
  source_layer: 易传；孔颖达疏
  source_lines: [zhouyi:L3532, zhouyi:L3670, zhouyi-zhengyi:L154, zhouyi-zhengyi:L5775]
  chunk_id: [ck-ecfb9ca45a3a, ck-bbe02fd37700, ck-9162a2e78e03, ck-7fbfe4f5e2c3]
  tags: [term, line-position, structure]
  task_ids: [ZY-T03, ZY-T06]

- id: g07
  term: 象
  type: term
  source_chapter: 系辞上、系辞下
  author_definition: |
    系辞释“象也者，像也”，并说圣人拟取事物形容、象其物宜而成象；它是卦形、自然物象与人事类比之间的解释媒介。
  key_distinction: |
    ≠ 现实因果证据。
    ≠ 看见某象就可无限追加人物、疾病、地点细节。
    “四象”在太极生成链中另有特定用法，不可与一般“卦象/物象”混同。
  why_it_matters: |
    象是经典辅助六爻的主要接口，也是过度联想的主要风险点；输出必须说明类比链和边界。
  source_layer: 易传
  source_lines: [zhouyi:L3550, zhouyi:L3588, zhouyi:L3595, zhouyi:L3612]
  chunk_id: [ck-ecfb9ca45a3a, ck-81f12ddb0aa9]
  tags: [term, core-concept, imagery, analogy, boundary]
  task_ids: [ZY-T02, ZY-T03, ZY-T04, ZY-T09]

- id: g08
  term: 彖
  type: term
  source_chapter: 彖传；周易正义·乾
  author_definition: |
    易传说彖“言乎象”或为一卦之“材”；孔疏引《略例》称其“统论一卦之体，明其所由之主”，并保存“彖，断也”的旧说。
  key_distinction: |
    ≠ 卦辞本身。
    = 对全卦总体结构、德性、卦名和主旨的传文解释。
  why_it_matters: |
    下游应先用彖把握全卦，再读动爻；引用时必须标作“传”，不能冒充经文原话。
  source_layer: 易传；王弼《略例》经孔疏引用；孔颖达疏
  source_lines: [zhouyi:L3535, zhouyi:L3612, zhouyi-zhengyi:L178]
  chunk_id: [ck-ecfb9ca45a3a, ck-81f12ddb0aa9, ck-2f52fd159614]
  tags: [term, source-layer, whole-hexagram]
  task_ids: [ZY-T02, ZY-T07, ZY-T08]

- id: g09
  term: 大象／小象
  type: term
  source_chapter: 象传
  author_definition: |
    大象以全卦上下卦之物象引出君子或先王的行动取向；小象逐条解释爻辞及爻位关系。二者都属于传文。
  key_distinction: |
    ≠ 卦辞或爻辞原文。
    大象偏全卦类比，小象偏具体爻位；当前聚合《小象》页有转录错误，须优先用单卦页并交叉核对。
  why_it_matters: |
    它决定“全卦行动提示”和“动爻解释”应分栏，也决定引文校验策略。
  source_layer: 易传；版本审计说明
  source_lines: [zhouyi:L2430-L3394]
  chunk_id: [ck-8e780ff66e91]
  tags: [term, source-layer, imagery, version-audit]
  task_ids: [ZY-T02, ZY-T07]

- id: g10
  term: 文言
  type: term
  source_chapter: 文言传；周易正义·乾
  author_definition: |
    专门申释乾、坤经文、四德与六爻义理的传文。孔疏主张其作用是“赞明易道、申说义理”，而非单纯文饰华彩。
  key_distinction: |
    ≠ 所有六十四卦都有的栏目。
    ≠ 经文作者对自己的直接注解；它是经典解释层。
  why_it_matters: |
    乾坤解读常高度依赖文言；若不标层，最容易把伦理化解释误写成原始卦爻辞。
  source_layer: 易传；孔颖达疏
  source_lines: [zhouyi:L3396-L3520, zhouyi-zhengyi:L206]
  chunk_id: [ck-0eb44dbd2943, ck-82d589b52d3a]
  tags: [term, source-layer, qian-kun]
  task_ids: [ZY-T02, ZY-T07]

- id: g11
  term: 辞
  type: term
  source_chapter: 系辞上、系辞下
  author_definition: |
    系于卦爻之下、用来指明趋向并断其吉凶的文字；系辞说“辩吉凶者存乎辞”“辞也者，各指其所之”。
  key_distinction: |
    ≠ 对未来事实的无条件保证。
    = 文本对特定卦爻处境、行动和得失方向的表达。
  why_it_matters: |
    下游应保留原辞并解释其条件，不能只输出现代结论或把传、注、疏混写成“爻辞”。
  source_layer: 易传
  source_lines: [zhouyi:L3532-L3535, zhouyi:L3550, zhouyi:L3588]
  chunk_id: [ck-ecfb9ca45a3a, ck-81f12ddb0aa9]
  tags: [term, core-concept, source-layer, judgment]
  task_ids: [ZY-T01, ZY-T03, ZY-T07]

- id: g12
  term: 变／化
  type: term
  source_chapter: 系辞；周易正义·乾
  author_definition: |
    系辞以刚柔相推生变化，并说“化而裁之谓之变”；孔疏又分“变”为后来渐改其前，“化”为有无之间忽然改易。两词共同指处境不固定及其转化。
  key_distinction: |
    ≠ “之卦自动覆盖本卦”。
    ≠ 每一变化都能换算成确定日期或确定事件。
    孔疏的渐变/骤化区分是注疏层解释，不应冒充唯一字典义。
  why_it_matters: |
    是连接动爻、之卦与现实行动调整的核心词；需要同时保留本卦背景和变化方向。
  source_layer: 易传；孔颖达疏
  source_lines: [zhouyi:L3532, zhouyi:L3588, zhouyi-zhengyi:L178]
  chunk_id: [ck-ecfb9ca45a3a, ck-81f12ddb0aa9, ck-2f52fd159614]
  tags: [term, core-concept, change, moving-line]
  task_ids: [ZY-T03, ZY-T06, ZY-T08]

- id: g13
  term: 通／变通
  type: term
  source_chapter: 系辞上、系辞下
  author_definition: |
    系辞说“一阖一辟谓之变，往来不穷谓之通”，又说“推而行之谓之通”；变通是将变化推行、使之不穷并趋合时势的过程。
  key_distinction: |
    ≠ 无原则地改变解释以迎合结果。
    = 在保留文本条件的前提下，依据时势调整实行方式。
  why_it_matters: |
    支撑条件化、非宿命式输出，也要求记录解释为何适用于当前处境，防止事后圆说。
  source_layer: 易传
  source_lines: [zhouyi:L3581, zhouyi:L3588, zhouyi:L3595]
  chunk_id: [ck-81f12ddb0aa9]
  tags: [term, adaptation, change, anti-determinism]
  task_ids: [ZY-T03, ZY-T06, ZY-T09]

- id: g14
  term: 占
  type: term
  source_chapter: 系辞上
  author_definition: |
    系辞称“极数知来之谓占”，并说人在行动时观其变而玩其占；它是传统文本内部以数与变决疑、判断趋向的用途。
  key_distinction: |
    ≠ 经科学验证的未来预测。
    ≠ 任意套话或事后挑选最合意解释。
    = 传统占筮语境中的判断活动，须预先固定问题和起卦记录。
  why_it_matters: |
    允许本包服务占问，但要求所有预测性表达标为传统术数推演并使用条件语言。
  source_layer: 易传
  source_lines: [zhouyi:L3532, zhouyi:L3541]
  chunk_id: [ck-ecfb9ca45a3a]
  tags: [term, divination, epistemic-boundary]
  task_ids: [ZY-T03, ZY-T08, ZY-T09]

- id: g15
  term: 筮／蓍
  type: term
  source_chapter: 系辞上；说卦
  author_definition: |
    筮是借蓍草和数的程序形成卦爻、用于决疑的传统实践；系辞称“蓍之德圆而神”，并叙大衍、十八变等程序背景。
  key_distinction: |
    ≠ 卦辞解释本身。
    ≠ 程序随机起卦天然等同古代蓍法；现代实现只是替代抽样机制，必须记录算法和只随机一次的承诺。
  why_it_matters: |
    能把“如何得到卦”与“如何解释卦”分开，方便审计随机起卦而不伪称复原全部古法。
  source_layer: 易传；传统实践描述
  source_lines: [zhouyi:L3561-L3581, zhouyi:L3663-L3670]
  chunk_id: [ck-81f12ddb0aa9, ck-bbe02fd37700]
  tags: [term, casting, divination, reproducibility]
  task_ids: [ZY-T03, ZY-T08, ZY-T09]

- id: g16
  term: 吉／凶
  type: judgment-term
  source_chapter: 系辞上
  author_definition: |
    系辞释“吉凶者，失得之象也”，又称其“言乎其失得”；它们是对得失方向的规范性判断。
  key_distinction: |
    ≠ 统计概率。
    ≠ 吉就必成、凶就必败的无条件承诺。
    判断常依赖所处之时、爻位和采取的行动。
  why_it_matters: |
    下游必须把吉凶翻译成有条件的机会与风险，不可制造确定性预测。
  source_layer: 易传
  source_lines: [zhouyi:L3532-L3535]
  chunk_id: [ck-ecfb9ca45a3a]
  tags: [term, judgment, conditionality]
  task_ids: [ZY-T03, ZY-T06, ZY-T09]

- id: g17
  term: 悔／吝
  type: judgment-term
  source_chapter: 系辞上
  author_definition: |
    系辞以悔吝为“忧虞之象”，又说它们“言乎其小疵”；所示是忧惧、局促或较轻的过失状态，并非与大凶等量。
  key_distinction: |
    ≠ 凶的同义词。
    ≠ 现代心理学诊断。
    “悔亡”表示相应悔态消除，也不能自动升级为大吉。
  why_it_matters: |
    有助于建立风险强度层级，避免把所有不利词都渲染成灾难。
  source_layer: 易传；孔疏对“有悔/悔亡”的展开
  source_lines: [zhouyi:L3532-L3535, zhouyi-zhengyi:L166]
  chunk_id: [ck-ecfb9ca45a3a, ck-13db7e9b547f]
  tags: [term, judgment, risk-scale]
  task_ids: [ZY-T03, ZY-T09]

- id: g18
  term: 无咎
  type: judgment-term
  source_chapter: 系辞上；周易正义·乾
  author_definition: |
    系辞直释“无咎者，善补过也”；孔疏据九三说明，能戒慎补过才免于罪咎，若不如此仍会有咎。
  key_distinction: |
    ≠ 大吉。
    ≠ 什么都不做也必然安全。
    = 常表示满足某种补救、戒慎或合宜条件后避免过失。
  why_it_matters: |
    这是实际占问中最易被误报为“很好”的词；正确输出必须同时给出免咎条件。
  source_layer: 易传；孔颖达疏
  source_lines: [zhouyi:L3535, zhouyi-zhengyi:L158]
  chunk_id: [ck-ecfb9ca45a3a, ck-13db7e9b547f]
  tags: [term, judgment, corrective-action, high-value-distinction]
  task_ids: [ZY-T03, ZY-T06, ZY-T08]

- id: g19
  term: 时
  type: term
  source_chapter: 彖传；系辞下；周易正义·系辞
  author_definition: |
    指一卦所象的具体处境阶段，以及某爻在该处境中行动是否合宜的条件。王注系统概括“卦者时也”，六爻则各示适时之功；系辞称变通“趣时”。
  key_distinction: |
    ≠ 后世六爻的日辰、月建或具体“应期”。
    ≠ 看到“七日、十年、八月”即可机械换算日历日期。
    = 行动成立的情势和阶段条件。
  why_it_matters: |
    时是义理辅助六爻的核心接口，也是在用户追问“什么时候”时必须设置的防过度确定边界。
  source_layer: 易传；王弼注法经孔疏说明
  source_lines: [zhouyi:L3595, zhouyi:L3647, zhouyi-zhengyi:L6422]
  chunk_id: [ck-81f12ddb0aa9, ck-dbb29901433d]
  tags: [term, time-condition, anti-literal-timing]
  task_ids: [ZY-T03, ZY-T06, ZY-T08, ZY-T09]

- id: g20
  term: 位
  type: term
  source_chapter: 文言；系辞上、系辞下；周易正义·乾
  author_definition: |
    六爻从初至上的结构位置，并由内外、上下、尊卑及所处阶段产生解释差异。系辞说“列贵贱者存乎位”；孔疏说明一二为地、三四为人、五上为天只是一种解释结构。
  key_distinction: |
    ≠ 现实中人的固定社会等级或价值高低。
    ≠ 后世六爻的世爻/应爻位置体系。
    = 文本内部的关系坐标，必须结合卦与时解释。
  why_it_matters: |
    同样的阴阳性质处于不同位置可能判断不同；但古代尊卑类比不能直接正当化现代权力不平等。
  source_layer: 易传；孔颖达疏
  source_lines: [zhouyi:L3535, zhouyi:L3647-L3650, zhouyi-zhengyi:L154]
  chunk_id: [ck-ecfb9ca45a3a, ck-81f12ddb0aa9, ck-9162a2e78e03]
  tags: [term, line-position, social-boundary]
  task_ids: [ZY-T06, ZY-T08, ZY-T09]

- id: g21
  term: 中／中正
  type: term
  source_chapter: 彖传；周易正义·乾
  author_definition: |
    二、五居各自三爻卦之中，注疏常以“不偏”“中和”说明“中”；若又合乎相应阴阳位置则称中正。九二可“居中不偏”而非君位，显示中与尊位并非同义。
  key_distinction: |
    中 ≠ 自动吉；中正也不是脱离全卦即可套用的万能吉断。
    “正中/中正”在具体章句中可侧重不同，须回到该卦传注。
  why_it_matters: |
    这是王弼—孔疏结构分析的高频依据；正确使用可以说明判断链，错误使用则会退化为机械打分。
  source_layer: 易传；王弼注；孔颖达疏
  source_lines: [zhouyi:L396-L428, zhouyi-zhengyi:L152-L154, zhouyi-zhengyi:L6899-L6905]
  chunk_id: [ck-e59b75691cc7, ck-9162a2e78e03, ck-9d6754d54e1b]
  tags: [term, line-position, interpretive-rule, non-mechanical]
  task_ids: [ZY-T06, ZY-T07, ZY-T08]

- id: g22
  term: 正／当位／得位
  type: term
  source_chapter: 彖传、象传；周易正义各卦
  author_definition: |
    “正”可表示行动或德性正当，也可在爻位结构中表示阴阳居相应位置；“当位/得位”是后一路用法。注疏实际判断仍会合看中、应、时及全卦主旨。
  key_distinction: |
    ≠ “阳在阳位、阴在阴位就必吉”。
    ≠ 现代法律意义的正确或事实真伪。
    同一字兼有规范义与位置义，必须按语境拆分。
  why_it_matters: |
    防止把位置规则机械化，也防止将古代规范评价直接替代现代伦理判断。
  source_layer: 易传；王弼注；孔颖达疏
  source_lines: [zhouyi:L404-L428, zhouyi:L3535, zhouyi-zhengyi:L154]
  chunk_id: [ck-e59b75691cc7, ck-ecfb9ca45a3a, ck-9162a2e78e03]
  tags: [term, line-position, polysemy, boundary]
  task_ids: [ZY-T06, ZY-T07, ZY-T09]

- id: g23
  term: 应
  type: term
  source_chapter: 彖传；周易正义·乾
  author_definition: |
    在六爻结构中常指上下两体相隔三位的对应关系，孔疏列初与四、二与五、三与上相应；经传也用“感应、相求”表达关系能否相接。
  key_distinction: |
    ≠ 后世纳甲六爻“世／应”中的应爻全部规则。
    ≠ 现实中的某个人已被证明与该爻一一对应。
    = 原典注疏用于解释爻际呼应的一种结构关系。
  why_it_matters: |
    用户熟悉六爻后很容易把两个时代的“应”混为一谈；词典必须强制标注体系来源。
  source_layer: 易传；孔颖达疏
  source_lines: [zhouyi:L234, zhouyi-zhengyi:L154]
  chunk_id: [ck-e59b75691cc7, ck-9162a2e78e03]
  tags: [term, relation, source-separation, liuyao-collision]
  task_ids: [ZY-T06, ZY-T07, ZY-T08]

- id: g24
  term: 比
  type: term
  source_chapter: 周易正义·屯、比、睽
  author_definition: |
    在爻际分析中多指相邻爻的亲比、接近关系；注疏常区分“近而相得”与“近而不相得”。在《比》卦中“比”又有亲附、辅佐的卦义。
  key_distinction: |
    ≠ 只有“相邻”一个机械条件；相近仍可能不相得。
    ≠ 后世六爻所有合、冲、六亲关系的代称。
    “比”作为爻际关系与作为第八卦卦名须分开。
  why_it_matters: |
    让下游能区分邻接关系、是否相得和卦名义，避免看见相邻就直接断合作或感情亲近。
  source_layer: 王弼注；孔颖达疏
  source_lines: [zhouyi-zhengyi:L492, zhouyi-zhengyi:L915, zhouyi-zhengyi:L3361]
  chunk_id: [ck-2af78a248937, ck-a95dcccf3984, ck-c446f988be35]
  tags: [term, relation, polysemy, non-mechanical]
  task_ids: [ZY-T06, ZY-T07, ZY-T08]

- id: g25
  term: 刚／柔
  type: term
  source_chapter: 系辞上、系辞下
  author_definition: |
    刚柔既指阳、阴爻的相对性质，也用来描述推动、承受、强健、柔顺等关系。系辞称刚柔相推而生变化、又称其为“立本者”。
  key_distinction: |
    ≠ 男性/女性人格的固定本质。
    ≠ 刚必好、柔必坏；孔疏明确说刚若犯物、柔若卑佞，都偏离其义。
  why_it_matters: |
    能支持结构分析，同时避免把阴阳刚柔变成性别刻板印象或人格标签。
  source_layer: 易传；王弼/韩康伯注；孔颖达疏
  source_lines: [zhouyi:L3532, zhouyi:L3595, zhouyi:L3650, zhouyi-zhengyi:L6903-L6905]
  chunk_id: [ck-ecfb9ca45a3a, ck-81f12ddb0aa9, ck-9d6754d54e1b]
  tags: [term, polarity, change, gender-boundary]
  task_ids: [ZY-T03, ZY-T06, ZY-T09]

- id: g26
  term: 阴／阳／道
  type: term
  source_chapter: 系辞上；说卦
  author_definition: |
    系辞以“一阴一阳之谓道”描述两种相反相成力量的交替；说卦又以阴阳、柔刚安排六画。这里的“道”是贯通其运行关系的经典概念。
  key_distinction: |
    ≠ 简化成女性/男性、坏/好、负/正二元标签。
    ≠ 可直接测量并证明事件因果的现代物理能量。
  why_it_matters: |
    它是全书变化语言的底层概念，但也是现代神秘化和性别本质化最常见的来源，必须保留关系性而非实体化解释。
  source_layer: 易传
  source_lines: [zhouyi:L3541, zhouyi:L3670]
  chunk_id: [ck-ecfb9ca45a3a, ck-bbe02fd37700]
  tags: [term, polarity, philosophy, boundary]
  task_ids: [ZY-T03, ZY-T04, ZY-T09]

- id: g27
  term: 元／亨／利／贞（四德）
  type: term
  source_chapter: 文言；周易正义·乾
  author_definition: |
    文言释元为善之长、亨为嘉之会、利为义之和、贞为事之干；孔疏又保存“元始、亨通、利和、贞正”的训释，并说明四字在不同卦爻未必都以同一“四德”方式出现。
  key_distinction: |
    ≠ 固定翻译为“大吉大利、一定成功”。
    ≠ 每见“利”或“贞”都可自动凑成四德。
    = 乾卦传注中的德性组合；到其他卦须按句法与条件另解。
  why_it_matters: |
    这是卦辞中最高频、最易被俗化的判断语汇之一；准确分解可显著降低“见吉字就报喜”的误读。
  source_layer: 易传；孔颖达疏所存旧训与裁释
  source_lines: [zhouyi:L227-L253, zhouyi-zhengyi:L146, zhouyi-zhengyi:L206]
  chunk_id: [ck-e59b75691cc7, ck-9162a2e78e03, ck-82d589b52d3a]
  tags: [term, four-virtues, judgment, polysemy]
  task_ids: [ZY-T01, ZY-T02, ZY-T03, ZY-T07]

- id: g28
  term: 太极—两仪—四象—八卦
  type: concept-chain
  source_chapter: 系辞上
  author_definition: |
    系辞提出“易有太极，是生两仪，两仪生四象，四象生八卦”，构成从统摄原则到两分、四分、八卦的生成序列。
  key_distinction: |
    此处“四象”是生成链中的层级，≠ 泛指所有卦象，也不应未经来源便固定为某一套后世图表。
    该序列是经典宇宙论/象数表达，≠ 现代宇宙学实证模型。
  why_it_matters: |
    能回答基础学习中的结构问题，并防止把后世河图洛书、八宫或流派图式无来源地塞进经传层。
  source_layer: 易传
  source_lines: [zhouyi:L3581]
  chunk_id: [ck-81f12ddb0aa9]
  tags: [term, concept-chain, cosmology, source-boundary]
  task_ids: [ZY-T03, ZY-T04, ZY-T07]

- id: g29
  term: 卦主／一为主
  type: interpretive-term
  source_chapter: 王弼《略例·论彖》（孔疏引）
  author_definition: |
    王弼方法以“众不能治众，治众者至寡”为理据，主张论一卦之体往往取一爻或一个关键结构为主，以贯通全卦大略。
  key_distinction: |
    ≠ 经文自带、所有学派一致认可的明文规则。
    ≠ 后世六爻的“用神”或“世爻”。
    = 王弼义理解释的一种注家方法，具体卦仍须核对注疏如何选主。
  why_it_matters: |
    能解释王注为何突出某一爻，也能防止下游把注家选择伪装成原典唯一答案或纳甲取用规则。
  source_layer: 王弼《略例》经孔颖达疏引用
  source_lines: [zhouyi-zhengyi:L6422]
  chunk_id: [ck-dbb29901433d]
  tags: [term, commentator-method, source-layer, liuyao-collision]
  task_ids: [ZY-T06, ZY-T07, ZY-T08]

- id: g30
  term: 不可为典要／唯变所适
  type: methodological-term
  source_chapter: 系辞下；周易正义·乾
  author_definition: |
    系辞以“上下无常，刚柔相易，不可为典要，唯变所适”强调爻位与刚柔会随情境变化；韩康伯注以“不可立定准”说明不能设一成不变的准则。
  key_distinction: |
    ≠ 可以随意解释、无需证据。
    = 反对把活的时位关系压成僵硬口诀，同时仍须受卦爻原文、问题范围和来源层约束。
  why_it_matters: |
    这是防机械套规则和防事后圆说必须同时使用的方法边界：可以变通，但要留下可审计的解释链。
  source_layer: 易传；韩康伯注；孔颖达疏
  source_lines: [zhouyi:L3645, zhouyi-zhengyi:L146, zhouyi-zhengyi:L6843-L6865]
  chunk_id: [ck-81f12ddb0aa9, ck-9162a2e78e03, ck-9d6754d54e1b]
  tags: [term, methodology, non-mechanical, auditability]
  task_ids: [ZY-T03, ZY-T06, ZY-T08, ZY-T09]
```

## 覆盖说明

- 核心对象与符号：g01–g06。
- 经、传、注、疏解释媒介：g07–g13、g29–g30。
- 占筮与判断等级：g14–g18。
- 时位关系及与后世六爻同名词辨析：g19–g24。
- 阴阳刚柔与关键概念链：g25–g28。
- 两套 FTS5 索引均完成关键词与邻接块预筛；所有定义与引文随后回到 `source/zhouyi/raw-wikitext.txt` 和 `source/zhouyi-zhengyi/raw-wikitext.txt` 核验。
