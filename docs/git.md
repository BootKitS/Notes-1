## Commit Message 格式
目前规范使用较多的是 [Angular 团队的规范](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines), 它的 message 格式如下:
```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

标题行: 必填, 描述主要修改类型和内容
主题内容: 描述为什么修改, 做了什么样的修改, 以及开发的思路等等
页脚注释: 放 Breaking Changes 或 Closed Issues

分别由如下部分构成:

- type: commit 的类型
    - feat: 新特性
    - fix: 修改问题
    - refactor: 代码重构
    - docs: 文档修改
    - style: 代码格式修改, 注意不是 css 修改
    - test: 测试用例修改
    - chore: 其他修改, 比如构建流程, 依赖管理
- scope: commit 影响的范围, 比如: view, model, utils, build...
- subject: commit 的概述, 建议符合  [50/72 formatting](https://stackoverflow.com/questions/2290016/git-commit-messages-50-72-formatting)
- body: commit 具体修改内容, 可以分为多行, 建议符合 [50/72 formatting](https://stackoverflow.com/questions/2290016/git-commit-messages-50-72-formatting)
- footer: 一些备注, 通常是 BREAKING CHANGE 或修复的 bug 的链接


## Git 分支规范

### 分支构成

- master 主分支
- dev 开发分支

### 分支操作
    
- 新增功能，或者修复bug时，从以上分支或者其他主要分支拉取并新建分支格式为：
    - `<username>/<fix | feat>_<something>`
    - 例如：`tuo/feat_vcode` (新增验证码功能)
- 每次合并代码之前使用 `git rebase <a branch>`，此分支为将要合并进去的分支  
    - 详细操作请看 [官方文档](https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%8F%98%E5%9F%BA)
    - 如有冲突请仔细检查并解决冲突
    - 此操作可保持提交记录整洁


## Git 命令

[官方文档](https://git-scm.com/book/zh/v2/)

- `git commit --amend` 修改最近一次提交记录，包括commit message 、提交的内容(需将已修改的文件加入暂存区)
- `git stash` 保存工作区，增加参数 `pop` 可恢复
- `git rebase -i <CommitHash>` 修改历史提交记录，根据提示具体操作
- `git branch -d <BranchName>` 删除本地分支
- `git branch --remotes -d origin/<BranchName>` 已删除远程跟踪分支
- `git push origin --delete <BranchName>`  或 `git push origin  :<BranchName>` 删除远程分支
- `git remote prune origin` 从本地版本库中去除远程已经删除的分支

## 学习 Git 命令 [Learn Git](https://learngitbranching.js.org/)
