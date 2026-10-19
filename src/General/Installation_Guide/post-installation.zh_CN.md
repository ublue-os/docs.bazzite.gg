---
title: 安装完成后
---

# 安装完成后

## 初始设置

![GRUB 菜单，显示两次部署和 UEFI 固件菜单的选项](../../img/GRUB_Menu.png)

第一次启动 Bazzite 时 GRUB 菜单默认自动显示，应包括两次部署的对应选项。之后如果碰到问题，可以使用这一菜单回滚到上一个系统部署。

[**更新、回滚和镜像切换指南**](../../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md)提供了更多相关信息。

## Steam 游戏模式初始设置（仅限掌机版）

![Steam 游戏模式初始设置|1920x1080, 50%](../../img/deck-edition.png)

掌机版镜像开机默认启动到 Steam 游戏模式。第一次启动时，会要求进行 Steam 的相关配置。

[**掌机版的文档**](../../Handheld_and_HTPC_edition/index.md)提供了更多相关信息。

## 配置系统设置

有许多个性化设置内容都建议在第一次启动时就配置好，比如分辨率或 UI 倍率等影响显示的内容。启动你的桌面环境对应的设置程序以进行配置。

### 倍率设置

![显示器配置（KDE Plasma）|690x370, 75%](../../img/KDE_Display_Settings.png)
**_KDE Plasma 的系统设置程序_**

![显示器（GNOME）|690x344, 75%](../../img/GNOME_Display_Settings.png)
**_GNOME 的设置程序_**

按需调整系统设置。

### 修改默认密码
<sub>（如果使用旧版安装器且安装时没有设置密码）</sub>

![KDE Plasma 的密码管理界面|584x500, 75%](../../img/change-pass.png)

在桌面模式下，选择**系统设置 → 用户 → 修改密码**。

## 双启动相关的安装后配置

!!! note

    该部分仅适用于 Bazzite 和 Windows 双启动的用户。

使用以下命令刷新 GRUB 配置，以在菜单中同时显示 Bazzite 和 Windows 的启动选项：

```
ujust regenerate-grub
```

### 将 Bazzite 配置为默认启动项

如果`Windows Boot Manager`为默认启动项，那么开机时不会进入 GRUB 菜单，这可能会导致无法启动 Bazzite。因此我们建议在系统 BIOS 配置中将 Bazzite 设置为默认启动项。

如果 Bazzite 能够正常启动但 GRUB 菜单没有出现，尝试在开机时按<kbd>↓</kbd>直到菜单出现。

### 从 Steam 菜单快捷重启到 Windows

以下`ujust`命令会在 Steam 中添加一个非 Steam “游戏”，运行即可自动重启到 Windows。

```
ujust setup-boot-windows-steam
```

### 双启动配置下调整存储空间

!!! note

    该部分一般是在双启动运行一段时间之后才需要考虑的问题。

**请参考以下视频指南**:

https://www.youtube.com/watch?v=uy8mi1pAj8E

<hr>

## 接下来该做什么？

### 用 Bazzite Portal 进行一些常用配置

![Bazzite Portal 截图|1364x1074, 50%](../../img/Bazzite_Portal.png)

Bazzite Portal 提供了许多系统维护、一些常用程序的安装和一些高级系统设置的简单配置。

### 使用 Bazaar 应用商店安装其他程序

![Bazaar 应用商店的截图|1649x1274, 50%](../../img/Bazaar.png)

Bazaar 应用商店一般会是绝大多数软件安装的来源，但如果有无法通过 Flatpak 安装的程序，则应参考[**安装和管理程序**](../../Installing_and_Managing_Software/index.md)的文档。

<hr>

## Bazzite，启动！

**至此 Bazzite 就装好了！**

对于游戏部分，我们有专门的[**文档**](../../Gaming/index.md)，涵盖了：

- 配置 **Steam** 和 **Proton** 以支持 Windows 游戏
- 配置 **Lutris** 和其他游戏启动器（Epic Games、GOG、Amazon Games 等）
- 游戏和模组管理
- 常见游戏问题的处理

那么，玩的开心！如果碰到问题也请[**报告**](../../General/reporting_bugs.md)，这样才能尽快修复。
