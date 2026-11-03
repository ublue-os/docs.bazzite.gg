---
title: Bazzite 和 SteamOS
---

# Bazzite 和 SteamOS

## SteamOS 是什么？

**SteamOS** 是 Valve 维护的，最初面向 Steam Deck 的操作系统。SteamOS 通过游戏模式操作 Steam 客户端，并包含简化版的 **KDE Plasma** 桌面环境，允许用户进行一些常见于其他 Linux 系统的操作，但在完全体的桌面环境下可能会显得操作受限。

## Bazzite 是什么？

Bazzite 是一款社区维护的，游戏优先的 Linux 操作系统，自带最新的 Linux 驱动和面向不同需求的变种镜像：**桌面版 (Bazzite)**、**掌机版（Bazzite-Deck）**和 **开发者版（Bazzite-DX）**。Bazzite 基于 [**Fedora Linux**](https://fedoraproject.org/)，并采用[**原子化的更新体系**](https://github.com/bootc-dev/bootc)，保证更新出现问题时总能回滚到上一个确定正常的版本。

除此之外，Bazzite 也更加面向日常使用，同时兼顾**游戏**、**多媒体**和**软件开发**等方面。更频繁的驱动更新也保证 Bazzite 在 Linux 中的设备支持足够靠前，不论是 **AMD**、（较新的）**NVIDIA** 还是 **Intel** 显卡。Bazzite 还支持 **Lenovo**、**ASUS**、**Ayn**、**GPD** 和 **OneXPlayer** 等品牌的掌机设备。

### 和 SteamOS 相比，Bazzite 提供的优化点

-   支持和 **Windows** 系统共存的**双启动**环境；
-   兼容**更多的** x86 掌机：Lenovo Legion Go/S、ASUS ROG Ally/X、OneXPlayer F1/G1/X1 及变种、GPD Win 4/Mini/Max、Ayn Loki、MSI Claw 1<span></span>st Gen AI7+/8+、Zotac Zone、Ayaneo Air/Geek/Next、Steam Deck LCD/OLED；
-   支持桌面级显卡和风扇的调节；
-   **超 雄 更 新**
  -   **每次更新前的版本**都可以通过 GRUB 直接回滚；
  -   掌机版下，如果连续三次启动失败，会自动执行回滚；
  -   **最近 90 天内发布的所有版本都在线上保留**，一条命令即可在线回滚到特定版本；
-   **Linux 内核**、**显卡驱动**和 [**Gamescope**](https://github.com/ValveSoftware/gamescope) 合成器等软件更新更加频繁；
-   更及时更新的 **KDE Plasma** 和 **GNOME** 桌面环境；
-   自带**游戏相关的实用软件**, 包括 **Lutris、ScopeBuddy GUI、ProtonUp-QT/ProtonPlus、Protontricks** 等；
-   **GNOME** 桌面环境作为 KDE Plasma 的替代；
-   通过 Flatpak 支持的**虚拟化**和 **GPU 穿透**；
-   通过 [Waydroid](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md) 安装 **Android 程序**；
-   多种方式配置 [**Sunshine**](/Advanced/sunshine/) 的脚本，让游戏串流更方便；
-   **[Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal.md)** 和 [`ujust`](/Installing_and_Managing_Software/ujust.md) 快捷脚本提供方便的系统设置或常用软件的配置；
-   默认使用 **Btrfs** 文件系统，支持自动**去重**和**压缩**（SteamOS 使用的是 **Ext4**），并支持**内部存储**和 **SD 卡**的**自动挂载**。

### 日常使用

-   系统组件更新更加频繁；
-   桌面模式使用 Wayland，保证在高分辨率显示配置下显示比例仍然正确；
-   绝大多数自带软件包按 Fedora 的更新周期运作，除非测试中发现问题（此时可能会延后更新或提前修复）。

### 开发者

-   通过 [Distrobox](https://distrobox.it) 使用其他发行版的包管理器和软件仓库；
-   预安装了 [Homebrew](https://brew.sh/) 用于管理用户级的命令行程序；
-   Fedora 软件包支持[加入系统树](/Installing_and_Managing_Software/rpm-ostree.md)，在系统更新中也能保留；
-   更多信息请参考 [Bazzite DX 官网](https://dev.bazzite.gg)。

### 安全性提升

Bazzite 支持 LUKS 加密、安全启动，和基于 TPM 的自动解锁。除此之外，Bazzite 默认启用并预先配置了 [SELinux (安全增强的 Linux)](https://www.redhat.com/en/topics/linux/what-is-selinux) 。

安全启动在和 Windows 双启动的环境下同样有用，尤其是考虑到有些 Windows 上的反作弊组件要求启用安全启动。
>请参考[**安全启动相关指南**](/General/Installation_Guide/secure_boot.md)。
