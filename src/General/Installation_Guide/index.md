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

## Installing Bazzite



## **Troubleshooting Installation**:

- Use a download manager (like [**Motrix**](https://motrix.app/)) if the direct download fails or is downloading too slow.

- Make sure to only select the appropriate drives to avoid losing data on others, and it is best practice to safely remove any external drives before proceeding.

### Alternative Bazzite Installation Guide

Read the [**Alternative Troubleshooting Guide**](./alternate-install-guide.md) if you are having issues booting the Bazzite installer.
