---
title: Distrobox Containers
---

# Distrobox Containers

![distrobox|510x413](../img/distrobox.png)

## Basic Usage

Run other minimal variants of popular Linux distributions in Bazzite inside of a container and access each distribution's packages without any of their dependencies and libraries affecting the host machine.

- Containers are **not** virtual machines.
- Containers are intended to be **disposable** and may run into issues where they need to be recreated.
- Using this method to obtain software **requires knowledge of how traditional Linux operating systems install packages**.
  - Create a test container to familiarize yourself with basic Linux commands before diving in further.

Distrobox containers run sub-systems of other popular [Linux distributions](https://distrobox.it/compatibility/#containers-distros) with access to their package managers (`apt`, `dnf`, `pacman`, etc.) and their package formats (`.deb`/`.rpm`) and any additional repositories like the [AUR](https://aur.archlinux.org/). Distrobox containers can be used for both **development environments** and **installing applications that are not available in any of the other installation methods** which can be exclusive to specific package managers.

---

### **Linux Distribution Examples**

!!! warning "Be wary of installing software from community repositories such as the AUR, COPR, and PPA. Anyone can host packages there and packages will be of varying qualities."

| OS                                  | Package Manager    | Search for Packages                                                       |
| ----------------------------------- | ------------------ | ------------------------------------------------------------------------- |
| [Fedora][fedora]                    | [`dnf`][dnf]       | [Fedora Packages][fedora_pkgs] / [COPR Packages][copr]                    |
| [Arch][arch]                  | [`pacman`][pacman] | [Arch Linux Packages][arch_pkgs] / [AUR Packages][aur_pkgs]               |
| [Debian][debian] / [Ubuntu][ubuntu] | [`apt`][apt]       | [Debian Packages][deb_pkgs] / [Ubuntu Packages][ubuntu_pkgs] ([PPA][ppa]) |
| [openSUSE][osuse]                   | [`zypper`][zypper] | [openSUSE Packages][osuse_pkgs]                                           |
| [Void][void]                  | [`xbps`][xbps]     | [Void Linux Packages][void_pkgs]                                          |
| [Alpine][alpine]              | [`apk`][apk]       | [Alpine Linux Packages][alpine_pkgs]                                      |

---

#### Arch Linux Distrobox Container Example

![i use arch btw|1022x822, 75%](../img/i_use_arch_btw.png)

<small>_I use Arch (in a container) btw._</small>

---

## Distrobox Graphical Interface

![Distroshelf|970x752, 75%](../img/distroshelf_fixedcrop.png)

Distrobox containers can be created and managed graphically with [**DistroShelf**(GNOME)](https://github.com/ranfdev/DistroShelf) or [**Kontainer**(KDE Plasma)](https://github.com/DenysMb/Kontainer) which are pre-installed. You may also install them through [Bazaar](/Installing_and_Managing_Software/Flatpak.md).

---

## Command Line Usage

Distroboxes can be managed and integrated through various GUI apps. Nevertheless, you may still interact with Distrobox through the command line.

---

### Desktop Integration

Applications with a graphical user interface can integrate with your system with an application shortcut by exporting the application using the below command in the container terminal window:

```bash
distrobox-export --app <package>
```
To "un-export" the app, enter the command below in the container terminal window:

```bash
distrobox-export --delete --app <package>
```

---

### Manually Create Pre-Configured Distrobox Containers

```bash
ujust distrobox-assemble
```

Select the container that you want to use.

> **Advanced users**: Declare your own custom Distrobox containers following the [`distrobox-assemble` documentation](https://distrobox.it/usage/distrobox-assemble/).

---

### Entering The Container

Swap between different containers in your host within the terminal application or alternatively use the following command:

```bash
distrobox enter <container>
```

---

### Removing Distrobox Containers

Delete containers graphically with DistroShelf/Kontainer.

Alternatively, use the command line:

```bash
distrobox stop <container_name>
distrobox rm -f <container_name>
```

---

## Distrobox Video Guide

https://youtu.be/5m0YfIiypwA

---

## Project Website

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
