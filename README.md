# Personal Wisdom Skills

个人可调用知识与传统文化 Skills 仓库。第一阶段构建一个以《增删卜易》为来源、能够自动触发的六爻占问 Skill。

## Repository layout

- `books/` — Cangjie source audits and capability bundles
- `skills/` — installable Agent Skills
- `tests/` — repository-level tests
- `docs/` — designs, plans, and learning notes

## Safety

Do not commit personal birth data, private questions, API keys, paid ebooks, or chat exports. Traditional divination is presented as cultural interpretation and reflection, not scientific prediction.

## Install / 安装

当前本机安装路径：

```text
D:\Codex\skills\traditional-divination-skill
```

从仓库更新本机安装副本前，应先运行测试和 Skill 校验，且不要静默覆盖安装目录中的个人修改。

## Use / 使用

安装后通常不需要记命令，直接在新任务中说：

> 帮我用六爻看看未来三个月的感情发展，我不懂怎么起卦，请一步一步问我。

也可显式输入 `$traditional-divination-skill`。当前版本可靠计算三钱六爻的本卦、动爻和变卦；《增删卜易》方法仍按 Cangjie 流程进行来源审计，未通过前不会声称完整实现纳甲断法。
