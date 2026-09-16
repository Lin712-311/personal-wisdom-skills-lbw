# 《周易》经传与《周易正义》案例、例题候选（Stage 1）

> 提取口径：`reported_case` 仅表示原文转述了某个人物或古代事件，不等于现代史学已证实；`worked_example` 表示文本用一个情境、数字或爻辞演示解释方法，不当作真实发生的事件。引文已回到两份 `raw-wikitext.txt` 逐条核验。

```yaml
- id: c01
  title: 包犧观象作卦并以离制罔罟
  type: case
  example_kind: reported_case
  source_chapter: 易传·系辞下第二章；周易正义·08.2
  source_layer: 易传转述；韩康伯注；孔颖达疏
  source_quote: |
    「古者包犧氏之王天下也，仰则观象于天，俯则观法于地……
    于是始作八卦……作结绳而为罔罟，以佃以渔，盖取诸离。」
    孔疏又指出：诸儒多从卦爻之象理解制器，而韩注直接取卦名；
    依韩学虽如此解释，孔疏仍评其「于义未善」。
  summary: |
    文本把“近取诸身、远取诸物”的观察写成八卦与渔猎器具的起源故事，
    用来展示“观象—分类—制器”的解释链。孔疏同时保留了对韩注“取名不取象”
    的方法异议，是来源冲突审计的直接材料。此为传统起源叙事，不作已证实史实。
  bound_to:
    - 象到器的类比推演
    - 注疏异说与来源冲突审计
  outcome: |
    原文称罔罟用于畋猎和捕鱼；未给出可独立核验的历史证据。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L3598
      chunk_id: ck-81f12ddb0aa9
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L6488-L6494
      chunk_id: ck-2d5924e6d646
  task_ids: [ZY-T03, ZY-T04, ZY-T07]
  tags: [reported-case, traditional-origin, image-to-instrument, source-conflict]

- id: c02
  title: 神农以益制耒耜、以噬嗑设市
  type: case
  example_kind: reported_case
  source_chapter: 易传·系辞下第二章；周易正义·08.2
  source_layer: 易传转述；韩康伯注；孔颖达疏
  source_quote: |
    「包犧氏没，神农氏作，斲木为耜，揉木为耒，耒耨之利，以教天下，
    盖取诸益。日中为市，致天下之民，聚天下之货，交易而退，各得其所，
    盖取诸噬嗑。」
  summary: |
    原文以农业工具和市场制度为两个传统转述例：益被解释为“制器致丰、利益万物”，
    噬嗑被解释为“聚合异方之货并设法合物”。它展示注疏如何从卦名义理回释制度用途，
    不是可复现的技术发明史。
  bound_to:
    - 卦名义理到现实制度的有限类比
    - 取象制器的注疏方法
  outcome: |
    文本称耒耜用于教民耕作，市场使交易者各得其所；实际历史结果未说明。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L3600
      chunk_id: ck-81f12ddb0aa9
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L6496-L6498
      chunk_id: ck-2d5924e6d646
  task_ids: [ZY-T03, ZY-T04, ZY-T07]
  tags: [reported-case, traditional-origin, agriculture, market, analogy]

- id: c03
  title: 黄帝尧舜九事展示“穷则变、变则通”
  type: case
  example_kind: reported_case
  source_chapter: 易传·系辞下第二章；周易正义·08.2
  source_layer: 易传转述；韩康伯注；孔颖达疏
  source_quote: |
    「易穷则变，变则通，通则久……黄帝、尧、舜垂衣裳而天下治，
    盖取诸乾坤。」下列舟楫、牛马、重门击柝、杵臼、弧矢、宫室、
    棺椁、书契等，并分别称取诸涣、随、豫、小过、睽、大壮、大过、夬。
  summary: |
    这组九事以技术或制度替代旧有做法，作为“问题穷尽后随时改变”的成组例证。
    孔疏明确说它只是“举大略，明前后相代之义，不必确在一时”，并质疑《帝王世纪》
    把九事全归黄帝、令尧舜无事的说法。因此应把它当传统文明起源叙事和类比用例，
    不能当精确年代或发明人证据。
  bound_to:
    - 穷则变、变则通、通则久
    - 卦义到器用的成组类比
    - 传统叙事的不确定性标注
  outcome: |
    文本内部结果包括“天下治”、交通远达、防御、加工食物、居住避雨、书契治理等；
    各项真实发生时间与归属未说明且孔疏承认不必确在一时。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L3602-L3609
      chunk_id: ck-81f12ddb0aa9
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L6500-L6546
      chunk_id: ck-2d5924e6d646
  task_ids: [ZY-T03, ZY-T04, ZY-T07]
  tags: [reported-case, nine-inventions, change, adaptation, traditional-narrative]

- id: c04
  title: 大衍筮法的策数与十八变演算
  type: case
  example_kind: worked_example
  source_chapter: 易传·系辞上第九章；周易正义·07.08
  source_layer: 易传程序；韩康伯注；孔颖达疏
  source_quote: |
    「大衍之数五十，其用四十有九，分而为二以象两，挂一以象三，
    揲之以四以象四时，归奇于扐以象闰……四营而成易，十有八变而成卦。」
    孔疏列：老阳一爻三十六策，六爻二百一十六；老阴一爻二十四策，
    六爻一百四十四；合三百六十。三变定一爻，六爻共十八变。
  summary: |
    这是文本中最接近可执行算法的演算例。输入为四十九策，单次变化依次执行分二、挂一、
    揲四、归奇；三变确定一爻，十八变得到六爻。孔疏还说明三揲所得多寡如何对应老阴、
    老阳、少阴、少阳。它没有给出一轮完整随机投筮记录，因此不能伪造具体样本卦。
  bound_to:
    - 蓍草筮法程序
    - 爻值与动静判定的原典来源
    - 现代程序起卦的来源差异记录
  input: |
    大衍五十、实际使用四十九策；每爻进行三变，共生成六爻。
  computation: |
    四营构成一变；三变定一爻；六爻共十八变。老阳 36×6=216，
    老阴 24×6=144，合计 360；两篇 384 爻按阴阳各半推得 11520 策。
  outcome: |
    得到一卦的程序被说明；原文没有给出某次实际操作的六个爻值或所得卦名。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L3565-L3567
      chunk_id: ck-ecfb9ca45a3a
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L6135-L6153
      chunk_id: ck-180e99eafc44
  task_ids: [ZY-T03, ZY-T08]
  tags: [worked-example, yarrow-stalk, calculation, eighteen-changes]

- id: c05
  title: 鸣鹤在阴演示“由爻象推到言行影响”
  type: case
  example_kind: worked_example
  source_chapter: 易传·系辞上第八章；周易正义·07.07
  source_layer: 易传解释；韩康伯注；孔颖达疏
  source_quote: |
    「鸣鹤在阴，其子和之……」子曰：「君子居其室，出其言善，
    则千里之外应之……言行，君子之枢机；枢机之发，荣辱之主也。」
  summary: |
    文本取《中孚》九二的鹤鸣相和，演示从同类相应的象转入“言行会向远近扩散”的伦理解释。
    孔疏明确称这是为“拟议而动”举证。它是释爻的示范，不是千里感应的经验性证明。
  bound_to:
    - 经文到传文的解释链
    - 拟议而动与行动后果
    - 象征类比的边界
  outcome: |
    文本给出的规范性结果是：善言获响应、恶言遭违离，言行关系荣辱；现实结果未说明。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L3550-L3552
      chunk_id: ck-ecfb9ca45a3a
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L6027-L6035
      chunk_id: ck-1dabed699d04
  task_ids: [ZY-T02, ZY-T03, ZY-T07]
  tags: [worked-example, zhongfu, analogy, speech, action]

- id: c06
  title: 负且乘演示“失位如何被解释为自招风险”
  type: case
  example_kind: worked_example
  source_chapter: 易传·系辞上第八章；周易正义·07.07
  source_layer: 易传解释；韩康伯注；孔颖达疏
  source_quote: |
    「负且乘，致寇至。」……「负也者，小人之事也；乘也者，君子之器也……
    慢藏诲盗……『负且乘，致寇至』，盗之招也。」
  summary: |
    文本把“负物者却乘车”的不匹配解释成身份、器用与位置不相称，并由此推导资源暴露和冲突风险。
    孔疏称此例说明“当量身而行”。现代复用只能抽象成“角色—权限—资源是否匹配”的审计问题，
    不得保留其小人/君子的等级身份判定，也不得用“冶容诲淫”归责受害者。
  bound_to:
    - 时位中应比结构分析
    - 经传注疏的伦理类比
    - 时代偏见与安全边界
  outcome: |
    文本设定的结果是“致寇至/盗之招”；这是解释性情境，不是已记录的真实案件。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L3562
      chunk_id: ck-ecfb9ca45a3a
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L6079-L6089
      chunk_id: ck-1dabed699d04
  task_ids: [ZY-T02, ZY-T03, ZY-T06, ZY-T09]
  tags: [worked-example, position, role-fit, risk, historical-bias]

- id: c07
  title: 射隼演示“藏器于身、待时而动”
  type: case
  example_kind: worked_example
  source_chapter: 易传·系辞下第四章；周易正义·08.4
  source_layer: 易传解释；韩康伯注；孔颖达疏
  source_quote: |
    「公用射隼于高墉之上，获之，无不利。」子曰：
    「君子藏器于身，待时而动，何不利之有。动而不括，是以出而有获。」
  summary: |
    文本把弓矢、射者与可射之时拆开，演示“先具备能力，再等待合适窗口”的时位解释。
    孔疏进一步用解卦上六与六三的爻位关系说明为何此时可以行动。
  bound_to:
    - 时机与行动条件
    - 动爻的时位解释
    - 全卦结构而非关键词断语
  outcome: |
    示范情境写作“获之，无不利”；没有真实人物、日期或后续事件。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L3621
      chunk_id: ck-81f12ddb0aa9
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L6616-L6618
      chunk_id: ck-6965fe71e15f
  task_ids: [ZY-T02, ZY-T03, ZY-T06]
  tags: [worked-example, timing, preparation, line-position]

- id: c08
  title: 困六三演示“非所困而困、非所据而据”
  type: case
  example_kind: worked_example
  source_chapter: 易传·系辞下第四章；周易正义·08.4
  source_layer: 易传解释；孔颖达疏
  source_quote: |
    「困于石，据于蒺藜，入于其宫，不见其妻，凶。」子曰：
    「非所困而困焉，名必辱；非所据而据焉，身必危。」
  summary: |
    传文把《困》六三的物象改写为“错误接近上方对象、错误压在下方对象”的位置关系；
    孔疏再以六三与九四、九二及无应解释这一链条。它适合作为“爻位—关系—条件—判断”
    的 worked example，而不是现实死亡预测模板。
  bound_to:
    - 时位中应比结构分析
    - 爻位证据链审计
    - 禁止把象辞字面化为死亡预测
  outcome: |
    文本内部判断为名辱、身危、不见其妻、凶；没有真实事件结果。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L3619
      chunk_id: ck-81f12ddb0aa9
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L6612-L6614
      chunk_id: ck-6965fe71e15f
  task_ids: [ZY-T02, ZY-T06, ZY-T09]
  tags: [worked-example, kun, line-position, response, safety]

- id: c09
  title: 文王与箕子被用作明夷的历史型例证
  type: case
  example_kind: reported_case
  source_chapter: 明夷卦彖传、六五；周易正义·04明夷
  source_layer: 经（六五）；彖传；王弼注；孔颖达疏
  source_quote: |
    「内文明而外柔顺，以蒙大难，文王以之……内难而能正其志，箕子以之。」
    孔疏释文王“内怀文明……外执柔顺”，称其蒙难而身得保全；
    又以箕子近殷纣而执志不回，说明“利贞”。
  summary: |
    明夷用文王和箕子说明在昏暗、危险环境中如何外晦内明、保持正志。
    这是彖传和注疏采用的历史型道德例证；人物叙事应标为文本传统，不从这里证明具体史实。
  bound_to:
    - 全卦主旨与人物例证
    - 艰贞、用晦而明的条件解释
    - 经传注疏分层
  outcome: |
    孔疏称文王以外柔顺而身得保全；箕子“执志不回、明不可息”。
    未说明可独立核验的事件时间线。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L1387-L1391
      chunk_id: ck-44440ccf8bdb
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L3176-L3178, L3218-L3222
      chunk_id: ck-cf4137876423
  task_ids: [ZY-T01, ZY-T02, ZY-T07]
  tags: [reported-case, mingyi, king-wen, jizi, source-layering]

- id: c10
  title: 帝乙归妹说明“居中、履顺、降身相应”
  type: case
  example_kind: reported_case
  source_chapter: 泰六五；归妹六五；周易正义·01泰
  source_layer: 经；象传；王弼注；孔颖达疏
  source_quote: |
    「帝乙归妹，以祉，元吉。」孔疏曰：作《易》者引“帝乙归妹”，
    以明女处尊位而履中居顺、降身应二、不失其礼。
  summary: |
    注疏将帝乙嫁妹的传统叙事绑定到泰六五的爻位结构，用作“尊位而能下应”的例证。
    它反映古代婚姻和尊卑伦理；现代关系解释不得据此要求一方服从或降低地位。
  bound_to:
    - 中位与应爻的结构解释
    - 经文典故的注疏展开
    - 古代婚姻伦理边界
  outcome: |
    爻辞给出“以祉、元吉”；历史婚姻的实际结果未说明。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L584; L1963-L1975
      chunk_id: ck-e99800c7d57a
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L1147-L1151
      chunk_id: ck-3916e7369ab0
  task_ids: [ZY-T01, ZY-T02, ZY-T06, ZY-T09]
  tags: [reported-case, diyi, marriage, line-position, historical-bias]

- id: c11
  title: 康侯受赐与一日三接说明晋进
  type: case
  example_kind: reported_case
  source_chapter: 晋卦辞、彖传；周易正义·04晋
  source_layer: 经；彖传；孔颖达疏
  source_quote: |
    「晋：康侯用锡马蕃庶，昼日三接。」孔疏释为升进之臣被天子赐以众多车马，
    且一昼三次接见；又与讼卦“终朝三褫”对释，说明黜陟之速。
  summary: |
    这是晋卦用来具象化“进”的人物情境。孔疏把坤顺、离明及柔进上行连接到受赏和亲宠，
    并与讼卦失服相对照。康侯的具体历史身份与事件真实性在本来源中未核定。
  bound_to:
    - 卦体、爻位与卦辞情境的会合
    - 晋退对照解释
    - 经传注疏分层
  outcome: |
    文本内结果是获赐马蕃庶并一日三接；来源未交代其后续人生结果。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L1350-L1359
      chunk_id: ck-44440ccf8bdb
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L3098-L3108
      chunk_id: ck-d53ce34649a9
  task_ids: [ZY-T01, ZY-T02, ZY-T06, ZY-T07]
  tags: [reported-case, jin, reward, promotion, comparison]

- id: c12
  title: 高宗伐鬼方三年克之
  type: case
  example_kind: reported_case
  source_chapter: 既济九三；周易正义·06既济
  source_layer: 经；象传；王弼注；孔颖达疏
  source_quote: |
    「高宗伐鬼方，三年克之，小人勿用。」孔疏认高宗为殷王武丁，
    以其在衰势中三年乃克，解释“居衰末而能济”；《象》曰「憊也」。
  summary: |
    经文把长期征伐作为既济九三的情境，注疏据此强调即使最终完成，过程也衰惫而漫长，
    并非“见三年就机械断三年应期”。这是带历史人物的文本转述，不凭本来源证明征战细节。
  bound_to:
    - 既济中的持续成本与终局风险
    - 数字不得机械转成现代应期
    - 爻位与人物典故结合
  outcome: |
    经文明确说“三年克之”，象传强调“憊”；小人用事的实际例子未说明。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L2249, L2261
      chunk_id: ck-b3594fe9c2b7
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L5547-L5553
      chunk_id: ck-e1d5555c3013
  task_ids: [ZY-T01, ZY-T02, ZY-T06, ZY-T09]
  tags: [reported-case, gaozong, jiji, duration, anti-literal-timing]

- id: c13
  title: 东邻杀牛与西邻禴祭的对照情境
  type: case
  example_kind: worked_example
  source_chapter: 既济九五；周易正义·06既济
  source_layer: 经；象传；王弼注；孔颖达疏
  source_quote: |
    「东邻杀牛，不如西邻之禴祭，实受其福。」《象》曰：
    「东邻杀牛，不如西邻之时也；实受其福，吉大来也。」
    王注总结「在于合时，不在于丰也」。
  summary: |
    这是“投入丰厚”与“合时、修德、致敬”之间的对照例。注疏用它说明判断不能只看资源规模，
    还要看时与行为质量。东邻、西邻在本文中是说明性角色，不应当作经核验的祭祀事件。
  bound_to:
    - 时重于表面规模
    - 对照情境的条件判断
    - 防止只凭单一强弱指标断吉凶
  outcome: |
    文本设定西邻“实受其福、吉大来”；现实事件未说明。
  evidence:
    - source_file: source/zhouyi/raw-wikitext.txt
      lines: L2251-L2263
      chunk_id: ck-b3594fe9c2b7
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L5563-L5573
      chunk_id: ck-e1d5555c3013
  task_ids: [ZY-T02, ZY-T06, ZY-T09]
  tags: [worked-example, comparison, timing, sincerity, jiji]

- id: c14
  title: “丧羊于易”展示注疏内部争议
  type: case
  example_kind: worked_example
  source_chapter: 大壮六五；周易正义·04大壮
  source_layer: 经；王弼注；庄氏异议（孔疏转述）；孔颖达疏
  source_quote: |
    王注一方面说「必丧其羊，失其所居」，另一方面说「能丧壮于易，不于险难，故得无悔」。
    庄氏据此批评两义矛盾；孔疏回答前者是必然趋势，后者是趁平易、寇难未来时主动舍壮。
  summary: |
    此例不讲现实事件，而是一次完整的注疏解释争论：同一句“丧羊”究竟同时包含被迫失去与主动舍弃，
    庄氏指出张力，孔疏用“趋势—预防时机”两阶段化解。它可训练 Skill 展示支持、反对和裁断，
    不把孔疏裁断伪装成唯一古义。
  bound_to:
    - 经传注疏冲突矩阵
    - 时机与主动预防
    - 同一爻辞的多义审计
  outcome: |
    注疏层结论是六五应在险难未至时舍其壮，因此“无悔”；不存在现实事件结果。
  evidence:
    - source_file: source/zhouyi-zhengyi/raw-wikitext.txt
      lines: L3067-L3073
      chunk_id: ck-d53ce34649a9
  task_ids: [ZY-T02, ZY-T06, ZY-T07]
  tags: [worked-example, commentary-dispute, dazhuang, interpretation-audit]
```

## 检索与覆盖说明

- 两套 FTS 索引均已查询，并用 `--neighbors 1` 检查命中块上下文；核心检索词包括：`古者`、`昔者`、`包犧`、`神农`、`黄帝 尧 舜`、`制器`、`大衍之数`、`十八变`、`筮`、`占`、`帝乙归妹`、`康侯`、`文王以之`、`箕子`、`高宗伐鬼方`、`东邻杀牛`、`负且乘`、`鸣鹤在阴`、`困于石`、`公用射隼`、`丧羊于易`。
- 每个收录条目均回查 `raw-wikitext.txt` 行号；邻接块用于确认章节和上下文，未把索引摘要当最终证据。
- 未发现作者亲历型 `firsthand` 案例；古代人物与文明起源材料均为经传或注疏的 `reported_case`，神话性出生叙事没有作为史实案例收录。
- 未发现带一整组实际蓍草余数、六爻结果及所得卦名的完整占筮实录。`c04` 仅是程序与策数演算，明确把“实际样本卦未说明”写入 outcome。
- 卦爻辞中还有大量无名情境（婚媾、征伐、田猎、涉川等）；只有在传文或注疏明确拿来演示解释方法、或具有清楚的历史转述功能时才收入，避免把全部爻辞误称为真实案例。
- 《周易正义》援引《帝王世纪》《左传》《公羊传》《诗》等外部古籍；本阶段只记录《正义》如何使用它们，尚未逐一完成外部版本核验。
