# Stage 1 候选：框架、流程、推理与排障机制

> 提取范围：《周易》经、易传，以及王弼／韩康伯注、孔颖达疏。以下为不筛选候选，不表示现代事实判断或预测有效性；“经／传／注／疏”按来源分层。后世纳甲、六亲、世应、月建日辰等不在本文件中。

```yaml
- id: f01
  title: 卦总一时、爻趋其时的双层分析
  type: framework
  source_layer: 注疏（韩康伯注、孔颖达疏）
  source_chapter: 周易正义·系辞下卷八之一
  source_location: zhouyi-zhengyi:L6420-L6430
  source_quote: |
    “卦既总主一时，爻则就一时之中，各趣其所宜之时。”
  summary: |
    先把一卦看作共同的处境或阶段，再把每一爻看作该处境内部不同位置的适时行动。卦提供全局边界，爻提供局部变化，二者不能互相替代。
  tags: [hexagram, line, timing, two-level-analysis]
  task_ids: [ZY-T02, ZY-T06, ZY-T08]

- id: f02
  title: 彖象定卦义、爻辞察适时之功
  type: procedure
  source_layer: 注疏（韩康伯注、孔颖达疏）
  source_chapter: 周易正义·系辞下卷八之一
  source_location: zhouyi-zhengyi:L6420-L6422
  source_quote: |
    “立卦之義，則見於《彖》、《象》；適時之功，見存之爻辭。”
  summary: |
    形成解释时，先用彖、象确定全卦结构和主旨，再到相关爻辞判断处在该时中的行动条件；不应只摘一条爻辞脱离全卦下结论。
  inputs: [本卦, 相关爻位, 经传文本]
  outputs: [全卦主旨, 爻位条件, 二者一致或冲突说明]
  steps:
    - 查彖与大象，建立全卦语境。
    - 查相关爻辞与小象，识别该位置的行动条件。
    - 检查局部判断是否仍受全卦之时约束。
  missing_conditions: [若用于六爻，动爻与之卦必须由外部六爻引擎提供]
  tags: [interpretation, sequence, 彖, 象, 爻辞]
  task_ids: [ZY-T01, ZY-T02, ZY-T06, ZY-T08]

- id: f03
  title: 彖辞统论卦体与所由之主
  type: framework
  source_layer: 疏（孔颖达引《略例》）
  source_chapter: 周易正义·乾
  source_location: zhouyi-zhengyi:L178
  source_quote: |
    “彖者何也？統論一卦之體，明其所由之主。”
  summary: |
    阅读彖辞时寻找两个对象：全卦由哪些结构组成，以及什么少数关键因素统摄全卦。它是一种从全局到主导因素的压缩方法，不等于每卦机械指定同一爻为主。
  tags: [彖, whole-part, governing-factor, compression]
  task_ids: [ZY-T02, ZY-T06]

- id: f04
  title: 约以存博、简以兼众
  type: framework
  source_layer: 注疏（韩康伯注、孔颖达疏）
  source_chapter: 周易正义·系辞下卷八之七
  source_location: zhouyi-zhengyi:L6883-L6885
  source_quote: |
    “舉立象之統，論中爻之義，約以存博，簡以兼眾，雜物撰德，而一以貫之。”
  summary: |
    面对六爻的繁多信息，先用彖辞和中爻寻找统摄线索，再回查各爻是否被该线索合理覆盖。该法用于减复杂度，但不能以“主线”抹掉反例或其他爻的条件。
  tags: [complexity-reduction, middle-lines, synthesis, 彖]
  task_ids: [ZY-T02, ZY-T03, ZY-T06]

- id: f05
  title: 爻位—三才—中正结构矩阵
  type: framework
  source_layer: 易传与注疏
  source_chapter: 系辞下第八章；周易正义·乾
  source_location: zhouyi:L3647-L3652; zhouyi-zhengyi:L154-L158,L6899-L6905
  source_quote: |
    “二與四同功而異位……三與五同功而異位……兼三材而兩之，故六。”
  summary: |
    把六位按初至上、上下卦、天地人三才、中与不中、当位与失位来审计。文本给出二／四、三／五的倾向，但注疏同时显示它们只是条件，不能把“中正=必吉、失位=必凶”写成硬规则。
  tags: [line-position, 三才, 中正, conditional-reasoning]
  task_ids: [ZY-T03, ZY-T06]

- id: f06
  title: 应、比与时势的例外审计
  type: troubleshooting
  source_layer: 注疏（韩康伯注、孔颖达疏）
  source_chapter: 周易正义·系辞下卷八之九
  source_location: zhouyi-zhengyi:L6977-L6989
  source_quote: |
    “相違而無患者，得其應也；相順而皆凶者，乖於時也。存事以考之，則義可見矣。”
  summary: |
    当“相近却不相得”或“关系看似和顺”与结论冲突时，继续检查外应与所处之时。应可以缓解近比冲突，而乖时可使表面相顺仍然不利；最后要以具体卦爻事例复核。
  inputs: [相邻爻关系, 对应爻关系, 全卦之时]
  outputs: [主判断, 例外条件, 支持事例]
  steps:
    - 判断近爻是否相得。
    - 检查是否另有上下相应。
    - 检查双方虽顺是否乖于全卦时势。
    - 用同类卦爻事例验证解释是否成立。
  missing_conditions: [“相得”的具体判准须在逐卦注疏中核定]
  tags: [应, 比, exception, troubleshooting, timing]
  task_ids: [ZY-T06]

- id: f07
  title: 唯变所适：以变为常而不立定准
  type: framework
  source_layer: 易传、韩康伯注与孔颖达疏
  source_chapter: 系辞下第七章；周易正义·系辞下卷八之七
  source_location: zhouyi:L3644-L3647; zhouyi-zhengyi:L6843-L6865
  source_quote: |
    “不可為典要，唯變所適……循其辭，度其義，原尋其初，要結其終。”
  summary: |
    不把一条象、一个爻位或一个词固定成跨情境口诀。稳定的方法不是固定答案，而是循原文、度义、追溯起点、检查终局，并选择适合当前变化阶段的解释。
  tags: [adaptation, anti-dogma, contextual-reasoning, change]
  task_ids: [ZY-T03, ZY-T06, ZY-T09]

- id: f08
  title: 原始要终的六爻阶段审读
  type: procedure
  source_layer: 易传
  source_chapter: 系辞下第七章
  source_location: zhouyi:L3647
  source_quote: |
    “原始要終以為質也。六爻相雜，唯其時物也。其初難知，其上易知，本末也。”
  summary: |
    把六爻视作从初始到终局的阶段序列：先辨起点，再识别中段关系，最后用上爻检查走到极处的结果。该过程解释阶段，不提供现代日历上的精确应期。
  inputs: [本卦六爻, 所问问题的观察期限]
  outputs: [起点, 中段转折, 终局倾向]
  steps:
    - 标记初爻所示的起始条件。
    - 逐位记录条件、关系和行动变化。
    - 用上爻检查该趋势达到极处后的后果。
  missing_conditions: [实际时间换算不在原典中]
  tags: [beginning-end, stage-model, six-lines, timeline]
  task_ids: [ZY-T02, ZY-T06, ZY-T08]

- id: f09
  title: 辞—变—象—占四路用途分流
  type: framework
  source_layer: 易传
  source_chapter: 系辞上第十章
  source_location: zhouyi:L3569-L3576
  source_quote: |
    “以言者尚其辭，以動者尚其變，以制器者尚其象，以卜筮者尚其占。”
  summary: |
    先判断任务属于语言理解、行动变化、器用类比还是占筮决疑，再选择相应材料。它防止把整部《周易》压缩成单一预测术，也防止用取象代替原文或行动分析。
  tags: [routing, four-modes, 辞, 变, 象, 占]
  task_ids: [ZY-T03, ZY-T04, ZY-T08]

- id: f10
  title: 居观象辞、动观变占
  type: procedure
  source_layer: 易传
  source_chapter: 系辞上第二章
  source_location: zhouyi:L3531-L3535
  source_quote: |
    “居則觀其象而玩其辭，動則觀其變而玩其占。”
  summary: |
    未行动时以象和辞澄清处境；准备行动时再检查变动及占断所附条件。这里的“玩”是反复体会，不是跳过证据直接报吉凶。
  inputs: [问题状态, 卦象, 卦爻辞, 变动信息]
  outputs: [静态处境说明, 行动条件说明]
  steps:
    - 区分当前是理解处境还是准备行动。
    - 静态阶段查象与辞。
    - 行动阶段查变与占，并保留条件语句。
  missing_conditions: [变动爻如何生成须由起卦程序提供]
  tags: [reflection, action, interpretation, divination]
  task_ids: [ZY-T02, ZY-T03, ZY-T08]

- id: f11
  title: 拟形容—观会通—系辞的象爻生成链
  type: procedure
  source_layer: 易传与孔颖达疏
  source_chapter: 系辞上第八章；周易正义·系辞上卷七之六
  source_location: zhouyi:L3549-L3550; zhouyi-zhengyi:L6011-L6021
  source_quote: |
    “擬諸其形容，象其物宜……觀其會通……繫辭焉以斷其吉凶。”
  summary: |
    先用形态和适宜性建立象，再观察事物如何会合变通，最后才以文字表达得失。用于现代解释时应把“象征类比”和“现实因果”分开。
  inputs: [卦体, 物象, 变化关系]
  outputs: [象征映射, 会通条件, 文辞判断]
  steps:
    - 比拟对象形态，但不把相似当因果。
    - 检查对象在具体情境中的会合与变通。
    - 用卦爻辞限定判断方向与条件。
  missing_conditions: [类比有效范围需由任务语境另行限制]
  tags: [analogy, symbol, convergence, inference-chain]
  task_ids: [ZY-T02, ZY-T03, ZY-T04, ZY-T09]

- id: f12
  title: 拟而后言、议而后动
  type: procedure
  source_layer: 易传与孔颖达疏
  source_chapter: 系辞上第八章；周易正义·系辞上卷七之六
  source_location: zhouyi:L3550-L3562; zhouyi-zhengyi:L6023-L6043
  source_quote: |
    “擬之而後言，議之而後動，擬議以成其變化。”
  summary: |
    先比拟和核对表达是否贴合处境，再讨论行动及其外部响应，最后执行。注疏把言行视为会放大到远处的“枢机”，因此要求在微小处先审慎。
  inputs: [拟表达内容, 拟采取行动, 可能响应]
  outputs: [经校核的表述, 经讨论的行动方案]
  steps:
    - 拟度事实与比喻是否相称。
    - 讨论行动条件及善恶响应。
    - 只在前两步成立后行动。
  missing_conditions: [现实结果仍需证据验证]
  tags: [deliberation, communication, action-gate, prudence]
  task_ids: [ZY-T03, ZY-T09]

- id: f13
  title: 大衍揲蓍的四营十八变流程
  type: procedure
  source_layer: 易传与孔颖达疏
  source_chapter: 系辞上第九章；周易正义·系辞上卷七之八
  source_location: zhouyi:L3565-L3567; zhouyi-zhengyi:L6091-L6153
  source_quote: |
    “分而為二……掛一……揲之以四……歸奇於扐……四營而成易，十有八變而成卦。”
  summary: |
    以四十九策为操作数，每一变依次分二、挂一、揲四、归奇；三变定一爻，六爻共十八变成卦。它是文本记载的蓍筮程序，不是纳甲装卦算法。
  inputs: [四十九策, 六次爻位顺序]
  outputs: [六个七八九六爻值, 一卦]
  steps:
    - 将四十九策任意分为两部分。
    - 从一侧取一策挂置。
    - 两部分分别以四计数。
    - 合并余数与挂策，完成一变。
    - 重复三变确定一爻，自下而上完成六爻。
  missing_conditions: [现代程序随机实现应另行记录随机算法；本段不含纳甲、六亲、世应]
  tags: [yarrow, casting, algorithm, reproducibility]
  task_ids: [ZY-T03, ZY-T08]

- id: f14
  title: 七八静、九六变的爻值判定
  type: framework
  source_layer: 疏（孔颖达保存先儒说）
  source_chapter: 周易正义·乾
  source_location: zhouyi-zhengyi:L150
  source_quote: |
    “七為少陽，八為少陰，質而不變……九為老陽，六為老陰，文而從變。”
  summary: |
    用七、八、九、六区分阴阳与变不变：七八为少而不变，九六为老而变。孔疏将其作为一说保存，实际实现应注明所采用的爻值传统。
  tags: [line-value, changing-line, casting, variant-tradition]
  task_ids: [ZY-T03, ZY-T08]

- id: f15
  title: 参伍—错综—通变—极数
  type: procedure
  source_layer: 易传与孔颖达疏
  source_chapter: 系辞上第十章；周易正义·系辞上卷七之九
  source_location: zhouyi:L3570-L3576; zhouyi-zhengyi:L6190-L6192
  source_quote: |
    “參伍以變，錯綜其數，通其變……極其數，遂定天下之象。”
  summary: |
    对数与结构作交叉组合，汇总变化，再在给定体系内穷尽数值以确定象。作为现代程序框架时，其输出只是传统系统内部的卦象，不证明现实预测力。
  inputs: [爻值或蓍数]
  outputs: [组合后的阴阳结构, 卦象]
  steps:
    - 交叉组合并汇总相关数值。
    - 识别阴阳变化模式。
    - 在规则边界内定象。
  missing_conditions: [具体数值编码须与所用起卦法一致]
  tags: [number, transformation, aggregation, inference]
  task_ids: [ZY-T03, ZY-T08, ZY-T09]

- id: f16
  title: 吉—凶—悔吝—无咎的结果分层
  type: framework
  source_layer: 易传
  source_chapter: 系辞上第二、三章
  source_location: zhouyi:L3532-L3535
  source_quote: |
    “吉凶者，失得之象也；悔吝者，憂虞之象也……无咎者，善補過也。”
  summary: |
    将判断拆成得失、忧虞或小疵、补过免咎等不同层级。无咎不等于大吉，悔吝也不等于必然失败；输出应说明风险强度和转化条件。
  tags: [outcome-scale, risk, 吉凶, 悔吝, 无咎]
  task_ids: [ZY-T03, ZY-T09]

- id: f17
  title: 无咎的补过闭环
  type: troubleshooting
  source_layer: 易传与孔颖达疏
  source_chapter: 系辞上第三章；周易正义·乾九三
  source_location: zhouyi:L3535; zhouyi-zhengyi:L158
  source_quote: |
    “無咎者，善補過也……既能如此戒慎，則無罪咎；如其不然，則有咎。”
  summary: |
    出现危险或过失征兆时，不把“无咎”当无条件安全，而是寻找文本要求的戒慎、修正或补救行为；完成后再检查风险是否因此解除。
  inputs: [风险征兆, 爻辞中的条件, 可执行补救]
  outputs: [补过动作, 条件满足状态, 剩余风险]
  steps:
    - 找出造成咎的行为或位置条件。
    - 提取爻辞要求的戒慎或补救。
    - 验证条件是否真正完成，未完成则保留风险。
  missing_conditions: [现实安全问题必须使用现实证据和专业意见复核]
  tags: [recovery, remediation, conditional-safety, 无咎]
  task_ids: [ZY-T03, ZY-T06, ZY-T09]

- id: f18
  title: 大象的上下体组合与实象／假象审计
  type: framework
  source_layer: 疏（孔颖达）
  source_chapter: 周易正义·乾
  source_location: zhouyi-zhengyi:L190
  source_quote: |
    “或有實象，或有假象……雖有實象、假象，皆以義示人，總謂之象也。”
  summary: |
    先识别大象使用上下两体的哪种组合方式，再区分现实中可直接观察的“实象”和为表达义理而构造的“假象”，最后才转译成人事行动。假象不能字面化为现实事实。
  tags: [大象, upper-lower-trigram, real-image, constructed-image]
  task_ids: [ZY-T02, ZY-T04, ZY-T09]

- id: f19
  title: 仰观俯察、近身远物的取象尺度
  type: framework
  source_layer: 易传与孔颖达疏
  source_chapter: 系辞下第二章；说卦
  source_location: zhouyi:L3598; zhouyi-zhengyi:L6488-L6494,L7151-L7165
  source_quote: |
    “仰則觀象於天，俯則觀法於地……近取諸身，遠取諸物。”
  summary: |
    取象可以从宏观天地、具体环境、自身结构和外物四个尺度寻找相似关系。输出必须标明这是类比尺度，不得由身体之象直接推出疾病诊断。
  tags: [象, analogy-scale, 说卦, boundary]
  task_ids: [ZY-T04, ZY-T09]

- id: f20
  title: 杂卦的同类归纳与反差辨义
  type: framework
  source_layer: 韩康伯注与孔颖达疏
  source_chapter: 周易正义·杂卦第十一
  source_location: zhouyi-zhengyi:L7265-L7269
  source_quote: |
    “雜糅眾卦，錯綜其義，或以同相類，或以異相明也。”
  summary: |
    将多卦重新配对：相同者归类，相反者互相照明。它适合建立对卦检索和比较矩阵，但其配对次序不必当作事件发生顺序。
  tags: [comparison, contrast, classification, 杂卦]
  task_ids: [ZY-T05]

- id: f21
  title: 序卦的状态转移链
  type: framework
  source_layer: 易传与韩康伯注
  source_chapter: 序卦；周易正义·序卦第十
  source_location: zhouyi:L3745-L3813; zhouyi-zhengyi:L7241-L7253
  source_quote: |
    “物不可以終通，故受之以否；物不可以終否，故受之以同人。”
  summary: |
    用“状态不可永久维持—于是转入下一状态”组织六十四卦，形成连续转移链。可用于学习卦序和提出下一阶段假设，但这种叙事不是历史因果或现实预测定律。
  tags: [sequence, state-transition, 序卦, process-model]
  task_ids: [ZY-T05, ZY-T09]

- id: f22
  title: 穷—变—通—久的适应循环
  type: framework
  source_layer: 易传
  source_chapter: 系辞下第二章
  source_location: zhouyi:L3602
  source_quote: |
    “易窮則變，變則通，通則久。”
  summary: |
    当既有路径走到尽头时，先改变结构或做法；变化若重新打通约束，才可能持续。它是条件循环，不是“任何改变都会变好”。
  tags: [adaptation-cycle, bottleneck, change, sustainability]
  task_ids: [ZY-T03, ZY-T05, ZY-T09]

- id: f23
  title: 知几：微弱信号的早期处置
  type: troubleshooting
  source_layer: 易传与孔颖达疏
  source_chapter: 系辞下第四章；周易正义·系辞下卷八之四
  source_location: zhouyi:L3629-L3631; zhouyi-zhengyi:L6644-L6646
  source_quote: |
    “幾者，動之微，吉之先見者也。君子見幾而作，不俟終日。”
  summary: |
    将尚未放大的微小变化视为预警信号，在其演化为明显后果前行动。现代应用需先用可观察证据确认信号，避免把任何偶然都解释为“征兆”。
  inputs: [微小变化, 可验证指标, 行动阈值]
  outputs: [是否触发行动, 复核记录]
  steps:
    - 记录具体而可观察的变化。
    - 判断它是否与已定义风险路径有关。
    - 达到阈值即行动，并记录后续结果。
  missing_conditions: [原典没有现代统计阈值]
  tags: [early-warning, weak-signal, action-threshold, troubleshooting]
  task_ids: [ZY-T03, ZY-T09]

- id: f24
  title: 安—危、存—亡、治—乱的反向风险检查
  type: troubleshooting
  source_layer: 易传
  source_chapter: 系辞下第四章
  source_location: zhouyi:L3625
  source_quote: |
    “安而不忘危，存而不忘亡，治而不忘亂。”
  summary: |
    在状态良好时主动检查其反面失效模式：稳定时查危机、存续时查灭失、秩序时查混乱。它是预防性检查，不是宣告危险必然发生。
  inputs: [当前稳定状态, 反面失效模式]
  outputs: [风险清单, 预防动作]
  steps:
    - 写出当前被视为“安全／存在／有序”的依据。
    - 对应枚举其反面如何可能发生。
    - 为高影响路径设置观察与预防措施。
  missing_conditions: [概率与损失需用现实数据评估]
  tags: [inversion, resilience, prevention, risk-review]
  task_ids: [ZY-T09]

- id: f25
  title: 安身—易心—定交的行动前置三门
  type: procedure
  source_layer: 易传
  source_chapter: 系辞下第四章
  source_location: zhouyi:L3633
  source_quote: |
    “安其身而後動，易其心而後語，定其交而後求。”
  summary: |
    行动、表达请求和向他人求助前分别检查自身是否安定、心态是否平和、关系是否建立；任一门不满足时先修复前置条件。
  inputs: [拟行动, 拟表达, 拟请求对象]
  outputs: [行动就绪判断, 待修复条件]
  steps:
    - 确认自身安全与能力边界后再行动。
    - 调整恐惧或敌意后再表达。
    - 确认关系与授权后再提出请求。
  missing_conditions: [现代具体关系规范需另行设定]
  tags: [readiness, communication, relationship, gating]
  task_ids: [ZY-T03, ZY-T09]

- id: f26
  title: 渐积—阈值—后果的累积模型
  type: framework
  source_layer: 易传（文言、系辞下）
  source_chapter: 坤文言；系辞下第四章
  source_location: zhouyi:L303,L3623
  source_quote: |
    “非一朝一夕之故，其所由來者漸矣……善不積不足以成名，惡不積不足以滅身。”
  summary: |
    结果常由微小行为累积而非瞬间产生；分析时应追踪趋势、累积量与临界点，而不是只看最后事件。它能帮助复盘，但古文中的道德因果不能替代实证因果分析。
  tags: [accumulation, threshold, trend, causal-caution]
  task_ids: [ZY-T03, ZY-T09]

- id: f27
  title: 异说并列—证据核对—显式裁断
  type: procedure
  source_layer: 疏（孔颖达）
  source_chapter: 周易正义·系辞上卷七之八等
  source_location: zhouyi-zhengyi:L1-L129,L6105
  source_quote: |
    “義有多家，各有其說，未知孰是。今案王弼云……”
  summary: |
    先列出不同注家的解释，再核对经传语句和篇章次序，最后说明采用哪一说及理由；若证据不足就保留“未知孰是”。同时要暴露《正义》尊王弼的立场。
  inputs: [经传原文, 王韩注, 孔疏保存的异说]
  outputs: [异说矩阵, 采用意见, 证据与未决点]
  steps:
    - 按来源层列出各说，不合并改写。
    - 检查各说能否解释原文与上下文。
    - 记录孔疏的裁断及其学派偏好。
    - 无充分证据时保留分歧。
  missing_conditions: [仍需可靠校勘本验证异文]
  tags: [commentary, disagreement, adjudication, provenance]
  task_ids: [ZY-T01, ZY-T07]

- id: f28
  title: 不可一例、一类取义的反机械化检查
  type: troubleshooting
  source_layer: 疏（孔颖达）
  source_chapter: 周易正义·乾
  source_location: zhouyi-zhengyi:L146,L178,L206
  source_quote: |
    “不可一例求之，不可一類取之……若一一比並，曲生節例，非聖人之本趣。”
  summary: |
    当解释器试图把同一个词、象或德目固定映射到所有卦时，停止套表，回到本卦时、位、上下文和具体文例。跨卦规律只能作为待检假设，不能覆盖文本差异。
  inputs: [拟套用的通则, 当前卦爻上下文]
  outputs: [适用或不适用判断, 当前卦的特定解释]
  steps:
    - 标记正在跨卦复用的规则。
    - 查当前卦是否具备相同结构与语境。
    - 若有反例或语序差异，取消硬套并逐卦解释。
  missing_conditions: [需跨卦反例库支持自动检测]
  tags: [anti-pattern, exception, context, troubleshooting]
  task_ids: [ZY-T03, ZY-T06, ZY-T07]

- id: f29
  title: 自然象—卦德—人事的三段转译
  type: procedure
  source_layer: 疏（孔颖达）
  source_chapter: 周易正义·乾
  source_location: zhouyi-zhengyi:L146,L190,L206
  source_quote: |
    “聖人當法此自然之象而施人事……但須量力而行，各法其卦也。”
  summary: |
    先说明自然或卦体之象，再抽取卦德或功能，最后转译为与角色和能力相称的人事行动。必须保留“类比转译”标记，不能把自然现象当作现实事件的因果证明。
  inputs: [自然物象, 卦德, 使用者角色与能力]
  outputs: [传统类比, 可执行但有限的行动启发]
  steps:
    - 描述文本中的自然象或卦体关系。
    - 抽取其功能性卦德。
    - 依现实角色和能力缩放为行动启发。
    - 标注类比边界并要求现实验证。
  missing_conditions: [现代伦理和可行性评价来自原典之外]
  tags: [translation, analogy, action, boundary]
  task_ids: [ZY-T02, ZY-T04, ZY-T09]

- id: f30
  title: 本卦—动爻—之卦的经典义理桥接
  type: procedure
  source_layer: 易传与注疏（综合流程，不含纳甲）
  source_chapter: 系辞上第二、三章；系辞下第一、七章
  source_location: zhouyi:L3532-L3535,L3595,L3644-L3654; zhouyi-zhengyi:L6420-L6430
  source_quote: |
    “卦者時也；爻者趣時者也……變通者，趣時者也。”
  summary: |
    接收外部引擎已经算出的本卦、动爻和之卦：本卦给当前之时，动爻给此时内部的变动条件，之卦只作为变化方向的后续语境；分别查经传注疏，不重新装卦或计算纳甲。
  inputs: [本卦, 动爻列表, 之卦, 问题与观察期限]
  outputs: [本卦语境, 动爻条件, 变化方向, 来源分层引文]
  steps:
    - 验证卦名、爻位和之卦输入完整。
    - 依 f02 查本卦彖象与动爻经传。
    - 依 f01、f07 检查时势与变通。
    - 查之卦作为后续情境，不覆盖本卦和动爻条件。
    - 分列经、传、注、疏与现代反思。
  missing_conditions: [纳甲、六亲、世应、旺衰、六神均由外部六爻 Skill 提供]
  tags: [bridge, original-changing-result, provenance, liuyao-boundary]
  task_ids: [ZY-T01, ZY-T02, ZY-T06, ZY-T07, ZY-T08, ZY-T09]
```

## 覆盖与来源缺口

- 候选数：30（framework 14、procedure 11、troubleshooting 5）。
- 任务覆盖：`ZY-T01` 至 `ZY-T09` 均有候选映射；其中 `ZY-T08` 仅接收外部六爻引擎的本卦／动爻／之卦，不包含纳甲算法。
- 全量扫描：使用《周易》23 个分块和《周易正义》84 个分块回扫；重点方法段落在《系辞》上下、《说卦》《序卦》《杂卦》，并用六十四卦注疏中的乾、蒙、比、震等例证及跨卦时位／应比材料校验。
- 来源缺口：当前《周易》镜像标记 `Textquality|50%`；聚合《小象》有录入错误；《正义》存在 `02随`／`03随` 重复异文；王弼《周易略例》在本语料中仅由孔疏节引，未独立收录全文；程序随机起卦、现代风险规则与后世纳甲均是外部层，不能冒充原典。
