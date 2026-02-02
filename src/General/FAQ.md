---
title: Frequently Asked Questions
---

# Frequently Asked Questions (FAQ)

## Who is Bazzite for?

Bazzite is for those seeking an operating system that fits one of the following criteria:

- A desktop operating system designed for gaming with inspiration from SteamOS that has fairly low maintenance in comparison to other desktop Linux operating systems.
- A proper frontend for a controller-friendly experience for couch PC gaming.
- An alternative to Windows-based handhelds where a SteamOS-like experience is preferable and SteamOS currently does not run well or is missing functionality on the handheld hardware.
- A SteamOS-like experience on SteamOS handhelds (like the Steam Deck or Lenovo Legion Go S SteamOS Edition) with newer system packages and alternate desktop environments with the same image-based OS approach for stability.

## What Bazzite image do I use?

Bazzite's [website](https://bazzite.gg/#image-picker) offers a streamlined way of selecting the correct image which will be chosen based on hardware, desktop environment, and to include Steam Gaming Mode if the hardware supports it.

Bazzite offers multiple images, but most images will be following _one of these **three variants**_:

- **Variant 1**: Bazzite images that do **not** have Steam Gaming Mode and receive automatic updates daily with gaming packages pre-installed.
- **Variant 2**: Bazzite images that automatically boot into Steam Gaming Mode (like SteamOS) and are intended for controller-oriented setups.
- **Variant 3**: Bazzite images that are intended for software development.

### 1. Desktop Edition

<sub>(**Variant 1**)</sub>

**Steam Gaming Mode is not on these specific images!**

Intended specifically for desktops and laptops with a focus on gaming which is influenced by SteamOS's Desktop Mode and the maintenance-free nature of ChromeOS. A gaming-focused Fedora Atomic Desktop (Kinoite/Silverblue) operating system.  Steam and other gaming utilities are part of the base operating system. System rollbacks available with a rock-solid stable Fedora Linux base. Most modern PC hardware should be compatible outside of specific drivers that do not work well on desktop Linux.  [Flathub](https://flathub.org/) is enabled out of the box, so all of the applications that you would find on SteamOS are available on Bazzite.  System and application updates are automatically downloaded in the background and applied on a restart by default.

### [2. Bazzite-Deck Edition](../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)

<sub>(**Variant 2**)</sub>

"**Steam Gaming Mode**" is pre-installed and its features fully functional for supported hardware. This version of Bazzite boots directly into the Steam Gaming Mode session and is intended for handhelds and couch-gaming scenarios. It also includes a Desktop Mode session. System and application updates are manually upgraded in Steam Gaming Mode and applied on a reboot.

### [3. Bazzite-DX (Developer eXperience Edition)](https://dev.bazzite.gg/)

<sub>(**Variant 3**)</sub>

A version of Bazzite that specifically caters to software development. It is not installed via an ISO; instead, you switch to it by rebasing from your current image to a Bazzite-DX image.

#### Bazzite Image Chart Example

!!! not

    This does not include all of the Bazzite images.

Verify your Bazzite image by entering this **command** in the terminal:

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

SteamOS receives package and driver updates less frequently despite the rolling release base.  Bazzite will follow Fedora's update release cycle which means early access to new graphics card driver and kernel updates in comparison to SteamOS.  Fedora Linux and Universal Blue currently supports a specific "atomic" implementation to maintain multiple images that can receive all of the same updates at once, which is unlike a derivative Linux distribution.  **The goal of Bazzite is to have an operating system ready to game after installing it**.

### What are the advantages to using Fedora Atomic Desktop as a base?

Since Bazzite is a custom Fedora Atomic Desktop image, it makes use of read-only root files for stability purposes, and is built as a [**bootable container image**](https://containers.github.io/bootable/) which has advantages such as:

- Low risk of an unbootable system
- Rollback system updates if necessary, and the ability to pin your current deployment as a backup save state without losing user data.
- Smooth upgrade process from major Fedora point releases.
- Focus on containerized applications that do not interfere with your host system.

> Check out the [**Universal Blue homepage**](https://universal-blue.org) for more information on what this project is capable of.

## Are AMD and Intel graphics card drivers pre-installed?

**Yes** and they are updated during a system upgrade when new drivers are available. It is not possible to manually update them separately as they are part of the image.

### Are Nvidia graphics card drivers pre-installed?

**Yes, on the Nvidia images** and they are updated during a system upgrade when new drivers are available. It is not possible to manually update them.
- The legacy (`-nvidia`) image supports Pascal, Maxwell, and Volta architectures (GTX 900, GTX 1000, Nvidia Titan V, GTX 750 (TI) and GTX 745).
- The modern (`-nvidia-open`) image supports every Nvidia card from the Turing architecture and newer (GTX 16 and all RTX cards).

#### Will support for much older Nvidia graphics cards be added?

There are currently no plans to support Kepler and older architectures (Most GTX 700 cards and older) since they are **no longer supported** by the upstream Nvidia drivers.
- You can still install Bazzite, using the open-source nouveau driver.
    - However, the performance and stability of this driver lags behind the official Nvidia drivers.
- It is **not possible** to manually install the proprietary Nvidia drivers for your older card in Bazzite.
-     You would need a different Linux distribution that allows for such, if you wish to use the proprietary Nvidia drivers for your GPU.

### What if I change hardware?

Most hardware changes should **not** require any manual intervention outside of the expectations from that particular hardware which would be OS-agnostic.  However, if you swap from or to a Nvidia GPU, then [rebasing](../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/brh.md) will be necessary as a manual intervention to get the appropriate graphics drivers.

## Windows games claim that my graphic drivers are outdated, but I am not sure how to update them.

![](/../img/gpu_driver_warning.png)
Windows games cannot correctly detect Linux graphics drivers.
- Because the version numbers are different between the Windows and Linux drivers, games will occasionally warn you about outdated drivers.
- **You can safely ignore any such warning.**
- [Please see here for more details.](#are-amd-and-intel-graphics-card-drivers-pre-installed)

## Does Bazzite support CSM/Legacy Boot?

No. A notification with instructions on turning off CSM will occur when the installer detects Legacy BIOS boot: ![CSM](../img/csm.webp)

## Am I able to use AMD Fluid Motion Frames?

**Yes**, but only if the game supports it. It's not available globally for every game like on Windows, but:
* There may be individual game mods or [Decky plugins](https://github.com/xXJSONDeruloXx/Decky-Framegen) that mimic similar functionality.
* If you own [Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/) on Steam, you can set up a LSFG Vulkan layer with the `ujust get-lsfg` terminal command.

## Can I change the hostname of my device?

!!! note

    Hostnames must be **under 20 characters** due to a limitation with Distrobox containers.

Edit the `/etc/hostname` file with a new hostname, save it, and reboot.

```
hostnamectl hostname <hostname>
```

## I installed Windows but Bazzite won't boot { id="windows-bootloader-override" }

Flash the Bazzite Live ISO to a thumb drive, and run the **Bazzite Bootloader Restoration Tool**.

## Can I switch to a different desktop environment on my current installation?

<sub> (Example: Swapping from KDE Plasma to GNOME or vice-versa) </sub>

It is **not recommended to switch between desktop environments** due to configuration files having different standards **which usually lead to broken installations after rebasing to a different Bazzite image with a different desktop environment installed**.

## Am I able to install _this_ desktop environment or _that_ window manager?

Make your own [custom image based off Bazzite](/Advanced/creating_custom_image.md) with the desktop environment or standalone window manager change that you want.

## What is the `:0` and `:1` in the GRUB menu at boot?

This allows users to rollback a bad system upgrade by selecting the previous deployment.

- `:0` = Current deployment/newest update
- `:1` = Previous deployment/update.

Deployments can also be pinned to rollback for future use, so `:2`, `:3`, etc. can also exist as long as you have the storage space for it.

## Why is it called Bazzite?

[Fedora Linux's Atomic Desktops](https://fedoraproject.org/atomic-desktops/) originally followed a naming scheme based on [minerals.](https://fedoraproject.org/kinoite/) Bazzite is a mineral that is known for being strong, lightweight, and is [blue](https://universal-blue.org/).

<hr>

## I have questions or concerns that cannot be answered in the documentation

!!! note

    Search for the appropriate keywords in Bazzite's documentation first before proceeding with the next steps.

We strongly urge you to [report it to the issue tracker](https://github.com/ublue-os/bazzite/issues).  Keep in mind that certain areas and topics are out of our control especially when it comes to Nvidia driver problems, game compatibility, or other problems that plague the modern day Linux desktop regardless if you're running Bazzite or another Linux operating system.
