---
title: 常见问题
---

# 常见问题（FAQ）

## Bazzite 面向的用户是？

如果你想要符合以下任意要求的操作系统，那么 Bazzite 应该会很合适：

- 一个类似于 SteamOS，和其他 Linux 发行版相比维护成本较低的可用于桌面的操作系统；
- 更适合沙发上<del>葛优躺时</del>用手柄控制的前端用户界面；
- 在原装 Windows 的掌机设备上类似于 SteamOS 的操作体验，但 SteamOS 目前暂时不支持你的设备；
- 对已经运行 SteamOS 的掌机设备（比如 Steam Deck 或 Lenovo Legion Go S SteamOS Edition），想要更新版的软件包但也想保证系统组件的稳定性。

## 我应该选择哪个版本？

[Bazzite 官网](https://bazzite.gg/#image-picker) 提供了一个选择器，能够根据你的硬件、想要的桌面环境、是否需要 Steam 游戏模式（如果硬件支持）这几个问题决定最合适的版本。

Bazzite 有很多种镜像，但总体上来讲可以分成三类：

- **桌面版**: 不包含 Steam 游戏模式，但仍然预装一些游戏相关的软件包。每天自动更新。
- **掌机版**: 开机自动启动 Steam 游戏模式，类似于 SteamOS。更适合手柄控制。
- **开发者版**: 面向软件开发的 Bazzite 镜像。

### 1. 桌面版

**该版本不包含 Steam 游戏模式！**

灵感来源于 SteamOS 的桌面模式和 ChromeOS 的低维护形式，但是面向绝大多数的桌面和笔记本设备。基于 Fedora Atomic （Kinoite/Silverblue），将 Steam 和其他游戏相关的实用工具集成进系统镜像。兼容绝大多数较新硬件配置（只要 Linux 上游支持）。预配置的 [Flathub](https://flathub.org/) 保证和 SteamOS 能够使用的应用一致。应用程序和系统自动定时更新，每次重启时自动应用。

### [2. 掌机版（Bazzite-Deck）](../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)

预装了**Steam 游戏模式**，并在兼容的硬件上支持所有相关功能。该版本默认开机自动启动到 Steam 游戏模式，因此更适合掌机设备和手柄优先的配置。同样自带 GNOME 或 KDE Plasma 的桌面模式。更新不会自动安装，需要手动进行后重启以应用。

### [3. 开发者版（Bazzite-DX）](https://dev.bazzite.gg/)

专精软件开发相关优化的 Bazzite 版本。不提供 ISO，而是通过从已有的镜像切换来进行安装。

#### Bazzite 镜像对比表

!!! note

    这个表格不一定对应所有当前支持的 Bazzite 镜像。

在终端输入以下命令以确定当前运行的 Bazzite 镜像。

```
rpm-ostree status
```

!!! important

    Bazzite 镜像一般都应该以`ostree-image-signed:docker://ghcr.io/ublue-os/`开头。
    <sub> 之后的名称是实际的 Bazzite 版本，对应以下表格。</sub>

| **镜像名称**              | 桌面环境 | Steam 游戏模式 | 面向硬件                                 | 版本       |
| --------------------------- | ------------------- | ----------------- | ------------------------- | ---------- |
| `bazzite`                   | KDE Plasma          | 否                | AMD 或 Intel 显卡          | 桌面版      |
| `bazzite-nvidia`            | KDE Plasma          | 否                | NVIDIA 显卡                | 桌面版      |
| `bazzite-nvidia-open`       | KDE Plasma          | 否                | 较新的 NVIDIA 显卡          | 桌面版      |
| `bazzite-gnome`             | GNOME               | 否                | AMD 或 Intel 显卡          | 桌面版      |
| `bazzite-gnome-nvidia`      | GNOME               | 否                | NVIDIA 显卡                | 桌面版      |
| `bazzite-gnome-nvidia-open` | GNOME               | 否                | 较新的 NVIDIA 显卡          | 桌面版      |
| `bazzite-deck`              | KDE Plasma          | 是                | AMD 或 Intel Arc 显卡      | 掌机版      |
| `bazzite-deck-nvidia`       | KDE Plasma          | 是                | 较新的 NVIDIA 显卡          | 掌机版      |
| `bazzite-deck-nvidia-gnome` | GNOME               | 是                | 较新的 NVIDIA 显卡          | 掌机版      |
| `bazzite-deck-gnome`        | GNOME               | 是                | AMD 或 Intel Arc 显卡      | 掌机版      |

## 如果 SteamOS 基于 Arch Linux，为什么要换成 Fedora Atomic？

虽然 Arch Linux 为滚动发布，但 SteamOS 的更新基本独立，因此频率更低。Bazzite 基本遵循 Fedora 的发布频率，因此往往能够比 SteamOS 更早获取驱动程序和内核版本的更新。Fedora Atomic 和 Universal Blue 目前的实现使得同一套更新能够快速的在一台镜像的多个变体上应用，这与传统意义上的衍生发行版有所不同。**Bazzite 致力于保证安装好的系统开箱即用，可以快速上手游戏。**

### 用 Fedora Atomic 作为基础镜像有什么好处？

作为自定义的 Fedora Atomic 桌面镜像，Bazzite 同样采用只读根目录的处理方法，在此基础上通过[可引导容器](https://containers.github.io/bootable/)部署系统，有这样一些好处：

- 完全无法启动的概率更低；
- 回滚系统更新或锁定当前已知正常运行的系统版本，且不影响用户数据；
- 与 Fedora 基本同步的稳定大版本发布；
- 更适合容器化的程序部署，保证程序不会干扰系统运行。

> [**Universal Blue 的主页**](https://universal-blue.org) 提供了关于整个项目的更多信息。

## AMD 和 Intel 的显卡驱动有预先安装吗？

**是**。绝大多数硬件所需的驱动组件都直接集成在上游 Linux 内核中，并随系统一起更新。Bazzite 不支持手动安装不同的驱动或 Linux 内核版本，但反过来说，每个发布的 Bazzite 版本对应的版本组合都经过测试确定能够有效运作。

### NVIDIA 的显卡驱动有预先安装吗？

**在`-nvidia`和`-nvidia-open`版的镜像上是。**它们也同样和系统其他组件一起更新，不支持手动安装。

- `-nvidia`的旧镜像支持 Pascal、Maxwell 和 Volta 架构（GTX 900, GTX 1000, Nvidia Titan V, GTX 750 (TI) and GTX 745）；
- 更新的`-nvidia-open`镜像支持 Turing 及之后的所有架构（GTX 16 系和 RTX 全系）。

!!! notice "如果运行程序时碰到 NVIDIA 相关的问题，请确定你[运行的镜像](./#bazzite-image-chart-example)正确，且 [Flatpak 相关的运行时组件为最新](/General/issues_and_resolutions/#flatpak-apps-have-no-hardware-acceleration-on-nvidia)。"

#### 更老的 NVIDIA 显卡呢？

由于 NVIDIA 上游的驱动已经**不再支持** Kepler 架构及更老的显卡（绝大多数 GTX 700 系或更早的显卡），Bazzite 也无法为其提供支持。

-   使用开源的`nouveau`驱动可以运行 Bazzite；
    -   但`nouveau`驱动无法调用显卡的闭源固件（如 GSP），因此无法调节主频等配置，在性能和稳定性上也难免弱于官方驱动；
-   Bazzite **无法支持**手动安装的 NVIDIA 专有驱动；
-   如果你必须使用官方驱动，则必须选择其他的发行版。Bazzite 面临的限制也同样影响所有 Fedora 系的发行版。

!!! info

    NVIDIA 驱动在 495 及之后的版本中才支持 Wayland。由于 Kepler 架构及更老的显卡的驱动版本只到 470，且 Bazzite 不支持纯 X11 的显示协议，这意味着这些显卡很难在 Bazzite 上正常工作。这种情况下 Linux Mint 或 Debian 等其他发行版可能更为适合。

### 如果我更换了硬件，需要怎么处理？

绝大多数情况下不需要软件方面的任何额外操作。不过，如果是新装或移除了 NVIDIA 显卡，可能需要[切换镜像](../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/brh.md)以确保所使用的显卡驱动对应新的显卡配置。

## 手动运行系统更新时报错`error: System transaction in progress`

![](/../img/system-transaction-in-progress.png)

[桌面版](#1-desktop-edition)镜像默认在后台自动更新。如果更新正在进行时你触发了手动更新，则会出现这个警告。通常只需等待一小会，让自动更新自己完成即可。

## Windows 游戏提示显卡驱动需要更新，该怎么做？

![](/../img/gpu_driver_warning.png)
Windows 游戏往往难以正确判断 Linux 上的驱动程序版本是否为最新。

-   Windows 和 Linux 的驱动版本号往往不同，因此 Windows 游戏可能会提示版本号相关的错误；
-   **这类错误通常可以忽略；**
-   [更多信息请参考这一部分。](#are-amd-and-intel-graphics-card-drivers-pre-installed)

## Bazzite 支持 CSM/传统 BIOS 启动吗？

不支持。安装器检测到 CSM 启动时应该会输出警告并提供关闭 CSM 的相关步骤：![CSM](../img/csm.webp)

## 能使用 AFMF 或 FSR-FG 一类的帧生成技术吗？

**仅限支持 FSR 3.1 或更高的游戏。**简单来说：

-   AFMF 一类的驱动层面的帧生成在 Linux 使用的开源驱动下不可用；
-   特定游戏可能会有专门的模组或 [Decky 插件](https://github.com/xXJSONDeruloXx/Decky-Framegen)提供类似功能；
-   `Proton-CachyOS 11.0-20260702` 及其衍生版本会将支持 FSR 3.1+ 的游戏自动升级到 FSR4.1.1。具体信息请参考[Proton-CachyOS 的 GitHub 发布页](https://github.com/CachyOS/proton-cachyos/releases/tag/cachyos-11.0-20260702-slr)。对于 RDNA3 显卡，**Bazzite Portal** 也提供 FSR-MLFG 的快捷开关；
* 如果你在 Steam 上拥有 [Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/)，可以借助 **Bazzite Portal** 的快捷命令配置 LSFG 的 Vulkan 层。

## 能搞 GRUB 美化吗？

!!! note
    
    Bazzite 默认启动时隐藏 GRUB 菜单，除非双启动或者连续启动失败。
    
由于 OSTree 系统需要的一些特定的 GRUB 配置，Bazzite 无法支持 GRUB 自定义。如果遇到问题，我们建议删除所有 GRUB 自定义美化后再次尝试。

## 如何修改我的主机名称？

!!! note

    由于 Distrobox 容器的相关限制，主机名不能超过 **20 个字符**。

在终端输入以下命令：

```
hostnamectl hostname <hostname>
```

用你想要的主机名替代`<hostname>`。
## 我安装/更新了 Windows 之后 Bazzite 无法启动 { id="windows-bootloader-override" }

绝大多数情况下是 Windows 把 Bazzite 的引导组件当减速带肘了。Bazzite 的安装镜像提供了相关的修复工具，只需重新从 U 盘启动 ISO 并选择 **Bazzite Bootloader Restoration Tool** 即可。

## 我能不重装更换桌面环境吗？
<sub>（在目前 Bazzite 支持的配置下，也就是通过切换镜像进行 GNOME 和 KDE Plasma 之间的转换）</sub>

理论可以但**不推荐**，因为 GNOME 和 KDE Plasma 对一些共用的用户级配置文件的处理方式并不完全兼容，这会导致更换桌面环境后一些用户界面要素出现显示问题。[Mending Wall](https://flathub.org/en/apps/org.indii.mendingwall) 这一实用工具可以帮助处理配置文件的一些变化，但 Bazzite 无法为其提供支持。

最稳妥的更换桌面环境的方法仍然是手动备份用户文件之后完全重装。

## 能使用其他桌面环境或窗口管理器吗？

以 Bazzite 为基础[自制镜像](/Advanced/creating_custom_image.md)，即可配置你所想要的桌面环境或窗口管理器。

## GRUB 菜单中的`:0`和`:1`是什么？

`:0`和`:1`是回滚系统的相关机制。每次更新完成后，更新前的版本会成为`：1`，而新版本会成为`:0`。

- `:0` = 当前部署，通常是最新版本；
- `:1` = 上一个部署。

如果有已锁定的部署版本，则可能会进一步出现`:2`甚至`:3`等条目。如果空间足够，完全可以锁定更多版本。

## Bazzite 这个名字是怎么来的？

[Fedora Linux 的 Atomic 系列版本](https://fedoraproject.org/atomic-desktops/) 一开始是以[矿物质](https://fedoraproject.org/kinoite/)命名的。Bazzite 是一种强度较高、密度较小的矿物，而且是[蓝色](https://universal-blue.org/)的！

## 我想要一款不主要面向游戏的 Bazzite

Universal Blue 旗下还有两个和 Bazzite 同源但不主要面向游戏的系统。它们都仍然可以运行游戏，但和 Bazzite 相比没有那么多游戏特化的预装软件或系统优化。三个项目也在很大程度上共享开发资源和团队。

- [**Aurora**](https://getaurora.dev/) 对应 **KDE Plasma** 桌面环境；
- [**Bluefin**](https://projectbluefin.io/) 对应 **GNOME** 桌面环境。

## 文档里没有提到的问题？

!!! note

    在提出新问题之前，建议先根据问题相关的关键词再次搜索 Bazzite 文档。

欢迎在 [Bazzite 的 GitHub 仓库](https://github.com/ublue-os/bazzite/issues)中氵 issue。不过需要注意的是，有些问题往往不在 Bazzite 团队的能力范围内，比如 NVIDIA 驱动问题、特定游戏的兼容性，或一些整个桌面级 Linux 都有的大环境问题。
