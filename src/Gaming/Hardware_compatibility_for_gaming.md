---
title: Hardware Compatibility for Linux Gaming
---

# Hardware Compatibility for Linux Gaming

## Standard Hardware

### Minimum System Requirements

- **Architecture**: x86_64
- **Firmware**: UEFI (CSM/Legacy boot [**UNSUPPORTED**](../FAQ.md#does-bazzite-support-csmlegacy-boot))
- **Processor (CPU)** : 2GHz quad core processor or better
- **System Memory (RAM)**: 8GB
- **Graphics**: A graphics card that can utilize Vulkan 1.3 or higher, modern AMD GPUs work the best
- **Storage**: 50GB of free space on an internal **solid-state drive (SSD)**
  - **Recommended Storage**: 120GB of free space on an internal **solid-state drive (SSD)**
  - **External Storage & Secondary Drives**: All drives must be formatted as **BTRFS (SSDs)** or **Ext4 (Hard Disk Drives [HDDs])**, please backup the files and reformat them post-installation. 
- **Network**: Stable internet connection with no bandwidth caps
- **Additional Notes**: Certain peripherals are **not** compatible with Bazzite:
  - **Wi-Fi Adapter Example** - [a list of **known compatible** USB Wi-Fi adapters](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md)

>[**The Hardware for Linux website**](https://linux-hardware.org/?view=computers) is a good indicator for how well OEM hardware is supported on the Linux desktop.

### Steam Gaming Mode Requirements

!!! note

    These specific requirements only apply to [Bazzite-Deck images](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md) which ships with all handheld Bazzite ISO downloads.

- Modern AMD GPU
  - RX 4xx series and up
    - 600M/700M integrated GPUs are also supported
- Intel Arc GPUs are supported with **minor caveats** compared to AMD hardware
- Nvidia GPU support is supported with [**major caveats**](/Handheld_and_HTPC_edition/quirks/#nvidia-exclusive-issues) compared to AMD hardware out of control of the Bazzite maintainers
- Requires a [**Steam**](https://store.steampowered.com/) account
  - Signing up for an account can be done post-installation if you don't have one already


>[**The Hardware for Linux website**](https://linux-hardware.org/?view=computers) is a good indicator for how well OEM hardware is supported on the Linux desktop.

### Compatible Handhelds

The [**Handheld Wiki**](../Handheld_and_HTPC_edition/Handheld_Wiki/index.md) lists tested handhelds with proper support for the Steam Deck, ASUS ROG Ally, Lenovo Legion Go, and a handful of other handhelds.

<hr>

## Vulkan Compatible GPU

!!! attention

    Linux gaming is heavily dependent on having compatible hardware with Vulkan.

### Viewing Your GPU's Vulkan Version

If you're using a device with an older or weaker GPU that does not support **Vulkan 1.3 or later**, then you need to use older Proton and Wine builds like **Proton/WINE 6** or earlier.  Check which Vulkan version your GPU uses, enter this in the **terminal**:

```command
vulkaninfo | grep 'Instance Version'
```

- If it outputs less than `1.3` in the `Vulkan Instance Version:` or does not work at all, then you will run into issues including unplayable games and worse performance.
- Really old devices may need to resort to OpenGL translation which performs worse, has graphical issues, etc.

![Vulkan Command](https://github.com/user-attachments/assets/ccca14ca-3001-4aa6-bf47-e0dcbdb73936)

>Try using [**Proton-Sarek**](https://github.com/pythonlover02/Proton-Sarek) if your have hardware that can utilize Vulkan 1.1, but not newer Vulkan versions. It can be installed using ProtonPlus.

### GPUs Without Vulkan Support

However if your GPU does not support Vulkan at all then you must use an older Proton version (Proton 3, 4, or 5) and use this **launch option for most Steam games**:

```command
PROTON_USE_WINED3D=1 %command%
```

This will use the OpenGL translation as opposed to Vulkan.

<hr>

## Storage Filesystems

!!! note

    Bazzite will automatically mount secondary drives that are formatted as Ext4 or BTRFS by default.

**BTRFS is the default and recommended filesystem for Bazzite**.  Any secondary drives that you plan to play video games on should be **backed up and reformatted to either Ext4 or BTRFS, however the drive will lose all of the data when performing this operation**.  You can use [**GNOME Disks to format the drives appropriately at your own risk**](../Advanced/Auto-Mounting_Secondary_Drives.md).

### Unsupported Filesystems for Secondary Drives


!!! CRITICAL

    NTFS and exFAT/FAT32 ARE NOT SUPPORTED. BOTH FILESYSTEMS CAN AND WILL LEAD TO DATA CORRUPTION UNDER LINUX. DO NOT USE THEM!
    winBTRFS UNDER WINDOWS STILL HAS BUGS AND IS ALSO NOT A SOLUTION. 
    
    THERE IS CURRENTLY NO RELIABLE CROSS-PLATFORM FILESYSTEM THAT CAN BE SHARED WITH WINDOWS AND LINUX.

!!! warning

    You will lose all of your data reformatting secondary internal/external drives.

#### NTFS

If you are coming from Windows and plan to game on a secondary drive with games already installed on it, then we regret to inform you that the NTFS filesystem is **unsupported** for PC gaming on Bazzite.

Playing games off of NTFS causes various issues, including but not limited to **games not launching at all**, and will eventually result in **data corruption** and **permanent data loss**!

#### exFAT and FAT32

FAT32 and exFAT are **unsupported**. Both filesystems **do not support symbolic links** which is required for Proton prefixes to work properly.  However, there are scenarios where a microSD card is formatted to exFAT _may work_ in some cases, but this method is unsupported as something the Bazzite maintainers do not plan to accommodate.

### Sharing Games with a Windows Dual-Boot

Install the unofficial [WinBtrfs](https://github.com/maharmstone/btrfs) driver on your Windows installation **at your own risk**. Please make sure to read any documentation associated with this project before installing the driver on Windows.

#### Video Tutorial

https://www.youtube.com/watch?v=h6fc-3CCXbA
