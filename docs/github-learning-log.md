# GitHub 学习记录 / GitHub Learning Log

这个仓库采用“小步提交”的方式保存可回看历史。Git 是本地版本控制工具，GitHub 是保存与协作远程仓库的平台。

## 本次实际流程

```powershell
git clone https://github.com/Lin712-311/personal-wisdom-skills-lbw.git C:\Users\19364\Documents\Codex\personal-wisdom-skills-lbw
git status --short
git add README.md .gitignore docs
git commit -m "chore: initialize personal wisdom skills repository"
git branch -M main
git push -u origin main
git switch -c feature/traditional-divination-v1
git push -u origin feature/traditional-divination-v1
```

## 常用概念（中英文）

| 命令/概念 | 中文理解 | English meaning |
|---|---|---|
| `clone` | 把远程仓库完整复制到本机 | Copy a remote repository to your computer |
| `status` | 查看哪些文件新增、修改或已暂存 | Show changed, untracked, and staged files |
| `add` | 把指定改动放进下一次提交的暂存区 | Stage selected changes for the next commit |
| `commit` | 在本地创建一个带说明的版本快照 | Create a named local snapshot |
| `branch` | 建立一条独立开发线，避免直接改稳定版本 | Create an independent line of development |
| `merge` | 把一条分支的提交合入另一条分支 | Combine one branch into another |
| `push` | 把本地提交上传到 GitHub | Upload local commits to the remote |
| `pull` | 获取远程提交并合入当前分支 | Fetch and integrate remote commits |
| `origin` | 本地为主要远程仓库保存的默认别名 | Conventional name for the primary remote |

## 为什么先用功能分支

`main` 保存相对稳定的版本；`feature/traditional-divination-v1` 用来开发和测试。功能分支通过测试后再合并，这样 GitHub 上能清楚看到每一步，也能在错误时定位到具体提交。

## 安全习惯

- 提交前先看 `git status --short` 和 `git diff --cached`。
- 不提交 API key、`.env`、私人聊天、出生资料或问卦记录。
- 提交说明写清“做了什么”，例如 `feat:`（功能）、`fix:`（修复）、`docs:`（文档）、`test:`（测试）。
- `git push` 前先运行项目测试；远程有他人更新时先 `git pull` 并处理冲突。
