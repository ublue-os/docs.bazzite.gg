---
title: Post-Installation Setup
---

# Post-Installation Setup

## First Boot Setup

![Rollbacks|690x402, 50%](../../img/GRUB_Menu.png)

The first boot will show a screen showing your current and last deployment. It is important to note that the GRUB menu can be used to rollback Bazzite deployments if you encounter issues.

Read more about this in the [Updates, Rollback, and Rebasing documentation](../../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md).

It is important to configure the system settings on a first boot to personalize your desktop especially if you notice the scaling is incorrect on first-boot.

## Configure system settings

### Scaling Settings

![Display Settings (KDE Plasma)|690x370, 75%](../../img/KDE_Display_Settings.png)
**_KDE Plasma's System Settings application_**

![Display Settings (GNOME)|690x344, 75%](../../img/GNOME_Display_Settings.png)
**_GNOME's Settings application_**

Adjust the system settings to your preference.

### Changing Default Password
<sub> (If it wasn't changed in the installer) </sub>

![KDE Plasma's Change Password|584x500, 75%](../../img/change-pass.png)

Change it in the settings of Desktop Mode under the "User" category.

### Setting Up Steam Gaming Mode (Bazzite-Deck Only)

![Gaming Mode Setup|690x442, 50%](../../img/pLvHB1NAMlb3ghsR72q7l9Auj8B.jpeg)
^^^GET A NEW IMAGE THIS ONE IS BAD!

After completing all of the above, then your next boot will be in Steam Gaming Mode which requires additional setup for Steam.

>[Read the Bazzite-Deck documentation](<link>)

## Dual Boot Post-Configuration Setup

Show both your Windows and Bazzite installations in the GRUB menu to select from at boot by entering this **command into the terminal**:

```
ujust regenerate-grub
```

#### Bazzite as Primary Boot

If the `OS Boot Manager` has set `Windows Boot Manager` to be the first boot priority, then this may result in booting directly into Windows after the install instead of Bazzite. You may have to fix this in your BIOS settings.

Take note that the GRUB menu might not show up. In such case, spam the <kbd>↓</kbd> key when booting up.

#### Boot into Windows from Steam

Adds a script in Steam to boot into Windows.

```
ujust setup-boot-windows-steam
```

#### Expanding storage size in a Windows dual-boot scenario

!!! note

    This is for future reference after dual-booting for a while.

**Watch this video tutorial on how to expand the storage**:

https://www.youtube.com/watch?v=uy8mi1pAj8E


### Secondary Storage Filesystems

!!! note

    Bazzite will automatically mount secondary drives that are formatted as Ext4 or BTRFS by default.

**BTRFS is the default and recommended filesystem for Bazzite**.  Any secondary drives that you plan to play video games on should be **backed up and reformatted to either Ext4 or BTRFS, however the drive will lose all of the data when performing this operation**.  You can use [**GNOME Disks to format the drives appropriately at your own risk**](../Advanced/Auto-Mounting_Secondary_Drives.md).

#### Unsupported Filesystems for Secondary Drives

!!! CRITICAL

    NTFS and exFAT/FAT32 ARE NOT SUPPORTED. BOTH FILESYSTEMS CAN AND WILL LEAD TO DATA CORRUPTION UNDER LINUX. DO NOT USE THEM!
    winBTRFS UNDER WINDOWS STILL HAS BUGS AND IS ALSO NOT A SOLUTION. 
    
    THERE IS CURRENTLY NO RELIABLE CROSS-PLATFORM FILESYSTEM THAT CAN BE SHARED WITH WINDOWS AND LINUX.


!!! warning

    You will lose all of your data reformatting secondary internal/external drives.

##### NTFS

If you are coming from Windows and plan to game on a secondary drive with games already installed on it, then we regret to inform you that the NTFS filesystem is **unsupported** for PC gaming on Bazzite.  Playing games off of a NTFS formatted drive can cause various issues, including but not limited to **games not launching at all**, and will eventually result in **data corruption** and **permanent data loss**!

##### exFAT and FAT32

FAT32 and exFAT are **unsupported**. Both filesystems **do not support symbolic links** which is required for Proton prefixes to work properly.  However, there are scenarios where a microSD card is formatted to exFAT _may work_ in some cases, but this method is unsupported as something the Bazzite maintainers do not plan to accommodate.

#### Sharing Games with a Windows Dual-Boot

Install the unofficial [WinBtrfs](https://github.com/maharmstone/btrfs) driver on your Windows installation **at your own risk**. Please make sure to read any documentation associated with this project before installing the driver on Windows.

#### Video Tutorial

https://www.youtube.com/watch?v=h6fc-3CCXbA

## Recommended Next Steps

### Configure your system with the Bazzite Portal application

<screenshot the bazzite portal>

### Install additional software with the Bazaar app store

![Screenshot of the Bazaar app store|1649x1274, 50%](../../img/Bazaar.png)

### Play video games

<link gaming guide>
