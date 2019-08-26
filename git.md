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
