# 《周易》经传与《周易正义》反例／失败模式候选（Stage 1）

> 本文件只提取候选，不在本阶段把传统占筮主张判为科学事实。A 部分重建经、传、注、疏内部明确提出的失败机制；B 部分是现代项目边界，明确标作外加规范，不冒充古籍原话。
>
> 检索使用 `.cangjie/zhouyi` 与 `.cangjie/zhengyi` 两套 FTS5 索引，关键词覆盖 `再三瀆 / 不告 / 不可一例 / 不可一類 / 不可以一爻為例 / 不可為典要 / 唯變所適 / 失時 / 失位 / 不當位 / 亢 / 迷復 / 苦節 / 終亂 / 不能退 / 不能遂 / 往吝 / 終凶 / 失律`。每条引文均返回对应 `raw-wikitext.txt` 行窗口复核；聚合页不作为唯一证据。

## A. 古籍内部明确警告的失败模式

```yaml
- id: ce01
  title: 对同一疑问反复筮问，直到得到想要的答案
  type: counter-example
  source_layer: 经文（蒙卦卦辞）＋彖传
  source_chapter: 周易／蒙
  source_location: source/zhouyi/raw-wikitext.txt:L355-L364
  chunk_id: ck-a876867b04e3
  source_quote: |
    “初筮告，再三瀆，瀆則不告。”彖传释为：“再三瀆，瀆則不告，瀆蒙也。”
  failure_mode: |
    同一问题在没有新增事实时连续起卦，再从多个结果中挑选最顺眼的一次。
  mechanism: |
    文本内部把反复求问视为对占问的亵渎；在可审计流程中，它还会扩大结果空间，允许事后筛选和确认偏误。
  warning_signs:
    - 问题、对象和期限都没有变化却再次起卦
    - 因第一次结果“不喜欢”而要求重来
    - 只保存最后一次结果，不保留前次记录
  bound_to:
    - 起卦纪律与一次性承诺
    - 六爻桥接器
    - 高风险停机与现实核验器
  task_ids: [ZY-T03, ZY-T08, ZY-T09]
  tags: [repeat-casting, cherry-picking, internal-warning]

- id: ce02
  title: 把一个物象限制成唯一现实对象
  type: counter-example
  source_layer: 孔颖达疏
  source_chapter: 周易正义／乾卦名义
  source_location: source/zhouyi-zhengyi/raw-wikitext.txt:L142-L146
  chunk_id: ck-9162a2e78e03
  source_quote: |
    “若執一事，不可包萬物之象；若限局一象，不可總萬有之事……不可一例求之，不可一類取之。”
  failure_mode: |
    看到龙、马、水、火、身体部位或家庭角色，就不顾卦、爻、时位和问题上下文，直接锁定一个人物、疾病或事件。
  mechanism: |
    孔疏明确认为卦名取象体例不一，单一事物或单一象都不足以包摄万事；字面一一映射会把类比误当成确定指认。
  warning_signs:
    - “见到某象就一定代表某人／某病／某物”
    - 解释没有说明取象层与上下文
    - 同一象在不同段落中被强行保持同一个字典义
  bound_to:
    - 八卦取象限制器
    - 卦爻原典定位器
    - 来源分层与归属审计器
  task_ids: [ZY-T01, ZY-T04, ZY-T07, ZY-T09]
  tags: [literalism, symbol-mapping, rigid-analogy, internal-warning]

- id: ce03
  title: 把一个爻的吉凶条件推广成所有爻的通则
  type: counter-example
  source_layer: 孔颖达疏
  source_chapter: 周易正义／系辞上
  source_location: source/zhouyi-zhengyi/raw-wikitext.txt:L5759-L5761
  chunk_id: ck-7fbfe4f5e2c3
  source_quote: |
    “或吉凶據文可知……亦有爻處吉凶之際，吉凶未定……原夫《易》之為書，曲明萬象……不可以一爻為例，義有變通也。”
  failure_mode: |
    从某个爻的“中、正、应、无咎、吉、凶”总结一条跨卦公式，并机械用于所有卦爻。
  mechanism: |
    孔疏列出不写吉凶、吉凶未定、善应才无咎、一爻内小贞吉大贞凶、同一事情始终异等多类情况，说明判词依赖具体文本和条件。
  warning_signs:
    - 用一个案例证明“凡是某结构都吉／都凶”
    - 把“无咎”直接翻译成“大吉”
    - 不检查同爻内部或事情始终是否有相反条件
  bound_to:
    - 时位中应比结构分析器
    - 经传注疏冲突矩阵
    - 本卦—动爻—之卦义理辅助器
  task_ids: [ZY-T03, ZY-T06, ZY-T07]
  tags: [single-example-rule, overgeneralization, conditional-judgment, internal-warning]

- id: ce04
  title: 把《易》冻结成不随时势改变的口诀
  type: counter-example
  source_layer: 系辞下＋韩康伯注＋孔颖达疏
  source_chapter: 周易／系辞下第七章；周易正义／系辞下
  source_location: source/zhouyi/raw-wikitext.txt:L3644-L3647; source/zhouyi-zhengyi/raw-wikitext.txt:L6841-L6849, L6863-L6865
  chunk_id: [ck-81f12ddb0aa9, ck-9d6754d54e1b]
  source_quote: |
    “上下无常，剛柔相易，不可為典要，唯變所適。”韩注：“不可立定準也。”孔疏：“既無定準，唯隨應變之時所之適也。”
  failure_mode: |
    忽略爻位、阶段、情境变化和前后条件，只凭固定口诀生成唯一结论。
  mechanism: |
    系辞与注疏把变动、适时本身放在解释中心；静态规则若脱离“何时、何位、何种行动”，会抹掉同一结构在不同阶段的差异。
  warning_signs:
    - 结论中完全没有时间、位置或适用条件
    - 将某句口诀称为“任何卦都永远如此”
    - 不允许本卦、动爻与之卦之间出现张力
  bound_to:
    - 时位中应比结构分析器
    - 本卦—动爻—之卦义理辅助器
    - 经传注疏冲突矩阵
  task_ids: [ZY-T03, ZY-T06, ZY-T07, ZY-T08]
  tags: [static-formula, timing, change, internal-warning]

- id: ce05
  title: 只见失位便断凶，或只见得位便断吉
  type: counter-example
  source_layer: 小象＋王弼注＋孔颖达疏
  source_chapter: 周易正义／未济九二、九四
  source_location: source/zhouyi-zhengyi/raw-wikitext.txt:L5633-L5635, L5645-L5651
  chunk_id: ck-8e66eb5de702
  source_quote: |
    “位雖不正，中以行正也。”又释九四：“履失其位……志行其正，正則貞吉而悔亡。”
  failure_mode: |
    将阴阳是否居“正位”当作自动判决器，不再检查居中、志向、应比和全卦处境。
  mechanism: |
    未济九二、九四都提供“失位而仍可吉”的反例，说明位只是证据之一；其他结构和行动方向可以改变综合判断。
  warning_signs:
    - 结论只有“失位＝凶”或“得位＝吉”
    - 没有列出中、应、时或行动条件
    - 与爻辞明示判词冲突仍坚持位置口诀
  bound_to:
    - 时位中应比结构分析器
    - 规则冲突审计器
    - 本卦—动爻—之卦义理辅助器
  task_ids: [ZY-T02, ZY-T06, ZY-T07]
  tags: [position-determinism, counter-instance, evidence-ledger, internal-warning]

- id: ce06
  title: 同一“闭而不出”行为脱离阶段便被误判
  type: counter-example
  source_layer: 经文＋小象＋王弼注＋孔颖达疏
  source_chapter: 周易正义／节初九、九二
  source_location: source/zhouyi-zhengyi/raw-wikitext.txt:L5275-L5289
  chunk_id: ck-1dabed699d04
  source_quote: |
    初九“不出戶庭，無咎”，因其处立制之初而宜慎密；九二“不出門庭，凶”，注疏解释为“至二宜宣……失時之極”。
  failure_mode: |
    把“谨慎不出”固定判为好或坏，不判断当前究竟是保密准备期，还是应该公开行动的时点。
  mechanism: |
    相似行为在相邻爻位获得相反判断，差别来自阶段任务；正确行为错过时点也会转成失败。
  warning_signs:
    - 只评价行为标签，不评价发生时点
    - 将“谨慎”无限延长为拖延
    - 已具备行动条件仍用原先理由拒绝推进
  bound_to:
    - 时位中应比结构分析器
    - 本卦—动爻—之卦义理辅助器
  task_ids: [ZY-T02, ZY-T06, ZY-T09]
  tags: [wrong-timing, phase-change, delay, internal-warning]

- id: ce07
  title: 只知前进、占有和获益，不知退守与损失
  type: counter-example
  source_layer: 文言传
  source_chapter: 周易／乾上九
  source_location: source/zhouyi/raw-wikitext.txt:L250-L259
  chunk_id: ck-e59b75691cc7
  source_quote: |
    “亢之為言也，知進而不知退，知存而不知亡，知得而不知喪。”
  failure_mode: |
    在已经达到高位或强势阶段后继续加码，把过去的上升趋势当成可以永久延续。
  mechanism: |
    文言把“亢”解释为只接受单向增长而忽略反转可能；位置已至极点，继续推进会扩大回撤与后悔。
  warning_signs:
    - 计划只有扩张，没有退出条件
    - 将当前优势理解成永久优势
    - 不讨论失去、回撤或角色转换
  bound_to:
    - 本卦—动爻—之卦义理辅助器
    - 时位中应比结构分析器
    - 现实核验清单
  task_ids: [ZY-T02, ZY-T06, ZY-T09]
  tags: [overreach, escalation, reversal-risk, internal-warning]

- id: ce08
  title: 在缺少向导和环境知识时追逐目标
  type: counter-example
  source_layer: 经文＋小象
  source_chapter: 周易／屯六三
  source_location: source/zhouyi/raw-wikitext.txt:L323-L338
  chunk_id: ck-e59b75691cc7
  source_quote: |
    “即鹿无虞，惟入于林中，君子幾不如舍，往吝。”小象：“君子舍之，往吝窮也。”
  failure_mode: |
    在信息不足、没有熟悉路径的人协助时，因目标诱人而继续深入不确定环境。
  mechanism: |
    经传把“无虞而逐鹿”设为缺少导航仍追逐的反例；越投入越难退出，最终陷入困穷。
  warning_signs:
    - 目标清楚但路径、规则和风险不清楚
    - 没有领域知识或可靠向导
    - 已发现信息缺口仍以沉没成本为由继续
  bound_to:
    - 现实证据核验器
    - 本卦—动爻—之卦义理辅助器
  task_ids: [ZY-T02, ZY-T06, ZY-T09]
  tags: [no-guide, information-gap, sunk-cost, internal-warning]

- id: ce09
  title: 把争讼坚持到底
  type: counter-example
  source_layer: 彖传＋小象＋王弼注
  source_chapter: 周易／讼；周易正义／讼
  source_location: source/zhouyi/raw-wikitext.txt:L420-L437; source/zhouyi-zhengyi/raw-wikitext.txt:L723-L725
  chunk_id: [ck-a876867b04e3, ck-a37130aa2322]
  source_quote: |
    “終凶，訟不可成也。”小象又说：“訟不可長也。”王注指出，即使自认不枉，“訟至終竟，此亦凶矣”。
  failure_mode: |
    将诉争、争论或关系冲突本身当成必须赢到底的目标，不再评估停止、调解或改变方案。
  mechanism: |
    文本区分中途获得澄清与把争端拖到终局：持续对抗会放大险健相激的结构，使程序胜负吞没原始目标。
  warning_signs:
    - 成功标准变成“绝不先停”
    - 每次反驳都会制造新的争点
    - 继续争执的成本已超过最初利益
  bound_to:
    - 本卦—动爻—之卦义理辅助器
    - 现实核验与行动选项
  task_ids: [ZY-T02, ZY-T06, ZY-T09]
  tags: [conflict-escalation, litigation, stop-rule, internal-warning]

- id: ce10
  title: 小问题没有早辨，逐渐积成大患
  type: counter-example
  source_layer: 文言传
  source_chapter: 周易／坤初六
  source_location: source/zhouyi/raw-wikitext.txt:L301-L303
  chunk_id: ck-e59b75691cc7
  source_quote: |
    “非一朝一夕之故，其所由來者漸矣。由辨之不早辨也。”
  failure_mode: |
    把反复出现的小信号视作偶然，直到风险积累成难以逆转的状态。
  mechanism: |
    文言用“履霜—坚冰”的渐变链解释后果并非突然发生；早期辨识失败会让每次微小累积改变下一阶段的可选空间。
  warning_signs:
    - 同类小问题持续出现却没有记录趋势
    - 每次都说“这次不严重”
    - 只有灾害形成后才回看早期信号
  bound_to:
    - 风险信号清单
    - 本卦—动爻—之卦义理辅助器
  task_ids: [ZY-T02, ZY-T06, ZY-T09]
  tags: [gradual-escalation, early-warning, path-dependence, internal-warning]

- id: ce11
  title: 把节制推到刻薄和不可承受
  type: counter-example
  source_layer: 经文＋彖传＋王弼注＋孔颖达疏
  source_chapter: 周易／节；周易正义／节
  source_location: source/zhouyi/raw-wikitext.txt:L2149-L2164; source/zhouyi-zhengyi/raw-wikitext.txt:L5251-L5269
  chunk_id: [ck-23a4b3c28e89, ck-b9dd0f6d10cd]
  source_quote: |
    “苦節不可貞，其道窮也。”孔疏：“節須得中，為節過苦，傷於刻薄，物所不堪。”
  failure_mode: |
    将自律、制度或边界无限加码，直到自己和相关人员无法承受，仍把“更严”当作“更正确”。
  mechanism: |
    节卦没有把限制本身绝对化，而以能否得中、不伤财、不害民检验；过度节制会破坏制度原本要保护的对象。
  warning_signs:
    - 规则只有不断收紧，没有复核机制
    - 执行成本超过规则带来的收益
    - 用受苦程度证明道德正确
  bound_to:
    - 现实行动核验器
    - 时位中应比结构分析器
  task_ids: [ZY-T02, ZY-T06, ZY-T09]
  tags: [over-restraint, rigidity, proportionality, internal-warning]

- id: ce12
  title: 已经成功便停止维护和预防
  type: counter-example
  source_layer: 经文＋彖传＋大象＋王弼注＋孔颖达疏
  source_chapter: 周易／既济；周易正义／既济
  source_location: source/zhouyi/raw-wikitext.txt:L2245-L2264; source/zhouyi-zhengyi/raw-wikitext.txt:L5513-L5531
  chunk_id: [ck-b3594fe9c2b7, ck-e1d5555c3013]
  source_quote: |
    “初吉終亂。”彖传：“終止則亂。”孔疏：“人皆不能居安思危，慎終如始……若不進德脩業至於終極，則危亂及之。”
  failure_mode: |
    把阶段性完成误当成永久稳定，撤掉监测、维护和风险预案。
  mechanism: |
    既济的反例不是“成功必败”，而是完成后停止调整导致系统失去应变能力；稳定阶段仍包含向混乱转化的条件。
  warning_signs:
    - 达成目标后不再追踪关键指标
    - 没有维护、复发或退出预案
    - 用过去成功否定新风险信号
  bound_to:
    - 本卦—动爻—之卦义理辅助器
    - 现实复盘与风险核验器
  task_ids: [ZY-T02, ZY-T06, ZY-T09]
  tags: [complacency, maintenance, success-trap, internal-warning]

```

## B. 现代外部边界（不是古籍原话）

```yaml
- id: eb01
  title: 解释得通不等于预测已经得到科学验证
  type: external-boundary
  source_layer: 现代项目方法边界（非古籍原文）
  source_chapter: BOOK_OVERVIEW／未被证明的假设
  source_location: BOOK_OVERVIEW.md:L119-L125
  chunk_id: null
  source_quote: null
  failure_mode: |
    将卦后叙事与现实经历能够对应，直接当作超常预测能力的实验证据。
  mechanism: |
    六十四卦、多层注疏和灵活类比提供很大的解释空间；若不预先固定问题、算法、文本层和判定标准，事后拟合无法区分预测能力与选择性解释。
  warning_signs:
    - 只记录“准”的部分
    - 在结果发生后才改变判定标准
    - 用单个故事宣称方法普遍有效
  bound_to:
    - 所有预测性输出
    - 占例前瞻登记
    - 高风险停机与现实核验器
  task_ids: [ZY-T08, ZY-T09]
  tags: [external-boundary, scientific-validity, post-hoc-fit]

- id: eb02
  title: 不得用卦象替代医疗、法律、财务或安全判断
  type: external-boundary
  source_layer: 现代安全规范（非古籍原文）
  source_chapter: BOOK_OVERVIEW／现代应用边界
  source_location: BOOK_OVERVIEW.md:L131-L135
  chunk_id: null
  source_quote: null
  failure_mode: |
    依据卦象停药、诊断疾病、决定借贷投资、指控犯罪、处理人身安全或生育事项。
  mechanism: |
    这些决策需要可核验事实、专业资质和风险控制；象征解释既不能测量病理、法律责任或资产风险，也无法承担错误决定的现实后果。
  warning_signs:
    - 用户准备仅凭卦象执行不可逆行动
    - 请求替代医生、律师或持牌财务人员
    - 涉及自伤、暴力、急症、诈骗或重大财产风险
  bound_to:
    - 高风险停机与现实核验器
    - 六爻桥接器
    - 本卦—动爻—之卦义理辅助器
  task_ids: [ZY-T08, ZY-T09]
  tags: [external-boundary, high-stakes, professional-referral]

- id: eb03
  title: 不得把古代尊卑和受害者归责当作现代伦理
  type: external-boundary
  source_layer: 现代伦理边界；所针对材料属于系辞传、王韩注与孔疏的时代解释
  source_chapter: BOOK_OVERVIEW／时代局限；周易正义／系辞上“负且乘”疏
  source_location: BOOK_OVERVIEW.md:L106-L110; source/zhouyi-zhengyi/raw-wikitext.txt:L6081-L6089
  chunk_id: ck-180e99eafc44
  source_quote: |
    古注疏以君臣、尊卑解释位置，并在该段写有“慢藏誨盜，冶容誨淫”。本边界不接受这些话作为现代责任归属标准。
  failure_mode: |
    用阴阳、夫妇、尊卑或“冶容诲淫”等古代说法合理化控制、性别不平等，或把侵害责任转嫁给受害者。
  mechanism: |
    注疏反映前现代等级和性别秩序；将其从解释史直接转成现代规范，会掩盖同意、权利与行为人责任。
  warning_signs:
    - 以卦象要求一方天然服从
    - 根据衣着、性别或身份归责受害者
    - 用“天道／阴阳”回避现实中的同意与权利
  bound_to:
    - 感情与家庭问题输出
    - 八卦取象限制器
    - 来源分层与归属审计器
  task_ids: [ZY-T04, ZY-T07, ZY-T09]
  tags: [external-boundary, hierarchy, gender, victim-blaming]

- id: eb04
  title: 不把“七日、十年、三年”等直接换算成确定日期
  type: external-boundary
  source_layer: 现代解释纪律（非古籍原文）
  source_chapter: BOOK_OVERVIEW／核心命题与现代应用边界
  source_location: BOOK_OVERVIEW.md:L87-L88, L131-L135
  chunk_id: null
  source_quote: null
  failure_mode: |
    见到爻辞中的数字便承诺某天、某月或某年必然发生特定事件。
  mechanism: |
    数字在各卦注疏中可能承担周期、久暂、完成难度或历史叙事等不同功能；没有独立的应期规则和现实证据，无法唯一映射现代日历。
  warning_signs:
    - 未说明采用何种应期体系
    - 将古文数字直接替换为现代日期
    - 使用“必定、保证、精确到某日”等承诺语
  bound_to:
    - 所有时间预测
    - 六爻桥接器
    - 来源分层与归属审计器
  task_ids: [ZY-T03, ZY-T07, ZY-T08, ZY-T09]
  tags: [external-boundary, timing, false-precision]
```

## 覆盖与缺口

- 已覆盖：重复筮问、象征字面化、单爻机械推广、静态口诀、位置决定论、失时、过犹不及、缺少向导仍冒进、风险渐积、冲突升级与成功后懈怠。
- 已将现代科学效力、高风险专业判断、性别／等级伦理与精确日期承诺单列为外部边界；这些内容不得写成“《周易》证明”。
- 尚缺：当前材料只有《周易》经传和王韩注、孔疏，不能代表帛书、楚简、郑玄、虞翻等全部易学传统；相关异说需以后续可靠校勘本补充。
- 版本风险：中文维基文库《周易》标为 50% 校对，《小象》聚合页有转录错误，《周易正义》有重复“随”页；本文件优先采用单卦页和《正义》相互核对，但正式发布仍应做版本审计。
- 未覆盖的现代实证问题：本阶段未进行占筮预测效力的系统综述或实验评估，不能据本文件作有效性结论。

## 自检

- [x] 每条有 `failure_mode` 与可迁移的 `mechanism`
- [x] 每条列出可观察的 `warning_signs`
- [x] 每条绑定下游能力和 `task_ids`
- [x] 古籍警告与现代外部边界分区
- [x] 古籍引文已回原始归档核对行号与 `chunk_id`
- [x] 未把后世纳甲规则倒写成《周易》原文
