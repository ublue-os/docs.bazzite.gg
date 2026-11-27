---
title: 游戏与硬件兼容性
---

# 游戏与硬件兼容性

## 最低系统要求

- **引导固件**: UEFI （[**不支持**](../General/FAQ.md#does-bazzite-support-csmlegacy-boot) CSM/BIOS 启动）
- **处理器（CPU）** : 2GHz，四核
  - **架构**: x86-64
- **内存（RAM）**: 8GB
- **显卡**: 支持 Vulkan 1.3 或更高
- **存储**: 内置**固态硬盘（SSD）**上 50GB 的可用空间
  - **推荐配置**: 内置**固态硬盘（SSD）**上 120GB 的可用空间
  - 硬盘必须为 **GUID 分区表（GPT）**格式。在主启动记录（MBR）硬盘上安装 Bazzite 会出错。
    - Microsoft 在 Windows 上提供了[将已有的 MBR 硬盘无损转换为 GPT 格式的实用工具](https://learn.microsoft.com/en-us/windows/deployment/mbr-to-gpt)。
    !!! warning "在进行任何硬盘更改操作之前，请务必备份所有重要的个人文件。"
  - **外置或其他非系统盘**: 必须使用 **Btrfs**（固态硬盘）或 **Ext4**（机械硬盘）。 _将文件转移后，可以在安装完成之后进行格式化。_
  > 更多信息请参考[这一部分](#unsupported-filesystems-for-secondary-drives)。
- **网络连接**: 稳定的有线或无线连接。 _安装时不需要。_

!!! note "备注"

    有些外设硬件与 Linux 不兼容，因此无法和 Bazzite 配合使用，具体的兼容情况通常取决于厂商。对于 USB 连接的无线网卡，可以参考[这篇确认兼容的硬件列表](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md)。

>[**Hardware for Linux**](https://linux-hardware.org/?view=computers) 这个网站提供了一些 OEM 型号的电脑和 Linux 的兼容性的相关信息。

### Steam 游戏模式的系统要求

!!! note "备注"

    这些要求只适用于 [Bazzite 掌机版](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)（bazzite-deck），和 [SteamOS](https://store.steampowered.com/steamos/) 的要求基本一致。

- 较新的 AMD 显卡
  - RX 4xx 系及以上
    - 也支持 Radeon 600M/700M/8000S 等 APU 集显
- Intel Arc 显卡（和 AMD 相比存在**少量问题**）
- NVIDIA 显卡（理论能跑但存在[**严重问题**](/Handheld_and_HTPC_edition/quirks/#nvidia-gpu-exclusive-issues-with-steam-gaming-mode)） 
  - 这些问题为 NVIDIA 驱动在 Linux 端本身的问题，因此无法在 Bazzite 一侧解决
- [**Steam**](https://store.steampowered.com/) 账号
  - 如果目前没有账号，也可以在安装完成后在系统开机时注册

### 兼容的掌机

[**Handheld Wiki**](../Handheld_and_HTPC_edition/Handheld_Wiki/index.md) 列出了进行了测试且支持的的掌机型号，包括了 Steam Deck、ASUS ROG Ally、Lenovo Legion Go 等。

<hr>

## 支持 Vulkan 的显卡

!!! attention "备注"

    Linux 端运行游戏很大程度上依赖显卡对 [Vulkan](/General/terms/#software) 的支持。

### 查询显卡支持的 Vulkan 版本

有些较老的显卡可能只支持 **Vulkan 1.1 or 1.2**，但不支持 **Vulkan 1.3 或更新版本**。此时可能需要 Proton-CachyOS 配合 DXVK-Sarek，具体指南见下。在**终端**中输入这条命令来查询你的显卡支持的 Vulkan 版本：

```bash
vulkaninfo | grep 'Instance Version'
```

![Vulkan Command](https://github.com/user-attachments/assets/ccca14ca-3001-4aa6-bf47-e0dcbdb73936)

- 如果输出中`Vulkan Instance Version:`一行给出的值低于 1.3 或出现其他错误，则你的显卡不支持 Vulkan 1.3。这很可能会导致各类游戏出现问题或性能损失。

- 更老一些的显卡可能必须回退到 OpenGL 转译而非 Vulkan，这往往会导致进一步的问题或性能损失。

> 对于只支持 Vulkan 1.1 或 1.2 的显卡，有时可以使用 [**DXVK-Sarek**](https://github.com/pythonlover02/DXVK-Sarek) 进行 Vulkan 转译。 [Proton-CachyOS](https://github.com/CachyOS/proton-cachyos) 默认支持通过`PROTON_DXVK_SAREK=1`[环境变量](/Gaming/launch-options-env-variables)启用，但请注意这可能会触发联机游戏或各类反作弊组件的警告。

!!! info "ProtonPlus 和 ProtonUp-Qt 都可以用于安装 [Proton-CachyOS](https://github.com/CachyOS/proton-cachyos) 或其他版本的 Proton。"

### 不支持 Vulkan 的显卡

对于完全不支持 Vulkan 的显卡，必须为**所有通过 Proton 运行的游戏**设置以下启动选项：

```bash
PROTON_USE_WINED3D=1 %command%
```

这将强制游戏进行 OpenGL 而非 Vulkan 转译。

<hr>

## 文件系统

!!! note "备注"

    Bazzite 默认自动挂载使用 Ext4 和 Btrfs 文件系统的外接硬盘。

**Btrfs 是 Bazzite 默认选择并推荐使用的文件系统**。任何计划在 Bazzite 上使用并存储游戏的分区都应该使用**Ext4 或 Btrfs**文件系统，但**格式化的过程会不可逆清除所有数据**。[**可以使用 GNOME Disks 按需进行格式化**](../Advanced/Auto-Mounting_Secondary_Drives.md)，但请务必注意不要丢失数据。

!!! warning "格式化一个分区会清除上面的所有数据，且无法撤销。"

### 外接硬盘上不支持的文件系统

!!! warning "警告"

    NTFS 和 exFAT/FAT32 **不受支持**。这些文件系统在 Linux 上长期使用**一定**会导致无法在 Linux 上修复的数据损坏，且无法支持 Proton/WINE 需要的一些文件系统功能。不要将游戏安装在这些文件系统上！
    WinBtrfs 也并非完美，且由于 Windows 和 Linux 在文件权限管理上的重大差异，无法保证数据的安全性。
    
    换句话说，目前并不存在一个足够可靠的，能同时用于 Windows 和 Linux 的文件系统。

!!! warning "格式化一个分区会清除上面的所有数据，且无法撤销。"
    
!!! info "信息"
    
    使用`ujust _disable-ntfs-service`命令隐藏 NTFS 挂载时的警告。**这并不能阻止数据损坏，只是隐藏提示信息。**


#### NTFS

如果你先前使用的是 Windows 并且有在 Windows 下配置的安装了游戏的外接硬盘，有个坏消息：Bazzite **无法支持**安装在 NTFS 文件系统上的游戏。

游戏安装在 NTFS 分区上时会产生许多问题，包括**完全无法启动**等，且一定会导致难以修复的数据损坏。

#### exFAT 和 FAT32

FAT32 和 exFAT 都**不受支持**。两者都 **不支持符号链接**，因此 Proton Prefix 无法正常工作。不过，有些情况下可能会将一块 MicroSD 卡格式化成 exFAT 用于数据存储。这种做法有其意义，但 Bazzite 不计划提供支持。

除此之外，FAT 体系的文件系统都不是[日志式](https://en.wikipedia.org/wiki/Journaling_file_system)，因此出现数据损坏时将更难恢复。 Bazzite 不建议将重要数据保存在 FAT 文件系统中。

### 和双启动的 Windows 共用游戏库

非官方的 [WinBtrfs](https://github.com/maharmstone/btrfs) 项目提供了在 Windows 上操作 Btrfs 文件系统的驱动程序，但使用时应注意数据风险。在安装前，请务必阅读项目提供的文档及相关注意事项。

#### 视频指南

https://www.youtube.com/watch?v=h6fc-3CCXbA
