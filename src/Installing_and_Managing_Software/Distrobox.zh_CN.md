---
title: Distrobox 容器
---

# Distrobox 容器

![distrobox|510x413](../img/distrobox.png)

## 基本用法

在 Bazzite 系统下通过容器直接运行其他发行版的最小化版本，且不影响主机上的软件。

- 容器**不是**虚拟机；
- Distrobox 容器设计上更加**随用随弃**，如果出现问题则可能需要删除并重新创建；
- 通过 Distrobox 安装软件**更依赖传统 Linux 发行版的相关知识**。
  - 如有需要，可以先创建一个容器用于测试，之后再进行正式的操作。

Distrobox 可以运行[许多 Linux 发行版](https://distrobox.it/compatibility/#containers-distros)，包括它们对应的包管理器（`apt`、`dnf`、`pacman`等）和对应的包格式（`.deb`和`.rpm`），以及相关的其他软件仓库，比如 [AUR](https://aur.archlinux.org/)。因此，Distrobox 容器适合用于软件开发环境，也可以帮助安装一些不支持 Flatpak 一类的分发方式的软件。

### **Linux 发行版示例**:

| 发行版                               | 包管理器            | 搜索软件包                                                                        |
| ----------------------------------- | ------------------ | ------------------------------------------------------------------------- |
| [Fedora][fedora]                    | [`dnf`][dnf]       | [Fedora Packages][fedora_pkgs] / [COPR Packages][copr]                    |
| [Arch][arch]                  | [`pacman`][pacman] | [Arch Linux Packages][arch_pkgs] / [AUR Packages][aur_pkgs]               |
| [Debian][debian] / [Ubuntu][ubuntu] | [`apt`][apt]       | [Debian Packages][deb_pkgs] / [Ubuntu Packages][ubuntu_pkgs] ([PPA][ppa]) |
| [openSUSE][osuse]                   | [`zypper`][zypper] | [openSUSE Packages][osuse_pkgs]                                           |
| [Void][void]                  | [`xbps`][xbps]     | [Void Linux Packages][void_pkgs]                                          |
| [Alpine][alpine]              | [`apk`][apk]       | [Alpine Linux Packages][alpine_pkgs]                                      |

#### Arch Linux 的 Distrobox 创建示例：

![原来你也玩 Arch|1022x822, 75%](../img/i_use_arch_btw.png)

<small>_原来你也玩 Arch_</small>

## 使用场景

因此，Distrobox 容器适合用于**软件开发环境**，也可以帮助**安装一些不支持 Flatpak 一类的分发方式的软件**。

## Distrobox 图形化管理

![Distroshelf|970x752, 75%](../img/distroshelf_fixedcrop.png)

Bazzite 预装了 [**DistroShelf**](https://github.com/ranfdev/DistroShelf) 方便 Distrobox 的管理。

## 桌面环境集成

对于安装在 Distrobox 中且自带图形界面的程序，可以将它“导出”到主机上，这样就可以通过主机的图形界面直接调用：

```bash
distrobox-export --app <package>
```
使用以下命令以撤回导出：

```bash
distrobox-export --delete --app <package>
```

## 按预定义配置创建 Distrobox 容器

```command
ujust distrobox-assemble
```

在列表中选择需要的发行版。

> **高级用户**：参考[`distrobox-assemble`的官方文档](https://distrobox.it/usage/distrobox-assemble/)来定义你需要的容器配置。

### 进入容器

终端程序一般会提供进入容器的快捷选项，或者：

```
distrobox enter <container>
```

## 删除 Distrobox 容器

可以使用 DistroShelf 图形界面删除，或者通过命令行：

```command
distrobox stop <container_name>
```

```commmand
distrobox rm -f <container_name>
```

## Distrobox 视频指南

https://youtu.be/5m0YfIiypwA

## 项目官网

https://distrobox.it/

[fedora]: https://fedoraproject.org/
[dnf]: https://docs.fedoraproject.org/en-US/quick-docs/dnf/
[fedora_pkgs]: https://packages.fedoraproject.org/index-static.html
[copr]: https://copr.fedorainfracloud.org/
[arch]: https://archlinux.org/
[pacman]: https://wiki.archlinux.org/title/Pacman
[arch_pkgs]: https://archlinux.org/packages/
[aur_pkgs]: https://aur.archlinux.org/packages?SB=l&SO=d
[debian]: https://www.debian.org/
[ubuntu]: https://ubuntu.com/
[apt]: https://ubuntu.com/server/docs/package-management
[deb_pkgs]: https://packages.debian.org/stable/
[ubuntu_pkgs]: https://packages.ubuntu.com/
[ppa]: https://launchpad.net/ubuntu/+ppas
[osuse]: https://get.opensuse.org/
[zypper]: https://documentation.suse.com/smart/systems-management/html/concept-zypper/index.html
[osuse_pkgs]: https://search.opensuse.org/packages/
[void]: https://voidlinux.org/
[xbps]: https://docs.voidlinux.org/xbps/index.html
[void_pkgs]: https://voidlinux.org/packages/
[alpine]: https://www.alpinelinux.org/
[apk]: https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper
[alpine_pkgs]: https://pkgs.alpinelinux.org/packages
