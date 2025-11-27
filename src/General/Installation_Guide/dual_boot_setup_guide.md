---
title: Dual Boot Preliminary and Post-Installation Setup Guide
authors:
  - "@nicknamenamenick"
  - "@atimeofday"
  - "@damiankorcz"
  - "@aarron-lee"
  - "@Zeglius"
  - "@tired-runner"
tags:
  - Installation
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=2743", "fetched_at": "2024-09-03 16:43:23.309649+00:00"}-->
<!-- ANCHOR_END: METADATA -->

!!! note

    Make sure to read the [**Installation Guide**](./index.md) for your device first before proceeding.

{#
TODO (@Zeglius): The dual booting methods section seems irrelevant, given its pretty straightforward.
We might want to replace it with a mention of the Bootloader Restoration Tool and thats it.
#}

1. Installing Bazzite with a shared drive.
2. Installing Bazzite on a separate drive.

=== "Separate Drive"

    **When a dedicated drive is feasible, this method is recommended.**

    Install Bazzite on a separate internal or external drive.

    1. Install the other operating system on a drive (like Windows)
    2. Install Bazzite on a **second** drive
    3. Set Bazzite as the **default** in your boot order (optional)

    If you install Windows second, you should disconnect the Bazzite drive to prevent using the Windows installer of using its EFI partition.

    You can also install Windows to an external drive with Windows-to-Go using [Rufus](https://rufus.ie/en/) to dual boot if you do not have an internal drive available.


=== "Shared drive"

    1. (In Windows) Resize the Windows partition with the Disk Management app to have enough space for Bazzite.
    Usually should look something like this:
    ![](/img/dualbooting_partitions_windows.png)
    <i><small>Source: [diskpart.com](https://www.diskpart.com/windows-10/windows-10-disk-management-0528.html)</small></i>
    2. Run the Bazzite installer with [manual partitioning](./manual_partitioning.md)
    3. Reboot into Bazzite and run `ujust regenerate-grub` in the terminal to add Windows to the GRUB.


If you install Windows after Bazzite, you can restore Bazzite bootloader with the **Bootloader Restoring Tool** in the Live ISO.

<hr/>

### Note about dual booting other Fedora Atomic Desktop images on the **same** drive:

If you want to dual boot another **Fedora Atomic Desktop image** (like [Bluefin](https://projectbluefin.io/)) installed alongside Bazzite, then you would have to make an additional EFI partition and switch between them through the BIOS boot menu.

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

Adds a script in Steam to boot into Windows

```
ujust setup-boot-windows-steam
```

## Expanding storage size in a Windows dual-boot scenario

!!! note

    This is for future reference after dual-booting for a while.

**Watch this video tutorial on how to expand the storage**:

https://www.youtube.com/watch?v=uy8mi1pAj8E
