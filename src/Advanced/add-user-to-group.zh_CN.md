---
title: 将用户添加到组
---

# 将用户添加到组

## 前言

[用户和组](https://wiki.archlinuxcn.org/wiki/Users_and_groups) 是 Linux 上控制访问权限的两个层级。其配置关系到整个系统文件和设备等各方面的操作，因此十分重要。

!!! note "以下指南对其他基于 Fedora Atomic 的系统也基本适用。"

---

## 在 Atomic 系统下将用户添加到组

[Bazzite 基于 Fedora Atomic](/General/Fedora_Atomic_Comparison/#comparison-of-bazzite-upstream-fedora-atomic-desktop)，因此用户和组的配置方式与传统发行版略有不同，这导致单纯使用`usermod`通常不足以完成必要的配置。以下将给出完整的将用户添加到任意组的指南。

!!! warning "以下指南涉及对系统底层配置的修改，请务必小心。"

!!! info "如果你只是需要将用户添加到`input`组来解决一些游戏控制器兼容性相关的问题，建议使用**Bazzite Portal → Tweak System → Add input to your user groups**这一快捷命令。"

---

#### 1. 备份当前用户组配置 

在继续之前，用以下命令创建你当前的用户组配置的备份：

```bash
sudo cp /etc/group /etc/group.bak
```

这会把你当前的`/etc/group`文件复制到`group.bak`。除此之外，也建议你查看并手动记录当前`/etc/group`的内容，这样出现问题时会更方便修复。

---

#### 2. 从`/usr/`复制预先定义的组 ID

接下来，应确定要修改的组的 ID 以准备复制。对于预定义的组，以下命令可以提取出已经配置好的组 ID：

!!! tip "`<your_group_name>`必须替换成你实际需要的组的名称。"

```bash
grep "<your_group_name>" /usr/lib/group
```

!!! example "示例"

    对于`dialout`组，得到的结果应该是`dialout:x:18`：

    ```bash
    grep "dialout" /usr/lib/group
    ```
    预期输出：
    ```console
    dialout:x:18
    ```

!!! info "`/lib/`是指向`/usr/lib/`的符号链接。"

---

#### 3. 将所需的组 ID 写入到`/etc/group`

接下来需要将找到的组的条目写入到`/etc/group`。你可以手动添加，也可以通过以下命令快速导入：

!!! tip "`<your_group_name>`必须替换成你实际需要的组的名称。"

```bash
grep "<your_group_name>" /usr/lib/group | sudo tee -a /etc/group
```

!!! example "示例"
    
    ```bash
    grep "dialout" /usr/lib/group | sudo tee -a /etc/group
    ```

!!! warning "Bash 的`>`或`>>`操作符在此处**无法生效**，且`>`会完全覆盖文件的原有内容。建议严格按照此处给出的命令输入。"

---

#### 4. 使用`usermod`命令

接下来，用以下命令将用户添加到组：

!!! tip "`<your_group_name>`应对应实际的组名，`<username>`对应你的用户名。"

```bash
sudo usermod -aG <your_group_name> <username>
```
!!! example "示例"
    
    ```bash
    sudo usermod -aG dialout bazzite
    ```

---

#### 5. 检查无误后重启

修改完成后，务必再次查看`/etc/group`文件，确定以下三条都在：

!!! tip "`<your_group_name>`应对应实际的组名，`<username>`对应你的用户名，`<group_ID>`对应组ID。"

*   `wheel:x:10:<username>`
*   `<username>:x:1000`
*   `<your_group_name>:x:<group_ID>:<username>`

如果你的`/etc/group`文件缺少任意一条，**不要重新启动或关机**。如果无法从备份还原，立刻前往 [Bazzite 的官方 Discord](/community/#discord-no-discord-account)上求助。

如果一切正常，重新启动后修改就能生效。

---

## 配置出错后的修复
<small>_diannaobaozhale_</small>

如果你意外删除了 `/etc/group` 或写入了错误的配置，可能会出现一种意外情况：你可以正常使用图形界面，但以下功能无法使用：

*   重启后的用户登录
*   Polkit 审核
*   `sudo`

此时你将无法直接修复 `/etc/group`，因为这需要 Polkit 或者 `sudo` 提供批准。

为了修复该问题，需要在进入图形界面之前先行启动一个 Root Shell。

---

#### 1. 重新启动到 GRUB 菜单

重新启动设备，并在开机过程中按<kbd>Esc</kbd>键以进入 GRUB 菜单。对于双系统或没有隐藏 GRUB 菜单的配置，也可以在菜单出现时按<kbd>↓</kbd>以打断自动的倒计时。

!!! tip "提示"

    *   如果按<kbd>Esc</kbd>的次数太多，你可能会看到一个`grub>`的 Shell 界面；
    *   此时应输入`exit`并按<kbd>Enter</kbd>，以回到 GRUB 的主要菜单。

![为最新的启动菜单项修改命令|690x351,75%](../img/Edit_the_command_for_the_latest_boot_entry.png)

---

#### 2. 临时修改启动命令

选择最新的部署，按<kbd>E</kbd>以进行临时的启动命令修改。

![使用 init=/bin/bash 命令启动|689x359,75%](../img/Boot_with_init_bin_bash.jpeg)

在`linux`开头的一行的末尾，输入`init=/bin/bash`。

![重新启动|689x359,75%](../img/Reset_Password_Reboot.jpeg)

按<kbd>Ctrl</kbd>+<kbd>X</kbd>以使用新命令启动。

---

#### 3. 修复`/etc/group`

如果启动配置修改正确，你应该会进入一个 **root** 权限的 Shell，绕过`sudo`等限制。

用你习惯的命令行文本编辑器，比如`vim`或`nano`来修改`/etc/group`，确保其至少包含以下内容：

!!! tip "`<username>`必须对应修改为你实际使用的用户名。如果你在安装 Bazzite 时没有手动配置，则应使用默认的`bazzite`。"

*   `wheel:x:10:<username>`
*   `<username>:x:1000`

!!! example "示例"
    
    ```console
    bash-5.2# cat /etc/group
    wheel:x:10:bazzite
    bazzite:x:1000
    ```
!!! note "如果你有出现问题之前的`/etc/group`备份，则可以使用`cp /etc/group.bak /etc/group`命令以进行还原。"

---

#### 4. 将用户添加到`wheel`组

修改好`/etc/group`之后，为了将你的用户正确加入`wheel`组，必须暂时加载系统的 SELinux 策略。

挂载 SELinux
```bash
mount -t selinuxfs selinuxfs /sys/fs/selinux
```
加载 SELinux 策略
```bash
/sbin/load_policy
```
将用户添加到`wheel`组
!!! tip "`<username>`必须对应修改为你实际使用的用户名。如果你在安装 Bazzite 时没有手动配置，则应使用默认的`bazzite`。"
```bash
/sbin/usermod -aG wheel <username>
```
同步 I/O
```bash
sync
```
重新启动
```bash
/sbin/reboot -ff
```

---
