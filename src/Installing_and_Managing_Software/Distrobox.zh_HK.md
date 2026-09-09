---
title: Distrobox 容器
---

# Distrobox 容器

![distrobox|510x413](../img/distrobox.png)

## 基本操作

在 Bazzite 上透過 Distrobox 容器運行其他 Linux 發行版，能在不會影響 Bazzite 系統本身的情況下使用其他包管理器和軟件源。

- 容器**不是**虛擬機
- 容器為可輕易拋棄及重建的
- 使用包管理器需要對傳統 Linux 系統管理有一定的認知
  - 你可以先創建一個測試容器去嘗試試鹹淡

Distrobox 容器基於運行其他 [Linux 發行版](https://distrobox.it/compatibility/#containers-distros)的子系統而運作。 你可以將一個容器作為開發環境或是安裝軟件的工具使用。

---

### Linux 發行版例子

!!! warning "請小心並批判性地安裝在社區包源如 AUR、COPR、與PPA上的軟件包。任何人都可以註冊並在這些包源上發行軟件，因而其質量及安全性參差不齊。"

| OS                                  | Package Manager    | Search for Packages                                                       |
| ----------------------------------- | ------------------ | ------------------------------------------------------------------------- |
| [Fedora][fedora]                    | [`dnf`][dnf]       | [Fedora Packages][fedora_pkgs] / [COPR Packages][copr]                    |
| [Arch][arch]                  | [`pacman`][pacman] | [Arch Linux Packages][arch_pkgs] / [AUR Packages][aur_pkgs]               |
| [Debian][debian] / [Ubuntu][ubuntu] | [`apt`][apt]       | [Debian Packages][deb_pkgs] / [Ubuntu Packages][ubuntu_pkgs] ([PPA][ppa]) |
| [openSUSE][osuse]                   | [`zypper`][zypper] | [openSUSE Packages][osuse_pkgs]                                           |
| [Void][void]                  | [`xbps`][xbps]     | [Void Linux Packages][void_pkgs]                                          |
| [Alpine][alpine]              | [`apk`][apk]       | [Alpine Linux Packages][alpine_pkgs]                                      |

---

#### Arch Linux Distrobox 容器圖例

![i use arch btw|1022x822, 75%](../img/i_use_arch_btw.png)

<small>_I use Arch (in a container) btw._</small>

---

## Distrobox 圖形界面

![Distroshelf|970x752, 75%](../img/distroshelf_fixedcrop.png)

Distrobox containers can be created and managed graphically with [**DistroShelf**](https://github.com/ranfdev/DistroShelf) which is pre-installed.
你可以透過預安裝的 [**DistroShelf**(GNOME)](https://github.com/ranfdev/DistroShelf) 或 [**Kontainer**(KDE Plasma)](https://github.com/DenysMb/Kontainer) 創建及管理 Distrobox 容器。此外，你亦可如 Bazaar 應用商店中安裝它們。

---

## 命令行指令

你可於各種提供圖形介面的程式中創建及管理 Distrobox。當然，你亦可透過命令行指令進行更輕量化的管理和設置。

---

### 桌面集成功能

在 Distrobox 中運行的圖形軟件可以透過上述工具或以下指令集成於桌面中，如創建桌面捷徑、應用列表捷徑等。

```bash
distrobox-export --app <package>
```
若要移除這些集成的捷徑，你可以使用上述工具或以下指令。

```bash
distrobox-export --delete --app <package>
```

---

### 手動創建預設 Distrobox 容器

輸入以下指令並選擇欲使用的容器鏡像：

```bash
ujust distrobox-assemble
```

> **進階用戶**: 參考[`distrobox-assemble` 文檔](https://distrobox.it/usage/distrobox-assemble/)以編輯你的個人容器鏡像！

### 進入 Distrobox 容器

你可以透過命令行程式如 Konsole 、 Ptyxis 的內建 Distrobox 集成功能或者使用以下指令進入容器的 Shell：

```bash
distrobox enter <container>
```

---

### 移除 Distrobox 容器

你可透過上述工具或以下指令移除 Distrobox 容器：

```bash
distrobox stop <container_name>
distrobox rm -f <container_name>
```

---

## 項目網誌

https://distrobox.it/

---

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
