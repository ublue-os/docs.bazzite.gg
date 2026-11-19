---
title: 安装常见问题
---

# 安装常见问题

## 下载 ISO

如果浏览器下载太慢或不方便，可以考虑 [**Motrix**](https://motrix.app/) 或类似的下载器。

## 安装硬盘

为防止数据丢失，建议安装时只选择想使用的存储，并断开其他存储设备的连接。

---

## 报错 “Failed to open \EFI\BOOT\mmx64.efi - Not Found”

![Failed to open \EFI\BOOT\mmx64.efi - Not Found](../../img/efi-boot-fail.png)

最简单的解决方法是手动选择正确的 EFI 文件启动。在你的 BIOS 菜单中，寻找“从文件启动”、"Boot from file" 或类似选项，找到安装 Bazzite 启动组件的 EFI 分区，并选择`/EFI/fedora/grubx64.efi`。
操作一次之后，系统的启动管理器应该就能正确的显示一个`FEDORA`的启动选项，直接选择就可以启动 Bazzite。

---

## 安装镜像无法启动

!!! note

    新版的 ISO 不支持 CSM 启动，必须切换到 UEFI 模式。请参考 [**Bazzite 的系统需求**](../../Gaming/Hardware_compatibility_for_gaming.md#minimum-system-requirements)。

使用[旧版 ISO](./legacy-install.md)，或通过[其他方法](./alternate-install-guide.md)来安装 Bazzite。

---

## 错误代码 1

错误代码 1 本质上是安装过程中子部件出现没有具体信息的错误时 Anaconda 的通用信号，因此其本身提供的信息有限。我们注意到的一些常见原因包括：

- **已有的 Linux 安装**： 如果同一块硬盘上之前安装过其他 Linux，则可能会出现引导组件安装失败或 “bootloader write config” 相关的错误。
  - 即使旧的 Linux 安装不完整或已损坏，此类问题仍可能会出现。**Fedora 系**（Fedora、Fedora Atomic、Bazzite、Nobara 等）和 **Debian 系**（Debian、Ubuntu、Mint、PopOS 等）都可能触发。
  - **修复方法 1**：如果你有更多固态硬盘，且新硬盘没有安装过任何 Linux，可以将 Bazzite 安装到那里。
  - **修复方法 2**：手动清理旧的 Linux 的 EFI 记录，[具体步骤见下](#how-to-remove-an-orphaned-copy-of-grub)。
  - **修复方法 3**：如果你**不打算双启动**，可以用 GParted 或类似工具直接删除旧的 EFI 分区。
    - **注意**：该方法进行的更改无法撤销，且会影响到设备上其他能够引导的操作系统，**包括 Windows**。
  - **修复方法 4**：在同一块硬盘上新建一个独立的 EFI 分区。请参考[手动分区指南](./manual_partitioning.md)，并注意创建新 EFI 分区时不要删除旧的。
    - **注意**：有些系统的 BIOS 可能无法处理同一块硬盘上多个 EFI 分区的情况。
- **文件系统不对**：根目录的文件系统配置为 Ext4 可能也会导致这一错误。Bazzite 只支持使用 Btrfs 的根目录。
- **ISO 文件损坏**：检查校验和以确定下载的 ISO 文件没有问题。
- **U 盘过热**：改用 USB 3.0 的盘和接口通常会有帮助。

---

## 报错“No Space left on Device”
![No Space left on Device](../../img/no_more_space_left.png)

有时安装器所需的内存不足时这一信息也会意外出现。[**Bazzite 至少需要 8GB 内存才能运行**]((/General/Installation_Guide/Installing_Bazzite_for_Desktop_or_Laptop_Hardware.md/#minimum-system-requirements))，因此请确保你的配置符合系统要求。

---

## 报错“Bad shim signature, you need to load the kernel first”

![You need to load the kernel first](../../img/you-need-to-load-the-kernel-first.png)

该错误为安全启动相关，必须临时禁用才能解决。请参考[**对应文档**](/General/Installation_Guide/secure_boot.md)的方法 B 部分。

**视频指南**:

https://www.youtube.com/watch?v=Z_DsWqTuipU

---

## 报错“grub_memalign:552:out of memory”

```console
error: ../../grub-core/loader/i386/efi/linux.c:kernel_alloc:159:can't allocate kernel.
error: ../../grub-core/kern/mm.c:grub_memalign:552:out of memory.

Press any key to continue...
```

通常在 BIOS 菜单中禁用受信任平台模块（TPM）可以解决该问题。

---

## 报错“Device is Active”

如果有已安装的 Windows 启用了 BitLocker 加密，可能会碰到这一错误。两种解决方法：

A. **如果需要保留 Windows**：在 Windows 里人工压缩分区，之后在 Bazzite 安装时直接从腾出的可用空间开始配置；
B. **如果只需要 Bazzite**：在启动安装前使用 GParted 或类似工具删除 BitLocker 分区。

**视频指南**：

https://www.youtube.com/watch?v=FBGLLkIKp-w

---

### 检查存储配置时出错（Error checking storage configuration）

**视频指南**：

https://www.youtube.com/watch?v=VTnm9EiBdPA

---

## 无法分配请求的分区方案（Unable to allocate requested partition scheme）

该问题通常在超过 2TB 的硬盘上在 2TB 之外的范围创建分区时出现，类似于下图：

![Unable to allocation requested partition scheme](../../img/unable-to-allocation-requested-partition-scheme.png)

这似乎是安装器使用的 Anaconda 的技术限制。以下是一些解决方法：

- 使用其他硬盘；
- 如果和 Windows 双启动，尝试将 Windows 的分区压缩到 2TB 以下。如果 Windows 自己的磁盘管理工具无法操作，可能需要[EaseUS Partition Master](https://www.easeus.com/partition-master/)一类的工具以进行脱机压缩；
- 如果 2TB 前的分区没有要保留的数据，可以直接清空整块硬盘并重新安装。

---

## 安装器看不到需要的硬盘

存储设备配置为 Intel RAID 阵列时似乎会出现这个问题。由于 Intel RST 在 Linux 上的支持非常有限（仅限于一些企业级发行版），因此建议在 BIOS 中直接禁用。

不同 BIOS 对该功能的命名可能不同，但一般会是以下当中的某一个：

- VMD
- RST
- Rapid Storage Tech(nology)
- 存储模式（Storage mode）：AHCI
!!! warning "直接禁用 RAID 会导致已安装的 Windows 无法正常启动。如果仍需要和 Windows 双启动，请**在禁用 RAID 之前**参考[这份指南](https://support.thinkcritical.com/kb/articles/switch-windows-10-from-raid-ide-to-ahci)。"

!!! note "有些系统的 BIOS 在禁用 RAID 时不会自动清除已有的 RAID 阵列配置，此时必须手动清除先前配置的残余，才能继续安装 Bazzite。具体流程请参考生产商提供的指南文档。"

---

## 其他安装方法

!!! note

    **该方法使用更小的安装镜像，因此安装时能够绕过一些网络和存储相关的问题，但反过来也会导致掌机设备上一些显示的兼容性问题。**

如果以上方法都无法解决问题或有其他情况导致无法安装，请尝试我们支持的另一种安装方式：

[**从 Fedora Kinoite（KDE Plasma）或 Fedora Silverblue （GNOME）安装切换到 Bazzite**](/General/Installation_Guide/alternate-install-guide.md)

---

## 移除旧的 GRUB 组件
1. 启动新版的 Bazzite 安装镜像（不支持旧版），并展开应用程序菜单；
   ![](../../img/remove_grub_1.png)
2. 搜索找到或直接启动磁盘（GNOME Disks）程序；
   ![](../../img/remove_grub_2.png)
3. 选择计划安装 Bazzite 的硬盘；
   ![](../../img/remove_grub_3.png)
4. 找到硬盘上的 EFI 分区。通常是第一个（最左边）的分区，文件系统为 FAT，大小在几百 MB 这一量级；
   ![](../../img/remove_grub_5.png)
5. 选择<key>▶</key>以挂载该分区；
   ![](../../img/remove_grub_6.png)
6. 挂载好之后点击“Mounted at”之后的蓝色链接以在文件管理器中浏览分区内容；
   ![](../../img/remove_grub_7.png)
7. 双击进入`EFI`文件夹；
   ![](../../img/remove_grub_8.png)
8. 在当中找到`Ubuntu`、`Fedora`或其他 Linux 发行版的文件夹，并选择移动到回收站（Move to Trash）；
   ![](../../img/remove_grub_9.png)
!!! warning 
    不要操作其他文件夹，尤其是`Boot`、`Microsoft`或 OEM 厂商的文件夹（比如`Dell`、`HP`等），否则已安装的 Windows 可能无法启动。
9. 重新启动到安装镜像。如果上一次失败的安装创建了一些分区，可能需要将它们移除。
   ![](../../img/remove_grub_10.png)
