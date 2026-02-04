---
title: Installing Bazzite on Handheld Hardware
---

# Installing Bazzite for Handheld Hardware

![ASUS ROG Ally|690x301](../../img/ASUS_ROG_Ally.jpeg)

!!! Note
      
      This installation guide is for the **legacy ISO** and an updated guide for the new ISOs will be coming soon.

## Important Notes on Handheld Hardware

!!! attention

    Several handhelds require BitLocker to be unlocked (write down your recovery key too), Windows "Fast Startup" disabled, and **not** putting Windows into Hibernation Mode before installing Bazzite.


> [Bazzite's Handheld Wiki](/Handheld_and_HTPC_edition/Handheld_Wiki/) contains information on setting up your handheld after installing Bazzite and workarounds for known issues.

<hr>

## Pre-Installation

> Pre-requisites and steps before installing Bazzite.

#### Installer Requirements

!!! note

    Bazzite requires a stable internet connection with no bandwidth cap in place.

{% include 'installer_requirements.md' %}
- Optional: Physical keyboard (without one, your username will be `bazzite` and the password will be `bazzite`)

#### Steam Gaming Mode Requirements

- Compatible graphics card
  - A **modern AMD GPU**
  - An **Intel Arc GPU** (Other Intel GPU series will not boot Steam Gaming Mode)
    - Intel Arc handhelds will currently have missing functionality (TDP limit, controls, etc.)

Handheld users will also benefit from also reading the [Steam Gaming Mode documentation][Steam_Gaming_Mode].

{% include 'desktop_envs.md' %}

### Dual Boot Preliminary Setup + Post-Setup Guide

Read the [Dual Boot Guide](https://universal-blue.discourse.group/docs?topic=2743) **after** reading this guide first before proceeding.

<hr>

## Installation Guide

> The part of the guide that requires the most effort.

### 1. Download and Flash Bazzite

- Download [Bazzite](https://download.bazzite.gg) after choosing the correct handheld hardware with our Image Picker tool.
- Flash Bazzite to your bootable medium.
- Eject drive.

### 2. Boot Installation Medium

You may need to research your handheld on how to boot from removable storage. It may be similar to the Steam Deck with holding down one of the "volume buttons" and pressing another button, but like for other general hardware, it highly dependent on your hardware.

### 3. Installer Setup

> **NOTE**: If you do not have a physical wired keyboard connected, do **NOT** press “_User Creation_”, as it will remove the default username and password, and you will be unable to type a username or password without a physical keyboard.

> **default user**: `bazzite` > **default password**: `bazzite`

![Installer|690x348](../../img/uHKqd8F4nxZryfP8ebBz1DIbNVv.png)

<!--![Installer](../../img/zfpz6EXcBqQ6jxho1O9jLLSRUE9.png)--!

<!--
![Automatic Partitioning|690x359](../../img/83958112b4d1d96874868fa33f889bfd0162da9a.png)-->

![User setup example|690x359, 100%](../../img/anaconda_user_setup.png)

- Select your language, region, keyboard layout, and time zone.
- Select the drive that Bazzite is going to be installed on.
  - Delete any partitions that you have remaining on the drive **unless [dual booting on the same drive](/General/Installation_Guide/dual_boot_setup_guide/#b-same-drive-method)**.
  - If **[dual booting on the same drive](/General/Installation_Guide/dual_boot_setup_guide/#manual-partitioning-to-the-same-drive-for-dual-boot-setups)**, it is **strongly recommended** to do manual partitioning and create a separate EFI partition.
    - The separate EFI partition will help prevent Windows Updates from affecting your Bazzite installation later down the line.
  - Only use the automatic storage configuration when installing to separate drives
- Optionally encrypt the drive with a password if desired.
  - **If you lose this password, then it cannot be decrypted**.
  - **A PHYSICAL WIRED KEYBOARD IS REQUIRED TO UNLOCK THE DEVICE!**
- Setup a user account and begin the installation. (If you do not have a physical keyboard, skip this step and begin the installation)
  - Give administrative privileges and set a user password. (**required**)
- Begin the installation.
- Reboot device after it has finished installing.

#### Important information for users with Secure Boot **enabled**:

Read the [Secure Boot Guide](https://universal-blue.discourse.group/docs?topic=2742).

<hr>

## Post-Installation

> The fine tuning before gaming.

### GRUB Menu

![Rollbacks|690x402, 50%](../../img/GRUB_Menu.png)

The first boot will show a screen showing your current and last deployment. It is important to note that the GRUB menu can be used to rollback Bazzite deployments if you encounter issues.

Read more about this in the [Updates, Rollback, and Rebasing documentation](../../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md).

### Login to Steam & Reboot Device

Login to Steam then **reboot** your device when you finish setting up your device during the first-boot process.

![Steam Gaming Mode Setup|690x442, 50%](../../img/pLvHB1NAMlb3ghsR72q7l9Auj8B.jpeg)

After completing all of the above, then your next boot will be in Steam Gaming Mode which requires additional setup for Steam.

### Configuring System Settings for KDE Plasma and GNOME

![Display Settings (KDE Plasma)|690x370, 75%](../../img/KDE_Display_Settings.png)
**_KDE Plasma's System Settings application_**

![Display Settings (GNOME)|690x344, 75%](../../img/GNOME_Display_Settings.png)
**_GNOME's Settings application_**

After you have booted into the Desktop for the first-time configuration, then you can should adjust the settings to your liking. The most important setting that may need to be changed is the scaling setting in "Display(s) [and Monitor]" since it can be incorrect for the screen of your hardware on a fresh installation. Monitor orientation should also be corrected if it is rotated improperly.

### Installing Additional Software

The [Installing and Managing Applications documentation](../../Installing_and_Managing_Software/index.md) is useful to learn how to install additional software on Bazzite.

### Changing Default Password
<sub> (If it wasn't changed in the installer) </sub>

![KDE Plasma's Change Password|584x500, 75%](../../img/change-pass.png)

Change it in the settings of Desktop Mode under the "User" category.

### Post-Setup and Known Issues for Handhelds and Steam Gaming Mode

Read the [Handheld Wiki](https://universal-blue.discourse.group/docs?topic=1038) and [Steam Gaming Mode Overview documentation][Steam_Gaming_Mode] for information regarding Bazzite on handheld PCs.

### Calculating ISO SHA256 Checksum Hash

https://www.youtube.com/watch?v=wUDbMJtR1sM

<hr>

## **Video Tutorial**

!!! attention

    We strongly recommend **manual partitioning + creating a separate EFI partition** for dual-booting, **not** automatic partitioning.  See instructions for manual partitioning [here](/General/Installation_Guide/dual_boot_setup_guide/#manual-partitioning-to-the-same-drive-for-dual-boot-setups). The separate EFI partition will help prevent Windows Updates from affecting your Bazzite installation later down the line.

https://www.youtube.com/watch?v=JxPsKhJGTrs

<hr>

## Issues Installing Bazzite?

View the [Installation Troubleshoot Guide](./troubleshoot_guide.md).

<hr>

**See also:** [Upstream Manual Partitioning Guide](https://docs.fedoraproject.org/en-US/fedora-silverblue/installation/#manual-partition) & [Steam Gaming Mode][Steam_Gaming_Mode]

<-- [**View all Bazzite documentation**](../../index.md)

[Steam_Gaming_Mode]: ../../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md
