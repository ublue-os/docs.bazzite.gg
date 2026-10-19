---
title: 应急模式和急救模式
---

# 应急模式和急救模式

## 前言

Fedora 的`systemd`配置通常保证了系统出现问题时能够回退到应急模式或者急救模式，但由于 Fedora 和 Universal Blue 发行版在安装时都默认不设置 Root 用户密码，导致进入这些模式的时候会报错：

```
Cannot open access to console, the root account is locked.
```

不过 _Universal Blue_ 系列发行版最近抄到了上游 _Fedora CoreOS_ 的作业，所以现在启动到[应急模式](#booting-to-emergency-mode)和[急救模式](#booting-to-rescue-mode)时，即使 Root 用户没有设置过密码（锁定状态），应该也会给出提示：

```
Press Enter for maintenance
(or press Control-D to continue):
```

此时按<kbd>Enter</kbd>就能正常进入 Root Shell。SELinux 应该也会自动生效，除非已经被其他配置禁用。这使得强制修改用户密码一类的任务更加方便。

---

## 应急模式（Emergency mode）

应急模式启动最低限度的系统环境，因此急救模式因其他原因不可用时，应急模式可能仍能生效。在应急模式下，系统会只读挂载根目录，但不会尝试挂载任何其他文件系统，不会激活网络接口，并且只启动最低限度的必要服务。

1. 开机时按<kbd>Esc</kbd>已进入 GRUB 菜单；
   a. 如果按 <kbd>Esc</kbd> 的次数太多，可能会进入 GRUB shell （`grub>`）；
   b. 此时输入 `exit` 并按 <kbd>Enter</kbd> 以回到 GRUB 主菜单。
2. 通过上下键选择你要操作的部署（通常为`ostree:0`，即第一个选项），按 <kbd>E</kbd>以进入编辑模式；
3. 在自定义命令的界面中，找到 `linux` 开头的一行，按<kbd>Ctrl</kbd>+<kbd>E</kbd>以跳到行尾；
4. 在行尾添加`emergency`；
   a. 注意在`emergency`和前面已有的内容之间需要空格；
   b. `-b`、`systemd.unit=emergency.target`和`emergency`三者等价，但只需要使用一个。
5. 按 <kbd>Ctrl</kbd>+<kbd>X</kbd> 以按当前命令启动。

---

## 急救模式（Rescue mode）

急救模式提供一个单用户环境，允许在系统正常启动流程无法正常进行时进行一些基础的修复工作。急救模式下，系统会挂载所有预定义的文件系统，启用一些关键系统服务，但不启用网络，且维护用户登录之后不再允许其他用户登录。Fedora 的定义下急救模式即为单用户模式。

1. 开机时按<kbd>Esc</kbd>已进入 GRUB 菜单；
   a. 如果按 <kbd>Esc</kbd> 的次数太多，可能会进入 GRUB shell （`grub>`）；
   b. 此时输入 `exit` 并按 <kbd>Enter</kbd> 以回到 GRUB 主菜单。
2. 通过上下键选择你要操作的部署（通常为`ostree:0`，即第一个选项），按 <kbd>E</kbd>以进入编辑模式；
3. 在自定义命令的界面中，找到 `linux` 开头的一行，按<kbd>Ctrl</kbd>+<kbd>E</kbd>以跳到行尾；
4. 在行尾添加`single`；
   a. 注意在`single`和前面已有的内容之间需要空格；
   b. `1`、`s`、`S`、`systemd.unit=rescue.target`和`single`都等价，只需要使用一个。
5. 按 <kbd>Ctrl</kbd>+<kbd>X</kbd> 以按当前命令启动。

---

## 没有密码的 Root Shell 安全吗？

人工进入这两种模式的共同前提是用户能够修改 GRUB 启动的命令，因此如果 GRUB 配置了需要密码解锁（设置后 GRUB 默认禁止启动命令的修改），则这一绕过方法会自动失效。如果一个恶意用户能够修改 GRUB 参数，则他完全可以使用更直接的`init=/bin/bash`完全绕过验证流程，因此这一设计在安全性上不会产生损失。

反过来说，这种设计也保证了 SELinux 相关策略自动生效，防止标签出错影响系统稳定性。除此之外，应急模式在正常使用中也可能会因为系统定义自动挂载的文件系统检查失败而触发，因此新设计保证了此时用户能够进入一个可以进行操作的终端。

---

## 重置用户密码

忘记了用户的登录密码吗？参考 [Fedora Atomic 上游的文档](https://docs.fedoraproject.org/en-US/fedora-silverblue/troubleshooting/#_resetting_passwords_in_rescue_mode)进行重置。对于 Bazzite，如果你安装时没有进行设置，可以尝试默认密码`bazzite`。
