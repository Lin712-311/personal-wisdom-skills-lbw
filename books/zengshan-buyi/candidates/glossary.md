# 《增刪卜易》核心术语候选（Stage 1）

> 本文件只收集候选，不代表已通过 Stage 1.5 三重验证。术语解释重建的是古籍内部规则，不认可其具有经现代科学验证的预测效力。

## 预筛与来源口径

- 频次方法：对 `source/raw-wikitext.txt` 使用 `rg -o -F` 做大小写无关性不适用的固定字符串逐项计数，再以 `rg -n` 与原文行窗回查；计数包含目录、表格、占例和现代补充，只用于召回，不作为入选或真实性证明。
- 主要锚点频次：用神 329、主事爻 25、六亲 36、世爻 358、应爻 76、元神 82、忌神 86、仇神 12、动爻 173、变爻 29、旺相 198、休囚 173、月建 107、日辰 80、月破 100、旬空 97、生扶 89、克害 38、六合 71、六冲 141、三合 58、暗动 39、飞神 21、伏神 48、进神 72、退神 52、反吟 51、伏吟 21、随鬼入墓 26、应期 13、分占 19、多占 12、再占 53、两现 9。
- 覆盖：逐条回查卷一章 5–26及四篇总注、卷二章 27–32、序，以及分占的领域例。候选覆盖 `ZSBY-T01`–`ZSBY-T08`；`ZSBY-T09` 作为所有条目的来源层约束。
- 来源分层：下列定义证据均取古籍正文、明确的“野鹤曰/觉子曰/李我平曰”段或增删本未署名正文；`L21-L124` 的原剑现代增订、`L4602-L4692` 的疑似录入增补及 `L5097/L5199/L5331` 的“原剑按”不充当古籍定义证据。当前维基镜像转录质量有限，未署名正文不强判给某一作者。

---

- id: g01
  term: 用神／主事爻
  type: term
  author_definition: 针对本次所问的人或事所取的核心爻；不同问题按父母、官鬼、兄弟、妻财、子孙等类别取用，后文又把“定事吉凶之爻”称为主象或主事爻。
  key_distinction: 不是宗教意义的神，也不是固定取世爻；它是随问题改变的目标变量。主事爻是同一功能的总称。
  why_it_matters: 取用决定后续元神、忌神、旺衰、动变和应期的参照点，是 `ZSBY-T03/T04` 的入口。
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T08, ZSBY-T09]
  tags: [核心概念, 目标变量, 古籍正文]
  source_chapter: 用神章第八；各门类题头总注章第又二十六（L5165-L5176, L6004-L6006）
  source_quote: “主象，卽定事吉凶之爻。古法以卦中世爻爲主象，又名主事爻。”

- id: g02
  term: 六亲
  type: term
  author_definition: 父母、兄弟、官鬼、妻财、子孙五类爻名，由本宫五行关系排定；既指亲属，也映射文书、财物、功名、医药等事类。
  key_distinction: 不只表示血缘亲属，而是书内的五类关系与事物编码；具体所指必须由问题合同限定。
  why_it_matters: 六亲同时参与装卦与取用，误按日常亲属义理解会破坏 `ZSBY-T02/T03/T08` 的路由。
  task_ids: [ZSBY-T02, ZSBY-T03, ZSBY-T08, ZSBY-T09]
  tags: [表示系统, 类目映射, 古籍正文]
  source_chapter: 六亲歌章第五；用神章第八（L5075-L5095, L5172-L5176）
  source_quote: “占貨財、珠寶、倉庫一切使用之財物亦以妻財爻爲用神。”

- id: g03
  term: 世爻／应爻
  type: term
  author_definition: 世爻是卦中标识自身或问卦立场的爻，应爻与世隔两位；在具体门类中，应爻常作他人、对方或目的地等对象。
  key_distinction: 不是永远固定的两个人物标签；世应的语义服从占者、对象和事类，且有些问题会舍世应而专取六亲或内外卦。
  why_it_matters: 它们确定关系视角和输入结构，直接影响代占、彼此比较及领域解释。
  task_ids: [ZSBY-T02, ZSBY-T03, ZSBY-T08, ZSBY-T09]
  tags: [表示系统, 关系视角, 古籍正文]
  source_chapter: 世应章第六；各门类题头总注章第又二十六（L5105-L5115, L6004）
  source_quote: “隔世爻兩位卽是應爻，餘卦仿此。”

- id: g04
  term: 元神
  type: term
  author_definition: 生扶用神的爻；是否真正能生用神，还须看旺相、日月生扶、动化、空破、墓绝等条件。
  key_distinction: 不是精神实体或“元气”的泛称；它是相对当前用神才成立的支持因素，且“有元神”不等于一定有效。
  why_it_matters: 用于区分表面支持与有效支持，是建立支持/反对证据账本的核心角色。
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T09]
  tags: [四神, 支持因素, 古籍正文]
  source_chapter: 用神元神忌神仇神章第九；元神忌神衰旺章第十（L5183-L5186, L5209-L5226）
  source_quote: “元神，生用神之神卽爲元神。”

- id: g05
  term: 忌神
  type: term
  author_definition: 克害用神的爻；其危害是否成立，还要审旺衰、动静、日月生扶、空破、墓绝和与元神同动等条件。
  key_distinction: 不是普遍禁忌或固定凶物；它只相对于本次用神定义，也可能因休囚受制而无力。
  why_it_matters: 它是反对证据的主要角色，若脱离用神与效力条件，会把任何“忌神出现”误判为结果。
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T09]
  tags: [四神, 阻碍因素, 古籍正文]
  source_chapter: 用神元神忌神仇神章第九；元神忌神衰旺章第十（L5183-L5186, L5228-L5230）
  source_quote: “忌神克用神之爻也。”

- id: g06
  term: 仇神
  type: term
  author_definition: 克元神并生忌神的爻，是通过削弱支持、增强阻碍而作用于用神的二阶不利因素。
  key_distinction: 不是现实中的仇人，也不等同于直接克用神的忌神；其位置在“元神—忌神—用神”关系链中。
  why_it_matters: 它使规则账本能够表达间接作用，避免把所有不利信号压成同一种直接克害。
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T09]
  tags: [四神, 二阶因素, 古籍正文]
  source_chapter: 用神元神忌神仇神章第九（L5183-L5186）
  source_quote: “仇神者克元神而生忌神也。”

- id: g07
  term: 动爻／变爻
  type: term
  author_definition: 六爻中的老阳、老阴发动后阴阳转换；原位发动者为动爻，所化出的对应爻为变爻，变爻主要回头生克冲合本位动爻。
  key_distinction: “动”“变”是排卦中的形式运算，不是现实对象移动；书中特别限定变爻不能任意生克其他爻。
  why_it_matters: 它决定输入转换和作用边界，是装卦校验与冲突审计的高风险规则点。
  task_ids: [ZSBY-T02, ZSBY-T04, ZSBY-T05, ZSBY-T09]
  tags: [表示系统, 变换规则, 古籍正文]
  source_chapter: 动变章第七；动变生克冲合章第十五（L5122-L5161, L5372-L5387）
  source_quote: “變出之爻能生克沖合本位之動爻，不能生克他爻。”

- id: g08
  term: 旺相／休囚
  type: term
  author_definition: 依月令、季节及生扶等判断爻的相对强弱：当令者旺，受生而有余气者相，其余多作休囚；书中再以日月、动变修正。
  key_distinction: 不是物理能量或统计强度，而是术数系统内的情境效力标签；也不能只凭季节一项机械判定。
  why_it_matters: 同一生克、合冲、空破信号会因强弱条件而改变解释，贯穿整个规则账本。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T09]
  tags: [强弱状态, 时令, 古籍正文]
  source_chapter: 四时旺相章第又十五（L5394-L5409）
  source_quote: “正二月木爲旺、火爲相，其餘金火土作休囚。”

- id: g09
  term: 月建／月将／月令
  type: term
  author_definition: 三者在本书此处同指占卦月的当令地支，被赋予一月内生、克、冲、合、扶起飞伏及制约动变的权力。
  key_distinction: 不是日历月份本身，而是被当作全卦作用源的地支；它能令爻旺，也能把相冲之爻定为月破。
  why_it_matters: 月建是 `ZSBY-T04` 的一级作用源，也是旺衰、月破和应期的共同输入。
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T09]
  tags: [时间变量, 作用源, 古籍正文]
  source_chapter: 月将章第十六（L5412-L5419）
  source_quote: “月將卽是月建又爲月令。掌一月之權，司三旬之令。”

- id: g10
  term: 日辰／日建
  type: term
  author_definition: 占卦日的地支，书中视作与月建并列的作用源，可生克冲合诸爻，并以冲静爻区分暗动、日破，以冲空、冲合改变状态。
  key_distinction: 不是单纯日期标签；在内部规则里它具有四时皆旺的操作权，但仍须与月建及其他动爻合看。
  why_it_matters: 日辰连接强弱、暗动、冲空和应期，若漏记会使规则链不可复现。
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T09]
  tags: [时间变量, 作用源, 古籍正文]
  source_chapter: 日辰章第十七（L5508-L5543）
  source_quote: “日辰爲六爻之主宰，司四時之旺相。”

- id: g11
  term: 月破
  type: term
  author_definition: 爻的地支被当月月建相冲；书中修订旧说，主张发动、得生或等到出月、实破、逢合时，月破未必始终无用。
  key_distinction: 不是现实事物破损，也不是永久失效；它是随时间和动静条件变化的状态。
  why_it_matters: 月破同时影响效力与应期，而且是本书反驳“一概无用”旧诀的代表术语。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T09]
  tags: [时态状态, 辨误, 增删本正文]
  source_chapter: 月破章第二十七（L245-L306）
  source_quote: “月建沖之爲月破……目下雖破，出月則不破，今日雖破，實破之日則不破，合之日則不破。”

- id: g12
  term: 旬空／空亡
  type: term
  author_definition: 每一甲旬只有十日，未被轮到的两个地支称空亡或旬空；书中再按旺、动、生扶、填实、冲空等条件判断其是否实际有效。
  key_distinction: 不是绝对“不存在”；有出旬、填实、冲起与“到底全空”等分支，且作者常以再占处理歧义。
  why_it_matters: 它是效力判断与应期生成的核心时态，也暴露了规则解释自由度，必须留痕。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T07, ZSBY-T09]
  tags: [时态状态, 应期, 古籍正文]
  source_chapter: 旬空章第二十六（L5884-L5954）
  source_quote: “此十日之內，並無戌亥，以爻逢戌亥爲空亡，又名旬空，餘仿此。”

- id: g13
  term: 生扶／克害
  type: term
  author_definition: 生扶表示对用神或元神的支持，克害表示压制或伤害；书中要求比较来自月、日、动爻、变爻的多重作用及强弱，而非只看一处。
  key_distinction: 不是一般语言里的帮助与伤害，而是五行关系在特定爻位、时令和动变约束下的方向性操作。
  why_it_matters: 这是 `ZSBY-T04` 证据账本最基本的正反方向；没有来源、对象和效力条件便不能合并计数。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T09]
  tags: [作用关系, 证据方向, 古籍正文]
  source_chapter: 五行相生章第十一；五行相克章第十二；克处逢生章第十三（L5250-L5318）
  source_quote: “大凡用神、元神克少生多爲吉。忌神者以克少生多爲凶，所以忌神宜克不宜生也。”

- id: g14
  term: 六合／六冲
  type: term
  author_definition: 六合包括日月合爻、爻与爻合、动化合及卦的合变；六冲包括日月冲爻、卦逢六冲、动化冲及爻与爻冲。合常表聚结或牵绊，冲常表散开或冲起。
  key_distinction: 合不恒吉、冲不恒凶；必须结合所问是喜聚还是喜散、用神是否有气，以及合住、冲开、月破、暗动等具体类型。
  why_it_matters: 合冲跨越关系、状态和应期三层，最容易被固定口诀误用，须在冲突矩阵中保留条件。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T09]
  tags: [作用关系, 合冲, 古籍正文]
  source_chapter: 六合章第十九；六冲章第二十（L5595-L5664, L5667-L5740）
  source_quote: “沖者散也，凡占凶事宜於沖散、占吉事而不宜，必兼用神而言。”

- id: g15
  term: 三合局
  type: term
  author_definition: 申子辰、巳酉丑、寅午戌、亥卯未四组地支按规定的动爻或动变组合成局；局的六亲属性与对世爻的生克决定书内取义。
  key_distinction: 不是任见三个地支就算成局；需要满足动爻组合、补齐、空破填实或入墓冲开等条件，且成局本身不保证吉。
  why_it_matters: 三合把多个爻聚合成复合作用源，是规则冲突、内外卦比较与等待条件的重要节点。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T09]
  tags: [组合关系, 条件规则, 古籍正文]
  source_chapter: 六合章第十九（三合段，L5648-L5650）
  source_quote: “三合局中若有一空破者，待塡滿之日月成之。有一爻入墓者待沖開之日成之。”

- id: g16
  term: 暗动／日破
  type: term
  author_definition: 静爻受日辰冲时，旺相者称暗动，休囚衰弱者称日破；同一个“日冲静爻”因强弱不同而分成相反的效力状态。
  key_distinction: 暗动不是明示的动爻，日破也不同于月破；两者都不能只由“被日冲”一项机械决定。
  why_it_matters: 该对概念直接展示书中“同一操作、按强弱分支”的规则形态，是实现与审计时必须显式化的分支。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T09]
  tags: [时态状态, 分支规则, 古籍正文]
  source_chapter: 日辰章第十七；暗动章第二十二（L5517, L5769-L5785）
  source_quote: “靜爻旺相日辰沖之爲暗動，靜爻休囚日辰沖之爲破。”

- id: g17
  term: 飞神／伏神
  type: term
  author_definition: 用神不上卦且日月也不提供用神时，到本宫首卦寻相应六亲；藏在本卦某爻之下者为伏神，覆盖它的本卦之爻为飞神。
  key_distinction: 是排卦结构中的显隐关系，不是飞行或潜伏的实体；本书又明确说野鹤本人遇用神不现时倾向再占，而不依伏神定断。
  why_it_matters: 它既是传统取用的回退规则，也是作者修订旧法的关键冲突，必须同时记录规则与否定性按语。
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T05, ZSBY-T07, ZSBY-T09]
  tags: [显隐结构, 回退规则, 增删本正文]
  source_chapter: 飞伏神章第二十八（L309-L420）
  source_quote: “姤卦二爻之亥水卽爲飛神，寅木妻財卽爲伏神……予於用神不現，卽有伏神亦不用之，再占兩卦用神必現。”

- id: g18
  term: 进神／退神
  type: term
  author_definition: 特定地支之间的动化序列被称为进神或退神，象征推进与退减；是否当下进退仍受旺衰、空破、日月生扶和所问远近限制。
  key_distinction: 不是一般动作趋势，也不是看到“化进/化退”即可下结论；书中列出待时、填实和近事不退等多种条件。
  why_it_matters: 它把方向与时间条件绑定，是趋势判断、旧诀辨误和应期推导的共同术语。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T09]
  tags: [动变类型, 趋势, 增删本正文]
  source_chapter: 进神退神章第二十九（L431-L682）
  source_quote: “進神退神者，爻之動而化也，化進化退，吉凶禍福有喜忌之分。”

- id: g19
  term: 反吟／伏吟
  type: term
  author_definition: 反吟指内外卦或爻动变化形成反复冲克的型态，常取反复不定；伏吟指变化后地支重复，常取忧郁、滞留、欲动不能。
  key_distinction: 不是心理学的反刍或诗歌吟诵；反复/滞留只是附加象，书中仍要求先看用神旺衰及有无回头冲克。
  why_it_matters: 这对术语常被旧法当作独立凶断，本书则以用神条件修正，适合进入规则冲突矩阵。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T09]
  tags: [卦变类型, 反复滞留, 古籍正文]
  source_chapter: 反伏章第二十五（L5828-L5881）
  source_quote: “伏吟之卦，用神旺相，沖開之年月，其志則伸；用神休囚，沖開之年月，憂鬱不吉。”

- id: g20
  term: 随鬼入墓／三墓
  type: term
  author_definition: 三墓被本书限定为用爻入日墓、入动墓、动而化墓；所谓随鬼入墓，仍须配合世爻或用神的旺衰、受克和墓爻是否被冲破判断。
  key_distinction: 不是一见“入墓”就判凶；觉子明确删改这种机械断法，主张旺而有扶或墓被冲破时不能同论。
  why_it_matters: 这是“旧诀—增删修订—条件化例外”的典型，可检验冲突审计是否忠实记录反例。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T09]
  tags: [墓绝, 辨误, 觉子增删]
  source_chapter: 随鬼入墓章第三十；各门类题头总注（L685-L754, L6005）
  source_quote: “三墓，卽用爻入日墓、入動墓、動而化墓，非古法之世墓、身墓、命墓。”

- id: g21
  term: 应期
  type: term
  author_definition: 书内判断被认为会显现的年、月、日、时；按静爻逢值冲、动爻逢值合、空破填冲、入墓冲开、衰绝遇生旺等规则生成候选时间。
  key_distinction: 不是统计学置信区间或经验证的时间预测；远近尺度、多个候选点和“占近应远”等条款都增加解释弹性。
  why_it_matters: 它是 `ZSBY-T06` 的直接输出，必须附逐步推导、截止窗口和不确定性，不能写成必然事件。
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T09]
  tags: [时间映射, 输出规则, 古籍正文]
  source_chapter: 各门类应期总注章第又二十六（L6010-L6035）
  source_quote: “靜而逢值逢沖……動而逢合逢值……勿謂爻之不驗，遠近當分。”

- id: g22
  term: 分占／多占（含再占、复占）
  type: term
  author_definition: 分占是把父母、功名、财福、婚育等不同问题拆开，各占一卦；多占或再占是在用神不现、卦意恍惚或需合断时，再取一卦或由相关者另占。
  key_distinction: 分占解决“一个问题混入多个目标”，多占解决“同一目标仍不明”；两者不应混为无限重问，序中虽主张多占，也承认卦已明时不必再占。
  why_it_matters: 它既是问题合同和模糊回退的核心，也带来确认偏误风险，下游必须预设重占理由、采用判据和停止规则。
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T07, ZSBY-T08, ZSBY-T09]
  tags: [问题分解, 复核, 野鹤与觉子]
  source_chapter: 序；飞伏神章第二十八；身命章第三十六（L4553-L4570, L376-L409, L2077）
  source_quote: “卦有恍惚者，再占一卦，不可妄斷……乃分占之法也，占父母占兄弟，另占一卦終身財福何如。”

- id: g23
  term: 用神两现
  type: term
  author_definition: 同一类用神在一卦中出现两爻或更多时，旧法按旺相、动静、空破、受伤择一；野鹤用占例说明有时反而取空破之爻，并依多卦合断。
  key_distinction: 不是简单“选最旺的一爻”；本书把旧有优先级当作可被占例推翻的启发式，实际上没有给出唯一、无歧义的选择算法。
  why_it_matters: 它是 `ZSBY-T03` 的关键歧义分支，也是验证规则是否会事后选取最有利解释的审计点。
  task_ids: [ZSBY-T03, ZSBY-T05, ZSBY-T07, ZSBY-T09]
  tags: [取用歧义, 辨误, 增删本正文]
  source_chapter: 两现章第三十二（L830-L867）
  source_quote: “用神兩現……捨其休囚，用其旺相；捨其靜爻，而用動爻……此古法也。”
