# Comparison of Bazzite vs SteamOS

## What is Bazzite?

Bazzite is the largest community-driven Linux gaming operating system, featuring the latest Linux drivers, rich documentation, a large community, and a variety of flavors (**DX**, **Gnome**, **KDE**, and **Deck**). It is based on **Fedora** and features an atomic update system ([bootc](https://github.com/bootc-dev/bootc)), ensuring the previous update is always available if something goes wrong. It is also designed for daily driving, with a focus on **gaming** and **development**.  In addition, since Bazzite ships the **latest drivers**, you can be sure that if your device **can work** on Linux, then **it will work in Bazzite**.  Bazzite has great support for **AMD**, and decent support for recent **Intel Arc** (e.g., **MSI Claw**) and **Nvidia GPUs**. Bazzite also works well for **Lenovo**, **Asus**, **Ayn**, **GPD**, and **OneXPlayer** handheld devices.

## What is SteamOS?

**SteamOS** is an operating system originally designed for the Steam Deck. Much like ChromeOS is an OS for Chrome, SteamOS is an OS for the Steam client. It also features a basic desktop environment with **KDE**, **X11** that allows users to e.g., install mods and emulators, but may be limiting for desktop use.

In addition, due to its development model, it usually contains packages that are **1-2 years old**. For example, SteamOS 3.6 released with kernel 6.5 in October 2024, and was in service until May 2025. Kernel 6.5 released in August 2023, so on the 3.6 release day, the kernel was 14 months old and when it expired in May 2025, it was 21 months old.  This means that if you are excited to buy a new device and plop SteamOS on it, you will usually have to **wait a year** for it to update.

### Extra Features

- Access to both **KDE** and **Gnome** desktop environments
- Excellent **dual-boot** support with **Windows**.
- Works on **all** x86-based handhelds: **Legion Go/S, ROG Ally/X, OneXPlayer F1/G1/X1 variants, GPD Win 4/Mini/Max, Ayn Loki, MSI Claw 1st Gen AI7+/8+, Steam Deck LCD/OLED, Zotac Zone, Ayaneo Air/Geek/Next**.
- Support for **LACT** and **Cooler Control**, for tuning **desktop GPUs** and **fans**.
- **Fearless Updates**
  - You always have access to the **previous version** through the bootloader.
  - For handhelds, Bazzite **will automatically rollback** on the previous version after 3 failed boots.
  - A **backlog of the previous 90 days of updates** is available, and you can easily roll back to any version with a simple command or through Handheld Daemon.
- Ships the **newest software available**, along with Fedora, including **optimized** versions of the **Linux kernel**, **Mesa graphics drivers**, and **gamescope**.
- Useful **gaming-related software**, such as **Lutris, Umu-Launcher, ProtonUp-QT, Protontricks**, and more.
- Out of the box support for **virtualization** and **GPU passthrough**.
- **Android** applications can be installed with [Waydroid](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md) which is pre-installed.
- **Sunshine** is pre-installed, allowing you to easily stream your games.
- [`ujust`](/Installing_and_Managing_Software/ujust.md) convenience scripts for setting up software and tweaks such as secure boot, and additional software.
- Uses the disk format **btrfs** with **deduplication** and **compression** (SteamOS uses **ext4**) and supports **auto-mounting** for **internal drives** and **SD cards**.

### Daily Driving

- System packages are updated frequently.
- Wayland is used in desktop mode, ensuring correct scaling for high-DPI displays.
- Most desktop packages follow the Fedora lifecycle, with exceptions where there is a bug, where the package is selectively withheld or fixed earlier than Fedora.

### For Developers

- Access to multiple package managers and repositories in [containers](/Installing_and_Managing_Software/Distrobox.md).
- [Homebrew](https://brew.sh/) is pre-installed for command-line packages.
- [Layer](/Installing_and_Managing_Software/rpm-ostree.md) Fedora packages to the system which survive between system updates.
- Host software as services using [Quadlet](/Installing_and_Managing_Software/Quadlet.md).
- Check out [Development](/Dev/index.md) for more information.

### Security Improvements

Bazzite supports LUKS Disk Encryption, Secure Boot, and TPM unlock of the encrypted disk. Bazzite also has [SELinux (Security Enhanced Linux)](https://www.redhat.com/en/topics/linux/what-is-selinux) enabled and pre-configured by default.

Secure Boot support is also useful for dual-booting with Windows, since it is required for certain anti-cheat software. Read more in [Secure Boot](/General/Installation_Guide/secure_boot.md).

### Performance Improvements

Due to the use of latest drivers, Bazzite will have **better performance** than SteamOS on **recent devices**. For the devices that SteamOS works well on (i.e., the **Steam Deck** and **2+ year old AMD PCs**), due to their age, the performance difference is negligible.
