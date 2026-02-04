---
title: Installing Bazzite on Steam Deck Hardware
---

# Installing Bazzite on Steam Deck Hardware

![image|690x332](../../img/image.jpeg)

!!! Note
      
      This installation guide is for the **legacy ISO** and an updated guide for the new ISOs will be coming soon.

## Bazzite on the Steam Deck

### Status

Bazzite functions properly on the Steam Deck LCD and Steam Deck OLED models.

<hr>

## Pre-Installation

> Pre-requisites and steps before installing Bazzite.

#### Installer Requirements

!!! note

    Bazzite requires a stable internet connection with no bandwidth cap in place.

{% include 'installer_requirements.md' %}
- Optional: Physical keyboard (without one, your username will be `bazzite` and the password will be `bazzite`)

{% include 'desktop_envs.md' %}

!!! warning

    XHCI has to be set as the USB Mode for the Steam Deck for our ISO to boot! If it is set to DRD, please change it in your BIOS settings.
    More information can be found [here](https://github.com/ublue-os/bazzite/issues/808#issuecomment-1963141866).

<hr>

## Installation Guide

> The part of the guide that requires the most effort.

### 1. Download and Flash Bazzite

- Download [Bazzite](https://download.bazzite.gg) after choosing the Steam Deck ISO with our Image Picker tool.
- Flash Bazzite to your bootable medium.
- Eject drive.

### 2. Boot Installation Medium

Hold the 'Volume Down' (<kbd>-</kbd>) button and click the Power Button, and when you hear the chime, let go of both buttons, and you'll be booted into the Boot Manager.

When you get to the boot menu, select your bootable device to boot into the Bazzite installer.

### 3. Installer

!!! note "Installation without keyboard"

    If you do not have a usb physical keyboard connected, do **NOT** press "_User Creation_", since it will remove the default username and password, and you will be unable to type a username or password without a physical keyboard.

    **default user**: `bazzite`
    **default password**: `bazzite`

![Installer|690x348](../../img/uHKqd8F4nxZryfP8ebBz1DIbNVv.png)

<!--![Installer](../../img/zfpz6EXcBqQ6jxho1O9jLLSRUE9.png)-->

![Automatic drive configuration|690x497, 75%](../../img/anaconda_drive_configuration.png)

![User setup example|690x359, 75%](../../img/anaconda_user_setup.png)

- Select your language, region, keyboard layout, and time zone.
- Select the drive that Bazzite is going to be installed on.
  - Delete any partitions that you have remaining on the drive.
  - Recommended to use the automatic storage configuration.
- Optionally encrypt the drive with a password if desired.
  - **If you lose this password, then it cannot be decrypted**.
  - **A PHYSICAL WIRED KEYBOARD IS REQUIRED TO UNLOCK THE DEVICE!**
- Setup a user account. (If you do not have a physical, skip this step and begin the installation)
  - Give administrative privileges and **set a user password**.
- Begin the installation.
- Reboot device after it has finished installing.

## Post-Installation

> The fine tuning before gaming.

### GRUB Menu

![Rollbacks|690x402, 50%](../../img/GRUB_Menu.png)

The first boot will show a screen showing your current and last deployment. It is important to note that the GRUB menu can be used to rollback Bazzite deployments if you encounter issues.

Read more about this in the [Updates, Rollback, and Rebasing documentation](../../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md).

### Login to Steam & Reboot Device

Login to Steam then **reboot** your device when you finish setting up your device during the first-boot process.

#### Setting Up Steam Gaming Mode

![Gaming Mode Setup|690x442, 50%](../../img/pLvHB1NAMlb3ghsR72q7l9Auj8B.jpeg)

After completing all of the above, then your next boot will be in Steam Gaming Mode which requires additional setup for Steam.

> [Read further information about Steam Gaming Mode][Steam_Gaming_Mode]

### Configuring System Settings for KDE Plasma and GNOME

![Display Settings (KDE Plasma)|690x370, 75%](../../img/KDE_Display_Settings.png)
**_KDE Plasma's System Settings application_**

![Display Settings (GNOME)|690x344, 75%](../../img/GNOME_Display_Settings.png)
**_GNOME's Settings application_**

It is important to configure the system settings on a first boot to personalize your desktop especially if you notice the scaling is incorrect on first-boot.

### Installing Additional Software

The [Installing and Managing Applications documentation](../../Installing_and_Managing_Software/index.md) is useful to learn how to install additional software on Bazzite.


### Changing Default Password
<sub> (If it wasn't changed in the installer) </sub>

![KDE Plasma's Change Password|584x500, 75%](../../img/change-pass.png)

Change it in the settings of Desktop Mode under the "User" category.

### Calculating ISO SHA256 Checksum Hash

https://www.youtube.com/watch?v=wUDbMJtR1sM

<hr>

## Issues Installing Bazzite?

View the [Installation Troubleshoot Guide](./troubleshoot_guide.md).

<hr>

**See also:** [Upstream Manual Partitioning Guide](https://docs.fedoraproject.org/en-US/fedora-silverblue/installation/#manual-partition) & [Steam Gaming Mode][Steam_Gaming_Mode]

<-- [**View all Bazzite documentation**](../../index.md)

[Steam_Gaming_Mode]: ../../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md
