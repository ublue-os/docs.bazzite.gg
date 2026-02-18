---
title: Bazzite Installation Guide
---

# Bazzite Installation Guide

## Video Walkthrough

<link Wolfyreload's video>

## System Requirements

- Read the [**Hardware Compatibility Guide**](<link doc>) for Bazzite's system requirements.
- Secure Boot and Trusted Platform Module (TPM) are supported on most hardware, but you must [**enroll our key during or after installation**](./secure_boot.md).

### Installer Requirements

- A way to download the Bazzite ISO
  - A download manager (like [**Motrix**](https://motrix.app/)) if the direct download for the Bazzite ISO fails or is downloading too slow.
- A 16GB+ bootable medium like a Flash Drive
  - Software to flash the ISO like **Fedora Media Writer** ([**Windows/macOS**](https://github.com/FedoraQt/MediaWriter/releases) or [**Linux**](https://flathub.org/en/apps/org.fedoraproject.MediaWriter))
- A physical wired keyboard is **recommended** and **required for devices without a touchscreen**.
  - Otherwise, create a User Account with a **username** and a **user password** if you have a keyboard.

### Desktop Environments

All of the images come with the choice of [KDE Plasma](https://kde.org/plasma-desktop/) or
[GNOME](https://www.gnome.org/) for their desktop environment.

[Steam Gaming Mode](https://github.com/KyleGospo/gamescope-session) is an option and is recommended for HTPC setups.

More information can be found on our [FAQ](https://faq.bazzite.gg) about the differences between the image variants.

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
    - Choice of KDE Plasma or GNOME in Desktop Mode
    - Extra functionality with [Decky](https://github.com/SteamDeckHomebrew/decky-loader) [plugins](https://plugins.deckbrew.xyz/)

    {% endblock %}


## Installation Walkthrough

### Download Bazzite

<screenshot of Bazzite's website on download page>

### Flash ISO

<screenshot of Fedora Media Writer settings>

### Booting The Installer

<screenshot of Bazzite installer first-boot black screen in GRUB>

#### Network 

<screenshot of live ISO connecting to Wi-Fi symbol on KDE image>

#### Select Language, Region, and Keyboard Layout

<screenshot installer>

#### Partitioning Options

!!! warning

    Make sure to only select the appropriate drives to avoid losing data on others, and it is best practice to safely remove any external drives before proceeding.

If you are dual-booting with Windows then read the [dualbooting guide](<link guide>).  Automatic partitioning is the only option available in the live ISO, but it should work for most people's dual-booting usecases.  If you require manual partitioning, then use the legacy ISO and follow the [manual partitioning guide](<link this>).

#### User Account Setup

<screenshot of installer>

#### Reboot

## Post-Installation

<link guide>
