---
title: Dual Boot Preliminary and Post-Installation Setup Guide
---

# Dual Boot Preliminary and Post-Installation Setup Guide

!!! note

    Make sure to read the [**Installation Guide**](./index.md) for your device first before proceeding.

1. Installing Bazzite with a shared drive.
2. Installing Bazzite on a separate drive.

=== "Shared Drive"

    1. (In Windows) Disable **Bitlocker encryption** and **fastboot**, and reboot.
    2. (In Windows) Resize the Windows partition with the Disk Management app to have enough space for Bazzite.
    Usually should look something like this:
    ![](/img/dualbooting_partitions_windows.png)]
    <i><small>Source: [diskpart.com](https://www.diskpart.com/windows-10/windows-10-disk-management-0528.html)</small></i>
    3. Run the Bazzite installer with the automatic partitioning option.
    4. Reboot into Bazzite and run `ujust regenerate-grub` in the terminal to add Windows to the GRUB.


=== "Separate Drive"

    **When a dedicated drive is feasible, this method is recommended.**

    Install Bazzite on a separate internal or external drive.

    1. Install the other operating system on a drive (like Windows).
    2. Install Bazzite on a **second** drive.
    3. Set Bazzite as the **default** in your boot order (optional).

    If you install Windows second, you should disconnect the Bazzite drive to prevent using the Windows installer of using its EFI partition.

    You can also install Windows to an external drive with Windows-to-Go using [Rufus](https://rufus.ie/en/) to dual boot if you do not have an internal drive available.

If you install Windows after Bazzite, you can restore Bazzite's bootloader with the **Bootloader Restoring Tool** in the Live ISO.

## Manual Partitioning Instructions

!!! warning "Only users who are dual booting on the same drive should use these instructions. Automatic partitioning is preferred in other cases."

!!! warning "Bazzite only supports the BTRFS filesystem for `/`."

If you need a tutorial video for manual partitioning, watch this [tutorial at timestamp 9:10](https://www.youtube.com/watch?v=JxPsKhJGTrs&t=550s).

1.  Select Installation Destination
2.  Select `Advanced Custom(Blivet-GUI)` under Storage Configuration.
![Selecting manual partitioning](../../img/select_manual_partitioning.png)
3.  Create the following partitions and devices:
  - **/boot/efi**
    ![EFI partition](../../img/efi_partition.png)
    ```
    mount point: /boot/efi
    format:      EFI system partition
    size:        300MB
    ```
  - **/boot**
    ![boot partition](../../img/boot_partition.png)
    ```
    mount point: /boot
    format:      ext4
    size:        2GB
    ```
  - **btrfs partition**
    ![btrfs partition](../../img/btrfs_partition.png)
    ```
    mount point:
    format: btrfs
    size: [max]
    ```
  - **/**
    ![/ subvolume](../../img/root_subvolume.png)
    ```
    mount point: /
    format:      btrfs (subvolume)
    ```
  - **/var**
    ![/var subvolume](../../img/var_subvolume.png)
    ```
    mount point: /var
    format:      btrfs (subvolume)
    ```
  - **/var/home**
    ![/var/home subvolume](../../img/var_home_subvolume.png)
    ```
    mount point: /var/home
    format:      btrfs (subvolume)
    ```
4.  Select Done
5.  Select Accept Changes
6.  Continue with the installation.

<hr/>

### Note about dual booting other distributions

For Fedora Atomic Desktop images on the **same** drive:

- To dual boot another **Fedora Atomic Desktop image** (like [Bluefin](https://projectbluefin.io/)) installed alongside Bazzite, you must make an additional EFI partition and switch between them through your motherboard's UEFI boot menu.

For dual booting on **separate** drives:

- Use your motherboard's UEFI boot menu as the GRUB bootloader may not recognize each boot entry correctly.

!!! note 

    Dual booting with **other distributions**, especially **non-atomic Fedora**, is not officially supported. It is recommended to use your motherboard's UEFI boot menu or to forgo dual booting entirely to avoid unexpected issues. If something does go wrong, restore Bazzite's bootloader using the **Bootloader Restoring Tool** in the Live ISO.

## Dual Boot Post-Configuration Setup

Show both your Windows and Bazzite installations in the GRUB menu to select from at boot by entering this **command into the terminal**:

```
ujust regenerate-grub
```

### Bazzite as Primary Boot

If the `OS Boot Manager` has set `Windows Boot Manager` to be the first boot priority, then this may result in booting directly into Windows after the install instead of Bazzite. You may have to fix this in your BIOS settings.

Take note that the GRUB menu might not show up. In such case, spam the <kbd>↓</kbd> key when booting up.

<hr>

### Boot into Windows from Steam

Adds a script in Steam to boot into Windows.

```
ujust setup-boot-windows-steam
```

## Expanding storage size in a Windows dual-boot scenario

!!! note

    This is for future reference after dual-booting for a while.

**Watch this video tutorial on how to expand the storage**:

https://www.youtube.com/watch?v=uy8mi1pAj8E
