---
title: Installing and Managing Applications
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=35", "fetched_at": "2024-09-03 16:43:05.697052+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## Linux Package Formats

Fedora Atomic Desktops have read-only root files to prioritize stability.  Therefore, containerized applications that do not interfere with your host system will work best.

>Check out the [**Frequently Asked Questions**](../General/FAQ/#what-are-the-advantages-to-using-fedora-atomic-desktop) page for why this priority exists.

### **Package formats ranked from most recommended to least recommended for daily usage**:

1. [**`ujust`**](./ujust.md) (_Convenience Commands_) - Custom scripts maintained by Bazzite & Universal Blue contributors that can also install a small subset of applications.
2. [**Flatpak**](./Flatpak.md) (_Graphical Applications_) - Universal package format using a permissions-based model and should be used for most graphical applications.
3. [**Homebrew**](./Homebrew.md) (_Command-Line Tools_) - Install applications intended to run inside of the terminal (CLI/TUI).
4. [**Quadlet**](./Quadlet.md)  (_Services_) - Run containerized applications as a [systemd service](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-managing_services_with_systemd#sect-Managing_Services_with_systemd-Services).
5. [**Distrobox Containers**](./Distrobox.md) (_Linux Packages & Development Workflows_) - Access to most Linux package managers for software that do not support Flatpak and Homebrew and for use as development boxes.
6. [**AppImage**](./AppImage.md) (_Portable Graphical Applications_) - Portable universal package format that relies on specific host libraries at a system-level, usually obtained from a project's website.
7. [**`rpm-ostree`**](./rpm-ostree.md) (_System-Level Packages_) - Layer Fedora packages at a system-level (**not recommended, use as a last resort**)

```mermaid
---
title: "Installing Applications on Bazzite: A Decision Tree"
---
flowchart TD
    gui@{ shape: question, label: "Is it a GUI?" }
    flatpak@{ shape: question, label: "Does it have a Flatpak?" }
    brew@{ shape: question, label: "Does it have a brew formula?" }
    distrobox@{ shape: question, label: "Can you install it in a distrobox?" }
    appimage@{ shape: question, label: "Does it have an AppImage?" }
    layerQ@{ shape: question, label: "Can you layer it?" }
    inst[Install it]
    export[Install and export it]
    gearlever[Download it and put it in Gear Lever]
    layer[Layer it, but here be dragons!]
    custImg[Look into making a custom Bazzite image]
    gui-->|No|brew
    gui-->|Yes|flatpak
    brew-->|Yes|inst
    brew-->|No|distrobox
    flatpak-->|Yes|inst
    flatpak-->|No|distrobox
    distrobox-->|Yes|export
    distrobox-->|No|appimage
    appimage-->|Yes|gearlever
    appimage-->|No|layerQ
    layerQ-->|Yes|layer
    layerQ-->|No|custImg
```

## How do I run Windows applications?

**Use a [WINE](https://www.winehq.org/) front-end**:

- [**Steam**](https://store.steampowered.com/) (_pre-installed_) has a Windows compatibility layer built-in.
- [**Lutris**](https://lutris.net/about) (_pre-installed_) for non-Steam video games.
- [**Heroic**](https://heroicgameslauncher.com/) for Epic Games, GOG, and Amazon Games integration.
- [**Zoom Platform**](https://www.zoom-platform.com/) has a built-in [Windows compatibility layer](https://zoom-platform.sh/) making use of [`umu-launcher`](https://github.com/Open-Wine-Components/umu-launcher).
- [**WineZGUI**](https://github.com/fastrizwaan/WineZGUI) (Available in Bazaar) for Windows applications that don’t require special considerations for their prefix.

>Read the [**Bazzite Gaming Guide**](/Gaming/index.md) for more information on running Windows games on Linux.

## How do I install Android applications?

Follow the [**Waydroid Setup Guide**](./Waydroid_Setup_Guide.md) to install Android applications on Bazzite.

!!! note
    Waydroid is **not supported** on other Universal Blue images like [Aurora](https://getaurora.dev/) and [Bluefin](https://projectbluefin.io/).

### Video Showcase of Installing Software

!!! note

    This video is missing a Homebrew and Quadlet walkthrough.

https://www.youtube.com/watch?v=ITuT23YrgPs

<hr>

**See also**: [Updates, Rollbacks, & Rebasing](../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md)

<-- [**View all Bazzite documentation**](../index.md)
