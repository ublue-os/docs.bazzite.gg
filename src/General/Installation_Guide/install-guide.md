---
title: Bazzite Installation Guide
---

# Bazzite Installation Guide

## Video Walkthrough

<link Wolfyreload's video>

## System Requirements

- Read the [**Hardware Compatibility Guide**](./Gaming/Hardware_compatibility_for_gaming.md) for Bazzite's system requirements.
- **Secure Boot and Trusted Platform Module (TPM) are supported on most hardware**, but you must **enroll our key during or after installation**.

### Installer Requirements

- A way to download the Bazzite ISO
  - A download manager (like [**Motrix**](https://motrix.app/)) if the direct download for the Bazzite ISO fails or is downloading too slow.
- A 16GB+ bootable medium like a Flash Drive
  - Software to flash the ISO like **Fedora Media Writer** ([**Windows/macOS**](https://github.com/FedoraQt/MediaWriter/releases) or [**Linux**](https://flathub.org/en/apps/org.fedoraproject.MediaWriter))
- A physical wired keyboard is **recommended** and **required for devices without a touchscreen**.
  - Otherwise, create a User Account with a **username** and a **user password** if you have a keyboard.

### Desktop Environments

All of the images come with the choice of [**KDE Plasma**](https://kde.org/plasma-desktop/) or
[**GNOME**](https://www.gnome.org/) for their desktop environment.

[**Steam Gaming Mode**](https://github.com/KyleGospo/gamescope-session) is an option as an additional session to run on top of KDE Plasma or GNOME but is only recommended for Home Theatre PC (HTPC) and handheld setups.

More information can be found on our [**FAQ**](https://faq.bazzite.gg) about the differences between the image variants.

=== "KDE Plasma"

    #### [KDE Plasma (Default)](https://kde.org/plasma-desktop/)

    ![KDE Plasma|690x388, 75%](/img/KDE_Plasma_DE.jpeg)

    - KDE Plasma's default interface has a traditional and familiar layout
    - Highly customizable with tons of settings
    - Qt framework
    - Popular Linux distributions like SteamOS use KDE Plasma

=== "GNOME"

    #### [GNOME (`-gnome` images)](https://www.gnome.org/)

    ![GNOME|690x359, 75%](/img/GNOME_DE.png)

    - GNOME's default interface has an elegant and touch-friendly layout
    - Simple and concise
    - GTK framework
    - Popular Linux distributions like Ubuntu use GNOME

=== "Steam Gaming Mode"

    #### [Steam Gaming Mode (`-deck` images)](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)

    ![Gaming Mode|690x388, 75%](/img/Gaming_Mode.jpeg)

    !!! note

        Your device will automatically boot into the Steam Gaming Mode session at startup, and Desktop Mode can be accessed from the "**power menu**" in Steam Gaming Mode.

    {% block desktop_envs_steam_notes %}

    - **Requires a [Steam](https://store.steampowered.com/) account**
    - Included in the [Bazzite-Deck images](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)
    - Interface is designed for handheld and couch gaming
    - Controller friendly
    - Choice of KDE Plasma or GNOME as the Desktop Mode session
    - Extra functionality with [Decky plugins](https://github.com/SteamDeckHomebrew/decky-loader) [(See all plugins)](https://plugins.deckbrew.xyz/)

    {% endblock %}


## Installation Walkthrough

### Download Bazzite

![download|1871x856, 60%](../../img/live-installer-download.png)

<explain what each of these buttons mean for more context>

Download the Bazzite ISO of your choice. Choose the hardware you plan to install Bazzite on, the vendor of your primary GPU, the desktop environment of your choice, and if you want Steam Gaming Mode (Bazzite-Deck version of Bazzite intended for HTPC and handheld hardware).

### Calculating ISO SHA256 Checksum Hash

https://www.youtube.com/watch?v=wUDbMJtR1sM

### Flash ISO

![flash|771x623, 70%](../../img/live-installer-fedora-media-writer-1.png)
![flash|771x723, 70%](../../img/live-installer-fedora-media-writer-2.png)


### Booting The Installer

- Connect your bootable medium to your device and boot into it.
- After connecting the device, boot into the Bazzite installer.
- This depends on your motherboard hardware, but most of the time it could be a function keys like <kbd>F9</kbd> or similar.
  - Sometimes you need to consult the manual, look up your device online, or read any hotkeys that appear when you boot your PC.
    - Alternatively change the BIOS settings to boot with your bootable device first before your current storage, but this is **not recommended** to keep enabled after installing Bazzite.
- Verify the media correctly and proceed to the installer.

#### Handheld Devices

Hold the 'Volume Down' (<kbd>-</kbd>) button and click the Power Button, and when you hear the chime, let go of both buttons, and you'll be booted into the Boot Manager. When you get to the boot menu, select your bootable device to boot into the Bazzite installer.

#### GRUB Menu

![boot|1573x872, 50%](../../img/live-installer-grub.png)

#### Live Installer

![live|1431x897, 60%](../../img/live-installer-opening.png)



#### Network 

![network|495x593, 100%](../../img/live-installer-network.png)

Please note that an internet is not required to install Bazzite, but is useful if you're testing Bazzite before testing in the live environment.

#### Select Language, Region, and Keyboard Layout

![installer1|1295x1054, 62%](../../img/live-installer-language.png)

![installer1|1295x1054, 62%](../../img/live-installer-time-date.png)

#### Partitioning Options

!!! warning

    Make sure to only select the appropriate drives to avoid losing data on others, and it is best practice to safely remove any external drives before proceeding.

##### Dual Booting

!!! note

     The "format as efi" button when dual-booting says it will format the Windows EFI, but what it actually does is add itself to the EFI. This is an upstream bug with the installer.

If you are dual-booting with Windows then read the [dualbooting guide](<link guide>).  Automatic partitioning is the only option available in the live ISO, but it should work for most people's dual-booting usecases.  If you require manual partitioning, then use the legacy ISO and follow the [manual partitioning guide](<link this>).

^^^this should be a comment but maybe just have dualboot guide here and have the other one be the legacy one? idk.... ahhhhhhh... maybe secure boot guide should part of this too?

##### Disk Encryption

#### User Account Setup

![installer2|1288x1050, 62%](../../img/live-installer-user-setup.png)

!!! warning

    It is not recommended to enable a root account.

### Installing Bazzite

Please wait for Bazzite to install.  This may take a while.

![installing|1282x1036, 63%](../../img/live-installer-installing.png)


#### Reboot

![reboot|1288x1040, 62%](../../img/live-installer-installed.png)

## Secure Boot

## Post-Installation

Bazzite is now installed. Read the [**Post-Installation Guide**](<link guide>) for recommended next steps or start gaming!

--- other images (fix resolutions and scaling BEFORE moving them!)

![installing|1283x1042, 62%](../../img/live-installer-partitions.png)
![installing|1773x1247, 52%](../../img/live-installer-dualboot.png)
![installing|1273x1038, 63%](../../img/live-installer-drive.png)
![installing|1284x1045, 62%](../../img/live-installer-storage-encryption.png)


