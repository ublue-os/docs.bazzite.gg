---
title: Comparison of Bazzite and SteamOS
---

# Comparison of Bazzite and SteamOS

## What is SteamOS?

**SteamOS** is an operating system originally designed for the Steam Deck. SteamOS is an OS for the Steam client and also features a basic desktop environment with **KDE Plasma** that allows users to e.g., install mods and emulators, but may be limited for desktop use.

## What is Bazzite?

Bazzite is a community-driven Linux gaming operating system, featuring the latest Linux drivers and a variety of flavors (**Desktop (Bazzite)**, **Handheld/HTPC (Bazzite-Deck)**, and **Developer eXperience (Bazzite-DX)**). It is based on [**Fedora Linux**](https://fedoraproject.org/) and features an [**atomic update system**](https://github.com/bootc-dev/bootc), ensuring the previous update is always available if something goes wrong.

It is also designed for daily driving, with a focus on **gaming**, **multi-media**, and **development**.  In addition, since Bazzite ships the latest drivers, you can be sure that if your device can work on Linux, then it will work in Bazzite.  Bazzite has support for **AMD**, recent **Nvidia** and **Intel** GPUs. Bazzite also works well for **Lenovo**, **Asus**, **Ayn**, **GPD**, and **OneXPlayer** handheld devices.

### Extra Enhancements on Bazzite Compared to SteamOS

- Excellent **dual-boot** support with **Windows**.
- Works on **most** x86-based handhelds: Lenovo Legion Go/S, ASUS ROG Ally/X, OneXPlayer F1/G1/X1 variants, GPD Win 4/Mini/Max, Ayn Loki, MSI Claw 1st Gen AI7+/8+, Zotac Zone, Ayaneo Air/Geek/Next, Steam Deck LCD/OLED.
- Support for tuning desktop GPUs and fans.
- **Fearless Updates**
  - You always have access to the **previous version** through the bootloader.
  - For handhelds, Bazzite will automatically rollback on the previous version after 3 failed boots.
  - A **backlog of the previous 90 days of updates** is available, and you can easily roll back to any version with a simple command or through Handheld Daemon.
- Ships the **newest software available** including the **Linux kernel**, **graphics drivers**, and [**Gamescope**](https://github.com/ValveSoftware/gamescope).
- Useful **gaming-related software**, such as **Lutris, Umu-Launcher, ProtonUp-QT, Protontricks**, and more.
- Access to the **GNOME** desktop environment as an alternative to KDE Plasma.
- Out of the box support for **virtualization** and **GPU passthrough**.
- **Android applications** can be installed with [Waydroid](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md).
- **Sunshine** is pre-installed, allowing you to easily stream your games.
- [`ujust`](/Installing_and_Managing_Software/ujust.md) convenience scripts for setting up software and tweaks such as secure boot, and additional software.
- Uses the disk format **BTRFS** with **deduplication** and **compression** (SteamOS uses **Ext4**) and supports **auto-mounting** for both **internal drives** and **SD cards**.

### Daily Driving

- System packages are updated frequently.
- Wayland is used in desktop mode, ensuring correct scaling for high-DPI displays.
- Most desktop packages follow the Fedora lifecycle, with exceptions where there is a bug, where the package is selectively withheld or fixed earlier than Fedora.

### For Developers

- Access to multiple package managers and repositories in containers using [Distrobox](https://distrobox.it).
- [Homebrew](https://brew.sh/) is pre-installed for command-line packages.
- [Layer](/Installing_and_Managing_Software/rpm-ostree.md) Fedora packages to the system which survive between system updates.
- Check out [Development](https://dev.bazzite.gg) for more information.

### Security Improvements

Bazzite supports LUKS Disk Encryption, Secure Boot, and TPM unlock of the encrypted disk. Bazzite also has [SELinux (Security Enhanced Linux)](https://www.redhat.com/en/topics/linux/what-is-selinux) enabled and pre-configured by default.

Secure Boot support is also useful for dual-booting with Windows, since it is required for certain anti-cheat software. Read more in the [**Secure Boot Guide**](/General/Installation_Guide/secure_boot.md).
