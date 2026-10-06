---
title: 安全启动指南
tags:
  -  QR
search:
  exclude: true
---

# 安全启动指南

## Bazzite 支持安全启动

!!! note

    如果你的设备不支持安全启动或你不打算启用安全启动，则直接选择`Continue boot`。

!!! important

    安全启动的管理界面锁定为英语的 QWERTY 键盘布局，无关你键盘的硬件配置。如果你使用 AZERTY 等键位不同的布局，需注意对应关系。

Bazzite 支持安全启动（Secure Boot），但需要导入 Universal Blue 配置的密钥，否则之后的启动会失败。

## 安全启动重要提醒

- 出于安全考虑，输入密码时不会在屏幕上有任何反馈，包括星号。
- 如果禁用了安全启动之后进行 BIOS 更新，则安全启动可能会自行启用。此时必须走**方法 B** 来修复问题。
- Steam Deck 默认不启用安全启动，也不自带安全启动需要的密钥，因此不建议在 Steam Deck 上启用安全启动。

## 错误信息（**密钥没有正确导入**时）

```
error: ../../grub-core/kern/efi/sb.c:182:bad shim signature.
error: ../../grub-core/loader/1389/efi/linux.c:256:you need to load the kernel first.

Press any key to continue...
```

如果碰到这一情况，请按**方法 B** 进行修复。

### **方法 A** - 安装时配置

![Secure Boot 管理: Continue boot / Enroll MOK / Enroll key from disk / Enroll hash from disk](../../img/Secure_Boot.png 'Secure Boot')

!!! note

    如果你在安装时没有启用安全启动但之后启用，则在下一次系统启动时也会进入该界面。

退出 Bazzite 的安装程序之后，应该会出现一个蓝色的屏幕，提供导入密钥的选项。

如果你启用了安全启动，则选择`Enroll MOK`。如果提示输入密码，则输入：

```command
universalblue
```

如果你没有启用安全启动或硬件不支持，则选择`Continue boot`。

## **方法 B** - 安装后配置

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
## 重新启动并完成密钥导入

重新启动后，应该同样进入蓝色界面：

1.  选择 **Enroll MOK**.
2.  如果要求输入密码，则输入：
    ```command
    universalblue
    ```

再次重启之后，安全启动应该就能正常运作。
