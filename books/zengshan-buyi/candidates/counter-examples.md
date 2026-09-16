# 《增刪卜易》反例／失败模式候选（Stage 1）

> 本文件只收集候选，不在本阶段筛选、验证术数有效性或编译 skill。`failure_mode` 与 `mechanism` 对书内条目只重建文本内部的批评逻辑，不代表现代科学认可。
> 检索词为 `不可 / 不驗 / 謬 / 誤 / 妄 / 拘 / 泥 / 非 / 若捨 / 切勿 / 再占 / 混問 / 靈機`，并补查简体异形。`rg` 原文命中数依次为 66 / 29 / 20 / 19 / 13 / 24 / 7 / 184 / 1 / 2 / 40 / 0 / 4；“混問”虽无字面命中，但“一卦多问／二念”有明确同义材料。
> 索引共 13 块，其中卷二至卷四主要合并为超大块 `ck-a271e944b34d`（118,457 字符）；因此所有条目均回到 `source/raw-wikitext.txt` 的相邻行窗口核验。Stage 0 现代批判另列，绝不冒充野鶴、覺子或李我平原话。

## A. 书内明确警告的失败模式

```yaml
- id: ce01
  title: 一卦混入两三件事
  type: counter-example
  source_layer: 古籍主体／增删层（该段未单独署说话人，具体归属待校勘）
  source_chapter: 增刪黃金策千金賦章第三十四
  source_location: source/raw-wikitext.txt:L1467-L1471
  chunk_id: ck-a271e944b34d
  source_quote: |
    “若懷兩三事而占者，念旣不專心，何能一念多心？……愼勿兩念，二念不驗。”
  failure_mode: |
    把财、病、功名等独立目标塞入同一次提问，之后无法确定某一信号究竟回答哪件事。
  mechanism: |
    文本把失败归因于“二念不专”；从可审计角度看，混问同时破坏了用神选择、结果归属和失败判据。
  warning_signs:
    - 提问中同时出现两个以上可独立判断的目标
    - 同一结果可被解释为回答不同事项
    - 事后才决定哪个信号对应哪个问题
  bound_to:
    - 问题合同与分占器
    - 用神映射器
    - 占例前瞻登记
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T07]
  tags: [mixed-question, one-question-one-task, internal-warning]

- id: ce02
  title: 让他人代占造成意念与用神错配
  type: counter-example
  source_layer: 古籍主体／增删层（该段未单独署说话人，具体归属待校勘）
  source_chapter: 增刪黃金策千金賦章第三十四
  source_location: source/raw-wikitext.txt:L1494-L1508
  chunk_id: ck-a271e944b34d
  source_quote: |
    “我有心事，不可叫他人代我去占，我之一念，他又一念，事二念也……命他人而代者，難取用神，必然不驗。”
  failure_mode: |
    代占者、当事人与断卦者关注点不一致，导致主体、对象及用神的解释合同漂移。
  mechanism: |
    原文认为两人的念头会竞争；其可迁移风险是输入主体不清，使同一卦可在“本人之念”和“家人之念”间事后切换。
  warning_signs:
    - 当事人未亲自说明问题
    - 不清楚结果应以谁为“世”、谁为对象
    - 解释在本人利益与代问者利益间来回切换
  bound_to:
    - 问题合同与分占器
    - 代占主体标注
    - 用神映射器
  task_ids: [ZSBY-T01, ZSBY-T03]
  tags: [proxy-question, subject-ambiguity, internal-warning]

- id: ce03
  title: 用一卦兼断全家与所有事项
  type: counter-example
  source_layer: 古籍主体（“野鶴曰”）
  source_chapter: 舊宅章第一百一十三
  source_location: source/raw-wikitext.txt:L4244-L4248
  chunk_id: ck-a271e944b34d
  source_quote: |
    “若以一卦而斷全家之事者予則不能，須指其所疑之事而占之。”
  failure_mode: |
    从一个宅卦同时推断全家六亲、功名、财运、疾病和具体方位，产生大量互相冲突的解释。
  mechanism: |
    有限符号被重复映射到多个人与多项结果，任何异象都可能找到一个事后对应，无法确认命中对象。
  warning_signs:
    - 输出覆盖多人、多领域和多个时间窗口
    - 同一爻被同时解释为房屋、父母和其他人物
    - 出现矛盾时靠换象或换人化解
  bound_to:
    - 问题合同与分占器
    - 领域路由表
    - 规则冲突审计器
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T05, ZSBY-T08]
  tags: [overreach, multi-domain, post-hoc-mapping, internal-warning]

- id: ce04
  title: 舍弃用神而执独发独静或卦名
  type: counter-example
  source_layer: 古籍主体（“野鶴曰”）
  source_chapter: 獨發章第三十一；歸魂遊魂章第又二十六
  source_location: source/raw-wikitext.txt:L757-L760, L6049-L6055
  chunk_id: [ck-a271e944b34d, ck-070ff2cc49aa]
  source_quote: |
    “如捨其用神，執之而決事者，謬也，過也。”
    “須以用神爲主，然後以此參之，若捨用神執此而斷者，謬也。”
  failure_mode: |
    看到独发、独静、游魂或归魂等醒目标记便直接断吉凶或应期，不先检查当前问题的用神。
  mechanism: |
    次级特征被误当作主目标，方向与意义脱离问题语境；同一标记因此可在不同任务中导出相反结论。
  warning_signs:
    - 结论只引用一个卦型或动静特征
    - 没有明确当前问题的用神
    - 不检查旺衰、生克与任务类型
  bound_to:
    - 用神映射器
    - 内部规则证据账本
    - 规则冲突审计器
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T05]
  tags: [single-signal, useful-god, rigid-rule, internal-warning]

- id: ce05
  title: 把旬空或月破机械当成全无作用
  type: counter-example
  source_layer: 古籍主体（“野鶴曰／予”）
  source_chapter: 月破章第二十七；進神退神章第二十九；旬空章第二十六
  source_location: source/raw-wikitext.txt:L247-L271, L579-L581, L5900-L5903
  chunk_id: ck-a271e944b34d
  source_quote: |
    “古法謂之避空，予以爲謬也，此時逢空，出空一定遭傷。”
    “若以月破，百無所用，霄壤之隔也。”
  failure_mode: |
    一见空、破便把爻判为永久无效，或反过来把“空”解释成能避开既有的不利作用。
  mechanism: |
    文本把空破视为随动静、生扶、填实、冲合及时间改变的状态；二元化会遗漏条件与应期分支。
  warning_signs:
    - 使用“空破即永远无用”的绝对句
    - 不记录动静、生扶或填实条件
    - 用“避空”消除已经记录的不利信号
  bound_to:
    - 内部规则证据账本
    - 应期规则计算器
    - 规则冲突审计器
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06]
  tags: [void, month-break, binary-rule, internal-warning]

- id: ce06
  title: 不看旺衰而泛用随鬼入墓
  type: counter-example
  source_layer: 李文輝增删层（“覺子曰”）
  source_chapter: 隨鬼入墓章第三十
  source_location: source/raw-wikitext.txt:L687-L690
  chunk_id: ck-a271e944b34d
  source_quote: |
    “存畱驗，不驗又試，試之不驗，而再試之，一而十，十而百，全不驗者，始盡刪之。”
  failure_mode: |
    只要见世、命、身或用爻“随鬼入墓”便断凶，甚至让墓爻覆盖刑冲克害、空破和旺衰等其余信息。
  mechanism: |
    “入墓”在许多卦中都容易出现；若不要求与休囚无气等条件共同成立，它会成为高频但低区分度的万能凶兆。
  warning_signs:
    - 几乎每卦都能找到一个入墓关系
    - 不记录旺衰或生扶
    - 单一墓象压过全部相反证据
  bound_to:
    - 内部规则证据账本
    - 规则冲突与例外审计器
    - 占例完整登记
  task_ids: [ZSBY-T04, ZSBY-T05]
  tags: [tomb, overgeneralization, base-rate, internal-warning]

- id: ce07
  title: 以六神星煞直接断生死吉凶
  type: counter-example
  source_layer: 古籍主体（正文论述；具体编修层待校勘）
  source_chapter: 六神章第十八；疾病章第九十九
  source_location: source/raw-wikitext.txt:L5568-L5572, L3943-L3947
  chunk_id: [ck-62be6a1f002a, ck-a271e944b34d]
  source_quote: |
    “此皆不以五行，竟以六神而斷生死。”
    “以星煞六神而斷生死……予試多年或生或死，全憑用神，予皆不驗。”
  failure_mode: |
    因青龙、白虎、螣蛇等标签看似吉凶鲜明，便绕过用神和整体条件直接断病人生死。
  mechanism: |
    附和性标签会让既有结论显得更生动，却未提供独立的方向判据；单独使用时容易把象征联想误作证据。
  warning_signs:
    - 结论主要来自颜色、动物或神煞名称
    - 未说明用神状态
    - 在医疗或死亡问题上使用确定性措辞
  bound_to:
    - 规则冲突与例外审计器
    - 领域安全路由
    - 内部规则证据账本
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T08]
  tags: [six-spirits, symbolic-label, mortality, high-risk, internal-warning]

- id: ce08
  title: 把六合六冲或卦名机械化为固定结论
  type: counter-example
  source_layer: 古籍主体（“野鶴曰”）
  source_chapter: 身命章第三十六；六合章第十九；六沖章第二十
  source_location: source/raw-wikitext.txt:L2137-L2140, L5595-L5740
  chunk_id: [ck-a271e944b34d, ck-62be6a1f002a, ck-c34ee8199bab]
  source_quote: |
    “若之以兩卦六沖斷六十年之休咎，而世與財福置之於何地？”
  failure_mode: |
    看到六合就一律断成、六冲就一律断散，或用两个六冲卦概括数十年命运。
  mechanism: |
    卦型被从用神强弱和具体任务中抽离，时间跨度又任意扩大，导致粗粒度标签替代了可核查的条件链。
  warning_signs:
    - “六合必吉／六冲必凶”没有例外条件
    - 用单个卦型覆盖很长时期
    - 不检查官、父、世、财福等任务相关变量
  bound_to:
    - 内部规则证据账本
    - 应期规则计算器
    - 规则冲突与例外审计器
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T06]
  tags: [six-clash, six-combination, horizon-error, internal-warning]

- id: ce09
  title: 把偶然命中升级为通则
  type: counter-example
  source_layer: 古籍主体（“予”叙述）
  source_chapter: 增刪黃金策千金賦章第三十四
  source_location: source/raw-wikitext.txt:L1289-L1292
  chunk_id: ck-a271e944b34d
  source_quote: |
    “大凡爻象有一定不可移者，可以爲法，間有驗者，乃偶然之合耳。”
  failure_mode: |
    某口诀偶尔与结果相合，便把它保留为普遍规则，忽略更大量的不验情形。
  mechanism: |
    只记得命中而不登记总尝试数，会把偶合误认成稳定关系；规则因而无法估计失败率。
  warning_signs:
    - 证据只写“间有验者”
    - 缺少连续样本与不验记录
    - 从单例直接推出固定口诀
  bound_to:
    - 规则冲突与例外审计器
    - 占例结构化与前瞻检验模板
    - 证据等级标注
  task_ids: [ZSBY-T05]
  tags: [coincidence, cherry-picking, rule-induction, internal-warning]

- id: ce10
  title: 结果已清楚仍反复占到想要的答案
  type: counter-example
  source_layer: 古籍主体（序中“野鶴曰”）
  source_chapter: 序
  source_location: source/raw-wikitext.txt:L4560-L4565, L4715-L4718
  chunk_id: [ck-fa4fe72c8018, ck-6d7be6643114]
  source_quote: |
    “不必厭其子孫持世，務求其官鬼持世而後已，此非理也……得其一者則止，不必再占。”
  failure_mode: |
    因首个结果不合期待而继续重占，直到出现偏好的信号，再选择性采纳该次结果。
  mechanism: |
    重复抽取增加获得任意想要模式的机会；没有预定停止规则时，可把不满意结果丢弃而制造确认偏误。
  warning_signs:
    - 重占理由是“不喜欢首个结果”
    - 没有事先规定最大次数
    - 多次结果中只保留最合意的一卦
  bound_to:
    - 复核决策日志
    - 占例前瞻登记
    - 停止规则
  task_ids: [ZSBY-T07, ZSBY-T05]
  tags: [repeat-until-desired, confirmation-bias, stopping-rule, internal-warning]

- id: ce11
  title: 卦意含混时仓促下断
  type: counter-example
  source_layer: 古籍主体（各门类应期总注）
  source_chapter: 各門類應期總注章第又二十六
  source_location: source/raw-wikitext.txt:L6030-L6034
  chunk_id: ck-070ff2cc49aa
  source_quote: |
    “倘遇卦之不明，再占是一法。卦有恍惚者，再占一卦，不可妄斷。”
  failure_mode: |
    当证据冲突、用神不明或卦意恍惚时，仍输出单一确定结论。
  mechanism: |
    不确定性被隐藏，解释者被迫挑选某一条规则；这扩大任意性，也让后续无法区分原判与补判。
  warning_signs:
    - 多条规则方向相反却无冲突记录
    - 没有“不明／待核查”状态
    - 结论确定但推导链缺失
  bound_to:
    - 内部规则证据账本
    - 复核决策日志
    - 规则冲突与例外审计器
  task_ids: [ZSBY-T04, ZSBY-T05, ZSBY-T07]
  tags: [ambiguity, rash-judgment, uncertainty, internal-warning]

- id: ce12
  title: 把“见贵”信号误换成“得官”结论
  type: counter-example
  source_layer: 李文輝增删层（“覺子曰”）
  source_chapter: 謁貴求財章第六十九
  source_location: source/raw-wikitext.txt:L3440-L3444
  chunk_id: ck-a271e944b34d
  source_quote: |
    “切勿以此得見貴人之官星換作成名而斷也。”
  failure_mode: |
    因“谒贵”和“求名”都出现官星，便把成功见到贵人的信号直接解释为获得官职。
  mechanism: |
    相同符号在不同任务合同中承担不同输出；跨任务复用会发生标签泄漏，把过程节点误作最终成果。
  warning_signs:
    - 提问目标与输出目标不一致
    - 只因共享同一“官星”便合并两类任务
    - 缺少领域路由和完成标准
  bound_to:
    - 问题合同与分占器
    - 用神映射器
    - 领域路由表
  task_ids: [ZSBY-T01, ZSBY-T03, ZSBY-T08]
  tags: [task-confusion, label-leakage, intent-routing, internal-warning]

- id: ce13
  title: 由爻的五行直接指定针灸或寒热药
  type: counter-example
  source_layer: 李文輝增删层与李我平评议层
  source_chapter: 醫卜往治章第一百零四
  source_location: source/raw-wikitext.txt:L4113-L4115, L4151-L4153
  chunk_id: ck-a271e944b34d
  source_quote: |
    “切不可又以金臨子孫而用鍼，火屬子孫而用炙，錯也誤也。”
    “此書一出，寒熱之藥不可輕用。”
  failure_mode: |
    从金、火、水等象征映射直接选择针、灸或大寒大热药物，并把卦象当成处方依据。
  mechanism: |
    象征类别不能提供剂量、诊断、禁忌证或药物相互作用；机械映射会越过真实病情与专业评估。
  warning_signs:
    - 药物或治疗只由某爻五行决定
    - 未有医学诊断、剂量与禁忌证
    - 用卦象替代医生或紧急处置
  bound_to:
    - 领域安全路由
    - 医疗内容降级为历史参考
    - 高风险拒答边界
  task_ids: [ZSBY-T08]
  tags: [medical-harm, symbolic-prescription, professional-boundary, internal-warning]

- id: ce14
  title: 用固定爻位年数精确推断寿命
  type: counter-example
  source_layer: 古籍主体（“予”叙述）
  source_chapter: 壽元章第三十九
  source_location: source/raw-wikitext.txt:L2356-L2359
  chunk_id: ck-a271e944b34d
  source_quote: |
    “初爻管五年，二爻管五年，共作三十年……予試四十餘載，並無應驗，不以爲法……欺人之法，予不爲之。”
  failure_mode: |
    以每爻固定管五年等口径，给出精确寿数或死亡时间。
  mechanism: |
    固定换算缺少可重复依据，却会产生虚假的精确感；在生死问题上还可能诱发恐惧和错误行动。
  warning_signs:
    - 用固定算式给出寿命数字
    - 没有误差范围或失败定义
    - 把高风险结论表述为确定事实
  bound_to:
    - 应期规则计算器的禁用边界
    - 领域安全路由
    - 占例前瞻检验模板
  task_ids: [ZSBY-T05, ZSBY-T06, ZSBY-T08]
  tags: [false-precision, lifespan, mortality, internal-warning]
```

## B. 现代录入层与 Stage 0 现代批判候选

> 以下均不是古籍作者原话。`ce15` 是现代录入者对当前数字文本的自述；`ce16`–`ce19` 来自 `BOOK_OVERVIEW.md` 的 Stage 0 批判，用于后续 Boundary，不得反向归因给野鶴、覺子或李我平。

```yaml
- id: ce15
  title: 未校勘录入与现代增补被误当古籍正文
  type: counter-example
  source_layer: 现代录入／整理层（不是古籍作者原话）
  source_chapter: 錄入者言；原劍增訂說明
  source_location: source/raw-wikitext.txt:L14-L24, L4602-L4692
  chunk_id: [ck-a625cafe988b, ck-fa4fe72c8018, ck-6d7be6643114]
  source_quote: |
    “時間倉促，並未仔細校對，錯漏應該不少。”
    “於篇首增……及吾揣摩出的規律……”
  failure_mode: |
    把现代录入、整理者公式或疑似补写内容无标记地归为野鶴或李文輝原文。
  mechanism: |
    拼接镜像把不同时代和角色置于同一文件；若丢失说话人和版本标签，后续候选会发生来源污染。
  warning_signs:
    - 引文位于“錄入者言／原劍按／增訂說明”却标为古籍正文
    - 当前镜像错漏、异体与重复未核对
    - 现代公式没有来源层字段
  bound_to:
    - 来源分层与文本归属审计
    - 装卦工作表的版本标注
    - 全部候选的证据追踪
  task_ids: [ZSBY-T02, ZSBY-T09]
  tags: [modern-entry, provenance, textual-corruption, versioning]

- id: ce16
  title: 精选命中案例而缺少完整失败样本
  type: modern-critical-counterexample
  source_layer: Stage 0 现代批判（不是作者原话）
  source_chapter: BOOK_OVERVIEW.md · 作者与增删者的立场盲点／未被证明的假设
  source_location: BOOK_OVERVIEW.md:L115-L129
  chunk_id: null
  source_quote: |
    “占例多由断卦者叙述，缺少完整样本、失败记录和独立核验。”
  failure_mode: |
    只结构化“果然”“应验”的故事，遗漏连续试验中的不验、模糊结果和失访样本，再据此声称规则可靠。
  mechanism: |
    选择性报告和回忆偏差会系统性抬高表面命中率；没有分母、基准率与独立核验就无法评估增益。
  warning_signs:
    - 数据集几乎全是命中案例
    - 不知道总占次数和失败数
    - 结果由原断卦者回忆且无外部记录
  bound_to:
    - 占例结构化与前瞻检验模板
    - 规则冲突与例外审计器
    - 证据等级标注
  task_ids: [ZSBY-T05, ZSBY-T07]
  tags: [stage0-critique, selection-bias, missing-denominator, non-author]

- id: ce17
  title: 灵机变通与复占造成不可证伪解释
  type: modern-critical-counterexample
  source_layer: Stage 0 现代批判（不是作者原话）
  source_chapter: BOOK_OVERVIEW.md · 最强反对意见
  source_location: BOOK_OVERVIEW.md:L117-L133
  chunk_id: null
  source_quote: |
    “‘靈機變通’與‘占此應彼’給了事後改釋極大空間。”
  failure_mode: |
    结果不符时改换用神、事项、时间窗口或采用另一卦；结果相符时则保留原解释，体系因此很难失败。
  mechanism: |
    多重解释路径和复占机会提高事后命中概率；未预注册取用、结论、截止时间和停止规则时，无法证伪。
  warning_signs:
    - 结果发生后才确定应在哪个时间尺度
    - “占此应彼”用于吸收原问题的失败
    - 多卦合断却未预先规定采用规则
  bound_to:
    - 复核决策日志
    - 应期规则计算器
    - 占例前瞻登记
    - 规则冲突与例外审计器
  task_ids: [ZSBY-T03, ZSBY-T04, ZSBY-T05, ZSBY-T06, ZSBY-T07]
  tags: [stage0-critique, unfalsifiability, researcher-degrees-of-freedom, non-author]

- id: ce18
  title: 以卦象替代医疗法律财务等专业判断
  type: modern-critical-counterexample
  source_layer: Stage 0 现代批判（不是作者原话）
  source_chapter: BOOK_OVERVIEW.md · 可保留的方法论价值与边界
  source_location: BOOK_OVERVIEW.md:L135-L139, L158-L165
  chunk_id: null
  source_quote: |
    “医疗、法律、财务、犯罪风险、生育、死亡等高风险决策不得以卦象作为诊断、建议或行动依据。”
  failure_mode: |
    把传统术数内部推演包装成事实预测，用来诊断疾病、决定用药、处理诉讼、投资或人身安全。
  mechanism: |
    该体系未被前瞻对照研究证明有预测效力；替代专业判断会造成延误、损失或不可逆伤害。
  warning_signs:
    - 用户准备依据卦象停药、拒医、交易或采取法律行动
    - 输出使用“必然／一定”而无证据边界
    - 没有转交合格专业人士或紧急服务
  bound_to:
    - 领域安全路由
    - 所有历史重建型能力
    - 高风险拒答与转交
  task_ids: [ZSBY-T08]
  tags: [stage0-critique, safety, professional-boundary, non-author]

- id: ce19
  title: 由象征类别推断性别阶层或人格优劣
  type: modern-critical-counterexample
  source_layer: Stage 0 现代批判（不是作者原话）
  source_chapter: BOOK_OVERVIEW.md · 时代局限／作者与增删者的立场盲点
  source_location: BOOK_OVERVIEW.md:L108-L120, L158-L164
  chunk_id: null
  source_quote: |
    “依性别、阶层、残障、职业或婚育状况给人作道德与人格定性。”
  failure_mode: |
    把卦象映射为“贤／不贤、贵／贱、聪明／愚痴”等标签，并据此评价现实中的个人或群体。
  mechanism: |
    前现代制度和父权价值被编码进解释表；直接迁移会把历史偏见伪装成客观判断并造成歧视。
  warning_signs:
    - 从性别、职业、残障或婚育状态推出人格
    - 使用“下贱／鄙俗／愚痴”等本质化标签
    - 未说明制度背景与现代伦理边界
  bound_to:
    - 领域安全路由
    - 来源与时代语境审计
    - 人物评价禁用边界
  task_ids: [ZSBY-T08, ZSBY-T09]
  tags: [stage0-critique, discrimination, historical-bias, non-author]
```

## 覆盖备注

- 覆盖 `ZSBY-T01`：`ce01`–`ce03`, `ce12`。
- 覆盖 `ZSBY-T02`：`ce15`（现代增补与版本标注风险）。
- 覆盖 `ZSBY-T03`：`ce01`–`ce04`, `ce12`, `ce17`。
- 覆盖 `ZSBY-T04`：`ce04`–`ce08`, `ce11`, `ce17`。
- 覆盖 `ZSBY-T05`：`ce03`–`ce11`, `ce14`, `ce16`–`ce17`。
- 覆盖 `ZSBY-T06`：`ce05`, `ce08`, `ce14`, `ce17`。
- 覆盖 `ZSBY-T07`：`ce01`, `ce10`–`ce11`, `ce16`–`ce17`。
- 覆盖 `ZSBY-T08`：`ce03`, `ce07`, `ce12`–`ce14`, `ce18`–`ce19`。
- 覆盖 `ZSBY-T09`：`ce15`, `ce19`。
