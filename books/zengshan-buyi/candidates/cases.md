# 《增刪卜易》案例候选（Stage 1）

> 本文件只收集案例候选，不在此阶段筛选、验证术数有效性或把古籍占例当作现代科学证据。
> 原书占例数量很多；下列为覆盖不同方法主题与关键任务的代表性提取，**并未穷尽**，也不构成完整的成功或失败样本。
> 检索使用了 `占`、`得`、`占得`、`之卦`、`驗`、`不驗`、`果`、`後`、`次日`、`再占`、`又占`、`分占`、`應期` 等词。索引中卷二至卷四合并为超大块 `ck-a271e944b34d`，故所有候选均另回 `source/raw-wikitext.txt` 的行号窗口核验。

```yaml
- id: c01
  title: 现代录入层的六次摇钱排卦示例
  type: case
  example_kind: worked_example
  source_layer: 现代录入层（原文注释称“疑爲錄入者加的料”）
  source_chapter: 占卦法
  source_location: source/raw-wikitext.txt:L4602-L4644
  chunk_id: [ck-fa4fe72c8018, ck-6d7be6643114]
  source_quote: |
    “現搖一卦爲例……第一次搖得一背，畫作⚊……六次得兩背，畫作⚋……卽得水火旣濟卦。”
  summary: |
    录入者用六次铜钱结果演示自下而上记录六爻，再把上下三爻组成内外卦并命名为水火既济。
    这是排卦输入格式的演示，不是古籍主体中的实证事件。
  bound_to:
    - 六次爻值到本卦、动爻与卦名的转换
    - 来源层级标注
  outcome: 原文只给出演算结果“水火既济卦”，未说明现实事件结果。
  task_ids: [ZSBY-T02, ZSBY-T09]
  tags: [worked-example, casting, source-layer, modern-entry]

- id: c02
  title: 月破官爻经复占后断承袭世职
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 月破章第二十七
  source_location: source/raw-wikitext.txt:L253-L271
  chunk_id: ck-a271e944b34d
  source_quote: |
    “命之再占，又得出水地比卦……前卦官臨月破，定於實破之年，果於巳年承襲長房世職。”
  summary: |
    首卦官爻月破、世爻旬空造成疑义，叙述者要求再占；把两卦合看后，以“实破之年”给出应期。
  bound_to:
    - 月破不是一律无用
    - 卦意有疑时复占并合断
    - 实破应期
  outcome: 书中记为巳年承袭长房世职。
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T07]
  tags: [firsthand, month-break, re-divination, timing, office]

- id: c03
  title: 父亲归期按逢合与出空分两段应验
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 月破章第二十七
  source_location: source/raw-wikitext.txt:L273-L282
  chunk_id: ck-a271e944b34d
  source_quote: |
    “卯日有信，午未日必歸，果於卯日得信，乙未日到家……破而逢合之日也……出空之日到也。”
  summary: |
    同一归期问题被拆成“先得信”和“后到家”两个节点，分别以月破逢合和变爻出空解释应期。
  bound_to:
    - 事件分阶段输出
    - 月破逢合与旬空出空的应期
  outcome: 书中记为卯日得信、乙未日到家。
  task_ids: [ZSBY-T04, ZSBY-T06]
  tags: [firsthand, return, staged-outcome, timing]

- id: c04
  title: 父病用神不现时连续复占
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 飛伏神章第二十八
  source_location: source/raw-wikitext.txt:L378-L407
  chunk_id: ck-a271e944b34d
  source_quote: |
    “父母用神不現……令再卜之……前兩卦巳火旺不受傷克，乃應目前之愈，此卦亥水克父，今冬難延。”
  summary: |
    首卦父母用神不现，叙述者不直接采用伏神，而让本人、儿子和妻子多次占问；其后区分“目前可愈”与“今冬有危”。
  bound_to:
    - 用神不现时复占而非强取伏神
    - 多卦合断与近远期区分
    - 疾病领域路由（仅作历史文本重建）
  outcome: 书中记为病人眼前好转，后于亥月去世。
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T07, ZSBY-T08]
  tags: [firsthand, hidden-useful-god, repeated-divination, illness, high-risk]

- id: c05
  title: 乡试以官星进神断连捷
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 進神退神章第二十九
  source_location: source/raw-wikitext.txt:L447-L456
  chunk_id: ck-a271e944b34d
  source_quote: |
    “酉金官星持世旺相……九五爻上官進神財助生扶……果得連捷。”
  summary: |
    叙述者综合官星持世、暗动、进神和财爻生扶，判断当年乡试及次年考试连续成功。
  bound_to:
    - 进神与生扶的组合判断
    - 科举领域的用神路由
  outcome: 书中记为“果得连捷”，未给出更详细名次或日期。
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T08]
  tags: [firsthand, examination, advancing-spirit, outcome]

- id: c06
  title: 求婚以回头克解除日断允婚
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 進神退神章第二十九
  source_location: source/raw-wikitext.txt:L458-L469
  chunk_id: ck-a271e944b34d
  source_quote: |
    “必待午日沖去子水，午火又合世爻，其婚必成，果於午日允婚。”
  summary: |
    案例以财爻持世化进为主线，同时处理子孙回头克和鬼爻化退，最后把午日定为阻碍解除并合世的应期。
  bound_to:
    - 动变冲合的证据合并
    - 进退神与应期
    - 婚姻领域路由
  outcome: 书中记为午日允婚。
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T06, ZSBY-T08]
  tags: [firsthand, marriage, advancing-retreating, timing]

- id: c07
  title: 危症以近事不作退神断次日遇医
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 進神退神章第二十九
  source_location: source/raw-wikitext.txt:L517-L526
  chunk_id: ck-a271e944b34d
  source_quote: |
    “子孫持世，明日辰日必遇良醫，果於次日用鍼而愈……占近事豈可曰退？”
  summary: |
    叙述者把同一退神结构按近事与久远事区分，近事中不把它立即解释为退败，并给出次日应期。
  bound_to:
    - 进退神须结合时间尺度
    - 疾病与医者领域路由（仅作历史文本重建）
  outcome: 书中记为次日针治后痊愈。
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T08]
  tags: [firsthand, illness, retreating-spirit, timing, high-risk]

- id: c08
  title: 开金银器皿店以财爻化进择日
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 進神退神章第二十九
  source_location: source/raw-wikitext.txt:L660-L669
  chunk_id: ck-a271e944b34d
  source_quote: |
    “妻財持世化進神乃久遠豐隆之象……果開市於戌日，至今此店興盛豐隆。”
  summary: |
    案例把财爻持世化进解释为生意可久，并据此选择甲戌日开张。
  bound_to:
    - 财爻持世与化进
    - 开店领域路由
    - 动空填实的时点选择
  outcome: 书中记为戌日开市，且叙述时店铺仍兴盛。
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T08]
  tags: [firsthand, commerce, advancing-spirit, timing]

- id: c09
  title: 开煤应期初断六月未中
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 獨發章第三十一
  source_location: source/raw-wikitext.txt:L794-L805
  chunk_id: ck-a271e944b34d
  source_quote: |
    “予曰：財靜未月沖開，應在六月。及至六月，竟不見煤……至亥年辰月始得見煤。”
  summary: |
    叙述者先按静财逢冲把见煤定在六月，但六月没有发生；后来到亥年辰月才见煤，并事后改以独发亥水化辰土解释。
  bound_to:
    - 应期规则的误差与事后改释
    - 独发、静爻逢冲规则冲突审计
    - 求财/开采领域路由
  outcome: 初断六月未中；书中记为亥年辰月始见煤。原书未提供连续失败样本或独立核验。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T08]
  tags: [firsthand, mining, failed-timing, post-hoc, counterevidence]

- id: c10
  title: 女病先疑独静再由母亲复占
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 獨發章第三十一
  source_location: source/raw-wikitext.txt:L807-L825
  chunk_id: ck-a271e944b34d
  source_quote: |
    “然亦不敢竟斷，命伊母再占一卦……與前卦相合……果於寅日全愈。”
  summary: |
    首卦可按独静推寅日，但叙述者认为只凭独静无法区分生死，于是让母亲再占，并以两卦相合才下结论。
  bound_to:
    - 独静规则不得脱离用神
    - 复占确认与应期
    - 疾病领域路由（仅作历史文本重建）
  outcome: 书中记为寅日痊愈。
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T07, ZSBY-T08]
  tags: [firsthand, illness, solitary-static, re-divination, high-risk]

- id: c11
  title: 南行连续得到同卦后决定启程
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予占”自述；具体编修层未进一步校勘）
  source_chapter: 增刪黃金策千金賦章第三十五
  source_location: source/raw-wikitext.txt:L1386-L1417
  chunk_id: ck-a271e944b34d
  source_quote: |
    “連得三次，予始悟……卽於巳日起程……又得大有之大壯……此卦得之四次……乃促我行也。”
  summary: |
    叙述者因首两次占问仍有疑虑而暂不行，第三次同卦后改变判断，途中第四次又得同卦，被用作继续前行的确认。
  bound_to:
    - 复占与相同结果的合断
    - 墓、破、冲开的时间转换
    - 出行领域路由
  outcome: 书中记为叙述者最终启程并于次年二月到达目的地；“三四月如心”的完整结果未在本段单独交代。
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T07, ZSBY-T08]
  tags: [firsthand, travel, repeated-divination, uncertainty]

- id: c12
  title: 同时惦记求财与丈人病导致两卦所应互换
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 增刪黃金策千金賦章第三十五
  source_location: source/raw-wikitext.txt:L1471-L1493
  chunk_id: ck-a271e944b34d
  source_quote: |
    “神以前卦應丈人之病……後卦反應求財……予故曰：一念只占一事。”
  summary: |
    来人先问求财、后问丈人病，文本称两项意念混杂使前后两卦的对象互换；作者据此强调一次只问一事。
  bound_to:
    - 一念一事的问题合同
    - 混问导致取用与结果归属歧义
    - 案例解释自由度审计
  outcome: 书中明确说后卦对应求财且“不得”；丈人病的最终现实结果未说明，只记“病重辰日”。
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T05]
  tags: [firsthand, problem-contract, mixed-intent, attribution]

- id: c13
  title: 官员命家人代占防害导致取用分歧
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 增刪黃金策千金賦章第三十五
  source_location: source/raw-wikitext.txt:L1495-L1508
  chunk_id: ck-a271e944b34d
  source_quote: |
    “竟應官府自己之念，世爻爲用……至申日聞信，有人往上司揭告，被人勸阻，訟之未成。”
  summary: |
    官员让家人代占。若按家人代占主人，取父母爻；文本却说卦应了官员自己的念头，以世爻为用，因此借例反对代占个人事务。
  bound_to:
    - 明确占者、对象与代占关系
    - 取用歧义分支
  outcome: 书中记为申日获知有人欲揭告，但被劝阻，诉讼未成。
  task_ids: [ZSBY-T01, ZSBY-T03]
  tags: [firsthand, proxy-divination, problem-contract, use-selection]

- id: c14
  title: 表问流年实问援例功名
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 增刪黃金策千金賦章第三十五
  source_location: source/raw-wikitext.txt:L1547-L1556
  chunk_id: ck-a271e944b34d
  source_quote: |
    “此人已往軍前援例，故占流年……彼曰：煩人援例，如不知成否？……果於申日文書實收俱到。”
  summary: |
    来人表面问“流年”，真实关切是援例能否办成；叙述者在澄清目的后改按功名取官星，并以静爻逢冲定申日。
  bound_to:
    - 追问真实任务而非按表面题目机械取用
    - 领域路由决定用神
    - 静而逢冲应期
  outcome: 书中记为申日文书与实收俱到。
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T06, ZSBY-T08]
  tags: [firsthand, concealed-intent, clarification, office, timing]

- id: c15
  title: 占何时雨并在一小时内核对
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 天時章第三十五
  source_location: source/raw-wikitext.txt:L1651-L1660
  chunk_id: ck-a271e944b34d
  source_quote: |
    “本日卯時占何時雨？卽於辰時起雲，辰末巳初雷雨大作。”
  summary: |
    叙述者用父母爻暗动与变鬼解释当天起云及雷雨的小时应期；结果可在同日观察。
  bound_to:
    - 天时领域的快速反馈案例
    - 暗动与小时应期
  outcome: 书中记为辰时起云、辰末巳初雷雨。
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T08]
  tags: [firsthand, weather, rapid-feedback, timing]

- id: c16
  title: 连占三卦判卯日雨辰日晴
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 天時章第三十五
  source_location: source/raw-wikitext.txt:L1868-L1886
  chunk_id: ck-a271e944b34d
  source_quote: |
    “再占一卦……再占一卦又得艮之謙卦……果於寅日云卯日大雨辰日大晴。”
  summary: |
    首卦留下酉日或卯日两个候选，叙述者连续复占，把天气序列细化为寅日云、卯日雨、辰日晴。
  bound_to:
    - 多占缩小应期候选
    - 动空、出空与变爻的序列解释
  outcome: 书中记为寅日有云、卯日大雨、辰日大晴。
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T07, ZSBY-T08]
  tags: [firsthand, weather, repeated-divination, sequence]

- id: c17
  title: 以连续天时占例劝慰待赦官员
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 天時章第三十五
  source_location: source/raw-wikitext.txt:L2025-L2065
  chunk_id: ck-a271e944b34d
  source_quote: |
    “未時大雨，申時云散天開……公宜寬心，過半月，果蒙恩赦。”
  summary: |
    官员不信自己会获赦，叙述者先让多人连续占雨，并以当日未时雨、申时晴的可观察结果作为说服材料，再类推到赦免判断。
  bound_to:
    - 多占与短期可观察结果
    - 从天时案例类推人事的论证方式
    - 跨领域类推风险审计
  outcome: 书中记为未时大雨、申时转晴，官员半月后获赦。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T07, ZSBY-T08]
  tags: [firsthand, weather, pardon, analogy, repeated-divination]

- id: c18
  title: 孕妇平安与胎儿性别混问后同卦兼断
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”占例，附觉子按语）
  source_chapter: 胎孕章第八十七
  source_location: source/raw-wikitext.txt:L3764-L3773
  chunk_id: ck-a271e944b34d
  source_quote: |
    “彼曰：兩事俱問。予曰：日後須宜分占，不可同問……果於壬申日生女，產母平安。”
  summary: |
    来人同时问孕妇安危和胎儿性别，叙述者先指出应分占，但认为本卦两项皆现而作兼断；觉子随后限制临产危急时不可兼断性别。
  bound_to:
    - 复合问题应分占
    - 同卦兼断作为例外及其边界
    - 胎产领域路由（仅作历史文本重建）
  outcome: 书中记为壬申日生女、产妇平安。
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T05, ZSBY-T06, ZSBY-T08]
  tags: [firsthand, pregnancy, question-splitting, exception, high-risk]

- id: c19
  title: 舟行遇风雨后回看卦象形成顺风规则
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”亲历自述；具体编修层未进一步校勘）
  source_chapter: 行人章第九十四前占例
  source_location: source/raw-wikitext.txt:L3910-L3919
  chunk_id: ck-a271e944b34d
  source_quote: |
    “及至戊子日，風雨大作，舟泊南康，始悟此卦……果泊五日，巳日天晴得風順矣。”
  summary: |
    叙述者出舟前只看出“忧疑”，实际遇风雨停泊后才回看父爻与子孙变爻，并由此提出“子孙为行舟顺风”的经验解释。
  bound_to:
    - 从事后回看形成领域规则
    - 舟行领域的父母、子孙映射
    - 规则发现中的事后解释审计
  outcome: 书中记为戊子日遇风雨，在南康停泊五日，巳日天晴顺风；出发前未明确预判该过程。
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T08]
  tags: [firsthand, boat-travel, post-hoc-learning, weather]

- id: c20
  title: 子占父病问人参却断不必服药
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 醫卜往治章第一百零四
  source_location: source/raw-wikitext.txt:L4116-L4127
  chunk_id: ck-a271e944b34d
  source_quote: |
    “人參莫用，藥亦莫服，明日辰日沖空卽愈，果於雞鳴蘇醒，次日不藥而愈。”
  summary: |
    问题表面是能否服人参，叙述者却把发动的父母爻作为主要信息，转而判断病人次日会自行苏醒。
  bound_to:
    - 动爻优先与问题对象重定向
    - 医药领域路由（高风险，仅作历史文本重建）
    - 冲空应期
  outcome: 书中记为鸡鸣苏醒、次日未服药而愈；无现代医疗记录或独立核验。
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T06, ZSBY-T08]
  tags: [firsthand, medicine, problem-redirection, timing, high-risk]

- id: c21
  title: 占地形势后拒绝兼断名利六亲
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 占地形勢章第一百二十
  source_location: source/raw-wikitext.txt:L4416-L4425
  chunk_id: ck-a271e944b34d
  source_quote: |
    “彼曰：果一一無錯，此地吉否？予曰：此乃占地穴之形勢耳，非關吉凶禍福……須宜另占一卦。”
  summary: |
    叙述者先按世应、青龙白虎等描述地形，来人称与现场相符；但当来人追问整体吉凶时，叙述者拒绝用同一卦兼断功名、财运和六亲。
  bound_to:
    - 一卦一任务与领域边界
    - 地形描述和利害判断分开
    - 领域路由与另占条件
  outcome: 来人只确认地形描述“一一无错”；后续功名、财运、六亲结果未说明。
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T08]
  tags: [firsthand, geomancy, scope-boundary, question-splitting]

- id: c22
  title: 求财旬空经复占后断全无
  type: case
  example_kind: firsthand
  source_layer: 古籍主体／野鶴署名分页面
  source_chapter: 旬空章第二十六
  source_location: source/raw-wikitext.txt:L5902-L5926
  chunk_id: ck-d7b4e51ed9a2
  source_quote: |
    “古法有气不爲空，不敢竟斷，命之再占……後卦子水財空伏……後果全無。”
  summary: |
    首卦财爻旬空但仍“有气”，叙述者不肯立断，要求再占；第二卦财伏、空且受克后，才判断求财无望。
  bound_to:
    - 旬空有疑时复占
    - 两卦合断
    - 求财领域路由
  outcome: 书中记为最终全无所得。
  task_ids: [ZSBY-T04, ZSBY-T07, ZSBY-T08]
  tags: [firsthand, void, re-divination, finance]

- id: c23
  title: 远行求财旬空经复占后断可行
  type: case
  example_kind: firsthand
  source_layer: 古籍主体／野鶴署名分页面
  source_chapter: 旬空章第二十六
  source_location: source/raw-wikitext.txt:L5928-L5950
  chunk_id: ck-d7b4e51ed9a2
  source_quote: |
    “命之再占……此卦與前卦相同，此行大有財發……後到彼地……諸事順心，滿載而歸。”
  summary: |
    首卦世爻旬空但财旺生世，吉凶解释冲突；复占后叙述者把两卦合看，给出启程日和到地后的旺月判断。
  bound_to:
    - 旬空冲突的复占回退
    - 出空与出月应期
    - 出行求财领域路由
  outcome: 书中记为乙卯日起程，寅卯月间诸事顺心并满载而归。
  task_ids: [ZSBY-T04, ZSBY-T06, ZSBY-T07, ZSBY-T08]
  tags: [firsthand, void, travel, finance, re-divination]

- id: c24
  title: 问财福却转断读书功名及其反复
  type: case
  example_kind: firsthand
  source_layer: 古籍主体（“予”叙述；具体编修层未进一步校勘）
  source_chapter: 終身財福章第三十七
  source_location: source/raw-wikitext.txt:L2141-L2150
  chunk_id: ck-a271e944b34d
  source_quote: |
    “爾𨿽以財爲問，而神告將來可成名……後果於寅年醫好富翁，厚贈讀書。午年一榜。”
  summary: |
    来人因家贫询问财福并考虑行医，叙述者却按官父两旺转而判断会得到读书机缘、后有功名，同时以六冲和财绝解释仕途与财力不能持久。
  bound_to:
    - 财福、功名与职业问题的领域路由
    - 占此应彼的解释方式
    - 六冲与用神证据的冲突审计
  outcome: 书中记为寅年医好富翁而获资助读书，午年中榜并援例为县令，后来仕途受挫且囊中空乏。
  task_ids: [ZSBY-T01, ZSBY-T04, ZSBY-T05, ZSBY-T08]
  tags: [firsthand, wealth, career, office, scope-shift]
```
