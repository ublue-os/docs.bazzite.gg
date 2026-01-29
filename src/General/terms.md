---
title: Dictonary & Terminology
---

# Dictonary & Terminology

## General

- **[[Desktop] Linux](https://www.ubuntudocs.com/bdesktop/)**: A family of operating systems that share many of the same core software including the [Linux kernel](https://www.kernel.org/), [systemd](https://systemd.io/) and the [GNU core utilities](https://www.gnu.org/software/coreutils/).
- **[Desktop Environment](https://en.wikipedia.org/wiki/Desktop_environment)**: The graphical user interface (UI) and user experience (UX) for the Desktop Mode / Desktop images for Bazzite. Also known as a *DE*.
- **[Fedora Linux](https://fedoraproject.org/)**: A leading edge Linux operating system that has a new major release every 6 months.
- **[Fedora Atomic Desktop](https://fedoraproject.org/atomic-desktops/)**: An experimental version of Fedora Linux created to be as reliable and reproducible. Two of the most popular variants are known as [Fedora Silverblue](https://fedoraproject.org/atomic-desktops/silverblue/) and [Fedora Kinoite](https://fedoraproject.org/atomic-desktops/kinoite/) for the specific desktop environments that they use (GNOME and KDE Plasma respectively).
- ["**Immutable**"](https://blog.verbum.org/2020/08/22/immutable-%E2%86%92-reprovisionable-anti-hysteresis/): A term to describe Linux operating systems that do not follow the traditional filesystem layout where every single file can be removed by the user with root privileges.  It is more [nuanced than this in the case of Bazzite](https://docs.fedoraproject.org/en-US/fedora-silverblue/technical-information/#filesystem-layout), but is still considered "immutable" from the point of view of the extended Linux community.  The Bazzite team would **not** describe Bazzite as an "immutable" operating system.
- [**Open Gaming Collective (OGC)**](https://github.com/OpenGamingCollective): A working group for organizations and individuals interested in providing a collaborative framework for upstream changes to the various gaming components that will benefit all Linux gaming focused projects.

## Bazzite-Deck Images

- **[Steam Deck](https://store.steampowered.com/steamdeck)**: Valve's gaming handheld PC that utilizes their own operating system which runs their own Linux operating system based around the [Steam client](https://store.steampowered.com/about/download).
- **[SteamOS](https://www.steamdeck.com/en/software)**: Valve's Linux operating system based on [Arch Linux](https://archlinux.org/) that the Steam Deck runs.
- **[Gamescope](https://github.com/ValveSoftware/gamescope)**: Micro-compositor developed for SteamOS.  Usage includes scaling, filtering, framerate limiting, and HDR support.
- **[Steam Gaming Mode](https://github.com/KyleGospo/gamescope-session)**: A session that runs Steam's Big Picture Mode user interface inside of Gamescope.  Also known as *Game Mode*.

## Software

- **[Proton](https://github.com/ValveSoftware/Proton)**: Gaming-focused compatibility layer maintained by Valve to run Windows games using [WINE](https://www.winehq.org/), [DXVK](https://github.com/doitsujin/dxvk), [VKD3D](https://github.com/HansKristian-Work/vkd3d-proton), and other components.
- [**Vulkan**](https://www.vulkan.org/): Cross-platform, open standard graphics API derived from AMD's Mantle as an alternative to DirectX, which is Windows exclusive.
- [**OpenGL**](https://www.opengl.org/): Legacy graphics API when Vulkan is not available.
- **[Flatpak](https://flatpak.org/)**: Universal applications for Linux.  The default remote is from [Flathub](https://www.flathub.org).
- [**Containers**](https://www.redhat.com/en/topics/containers) - Isolated environments for software.

## Underlying Technology

- **[OSTree/libostree](https://ostreedev.github.io/ostree/introduction/)**: Upgrade system that Bazzite utilizes that allows for rolling back previous system updates or rebasing to different images entirely.
- **[Handheld Daemon (HHD)](https://github.com/hhd-dev/hhd)**: Handheld hardware-enablement software that provides controller functionality, power utilization, RGB, and more.
- **[Universal Blue](https://ublue.it)**: A FOSS collective that specializes in custom Fedora images.
- **[Bootable Container Image](https://docs.fedoraproject.org/en-US/bootc/getting-started/)**: Software and services are packaged inside of a container that run on top of an existing operating system (like Fedora) as as a means of delivering a specialized operating system.  Also known as a [*custom image*](../Advanced/creating_custom_image.md).
- **[Cloud-Native](https://aws.amazon.com/what-is/cloud-native/)**: Building and deploying software in an automated fashion. Provides features such as over-the-air updates, multiple images that receive the same upgrades upstream, etc.  For the case of Bazzite, every single upgrade is done in [Github](https://github.com/ublue-os/bazzite/).
