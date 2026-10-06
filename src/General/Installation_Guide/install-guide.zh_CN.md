---
title: Bazzite 安装指南
---

# Bazzite 安装指南

## 视频指南

https://www.youtube.com/watch?v=lBqbk6Z8HrQ

## 系统要求

- 对于 Bazzite 本身的系统要求，请参考[**硬件兼容性指南**](/Gaming/Hardware_compatibility_for_gaming.md)；
- 绝大多数较新的硬件都支持安全启动和 TPM，但安全启动支持需要[**手动导入 Bazzite 的密钥**](#secure-boot)；
- [**支持和 Windows 双启动的配置**](#dual-booting-windows)。

### 安装要求

- 下载 Bazzite ISO
  - 如果浏览器下载大文件遇到困难，可以考虑 [**Motrix**](https://motrix.app/) 一类的下载管理器。
- 16GB 或更大的存储设备，比如 U 盘
  - 有些设备支持从 SD 卡或 MicroSD 卡启动，但对固件有要求。
- 烧录 ISO 的工具：
  - **Fedora Media Writer（推荐）** （[Windows/macOS](https://github.com/FedoraQt/MediaWriter/releases), [Linux](https://flathub.org/en/apps/org.fedoraproject.MediaWriter)）
  - **Rufus** （[Windows](https://rufus.ie/)）
  - **Ventoy** （[Windows, Linux](https://www.ventoy.net/)）（[**安全启动需要额外配置**](https://www.ventoy.net/en/doc_secure.html)）
- 推荐有线键盘连接设备
  - 最新的镜像支持屏幕键盘，因此如果有触屏或有线鼠标连接，可以作为替代
  - 安装器通常需要鼠标或触屏来进行操作

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

## 备份数据

将安装 Bazzite 的硬盘上的个人数据应提前备份到其他存储设备上。

## 下载镜像

![download|1871x856, 60%](../../img/live-installer-download.png)

- 在 [Bazzite 官网](https://download.bazzite.gg) 上选择所需的镜像版本并下载；
- 将安装镜像烧录到另一个存储设备上；
- 如有需要，烧录完成后可以移除该设备。

### 计算 ISO 的 SHA256 校验和

**视频指南**:

https://www.youtube.com/watch?v=wUDbMJtR1sM

## 烧录镜像

![flash|771x623, 70%](../../img/live-installer-fedora-media-writer-1.png)
![flash|771x723, 70%](../../img/live-installer-fedora-media-writer-2.png)

用 Fedora Media Writer 或其他 ISO 烧录软件将镜像烧录到 U 盘上，完成之后弹出 ISO。

## 启动安装器

- 将烧录了安装镜像的存储插入设备并开机；
- 将存储作为第一启动设备以进入安装器；
- 具体操作流程取决于你的硬件，但通常需要进入 BIOS 菜单或（如果有）临时修改启动设备的菜单，一般是<kbd>F9</kbd>或附近的键；
  - 有的时候开机界面上会有相关的文本提示（按 XX 键以进入启动菜单/中断启动）。如有需要，也可以参考主板生产商的文档，或线上搜索主板型号；
    - 或者修改 BIOS 设置以将外接设备的优先级提高到内置硬盘之前，但这可能会影响安装完成后的启动顺序，因此不推荐。
- 使用镜像自带的验证功能以确保镜像完整，之后会自动进入安装器。

### 掌机

长按**音量下**键（<kbd>-</kbd>）的同时点按电源键，并在听到开机提示音时松开两个键，就可以进入启动管理器。在启动管理器内选择安装镜像所在的设备，即可进入安装器。

## Live 环境

![Bazzite 的 Live 安装器的 GRUB 菜单|800x600, 70%](../../img/live-installer-grub.png)

![Live 环境|1431x897, 60%](../../img/live-installer-opening.png)

Bazzite 的 Live 安装环境提供了和实际安装相近的桌面配置，以展示用户界面相关内容。

我们不建议在 Live 环境内尝试进行游戏，因为安装器环境的性能通常与实际安装后有明显差别。
另外，安装环境打包的内核版本与实际安装不同，因此不一定包含 Bazzite 的所有硬件支持，比如 Steam Deck 上的声卡等。

### 在 Live 环境下配置网络

![网络设置|495x593, 100%](../../img/live-installer-network.png)

Bazzite 的安装过程不需要联网，但在测试功能的时候往往会有用。准备好之后，选择桌面上的 **Install to Hard Drive** 选项以开始安装。

## 选择语言、地区和键盘布局

![欢迎页|1295x1054, 62%](../../img/live-installer-language.png)

![日期和时间页|1295x1054, 62%](../../img/live-installer-time-date.png)

选择语言、地区、时区和键盘布局。键盘布局会影响之后的输入操作，因此需要确定配置正确。

## 分区配置

![安装方案页，单系统安装|1273x1038, 63%](../../img/live-installer-drive.png)

!!! warning "警告"

    为了防止数据丢失，在选择安装目标时只选择直接需要的硬盘，并且尽量在启动安装之前先暂时移除其他硬盘。

选择你计划安装 Bazzite 的硬盘。目前安装器暂不支持手动分区，因此会删除该硬盘上现有的所有内容。

## 和 Windows 双启动

![安装方案页，双系统安装|1773x1247, 52%](../../img/live-installer-dualboot.png)

!!! note "备注"

    如果你不打算和 Windows 双启动，可以跳过这个部分。

!!! warning "警告"

     双启动相关选项下会提示将会格式化 EFI 分区，但实际上安装器只是将 Bazzite 的启动组件安装到相同 EFI 分区，原有的 Windows 的启动组件不会受影响。这是安装器上游项目里就有的一个显示问题，不会影响功能。

基于 Live 环境的新版 ISO 在双启动配置下只支持自动分区。自动分区进行的配置应该适合绝大多数情况，但如果你需要自定义分区方案，则必须下载**旧版的安装镜像**，并参考[对应的安装指南](./legacy-install.md)。**多块硬盘**双启动时，GRUB 可能难以检测到其他硬盘上的安装的 Windows，因此也建议通过系统的 BIOS 菜单配置引导顺序。

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

=== "多块硬盘"

    **除非完全没有多余硬盘可用，否则我们推荐这样配置。**

    Bazzite 将安装到单独的一块硬盘上，不论内置还是外接。

    1. 安装其他操作系统（比如 Windows）；
    2. 将 Bazzite 安装到独立的另一块盘上；
    3. （可选）设置 Bazzite 为默认引导。

    如果在安装 Bazzite 之后安装 Windows，建议在安装时移除 Bazzite 所在的硬盘，防止 Windows 意外选择错误的 EFI 分区进行安装。

    如果没有可用的内置硬盘，也可以借助 [Rufus](https://rufus.ie/en/) 等工具和 Windows To Go 以进行双启动。

### 和其他 Linux 系统双启动

!!! note "备注"

    Bazzite 和其他 Atomic 系统类似，需要 GRUB 层面上的一些特殊配置，因此暂时不支持和其他发行版双启动，尤其是**非 Atomic 的 Fedora**。如果必须这样配置，为了防止出现问题，我们建议通过系统 BIOS 配置引导顺序，而非任何一个发行版提供的 GRUB 菜单。如果 Bazzite 的引导组件丢失，可以通过新版安装镜像自带的 **Bootloader Restoring Tool** 进行修复。

如果是同一块硬盘上多个 Fedora Atomic 系统（比如 [Bluefin](https://projectbluefin.io/)）的双启动，由于目前它们基本上都共用 Fedora 的引导路径，因此必须为每个系统设置单独的 EFI 分区，并通过系统的 BIOS 菜单配置引导顺序。

## 硬盘加密

![存储配置页|1284x1045, 62%](../../img/live-installer-storage-encryption.png)

!!! warning "警告"

    硬盘加密的密码和用户的密码相互独立，如果你忘记了前者，所有数据将无法恢复！

Bazzite 安装时支持启用基于 [LUKS](https://docs.fedoraproject.org/en-US/quick-docs/encrypting-drives-using-LUKS/) 的硬盘加密，但**输入该密码需要有线键盘连接**。如果你不需要该功能，则不要勾选“加密我的数据”。绝大多数情况下硬盘加密不属于必要的安全措施，但如果你认为有硬盘被其他物理手段访问的风险，可以考虑启用。

## 用户设置

![创建账户页|1288x1050, 62%](../../img/live-installer-user-setup.png)

!!! warning "警告"

    不建议启用 Root 账户。

配置登录 Bazzite 使用的用户名和密码。之后需要管理员批准的操作也会使用该密码，因此请务必记住。

## 开始安装

![检查并安装页|1283x1042, 62%](../../img/live-installer-partitions.png)

![进行安装|1282x1036, 63%](../../img/live-installer-installing.png)

再次检查安装器列出的所有将要进行的系统改动，如果没有问题，选择“删除数据内容并安装”。进行安装可能需要一段时间。

## 重新启动

![安装完成|1288x1040, 62%](../../img/live-installer-installed.png)

安装完成后，重新启动设备。此时可以移除安装使用的 U 盘。

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
