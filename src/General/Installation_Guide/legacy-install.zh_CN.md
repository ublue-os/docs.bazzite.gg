---
title: 使用旧版 ISO 安装 Bazzite
---

# 使用旧版 ISO 安装 Bazzite

## 旧版 ISO

该指南针对的是旧版的基于 Anaconda 的安装镜像，目前由于新的安装器暂时不支持手动分区等一些问题所以保留支持。

## 系统要求

- 对于 Bazzite 本身的系统要求，请参考[**硬件兼容性指南**](/Gaming/Hardware_compatibility_for_gaming.md)；
- 绝大多数较新的硬件都支持安全启动和 TPM，但安全启动支持需要[**手动导入 Bazzite 的密钥**](#secure-boot)；
- [**支持和 Windows 双启动的配置**](#dual-booting-windows)。

### 安装需求

- 下载 Bazzite ISO
  - 如果浏览器下载大文件遇到困难，可以考虑 [**Motrix**](https://motrix.app/) 一类的下载管理器。
- 16GB 或更大的存储设备，比如 U 盘
  - 有些设备支持从 SD 卡或 MicroSD 卡启动，但对固件有要求。
- 烧录 ISO 的工具：
  - **Fedora Media Writer（推荐）** （[Windows/macOS](https://github.com/FedoraQt/MediaWriter/releases), [Linux](https://flathub.org/en/apps/org.fedoraproject.MediaWriter)）
  - **Rufus** （[Windows](https://rufus.ie/)）
  - **Ventoy** （[Windows, Linux](https://www.ventoy.net/)）（[**安全启动需要额外配置**](https://www.ventoy.net/en/doc_secure.html)）
- 推荐有线键盘连接设备（如果设备没有触屏则必要）
  - 如果需要自定义初始**用户名**和**密码**则必要。

### 桌面环境

目前提供 [**KDE Plasma**](https://kde.org/plasma-desktop/) 和 [**GNOME**](https://www.gnome.org/) 两种桌面环境的选项。

除此之外，两种镜像都可以额外增加 [**Steam 游戏模式**](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)，更适合家庭影院（HTPC）和掌机的配置。

Bazzite 文档的[**常见问题**部分](../../General/FAQ.md)进一步解释了不同镜像版本之间的差别。

=== "KDE Plasma"

    #### KDE Plasma（默认）

    ![Bazzite 运行 KDE Plasma 桌面环境|690x388, 75%](/img/KDE_Plasma_DE.png)

    - KDE Plasma 的默认外观更接近 Windows，方便迁移
    - 非常大的个性化空间
    - Qt 框架
    - SteamOS 同款，一些其他主流发行版也提供支持

=== "GNOME"

    #### GNOME（`-gnome`镜像）

    ![Bazzite 运行 GNOME 桌面环境|690x388, 75%](/img/GNOME_DE.png)

    - GNOME 的默认外观更适合触屏
    - 注重简洁性
    - GTK 框架
    - Ubuntu 和一些其他主流发行版的默认选择

=== "Steam 游戏模式"

    #### Steam 游戏模式（仅限掌机版镜像）

    ![Steam 游戏模式|690x388, 75%](/img/Gaming_Mode.jpeg)

    !!! note "备注"

        掌机版镜像默认**自动登录**到 Steam 游戏模式。访问桌面模式需要在 Steam 菜单的电源选项选择“切换到桌面”。

    {% block desktop_envs_steam_notes %}

    - **需要 [Steam](https://store.steampowered.com/) 账户**
    - [掌机版镜像](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)自带
    - 界面更适合掌机和手柄控制
    - 仍可选择 KDE Plasma 或 GNOME 作为独立的桌面环境
    - 通过 [Decky 插件](https://github.com/SteamDeckHomebrew/decky-loader) 增强 Steam 游戏模式。[官网列出了插件列表](https://plugins.deckbrew.xyz/)。

    {% endblock %}

## 0. 备份数据

将安装 Bazzite 的硬盘上的个人数据应提前备份到其他存储设备上。

## 1. 下载并烧录镜像

- 在 [Bazzite 官网](https://download.bazzite.gg) 上选择所需的镜像版本并下载；
- 将安装镜像烧录到另一个存储设备上；
- 如有需要，烧录完成后可以移除该设备。

### 计算 ISO 的 SHA256 校验和

**视频指南**:

https://www.youtube.com/watch?v=wUDbMJtR1sM

## 2. 启动安装器

- 将烧录了安装镜像的存储插入设备并开机；
- 将存储作为第一启动设备以进入安装器；
- 具体操作流程取决于你的硬件，但通常需要进入 BIOS 菜单或（如果有）临时修改启动设备的菜单，一般是<kbd>F9</kbd>或附近的键；
  - 有的时候开机界面上会有相关的文本提示（按 XX 键以进入启动菜单/中断启动）。如有需要，也可以参考主板生产商的文档，或线上搜索主板型号；
    - 或者修改 BIOS 设置以将外接设备的优先级提高到内置硬盘之前，但这可能会影响安装完成后的启动顺序，因此不推荐。
- 使用镜像自带的验证功能以确保镜像完整，之后会自动进入安装器。

### 掌机

长按**音量下**键（<kbd>-</kbd>）的同时点按电源键，并在听到开机提示音时松开两个键，就可以进入启动管理器。在启动管理器内选择安装镜像所在的设备，即可进入安装器。

## 3. 安装器

!!! note "备注"

    如果你没有连接有线键盘，**不要点击**"_创建用户_"。Bazzite 默认的用户名/密码配置在点击后会自动失效，如果没有连接键盘，安装将无法继续。

    **默认用户名**: `bazzite`
    **默认密码**: `bazzite`

![Automatic drive configuration|690x497, 75%](../../img/anaconda_drive_configuration.png)

![User setup example|690x359, 75%](../../img/anaconda_user_setup.png)

- 选择语言、地区、键盘布局和时区；
- 选择安装 Bazzite 的硬盘；
  - 除非你计划用这块硬盘双启动，否则建议删除硬盘上的所有分区；
  - 除非你计划用这块硬盘双启动，否则建议选择自动配置。
- 如果需要，设置系统盘加密的密码；
  - **如果你丢失了这个密码，所有数据将无法恢复**；
  - 该密码在启动时**必须用有线连接的键盘输入**！
- 设置用户；
  - 该用户必须有管理员权限，并设置密码。
- 开始安装；
- 安装完成后，重新启动系统。

## 双启动

!!! note "备注"

    如果你不打算和 Windows 双启动，可以跳过这个部分。

### 和 Windows 双启动

**多块硬盘**双启动时，GRUB 可能难以检测到其他硬盘上的安装的 Windows，因此也建议通过系统的 BIOS 菜单配置引导顺序。

### 视频指南

前半部分为同一块硬盘安装，后半为多块。

https://www.youtube.com/watch?v=KAt49B6rSFI

=== "共用硬盘，自动分区"

    1. 在 Windows 中，禁用 **BitLocker 驱动器加密**和**快速启动**，然后重新启动一次；
    2. 使用 Windows 的磁盘管理工具压缩 Windows 的分区，为 Bazzite 腾出空间；
    一般压缩之后的配置应该类似于：
    ![](/img/dualbooting_partitions_windows.png)
    <i><small>来源：[diskpart.com](https://www.diskpart.com/windows-10/windows-10-disk-management-0528.html)</small></i>
    3. 启动 Bazzite 的安装镜像，并按自动分区的流程操作；
    4. 安装完成后，在 Bazzite 上运行`ujust regenerate-grub`，以将 Windows 的启动选项加入 GRUB 菜单。

=== "共用硬盘，手动分区（仅限旧版安装镜像）"

    1. 使用 Windows 的磁盘管理工具压缩 Windows 的分区，为 Bazzite 腾出空间；
    一般压缩之后的配置应该类似于：
    ![](/img/dualbooting_partitions_windows.png)
    <i><small>来源：[diskpart.com](https://www.diskpart.com/windows-10/windows-10-disk-management-0528.html)</small></i>
    2. 启动 Bazzite 的安装镜像，并按[手动分区](#manual-partitioning-instructions)的流程操作；
    3. 安装完成后，在 Bazzite 上运行`ujust regenerate-grub`，以将 Windows 的启动选项加入 GRUB 菜单。

=== "多块硬盘"

    **除非完全没有多余硬盘可用，否则我们推荐这样配置。**

    Bazzite 将安装到单独的一块硬盘上，不论内置还是外接。

    1. 安装其他操作系统（比如 Windows）；
    2. 将 Bazzite 安装到独立的另一块盘上；
    3. （可选）设置 Bazzite 为默认引导。

    如果在安装 Bazzite 之后安装 Windows，建议在安装时移除 Bazzite 所在的硬盘，防止 Windows 意外选择错误的 EFI 分区进行安装。

    如果没有可用的内置硬盘，也可以借助 [Rufus](https://rufus.ie/en/) 等工具和 Windows To Go 以进行双启动。

如果 Windows 在 Bazzite 之后安装，可能需要 Live ISO 提供的 **Bootloader Restoring Tool** 来修复 Bazzite 的引导组件。

### 手动分区指南

!!! warning "一般推荐自动分区，除非需要在同一块硬盘上安装双系统。"

!!! attention "Bazzite 只支持 Btrfs 文件系统的根目录（`/`）。"

可以参考[这一指南（9:10 处开始，链接自带时间戳）](https://www.youtube.com/watch?v=JxPsKhJGTrs&t=550s).

1.  选择安装目标位置
2.  在**存储配置**栏下，选择`高级自定义 (Blivet-GUI)`；
![选择手动分区](../../img/select_manual_partitioning.png)
3.  创建以下这些分区：
  - **/boot/efi**
    ![EFI 分区](../../img/efi_partition.png)
    ```
    挂载点：/boot/efi
    文件系统：EFI 系统分区（EFI system partition）
    大小：300MiB
    ```
  - **/boot**
    ![启动分区](../../img/boot_partition.png)
    ```
    挂载点：/boot
    文件系统：ext4
    大小：2GiB
    ```
  - **系统分区（Btrfs 容器）**
    ![Btrfs 分区](../../img/btrfs_partition.png)
    ```
    挂载点：（不设置）
    文件系统: btrfs
    大小：（所有剩余空间）
    ```
  - **/**
    ![/ 子卷](../../img/root_subvolume.png)
    ```
    挂载点：/
    设备类型：Btrfs 子卷
    ```
  - **/var**
    ![/var 子卷](../../img/var_subvolume.png)
    ```
    挂载点：/var
    设备类型：Btrfs 子卷
    ```
  - **/var/home**
    ![/var/home 子卷](../../img/var_home_subvolume.png)
    ```
    挂载点：/var/home
    设备类型：Btrfs 子卷
    ```
4.  选择**完成**；
5.  选择**接受更改**；
6.  完成接下来的安装步骤。

### 和其他 Linux 系统双启动

!!! note "备注"

    Bazzite 和其他 Atomic 系统类似，需要 GRUB 层面上的一些特殊配置，因此暂时不支持和其他发行版双启动，尤其是**非 Atomic 的 Fedora**。如果必须这样配置，为了防止出现问题，我们建议通过系统 BIOS 配置引导顺序，而非任何一个发行版提供的 GRUB 菜单。如果 Bazzite 的引导组件丢失，可以通过新版安装镜像自带的 **Bootloader Restoring Tool** 进行修复。

如果是同一块硬盘上多个 Fedora Atomic 系统（比如 [Bluefin](https://projectbluefin.io/)）的双启动，由于目前它们基本上都共用 Fedora 的引导路径，因此必须为每个系统设置单独的 EFI 分区，并通过系统的 BIOS 菜单配置引导顺序。

多块硬盘双启动时，GRUB 可能难以检测到其他硬盘上的系统，因此也建议通过系统的 BIOS 菜单配置引导顺序。

## 安全启动

!!! note "备注"

    如果你不打算启用安全启动或硬件不支持，则可以跳过这一部分。

!!! important "备注"

    安全启动的管理界面锁定为英语的 QWERTY 键盘布局，无关你键盘的硬件配置。如果你使用 AZERTY 等键位不同的布局，需注意对应关系。

Bazzite 支持安全启动（Secure Boot），但需要导入 Universal Blue 配置的密钥，否则之后的启动会失败。

### 安全启动重要提醒

- 出于安全考虑，输入密码时不会在屏幕上有任何反馈，包括星号。
- 如果禁用了安全启动之后进行 BIOS 更新，则安全启动可能会自行启用。此时必须走**方法 B** 来修复问题。
- Steam Deck 默认不启用安全启动，也不自带安全启动需要的密钥，因此不建议在 Steam Deck 上启用安全启动。

### 错误信息（**密钥没有正确导入**时）

```
error: ../../grub-core/kern/efi/sb.c:182:bad shim signature.
error: ../../grub-core/loader/1389/efi/linux.c:256:you need to load the kernel first.

Press any key to continue...
```

如果碰到这一情况，请按**方法 B** 进行修复。

### **方法 A** - 安装时配置

![Secure Boot 管理: Continue boot / Enroll MOK / Enroll key from disk / Enroll hash from disk](../../img/Secure_Boot.png 'Secure Boot')

!!! note "备注"

    如果你在安装时没有启用安全启动但之后启用，则在下一次系统启动时也会进入该界面。

退出 Bazzite 的安装程序之后，应该会出现一个蓝色的屏幕，提供导入密钥的选项。

如果你启用了安全启动，则选择`Enroll MOK`。如果提示输入密码，则输入：

```command
universalblue
```

如果你没有启用安全启动或硬件不支持，则选择`Continue boot`。

### **方法 B** - 安装后配置

该方法需要**在 BIOS 中禁用安全启动**，**密钥导入完成后**可以重新启用。

在已经安装完成的 Bazzite 系统下，运行：

```
ujust enroll-secure-boot-key
```

如果要求输入密码，则输入：

```command
universalblue
```

**现在可以在 BIOS 下重新启用安全启动。**
如果硬件支持，用以下命令直接重新启动到 BIOS 菜单：

```command
ujust bios
```
### 重新启动并完成密钥导入

重新启动后，应该同样进入蓝色界面：

1.  选择 **Enroll MOK**.
2.  如果要求输入密码，则输入：
    ```command
    universalblue
    ```

再次重启之后，安全启动应该就能正常运作。

## **安装故障排除**:

请参考[**安装常见问题**](./troubleshoot_guide.md)或[**备选安装方式**](./alternate-install-guide.md)。

## 安装完成后

至此 Bazzite 安装就完成了。关于安装后的工作，请参考[**对应的文档**](./post-installation.md)。玩的开心！
