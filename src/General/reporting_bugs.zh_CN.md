---
title: 报告问题
---

# 报告问题

## 在哪里报告问题？

Bazzite 的 [**GitHub Issues**](https://github.com/ublue-os/bazzite/issues)。我们不建议在 Discourse 讨论区中报告问题，因为论坛上的其他内容可能会让真正问题相关的帖子难以追踪，并且 Bazzite 的贡献者也更倾向于在 GitHub 上同时进行代码维护和问题追踪。

如果你不确定碰到的是不是 Bazzite 的问题，也可以考虑 [Bazzite 的 Discord 服务器](/community/#discord-no-discord-account) 中的 #bazzite-help 频道。

>请尽量使用英文报告问题，但如果你使用 AI/LLM 进行翻译，则请同时提供原始语言的报告，以防翻译过程中信息丢失或产生歧义。
    
>或者，在报告标题中标注`[Needs Translation]`（需要翻译），这样社区成员也许能提供翻译相关的帮助。

## Bazzite 报告问题模板

![Bug report|690x174](../img/Bug_report.png)

![Template|690x436](../img/Bug_report_template.png)

## 尝试更新 Bazzite

有些情况下，Bazzite 的版本更新可能已经修复了你碰到的问题，但更新需要重启系统才能应用。因此，我们建议在报告问题前先检查并应用更新，之后再次尝试问题是否仍然存在。

>**请按照你的设备，参考对应部分**：
>[**Bazzite 更新指南**](../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/updating_guide.md)

## 提供设备信息

在终端内输入：

```
ujust device-info
```

报告问题时请附带输出中提供的链接。

## 系统崩溃了？

```command
ujust logs-last-boot
```
在报告问题时附带以上命令的输出。
