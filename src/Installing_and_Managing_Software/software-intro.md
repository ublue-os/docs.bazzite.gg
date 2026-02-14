---
title: Introduction to Installing Software on Bazzite
---

# Introduction to Installing Software on Bazzite

## Linux Package Formats
**Package formats ranked from most recommended to least recommended for daily usage**:

1. [**Bazzite Portal (`ujust` Commands)**](./ujust.md) (_Convenience Commands_) - Custom scripts maintained by Bazzite & Universal Blue contributors that can also install a small subset of applications. <small>(This takes precedent over other formats but since it can only install only a small set of software, it is considered as an extension to system-level settings as opposed to an app store.)</small>
2. [**Bazaar App Store (Flatpak)**](./Flatpak.md) (_Graphical Applications_) - Universal package format using a permissions-based model and should be used for most graphical applications, **it is primary method of obtaining software on Bazzite**.
3. [**Homebrew**](./Homebrew.md) (_Command-Line Tools_) - Install applications intended to run inside of the terminal (CLI/TUI).
4. [**Containers**](./Containers.md) - Run applications in an isolated environment to avoid dependency issues.
    4a. [**Distrobox Containers**](./Distrobox.md) (_Linux Packages & Development Workflows_) - Access to most Linux package managers for software that do not support Flatpak and Homebrew and for use as development boxes.
    4b. [**Quadlet**](./Quadlet.md)  (_Services_) - Run containerized applications as a [systemd service](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-managing_services_with_systemd#sect-Managing_Services_with_systemd-Services).
5. [**AppImage**](./AppImage.md) (_Portable Graphical Applications_) - Portable universal package format that relies on specific host libraries at a system-level, usually obtained from a project's website.
6. [**`rpm-ostree`**](./rpm-ostree.md) (_System-Level Packages_) - Layer Fedora packages at a system-level (**not recommended, use as a last resort**)

### Package Format Recommendation Scenarios
![Software Installation Decision Tree](../img/software-install-decision-tree-light.svg#only-light)
![Software Installation Decision Tree](../img/software-install-decision-tree-dark.svg#only-dark)
!!! note
        
        Please note that only a small selection of software are available to install in the Bazzite Portal so it is not listed in this table.

| **Package Format** | **Graphical Application (GUI)** | **Command‑Line / System‑Level Package** |
|--------------------|----------------------------------|------------------------------------------|
| **Bazaar App Store (Flatpak)** | Primary method for obtaining graphical applications. | Not recommended for command‑line applications or utilities. |
| **Homebrew** | Only a few apps (e.g., VSCode via [Universal Blue cask](https://github.com/ublue-os/homebrew-tap)) are recommended to install graphically. | Highly recommended for command‑line tools. |
| **Containers (Distrobox / Quadlet)** | If not available in Bazaar, install the generic Linux package inside a Distrobox container and export it. For services, create a Quadlet. | Recommended if a Homebrew package does not exist. |
| **AppImage** | Find an AppImage online at your own risk from a trusted source. Use Gear Lever (available in Bazaar) for proper system integration. | — |
| **Package Layering** | If none of the above options work, layer the package at your own risk. | Layer only if no other option works. |
| **Other** | Some software ships as a `.tar.gz` with an executable. It *may* run on Bazzite after making it executable in the file properties. Alternatively, use a Wine frontend (e.g., Lutris) for Windows versions. Waydroid may work if an Android port exists. | — |
| **[Custom Image](../Advanced/creating_custom_image.md)** | — | Intended for alternate desktop environments or software for unusual hardware; a custom Bazzite image may be required.  |

<hr>

## Other Software

Bazzite can also run Windows and Android applications too!  Please note that not all software intended for Windows and Android will run on Bazzite.

### Windows Executables

**Use a [WINE](https://www.winehq.org/) front-end**:

- [**Steam**](https://store.steampowered.com/) (_pre-installed_) has a Windows compatibility layer built-in.
- [**Lutris**](https://lutris.net/about) (_pre-installed_) for non-Steam PC games and non-gaming software.
- [**Faugus Launcher**](https://github.com/Faugus/faugus-launcher) (_Available in Bazaar_) as an alternative to Lutris.
- [**Heroic Games Launcher**](https://heroicgameslauncher.com/) (_Available in Bazaar_) for proper Epic Games, GOG, and Amazon Games integration.
- [**Greenlight**](https://flathub.org/en/apps/io.github.unknownskl.greenlight) (_Available in Bazaar_) for streaming Windows store games and Gamepass. <small>(**Streaming only**)</small>
- [**WineZGUI**](https://github.com/fastrizwaan/WineZGUI) (_Available in Bazaar_) for less complicated Windows applications that don’t require special considerations.

>Read the [**Bazzite Gaming Guide**](/Gaming/index.md) for more information on running Windows games on Linux.

### Android Apps

Follow the [**Waydroid Setup Guide**](./Waydroid_Setup_Guide.md) to install Android applications on Bazzite.
