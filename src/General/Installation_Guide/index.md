---
title: Bazzite Installation Guide
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=30", "fetched_at": "2024-09-03 16:43:25.704918+00:00"}-->
<!-- ANCHOR_END: METADATA -->


## Minimum System Requirements

- **Architecture**: x86_64
- **Firmware**: UEFI (CSM Support should be **disabled** if available)
- **Processor (CPU)** : 2GHz quad core processor or better
- **System Memory (RAM)**: 4GB
- **Graphics**: A graphics card that can utilize Vulkan 1.3 or higher, modern AMD GPUs work the best
- **Storage**: 64GB free on an internal **solid-state drive (SSD)**
  - **External Storage & Secondary Drives**: All drives must be formatted as **BTRFS (SSDs)** or **Ext4 (Hard Disk Drives [HDDs])**, please backup the files and reformat them post-installation. 
- **Network**: Stable internet connection with no bandwidth caps
- **Additional Notes**: Certain peripherals are **not** compatible with Bazzite:
  - **Wi-Fi Adapter Example** - [a list of **known compatible** USB Wi-Fi adapters](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md)

>[**The Hardware for Linux website**](https://linux-hardware.org/?view=computers) is a good indicator for how well OEM hardware is supported on the Linux desktop.

## Steam Gaming Mode Requirements

!!! note

    These specific requirements only apply to [Bazzite-Deck images](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md) which ships with all handheld Bazzite ISO downloads.

- Modern AMD GPU
  - RX 4xx series and up
    - 600M/700M integrated GPUs are also supported
- Intel Arc GPUs are supported with **minor caveats** compared to AMD hardware
- Nvidia GPU support is supported with [**major caveats**](/Handheld_and_HTPC_edition/quirks/#nvidia-exclusive-issues) compared to AMD hardware out of control of the Bazzite maintainers
- Requires a [**Steam**](https://store.steampowered.com/) account
  - Signing up for an account can be done post-installation if you don't have one already

## Installer Requirements

- Software to flash the ISO like [**Fedora Media Writer**]()
- A physical wired keyboard is **recommended** and **required for devices without a touchscreen**.
  - A User Account with a **username** and a **user password** if you have a keyboard if you want to setup a unique username and a password. 

## Secure Boot Information

Secure Boot is supported on most hardware, but you must [**enroll our key**](./secure_boot.md).

<explain that it might be better to turn it off before proceeding>

## Installing Bazzite

https://www.youtube.com/watch?v=KAt49B6rSFI

1. Download and Flash Bazzite

- Download [Bazzite](https://download.bazzite.gg) after choosing the correct ISO for your hardware with our Image Picker tool.
- Flash Bazzite to your bootable medium.
- Eject drive.

### Calculating ISO SHA256 Checksum Hash

https://www.youtube.com/watch?v=wUDbMJtR1sM

### 2. Boot Bazzite

- Connect your bootable medium to your device and boot into it.
- After connecting the device, boot into the Bazzite installer.
- This depends on your motherboard hardware, but most of the time it could be a function keys like <kbd>F9</kbd> or similar.
  - Sometimes you need to consult the manual, look up your device online, or read any hotkeys that appear when you boot your PC.
    - Alternatively change the BIOS settings to boot with your bootable device first before your current storage, but this is **not recommended** to keep enabled after installing Bazzite.
- Verify the media correctly and proceed to the installer.

#### Handheld Users

Hold the 'Volume Down' (<kbd>-</kbd>) button and click the Power Button, and when you hear the chime, let go of both buttons, and you'll be booted into the Boot Manager. When you get to the boot menu, select your bootable device to boot into the Bazzite installer.

### 3. Inside the Installation Medium

!!! note "Installing Bazzite without a physical keyboard connected to your device:"

    If you do not have a usb physical keyboard connected, do **NOT** press "_User Creation_", since it will remove the default username and password, and you will be unable to type a username or password without a physical keyboard.

    **default user**: `bazzite`
    **default password**: `bazzite`

![Automatic drive configuration|690x497, 75%](../../img/anaconda_drive_configuration.png)

![User setup example|690x359, 75%](../../img/anaconda_user_setup.png)

- Select your language, region, keyboard layout, and time zone.
- Select the drive that Bazzite is going to be installed on.
  - Delete any partitions that you have remaining on the drive **unless dual booting on the same drive**.
  - Recommended to use the automatic storage configuration **unless dual booting on the same drive**.
- Optionally encrypt the drive with a password if desired.
  - **If you lose this password, then it cannot be decrypted**.
  - A PHYSICAL WIRED KEYBOARD IS REQUIRED TO UNLOCK THE DEVICE!
- Setup a user account.
  - Give administrative privileges and **set a user password**.
- Begin the installation.
- Reboot device after it has finished installing.

## Post-Installation

![Rollbacks|690x402, 50%](../../img/GRUB_Menu.png)

The first boot will show a screen showing your current and last deployment. It is important to note that the GRUB menu can be used to rollback Bazzite deployments if you encounter issues.

Read more about this in the [Updates, Rollback, and Rebasing documentation](../../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md).

### Setting Up Steam Gaming Mode (Bazzite-Deck Only)

![Gaming Mode Setup|690x442, 50%](../../img/pLvHB1NAMlb3ghsR72q7l9Auj8B.jpeg)

After completing all of the above, then your next boot will be in Steam Gaming Mode which requires additional setup for Steam.

> [Read further information about Steam Gaming Mode][Steam_Gaming_Mode]

### Configuring System Settings for KDE Plasma and GNOME

![Display Settings (KDE Plasma)|690x370, 75%](../../img/KDE_Display_Settings.png)
**_KDE Plasma's System Settings application_**

![Display Settings (GNOME)|690x344, 75%](../../img/GNOME_Display_Settings.png)
**_GNOME's Settings application_**

It is important to configure the system settings on a first boot to personalize your desktop especially if you notice the scaling is incorrect on first-boot.

### Secondary Storage Filesystems

!!! note

    Bazzite will automatically mount secondary drives that are formatted as Ext4 or BTRFS by default.

**BTRFS is the default and recommended filesystem for Bazzite**.  Any secondary drives that you plan to play video games on should be **backed up and reformatted to either Ext4 or BTRFS, however the drive will lose all of the data when performing this operation**.  You can use [**GNOME Disks to format the drives appropriately at your own risk**](../Advanced/Auto-Mounting_Secondary_Drives.md).

#### Unsupported Filesystems for Secondary Drives

!!! warning

    You will lose all of your data reformatting secondary internal/external drives.

##### NTFS

If you are coming from Windows and plan to game on a secondary drive with games already installed on it, then we regret to inform you that the NTFS filesystem is **unsupported** for PC gaming on Bazzite.

##### exFAT and FAT32

FAT32 and exFAT are **unsupported**. Both filesystems **do not support symbolic links** which is required for Proton prefixes to work properly.  However, there are scenarios where a microSD card is formatted to exFAT _may work_ in some cases, but this method is unsupported as something the Bazzite maintainers do not plan to accommodate.

#### Sharing Games with a Windows Dual-Boot

Install the unofficial [WinBtrfs](https://github.com/maharmstone/btrfs) driver on your Windows installation at your own risk. Please make sure to read any documentation associated with this project before installing the driver on Windows.

#### Video Tutorial

https://www.youtube.com/watch?v=h6fc-3CCXbA

### Changing Default Password
<sub> (If it wasn't changed in the installer) </sub>

![KDE Plasma's Change Password|584x500, 75%](../../img/change-pass.png)

Change it in the settings of Desktop Mode under the "User" category.

## **Troubleshooting Installation**:

<link guide here>

