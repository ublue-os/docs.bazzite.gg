---
title: 常见问题及解决方法
---

# 常见问题及解决方法

## 目录

- [显卡与显示相关](#1-display-and-graphics)
- [手柄和游戏输入相关](#2-controllers-and-gaming-inputs)
- [网络相关](#3-network-and-wi-fi)
- [桌面环境配置相关](#4-desktop-environment-and-system-configuration)
- [特定软件相关](#5-application-and-software)

---

## 1. 显卡与显示相关

### 光标闪烁或不显示

比较常见的原因是显卡驱动的问题。作为临时修复，一般可以强制软件渲染光标。

=== "KDE Plasma"

    使用以下命令设置对应的环境变量：

    ```bash
    echo "KWIN_FORCE_SW_CURSOR=1" > ~/.config/environment.d/99-kwin-force-sw-cursor.conf
    ```

=== "GNOME"

    使用以下命令设置对应的环境变量：

    ```bash
    echo "MUTTER_DEBUG_DISABLE_HW_CURSORS=1" > ~/.config/environment.d/99-mutter-disable-hw-cursor.conf
    ```

!!! warning "该修复可能会影响设备的电池续航能力。"

---

### Flatpak 程序无法使用 NVIDIA 硬件加速

在 Bazzite 进行系统更新之后，NVIDIA 用户有时会碰到 Flatpak 安装的程序性能较差和/或失去视频加速的情况，通常伴随 **NVIDIA Flatpak 运行时组件版本不匹配**一类的警告。

此时需要通过 **Bazaar** 升级所有 Flatpak 包，或在 **Bazzite Portal** → **Manage Bazzite** 下选择 **Update Nvidia Flatpak Runtime**。

!!! info "Bazzite 在最近的版本提供了一个能够自动进行相关更新的脚本，但如果碰到类似于启动时没有网络连接这一类的情况，则可能仍需手动更新。最理想的解决方案需要上游 Flatpak 或者 NVIDIA 改善运行时组件的配置方式，或提供直接调用系统组件的“假包”，但这些方法都超出了 Bazzite 的能力范围。"

---

### HDMI-CEC 无法稳定运作

在 [Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal) 下选择 **Troubleshoot → Change CEC mode**。

!!! note "`cecd` 目前已知在需要转接头的 HTPC 配置下可能无法使用唤醒相关功能。如有需要，可以尝试 dGPU 模式下是否出现类似问题。"

*   dGPU 模式（旧版方法）：基于`libcec`和`cec-ctl`的传统配置，一般在 HTPC 环境下和 pulse8 和绿联（Ugreen）转接头的兼容性较好，有时也能解决一些独立显卡上 CEC 13 针没有连通的问题。
*   原生模式（新方法）：走 Valve 维护的`linux-cec`/`cecd`系统，并屏蔽旧版组件。

!!! info "原生模式直接编译运行 Valve 上游的 GitLab 仓库发布的`linux-cec`，并包含 inputattach 的 CEC 组件和 linuxconsoletools，因此 Pulse-Eight 系列的转接头往往能够无缝衔接 Linux 内核的 CEC 子系统，但绿联转接头目前总体兼容性会比较差。"

---

### 笔记本电脑的 NVIDIA Optimus 显卡无法识别

在安装了 NVIDIA Optimus 显卡的笔记本电脑上运行 Bazzite 时，可能会出现游戏默认运行在集成显卡上因此出现性能损失的情况。

此时建议通过预装的 [Cardwire](https://github.com/OpenGamingCollective/cardwire) 实用工具来配置显卡相关的功能。

> 关于 Cardwire 的更多信息请参考[这里](/Advanced/cardwire)。

!!! info "更高级的 Optimus 相关功能在 Linux 上并不可用，比如动态切换（MUX）的功能目前只有 AMD SmartMUX 有内核层面完成的一些前期工作。MUX 相关功能的设置目前需要重启才能生效。"

---

## 2. 手柄和游戏输入相关

### 桌面模式下游戏控制器和掌机摇杆无法使用

在 **Steam 设置 → Controller → Non-Game Controller Layouts → Desktop Layout** 下选择 **Edit** → **Enable Steam Input**，按照桌面模式需要的键盘和鼠标的操作方式进行修改。

!!! Tip "通常需要将 **Right Joystick Sensitivity** 调低到 50-80% 附近，否则鼠标移动速度会非常快。"

!!! Notice "KDE Plasma 6.7 新增了手柄直接控制桌面的功能，但其与 Steam 目前提供的模拟方式冲突，因此两者一般只需选一个启用。"

---

### Xbox 控制器通过蓝牙连接时陷入匹配循环，Xbox 按钮闪烁

该问题通常是因为控制器的固件需要更新。

最简单的方法是将其连接到运行 Windows 的实体机上，在上面安装 Xbox Accessories 程序以进行控制器的固件更新。更新完成后一般立刻就能正常连接。

更高级的方法是部署一台 Windows 的虚拟机并将控制器的连接重定向到虚拟机中以进行更新。

---

## 3. 网络相关

### 和 Windows 双启动的配置下无法连接网络

如果双启动配置下 Windows 的有线或无线网络能够正常连接但在 Bazzite 下不行，很有可能是 Windows 快速启动导致的问题。

启用快速启动时，Windows 会在关机时改为进入一种介于完全关机和休眠之间的状态，这能够缩短开机所需的时间，但也会导致网卡等特定硬件在启动到非 Windows 环境下时状态异常。一种绕过方法是在 Windows 中选择“重新启动”而非“关机”，这样保证进入 Linux 时能够完整重置所有硬件状态。但更推荐的方法一般是直接禁用快速启动：

-   进入**控制面板**
-   选择**电源选项**（在**硬件和声音**分类下）
-   选择**选择电源按钮的功能**
-   点击**更改当前不可用的设置**
-   取消勾选**启用快速启动（推荐）**
-   （可选）取消勾选**休眠**（和快速启动存在相似的问题）
-   选择**保存修改**

![在 Windows 里禁用快速启动](../img/disable-windows-fast-startup.gif)

关闭按快速启动后，Windows 在关机时也会完整重置硬件，不再干扰 Bazzite 下的正常运行。

---

### Wi-Fi 慢或有明显卡顿

Linux 默认的 Wi-Fi 节能设置有时会在特定网卡硬件下出现问题。如果该问题在 Windows 下不出现，可以考虑以下的解决方法。

> 掌机版镜像的用户应参考[这一指南](/Handheld_and_HTPC_edition/quirks/#wi-fi-is-slow-wi-fi-lag-spikes)。

在终端运行`ip link show`，以列出所有的网络设备，输出一般类似于这样：


```

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: wlp6s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff permaddr 00:00:00:00:00:00

```

我们要寻找的是无线网卡的名称。比如在以上的输出中（ROG Ally），对应的名称是`wlp6s0`。

!!! tip "`wlan0`是另一个比较常见的默认名称。"

接下来运行`iw wlp6s0 get power_save`（将`wlp6s0`对应替换成你上一步拿到的名字）以查询节能模式的状态：

```

Power save: on

```

接下来配置 NetworkManager 禁用所有无线网络设备的节能模式。在终端运行

```bash
echo -e "[connection]\nwifi.powersave = 2" | sudo tee /etc/NetworkManager/conf.d/wifi-powersave-off.conf
systemctl restart NetworkManager

```

再次运行`iw wlp6s0 get power_save`以确认节能模式已经关闭：

```
Power save: off

```

!!! warning "该修复可能会影响设备的电池续航能力。"

如果要还原设置，只需要删除之前保存的配置文件：

```bash
sudo rm /etc/NetworkManager/conf.d/wifi-powersave-off.conf
systemctl restart NetworkManager

```

---

### `iwd`相关问题

??? quote "更多信息"

    由于 Intel 将开源开发的优先级降低，[`iwd`](https://wiki.archlinux.org/title/Iwd)目前基本上已经不再受维护，且在较新的 Linux 内核上已经无法正常工作，因此较新的 Bazzite 版本已经不再包含 iwd。以下内容仅作为历史信息供参考。

    !!! warning "以下问题只针对[`iwd`](https://wiki.archlinux.org/title/Iwd)。由于 Intel 基本不再维护 iwd，Bazzite 强烈建议将[无线网络后端系统更换](./#switching-wi-fi-backends)回[`wpa_supplicant`](https://wiki.archlinux.org/title/Wpa_supplicant)。"

    !!! info "在较新的移除了[`iwd`](https://wiki.archlinux.org/title/Iwd)的镜像上，Bazzite 在启动时会自动把无线网络后端系统切换为[`wpa_supplicant`](https://wiki.archlinux.org/title/Wpa_supplicant)。以下内容只适用于仍安装了[`iwd`](https://wiki.archlinux.org/title/Iwd)的镜像。"

    ---

    #### 更换无线网络后端系统

    在 [Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal/) 的 **Troubleshooting** 页下选择 **Change Wi-Fi system back-end**。

    ---

    #### Wi-Fi 慢或有明显卡顿 （IWD）

    配置 iwd 在所有无线网络设备上禁用节能模式：

    ```bash
    echo -e "[DriverQuirks]\nPowerSaveDisable = *" | sudo tee /etc/iwd/main.conf
    systemctl restart iwd
    ```

    运行`iw wlp6s0 get power_save`以确认节能模式已经关闭：
    ```
    Power save: off
    ```

    !!! warning "该修复可能会影响设备的电池续航能力。"

    如果要还原设置，只需要删除之前保存的配置文件：
    ```bash
    sudo rm /etc/iwd/main.conf
    systemctl restart iwd
    ```

    ---

    #### 连接无线网络时报错："Failed to add new connection: 802.1x connections must have IWD provisioning files"

    NetworkManager 在使用`iwd`后端时无法自动生成 802.1x 的连接文件。

    如果必须使用`iwd`后端，则可以按以下步骤手动配置连接。对于`eduroam`：

    ```bash
    sudo nano /var/lib/iwd/eduroam.8021x
    ```

    在文件里输入以下内容：

    ```bash
    [Security]
    EAP-Method=PEAP
    EAP-Identity=anonymous@<university.domain>
    EAP-PEAP-Phase2-Method=MSCHAPV2
    EAP-PEAP-Phase2-Identity=<username@university.domain>
    EAP-PEAP-Phase2-Password=<password>

    [Settings]
    AutoConnect=true
    ```

    注意将`<university.domain>`、`<username@university.domain>`和`<password>`对应换成你的信息。完成后按`Ctrl+X`和`Y`以保存并退出编辑器。

    之后即可再次尝试连接。如果仍然不行，尝试以下命令：

    ```bash
    nmcli connection modify eduroam 802-1x.phase1-auth-flags 32
    ```

    之后再次尝试连接。

    ---

    #### 连接 802.1x 无线网络时报错："IP configuration was unavailable"

    !!! warning "以下问题只针对[`iwd`](https://wiki.archlinux.org/title/Iwd)。由于 Intel 基本不再维护 iwd，Bazzite 强烈建议将[无线网络后端系统更换](./#switching-wi-fi-backends)回[`wpa_supplicant`](https://wiki.archlinux.org/title/Wpa_supplicant)。"

    !!! warning "iwd 在较新的 Linux 内核上已经无法正常工作，因此较新的 Bazzite 版本已经不再包含 iwd。以下内容仅作为历史信息供参考。"

    通过`ujust logs-this-boot | grep NetworkManager`时可能注意到以下内容：

    ```console
    NetworkManager[1563]: <info>  [1770094603.8488] device (wlan0): state change: failed -> disconnected (reason 'none', managed-type: 'full')
    NetworkManager[1563]: <info>  [1770094603.8568] dhcp4 (wlan0): canceled DHCP transaction
    NetworkManager[1563]: <info>  [1770094603.8569] dhcp4 (wlan0): activation: beginning transaction (timeout in 45 seconds)
    NetworkManager[1563]: <info>  [1770094603.8569] dhcp4 (wlan0): state changed no lease
    ```

    使用`iwd`后端时，如果同一个企业无线网络已经在另一个操作系统下连接过或使用不同的后端系统连接过，则 NetworkManager 可能无法正确获取 DHCP 租约，导致 IP 配置失败。

    如果必须使用`iwd`后端，则可以按以下步骤进行配置。

    ```bash
    sudo mkdir -p /etc/iwd/
    sudo nano /etc/iwd/main.conf
    ```

    在文件里输入以下内容：

    ```ini
    [General]
    AddressRandomization=network
    ```

    完成后按`Ctrl+X`和`Y`以保存并退出编辑器。使用以下命令重新启动 iwd：

    ```bash
    systemctl daemon-reload
    systemctl restart iwd
    ```

    之后应该可以正常连接企业网络。

---

## 4. 桌面环境配置相关

### KDE Plasma 禁用特殊字符输入弹窗

KDE Plasma 6.7 为 Plasma 屏幕键盘新增了在长按特定键时弹窗以输入特殊字符的功能。

要禁用该功能的话，取消勾选**系统设置 → 键盘 → 屏幕键盘 → 备选字符：按住按键时弹出**。

![禁用特殊字符输入弹窗|1181x1024, 50%](/img/turn-off-special-char-pop-up.png)

---

### Dolphin 无法使用 SMB 协议共享的网络目录

Fedora Atomic 的系统的用户和组的配置方式与传统 Linux 有所不同，因此 Dolphin 提供的将用户添加到相关组的按钮实际无法工作。

需要将用户手动添加到**`usershares`**组。

> [这篇指南](/Advanced/add-user-to-group)提供了详细信息。

---

### Bazzite 桌面版配置自动登录

=== "KDE Plasma"

    在**系统设置 → 颜色和主题 → 登录屏幕**下勾选**"自动登录"**。“作为用户”选择你的用户名，“跟随会话”选择**"Plasma"**。设置完成后选择“应用”。

=== "GNOME"

    在**设置 → 用户**下，选择右上角的**解锁**，然后勾选**自动登录**。

---

### 一些技嘉主板无法从睡眠状态唤醒

<small>_生命因何而沉睡？因为你技嘉睡死过去了。_</small>

一些技嘉主板在系统挂起后无法正常恢复，屏幕无法点亮，只能重新启动。

目前的解决方法是禁用 GPP0 和 GPP8 唤醒。Bazzite 为此提供了一条隐藏的 ujust 指令：

```bash
ujust _toggle-gigabyte-wake-fix

```

---

## 5. 特定软件相关

### Firefox 和 KeePassXC 无法集成

KeePassXC （或任何其他通过 Flatpak 安装的密码管理器）因 Flatpak 沙盒限制，默认无法访问其他程序的环境。

一种方法是通过 Distrobox 安装 Firefox 和 KeePassXC，但这样反过来可能会有视频硬件加速相关的问题。

!!! info "你也可以尝试[该指南](https://discourse.flathub.org/t/how-to-run-firefox-and-keepassxc-in-a-flatpak-and-get-the-keepassxc-browser-add-on-to-work/437)提供的方法，但请注意该方法需要修改 Flatpak 的沙盒策略并配置自定义的浏览器扩展项。该方法并非由 Bazzite 设计，也无法支持，仅作为参考信息提供。"

---

### 在老设备上配置掌机模式

对于不支持 Steam 游戏模式的显卡，只使用 Bazzite 桌面版镜像，也能实现类似于掌机版的界面功能。

[启用自动登录](#setting-bazzites-desktop-editions-to-automatically-login)，并设置 Steam 开机自启动大屏幕模式，即可得到类似于掌机版的操作体验。

使用 Bazzite 桌面版的 GNOME 镜像的 NVIDIA 用户，可以参考这个视频指南（视频制作时 NVIDIA 显卡尚无法运行 Steam 游戏模式，但底层原理基本一致） ：

https://www.youtube.com/watch?v=F9l-RQvCPMo

!!! info "如果你的镜像自带的是 KDE Plasma 桌面环境，则可以跳过"Making Gnome look more familiar to Windows users"的部分。只需启用自动登录并在**系统设置 → 自动启动**中配置 Steam 大屏幕模式即可。"

---

### Steam 大屏幕模式性能较差

有时 Steam 大屏幕模式的界面本身较为卡顿，但从中启动的游戏不受影响。

如果碰到这类问题，需要完全退出 Steam，并通过 **Steam 大屏幕模式**的菜单项重新启动。另外应确保 **Steam 设置 → 界面 → 在网页视图中启用 GPU 加速渲染（需要重启）**为勾选状态。

> 该修复有时也能解决使用 NVIDIA 显卡时 Steam 游戏模式的一些问题，但同时可能会导致 Steam 菜单和边栏出现渲染错误。

---
