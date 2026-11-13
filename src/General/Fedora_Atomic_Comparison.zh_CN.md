---
title: Bazzite 和 Fedora Atomic
---

# Bazzite 和 Fedora Atomic

## Bazzite 是什么？

Bazzite 是一款基于 [**Fedora Atomic**](https://fedoraproject.org/atomic-desktops/) 桌面镜像序列下 [**Fedora Kinoite（KDE Plasma）**](https://fedoraproject.org/atomic-desktops/kinoite/)和 [**Fedora Silverblue（GNOME）**](https://fedoraproject.org/atomic-desktops/silverblue/)的自制镜像，提供了许多面向游戏玩家的用户体验的优化。

## 主要不同点

以下列出了一些 Bazzite 和 Fedora Atomic 上游相比额外增加的优化：

### 安装后所需配置更少

- 自带更多硬件设备的支持；
- 自带功能更全面的媒体编解码器，方便实现视频加速等相关需求；
- 预装 Steam 和 Lutris 等游戏相关实用工具；
- Fedora Flatpak 源默认替换为 [**Flathub**](https://flathub.org/)，提供的程序更多。

### 更易于使用

- [Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal/) 提供常用工具的快捷访问操作，[**`ujust`**](/Installing_and_Managing_Software/ujust/)提供更多常用脚本；
- [**掌机版镜像**](/Handheld_and_HTPC_edition/Steam_Gaming_Mode/)预配置且开机自动启动 Steam 游戏模式，方便掌机和控制器优先的使用场景。

### 开发者优化

- 预装了 Homebrew 用于用户级的命令行程序管理；
- Distrobox 提供其他发行版的容器环境，方便安装分发方式受限的软件或开发组件；
- [**Bazzite-DX**](https://dev.bazzite.gg/) 作为开发者特化的镜像版本。

### 其他优化

- 通过 [**Waydroid**](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md) 提供 Android 程序的支持；
- Firefox 自带 Flatpak 版而非随系统安装；
  - 如有需要可以直接卸载；
  - 不再绑定系统版本，因此可以更方便地进行更新。
- 自动挂载 Btrfs 和 Ext4 文件系统的外接存储设备；
- 自带一些 GNOME 扩展和 KDE Plasma 主题，方便个性化；
- 快捷回滚到 90 天内的任意 Bazzite 版本。
