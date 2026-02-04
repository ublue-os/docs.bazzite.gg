---
title: Installing Bazzite for HTPC Hardware
---

# Installing Bazzite for HTPC Hardware

![HTPC|609x371](../../img/HTPC.png)

!!! Note
      
      This installation guide is for the **legacy ISO** and an updated guide for the new ISOs will be coming soon.

## Pre-Installation

> Pre-requisites and steps before installing Bazzite.

### Minimum System Requirements

- **Architecture**: x86_64
- **Firmware**: UEFI (CSM/Legacy boot [**UNSUPPORTED**](../FAQ.md#does-bazzite-support-csmlegacy-boot))
- **Processor (CPU)** : 2GHz quad core processor or better
- **System Memory (RAM)**: 8GB
- **Graphics**: A graphics card that can utilize Vulkan 1.3+
- **Storage**: 64GB free on an internal solid-state drive
- **Network**: Stable internet connection with no bandwidth caps
- **Additional Notes**: Certain drivers are **not** compatible with Bazzite
  - For example: [A list of compatible USB Wi-Fi adapters](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md)

#### Steam Gaming Mode Requirements

- A modern AMD GPU
  - Intel Arc GPUs may work with **minor caveats**
  - Nvidia GPUs are currently in beta with **major caveats**
- [Steam](https://store.steampowered.com/) account

#### Installer Requirements

{% include 'installer_requirements.md' %}
- Physical keyboard

{% include 'desktop_envs.md' %}

## Installation Guide

> The part of the guide that requires the most effort.

### 1. Download and Flash Bazzite

- Download [Bazzite](https://download.bazzite.gg) after choosing the correct ISO for your hardware with our Image Picker tool.
- Flash Bazzite to your bootable medium.
- Eject drive.

#### Current Fedora Atomic Desktop Users

Current [Fedora Atomic Desktop](https://fedoraproject.org/atomic-desktops/) users can rebase with the terminal command listed on the website under the "Existing Fedora Atomic Desktop Users" section and can skip the next step.

### 2. Boot Bazzite

- Connect your bootable medium to your device and boot into it.
- After connecting the device, boot into the Bazzite installer.
- This depends on your motherboard hardware, but most of the time it could be a function keys like <kbd>F9</kbd> or similar.
  - Sometimes you need to consult the manual, look up your device online, or read any hotkeys that appear when you boot your PC.
    - Alternatively change the BIOS settings to boot with your bootable device first before your current storage, but this is **not recommended** to keep enabled after installing Bazzite.
- Verify the media correctly and proceed to the installer.

### Dual Boot Preliminary Setup + Post-Setup Guide

Read the [Dual Boot Guide](https://universal-blue.discourse.group/docs?topic=2743) **after** reading this guide before proceeding.

### 3. Installer

![Installer](../../img/anaconda_installer.png)

![Automatic drive configuration|690x497, 75%](../../img/anaconda_drive_configuration.png)

![User setup example|690x359, 75%](../../img/anaconda_user_setup.png)

- Select your language, region, keyboard layout, and time zone.
- Select the drive that Bazzite is going to be installed on.
  - Delete any partitions that you have remaining on the drive **unless dual booting on the same drive**.
  - Recommended to use the automatic storage configuration **unless dual booting on the same drive**.
- Optionally encrypt the drive with a password if desired.
  - **If you lose this password, then it cannot be decrypted**.
  - **A PHYSICAL WIRED KEYBOARD IS REQUIRED TO UNLOCK THE DEVICE!**
- Setup a user account.
  - Give administrative privileges and **set a user password**.
- Begin the installation.
- Reboot device after it has finished installing.

#### Important information for users with Secure Boot **enabled**:

Read the [Secure Boot Guide](https://universal-blue.discourse.group/docs?topic=2742) for more information.

<hr>

## Post-Installation

> The fine tuning before gaming.

### GRUB Menu

![Rollbacks|690x402, 50%](../../img/GRUB_Menu.png)

The first boot will show a screen showing your current and last deployment.  It is important to note that the GRUB menu can be used to rollback Bazzite deployments if you encounter issues.

Read more about this in the [Updates, Rollback, and Rebasing documentation](../../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md).

### Login to Steam & Reboot Device

Login to Steam then **reboot** your device when you finish setting up your device during the first-boot process.

#### Setup Steam Gaming Mode

![Steam Gaming Mode Setup|690x442, 50%](../../img/pLvHB1NAMlb3ghsR72q7l9Auj8B.jpeg)

After completing all of the above, then your next boot will be in Steam Gaming Mode which requires additional setup for Steam.

> [Read further information about Steam Gaming Mode][Steam_Gaming_Mode].

### Configuring System Settings for KDE Plasma and GNOME

![Display Settings (KDE Plasma)|690x370, 75%](../../img/KDE_Display_Settings.png)
**_KDE Plasma's System Settings application_**

![Display Settings (GNOME)|690x344, 75%](../../img/GNOME_Display_Settings.png)
**_GNOME's Settings application_**

It is important to configure the system settings on a first boot to personalize your desktop especially if you notice the scaling is incorrect on your first boot.

### Installing additional software

The [Installing and Managing Applications documentation](../../Installing_and_Managing_Software/index.md) is useful to learn how to install additional software on Bazzite.

### Calculating ISO SHA256 Checksum Hash

https://www.youtube.com/watch?v=wUDbMJtR1sM

<hr>

## Issues Installing Bazzite?

View the [Installation Troubleshoot Guide](./troubleshoot_guide.md).

<hr>

**See also:** [Upstream Manual Partitioning Guide](https://docs.fedoraproject.org/en-US/fedora-silverblue/installation/#manual-partition) & [Steam Gaming Mode Overview][Steam_Gaming_Mode]

<-- [**View all Bazzite documentation**](../../index.md)

[Steam_Gaming_Mode]: ../../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md
