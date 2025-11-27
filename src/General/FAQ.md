---
title: Frequently Asked Questions
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=33", "fetched_at": "2024-09-03 16:43:17.727110+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## Why is it called Bazzite?

[Fedora Linux's Atomic Desktops](https://fedoraproject.org/atomic-desktops/) originally followed a naming scheme based on [minerals.](https://fedoraproject.org/kinoite/) Bazzite is a mineral that is known for being strong, lightweight, and is colored [blue](https://universal-blue.org/).

## Who is Bazzite for?

- Individuals who desire a desktop operating system designed for gaming with inspiration from SteamOS that has fairly low maintenance in comparison to other desktop Linux operating systems.
- Individuals who want a controller-friendly experience for couch PC gaming.
- Individuals who own a [Handheld PC](../Handheld_and_HTPC_edition/Handheld_Wiki/index.md) and would prefer a SteamOS-like experience.
- Individuals who own a Steam Deck and feel limited by SteamOS and/or also desire newer system packages or alternate desktop enviornments.

## What is the difference between SteamOS and Bazzite?

Bazzite originally was developed for the Steam Deck targeting users who used their Steam Deck as their primary PC. Bazzite is a collection of custom Fedora Atomic Desktop images built with Universal Blue's tooling (with the power of [OCI](https://opencontainers.org/about/overview/)) as opposed to using an [Arch Linux](https://archlinux.org/) base with A/B updates utilizing [RAUC](https://github.com/rauc/rauc).  The main advantages of Bazzite versus SteamOS is receiving system packages in updates at a much faster rate and a choice of an alternative desktop environment.

> A list of major differences can be found in the [**SteamOS Comparison**](/General/SteamOS_Comparison.md), [**Steam Deck wiki entry**](/Handheld_and_HTPC_edition/Handheld_Wiki/Steam_Deck.md#how-similar-is-bazzite-to-steamos-on-steam-deck-hardware), and the [**Bazzite README**](https://github.com/ublue-os/bazzite/blob/main/README.md).

## What Bazzite image do I use?

Bazzite's [website](https://bazzite.gg/#image-picker) offers a streamlined way of selecting the correct image which will be chosen based on hardware, desktop environment, and to include Steam Gaming Mode if the hardware supports it.

Bazzite offers multiple images, but most images will be following _one of these **two variants**_:

- **Variant 1**: Bazzite images that do **not** have Steam Gaming Mode and receive automatic updates daily that can be viewed as a Fedora Atomic Desktop with gaming packages pre-installed.
- **Variant 2**: Bazzite images that automatically boot into Steam Gaming Mode (like SteamOS) and are intended for controller-oriented setups.

### 1. Desktop Edition

<sub>(**Variant 1**)</sub>

**Steam Gaming Mode is not on these specific images!**

Intended specifically for desktops and laptops with a focus on gaming which is influenced by SteamOS's Desktop Mode and the maintenance-free nature of ChromeOS. A gaming-focused Fedora Atomic Desktop (Kinoite/Silverblue) operating system.  Steam and other gaming utilities are part of the base operating system. System rollbacks available with a rock-solid stable Fedora Linux base. Most modern PC hardware should be compatible outside of specific drivers that do not work well on desktop Linux.  [Flathub](https://flathub.org/) is enabled out of the box, so all of the applications that you would find on SteamOS are available on Bazzite.  System and application updates are automatically downloaded in the background and applied on a restart by default.

### [2. Bazzite-Deck Edition](../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)

<sub>(**Variant 2**)</sub>

"**Steam Gaming Mode**" is pre-installed and its features fully functional for supported hardware. This version of Bazzite boots directly into the Steam Gaming Mode session and is intended for handhelds and couch-gaming scenarios. It also includes a Desktop Mode session. System and application updates are manually upgraded in Steam Gaming Mode and applied on a reboot.

#### Full Bazzite Image Chart

Verify your image by entering this **commmand**:

```
rpm-ostree status
```

!!! note

    Every Bazzite image should start with `ostree-image-signed:docker://ghcr.io/ublue-os/...`.
    <sub> The `...` is a placeholder for the actual image name which can be referenced in the chart below. </sub>

| Image                       | Desktop Environment | Steam Gaming Mode | Hardware                                 | Edition       |
| --------------------------- | ------------------- | ----------------- | ---------------------------------------- | ------------- |
| `bazzite`                   | KDE Plasma          | No                | AMD/Intel GPUs                           | Desktop       |
| `bazzite-nvidia`            | KDE Plasma          | No                | Nvidia GPUs                              | Desktop       |
| `bazzite-nvidia-open`            | KDE Plasma          | No                | Nvidia GPUs (Newer Nvidia GPUs)                             | Desktop       |
| `bazzite-gnome`             | GNOME               | No                | AMD/Intel GPUs                           | Desktop       |
| `bazzite-gnome-nvidia`      | GNOME               | No                | Nvidia GPUs                              | Desktop       |
| `bazzite-gnome-nvidia-open`      | GNOME               | No                | Nvidia GPUs (Newer Nvidia GPUs)                            | Desktop       |
| `bazzite-deck`              | KDE Plasma          | Yes               | AMD/Intel Arc GPUs                       | Bazzite-Deck |
| `bazzite-deck-nvidia`              | KDE Plasma          | Yes               | Nvidia GPUs (Newer Nvidia GPUs)                       | Bazzite-Deck |
| `bazzite-deck-nvidia-gnome`              | GNOME          | Yes               | Nvidia GPUs (Newer Nvidia GPUs)                       | Bazzite-Deck |
| `bazzite-deck-gnome`        | GNOME               | Yes               | AMD/Intel Arc GPUs                       | Bazzite-Deck |

## SteamOS is based on Arch Linux, so why use Fedora Atomic Desktop?

SteamOS receives package and driver updates less frequently despite the rolling release base.  Bazzite will follow Fedora's update release cycle which means early access to new graphics card driver and kernel updates in comparison to SteamOS.  Fedora Linux and Universal Blue currently supports a specific "atomic" implementation to maintain multiple images that can receive all of the same updates at once, which is unlike a derivative Linux distribution.  The **goal** of Bazzite is to have an operating system ready to game after installing it.

## What are the advantages to using Fedora Atomic Desktop?

Since Bazzite is a custom Fedora Atomic Desktop image, it makes use of read-only root files for stability purposes, and is built as a [**bootable container image**](https://containers.github.io/bootable/) which has advantages such as:

- Low risk of an unbootable system
- Rollback system updates if necessary, and the ability to pin your current deployment as a backup save state without losing user data.
- Smooth upgrade process from major Fedora point releases.
- Layer Fedora packages to the host that survive between updates.
- Focus on containerized applications that do not interfere with your host system.

> Check out the [**Universal Blue homepage**](https://universal-blue.org) for more information on what this project is capable of.

### How is Fedora Atomic Desktop different than Fedora Workstation?

If you're familiar with [Fedora Workstation](https://www.fedoraproject.org/workstation/) and [Fedora's Spins](https://www.fedoraproject.org/spins/), but not the Fedora Atomic Desktops paradigm then the major difference deals with obtaining a reproducable and consistent OS image, separation between installing additional software and the system, and stability between system upgrades.

#### Installing Software

There are **read-only root files** and an emphasis on installing applications as a [Flatpak](/Installing_and_Managing_Software/Flatpak.md), [Homebrew](/Installing_and_Managing_Software/Homebrew.md), or inside of a [Distrobox container](/Installing_and_Managing_Software/Distrobox.md).

>**Read more about [**obtaining software on Bazzite**](../Installing_and_Managing_Software/index.md)**.

#### Updates

Users can also rollback to a previous deployment if a system update breaks their workflow, or rebase entirely back to a stock Fedora Atomic image, [Aurora](https://getaurora.dev/), [Bluefin](https://projectbluefin.io/), or a [custom image by the community](https://universal-blue.discourse.group/t/list-of-community-created-custom-images/340). Do **not** rebase between different desktop environments.

>**Read more about how [**updates, rolling back, and rebasing works on Bazzite**](../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md)**.

## Is this another fringe Linux distribution?

Bazzite is **not** a Linux distribution in the traditional sense. Yes, it is a Linux operating system that is distributed for the public to use however it is a custom Fedora Atomic Desktop image with a recipe on top of it. Universal Blue images are a proof of concept of using containerized workflows with transactional and in-place operating system updates, and Bazzite exists by being gaming focused with inspiration from SteamOS.  Bazzite is a Fedora Atomic Desktop installation, but with the aid of Universal Blue's tooling, adds packages, services, drivers, etc. to the base image of it. Bazzite is using a new "**container-native**" approach that Fedora has been testing, and we are taking full advantage of it.  The team is utilizing the [Open Container Initiative (OCI)](https://opencontainers.org/about/overview/) to build the images, and are adding packages, services, and kernel modules to existing Fedora operating systems.

Unlike traditional Linux distributions, **most of the maintenance and security updates are done upstream** by Fedora and Universal Blue contributors while the primary Bazzite maintainers only have to focus on creating a great experience for an OS geared towards playing video games. Bazzite provides several images that all get the same additions and fixes through updates at the same time unless specified otherwise.  There can be a hypothetical scenario where everyone involved with Bazzite could stop maintaining the project at once and it will still continue to receive updates directly from upstream until the scheduled builds are broken.

**The purpose of Bazzite is to be Fedora Linux, but provide a great gaming experience out of the box while also being an alternative operating system for the Steam Deck and other handheld devices**.

## What are some of the utilities that Bazzite ships?

(_in alphabetical order_)

- [**Boxkit**](https://github.com/ublue-os/boxkit): Tool used for custom OCI Distrobox/Toolbox containers, and anything from [DaVinci Resolve](https://github.com/zelikos/davincibox) to [OBS Studio Portable](https://github.com/ublue-os/obs-studio-portable) can be accessed with this. (The software is in their own special container, so dependencies do not affect your host.)
- [**Handheld Daemon**](https://github.com/hhd-dev/hhd): Tool for configuring and managing handheld devices from gyro, LEDs, paddles, and TDP.
- [**Ptyxis**](https://devsuite.app/ptyxis/): Terminal with first-class container support.
- [**ScopeBuddy**](https://github.com/HikariKnight/ScopeBuddy): A manager script to make Gamescope easier on the Desktop.
- [**`ujust`**](../Installing_and_Managing_Software/ujust.md): Execute custom commands based on recipes.

## Is Secure Boot supported?

!!! warning

    The Steam Deck does not come with secure boot enabled and does not ship with any keys enrolled by default, so do not enable this on Steam Deck hardware unless you absolutely know what you're doing! (Steam Deck hardware only)

**Yes**, but you will have to enroll our key.  More information on enrolling the key in our [Secure Boot guide](https://universal-blue.discourse.group/docs?topic=2742).

## Are AMD, Intel, and Nvidia graphics card drivers pre-installed?

**Yes** and they are updated during a system upgrade when new drivers are available.

### What if I change hardware?

Most hardware changes should **not** require any manual intervention outside of the expectations from that particular hardware which would be OS-agnostic.  However, if you swap from or to a Nvidia GPU, then [rebasing](../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rebase_guide.md) will be necessary as a manual intervention to get the appropriate graphics drivers.

## Am I able to use AMD Fluid Motion Frames?

**Yes**, but only if the game supports it.  Not available globally for every game like on Windows however there may game mods or [Decky plugins](https://github.com/xXJSONDeruloXx/Decky-Framegen) that mimic similar functionality.

## Can I change the hostname of my device?

!!! note

    Hostnames must be **under 20 characters** due to a limitation with Distrobox containers.

Edit the `/etc/hostname` file with a new hostname, save it, and reboot.

```
hostnamectl hostname <hostname>
```
## I need a different version of Java

If its for Minecraft modding then install the [Prism Launcher](https://flathub.org/apps/org.prismlauncher.PrismLauncher) since this would not affect your host Java installation. If Java needs to be modified for development purposes then use [**Distrobox**](../Installing_and_Managing_Software/Distrobox.md). You will **not** be able to modify Java on your host at a system level.

**This also applies to other system-level packages that act as dependencies for other pieces of software or for development.**

## I installed Windows, now cant boot Bazzite { id="windows-bootloader-override" }

Flash the Bazzite Live ISO to a thumb drive, and run the **Bazzite Bootloader Restoration Tool**.

## Windows updated and grub no longer shows up

See [this](#windows-bootloader-override).

## Can I switch to a different desktop environment on my current installation?

<sub> (Example: Swapping from KDE Plasma to GNOME or vice-versa) </sub>

It is **not recommended to rebase between desktop environments** due to configuration files having different standards which usually lead to broken installations after rebasing between two different DEs.

>[**Read more about Rebasing on Bazzite**](/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rebase_guide.md).

## Am I able to install _this_ desktop environment or _that_ window manager?

Make your own [custom image based off Bazzite](/Advanced/creating_custom_image.md) with the desktop environment or standalone window manager change that you want.

## What is the `:0` and `:1` in the GRUB menu at boot?

This allows users to rollback a bad system upgrade by selecting the previous deployment.

- `:0` = Current deployment/newest update
- `:1` = Previous deployment/update.

Deployments can also be pinned to rollback for future use, so `:2`, `:3`, etc. can also exist as long as you have the storage for it.

>**See also**: [**Rolling Back System Updates**](/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rolling_back_system_updates.md)

## I have questions or concerns that cannot be answered in the documentation

!!! note

    Search for the appropriate keywords in Bazzite's documentation first before proceeding with the next steps.

Reach out to us on our [forums](https://universal-blue.discourse.group/c/bazzite/5), [Subreddit](https://www.reddit.com/r/Bazzite/) or [Discord](https://discord.gg/WEu6BdFEtp), but if it's an issue or bug you are encountering then we strongly urge you to [report it to the issue tracker](/General/reporting_bugs.md).  Keep in mind that certain areas and topics are out of our control especially when it comes to Nvidia driver problems, game compatibility, or other problems that plague the modern day Linux desktop regardless if you're running Bazzite or not.

<hr>

**See also**: [Upstream Fedora Silverblue FAQ](https://docs.fedoraproject.org/en-US/fedora-silverblue/faq/)

<-- [**View all Bazzite documentation**](../index.md)
