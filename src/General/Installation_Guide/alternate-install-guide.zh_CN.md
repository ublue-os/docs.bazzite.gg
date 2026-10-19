---
title: 备选安装方式
---

# 备选安装方式

!!! warning "警告"

    该方法使用的安装器没有针对掌机类硬件的相关优化，因此可能会出现显示问题。

## 从 Fedora Atomic 桌面镜像切换

如果 Bazzite 自己的 ISO 在你的配置下出现问题或者没有足够大的 U 盘，有一种安装方法是先安装 [Fedora Kinoite (**KDE Plasma**)](https://fedoraproject.org/atomic-desktops/kinoite/) 或 [Fedora Silverblue (**GNOME**)](https://fedoraproject.org/atomic-desktops/silverblue/)，取决于你想要的桌面环境。

1. Fedora Kinoite/Silverblue 的安装流程和 Bazzite 基本一致，但需注意**不要设置 Root 账户**；

2. 安装完成后，访问 Bazzite 官网并选择 ["**Existing Fedora Atomic Desktop Users**" 部分](https://download.bazzite.gg)，或参考 [FAQ 页提供的完整镜像列表](/General/FAQ/#bazzite-image-chart-example)，以确定切换镜像所需的命令；

3. 在终端输入先前确定的命令。注意这条命令需要下载完整的 Bazzite 镜像，因此可能需要花费一些时间，且没有进度条提示。

4. 操作完成后重新启动，即可进入 Bazzite。之前安装时设置的用户名和密码应该仍然有效。

5. Flatpak 的安装不受切换影响，因此 Bazzite 预装的 Fltapak 包需要手动安装。请参考[这一部分](#install-pre-installed-flatpak-applications)。

## 从 Fedora Atomic 切换时的安全启动相关配置

从 Fedora Silverblue 或 Fedora Kinoite 等镜像切换到 Bazzite 时，请参考 [**Bazzite 的主 README**](https://github.com/ublue-os/bazzite/blob/main/README.md#secure-boot) 以确定需要的安全启动相关配置。

## 预安装的 Flatpak 包

在终端输入以下命令：

```command
ujust _install-system-flatpaks
```

如果有提示，选择 **Flathub** 作为软件源。如果有 "System" 和 "User" 的选项，应选择 "**System**"。

> **将安装的包列表取决于镜像对应的桌面环境：**
>
> - [**KDE Plasma**](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/kinoite/usr/share/ublue-os/bazzite/flatpak/install)
> - [**GNOME**](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/silverblue/usr/share/ublue-os/bazzite/flatpak/install)

### 移除 Fedora Flatpak 软件源

使用 Warehouse 程序移除 Fedora Flatpak 软件源。该操作**不会影响**已安装的 Flatpak 包或用户数据。

## 切换到已签名的镜像

所有设置完成之后，出于安全考虑，应从**未签名**的镜像切换到**签名**镜像。在终端里输入：

```command
ujust verify-image
``` 
命令完成后，重新启动设备。

## 视频指南

https://www.youtube.com/watch?v=0NKEfVvdiOs
