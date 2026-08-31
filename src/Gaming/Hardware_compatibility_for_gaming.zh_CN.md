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
  - **外置或其他非系统盘**: 必须使用 **BTRFS**（固态硬盘）或 **Ext4**（机械硬盘）。 _将文件转移后，可以在安装完成之后进行格式化。_
  > 更多信息请参考[这一部分](#unsupported-filesystems-for-secondary-drives)。
- **网络连接**: 稳定的有线或无线连接。 _安装时不需要。_

!!! note

    有些外设硬件与 Linux 不兼容，因此无法和 Bazzite 配合使用，具体的兼容情况通常取决于厂商。对于 USB 连接的无线网卡，可以参考[这篇确认兼容的硬件列表](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md)。

>[**Hardware for Linux**](https://linux-hardware.org/?view=computers) 这个网站提供了一些 OEM 型号的电脑和 Linux 的兼容性的相关信息。

### Steam 游戏模式的系统要求

!!! note

    这些要求只适用于 [Bazzite 掌机版](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)（bazzite-deck），和 [SteamOS](https://store.steampowered.com/steamos/) 的要求基本一致。

- 较新的 AMD 显卡
  - RX 4xx 系及以上
    - 也支持 Radeon 600M/700M/8000S 等 APU 集显
- Intel Arc 显卡（和 AMD 相比存在**少量问题**）
- NVIDIA 显卡（理论能跑但存在[**严重问题**](/Handheld_and_HTPC_edition/quirks/#nvidia-gpu-exclusive-issues-with-steam-gaming-mode)） 
  - 这些问题为 NVIDIA 驱动在 Linux 端本身的问题，因此无法在 Bazzite 一侧解决
- [**Steam**](https://store.steampowered.com/) 账号
  - 如果目前没有账号，也可以在安装完成后在系统开机时注册

### Compatible Handhelds

The [**Handheld Wiki**](../Handheld_and_HTPC_edition/Handheld_Wiki/index.md) lists tested handhelds with proper support, including the Steam Deck, ASUS ROG Ally, Lenovo Legion Go, and a handful of other handhelds.

<hr>

## 支持 Vulkan 的显卡

!!! attention

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

!!! note

    Bazzite 默认自动挂载使用 Ext4 和 BTRFS 文件系统的外接硬盘。

**BTRFS 是 Bazzite 默认选择并推荐使用的文件系统**。任何计划在 Bazzite 上使用并存储游戏的分区都应该使用**Ext4 或 BTRFS**文件系统，但**格式化的过程会不可逆清除所有数据**。[**可以使用 GNOME Disks 按需进行格式化**](../Advanced/Auto-Mounting_Secondary_Drives.md)，但请务必注意不要丢失数据。

!!! warning "格式化一个分区会清除上面的所有数据，且无法撤销。"

### Unsupported Filesystems for Secondary Drives

!!! warning

    NTFS and exFAT/FAT32 are NOT SUPPORTED. These filesystems can and will eventually lead to DATA CORRUPTION under Linux, and/or does not support the features needed for Proton/WINE. Do NOT use them!
    WinBTRFS still have BUGS, and the file permission/ownership system on Windows is very different to that of Linux, with no guarantee that you won't run into issues and/or data loss later down the road.
    
    All of this means that there is Unfortunately no reliable cross-platform filesystem that can be shared between Windows and Linux.

!!! warning "格式化一个分区会清除上面的所有数据，且无法撤销。"
    
!!! info
    
    To disable the NTFS nag, run `ujust _disable-ntfs-service`. **ONLY DO THIS IF YOU KNOW WHAT YOU ARE DOING. THIS WILL NOT PREVENT DATA LOSS, ONLY DISABLE THE WARNING.**


#### NTFS

If you are coming from Windows and plan to game on a secondary drive with games already installed on it, then we regret to inform you that the NTFS filesystem is **unsupported** for PC gaming on Bazzite.

Playing games off of NTFS causes various issues, including but not limited to **games not launching at all**, and will eventually result in **data corruption** and **permanent data loss**!

#### exFAT 和 FAT32

FAT32 and exFAT are **unsupported**. Both filesystems **do not support symbolic links** which is required for Proton prefixes to work properly.  However, there are scenarios where a microSD card is formatted to exFAT _may work_ in some cases, but this method is unsupported as something the Bazzite maintainers do not plan to accommodate.

Additionally, the FAT family of filesystems are not [Journaling file systems](https://en.wikipedia.org/wiki/Journaling_file_system). This means data loss or corruption on FAT is more likely to happen, with recovery being much, much harder. Therefore, Bazzite also advises to avoid storing important data without backups on FAT filesystems.

### 和双启动的 Windows 共用游戏库

Install the unofficial [WinBtrfs](https://github.com/maharmstone/btrfs) driver on your Windows installation **at your own risk**. Please make sure to read any documentation associated with this project before installing the driver on Windows.

#### Video Tutorial

https://www.youtube.com/watch?v=h6fc-3CCXbA
