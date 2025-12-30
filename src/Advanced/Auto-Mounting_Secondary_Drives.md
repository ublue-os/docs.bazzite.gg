---
title: Auto-Mounting Secondary Drives
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=970", "fetched_at": "2024-09-03 16:43:14.005694+00:00"}-->
<!-- ANCHOR_END: METADATA -->

!!! info "MicroSD cards automatically mount without any manual intervention required."

## Video Guide

https://youtu.be/fN9lvkkrExI

## Setup an auto-mounting partition

1. Open Gnome Disks, should have an icon like this. ![GNOME|50x50, 50%](../img/GNOME_Disks_icon.png)

2. Wipe the partition you want to use, then use the leftover to create a new one.

   ![](../img/automount.1.png)

3. Give the drive a name and a filesystem.

!!! warning "Bazzite only supports BTRFS/Ext4 filesystems for reporting issues."

![](../img/automount.2_btrfs.1.png){data-gallery="step-2"}
![](../img/automount.2_btrfs.2.png){data-gallery="step-2"}
![](../img/automount.3.png){data-gallery="step-2"}

Now reboot, your partition should be mounted automatically. Should appear under `/run/media/system/PARTITION_NAME`.

![](../img/automount.4.png){data-gallery="step-3"}

## Manual mounting

![GNOME_Edit_Mount_Options|690x465, 75%](../img/GNOME_Edit_Mount_Options.png)

![GNOME_Mount_Options|549x500, 75%](../img/GNOME_Mount_Options_new.png)

Append `,user,exec` at the end if doesnt work properly.

![](../img/GNOME_Mount_Options_new.2.png)

## Troubleshooting

### Emergency Mode after mounting?

This video tutorial shows how to recover from your mounting mistakes.

https://www.youtube.com/watch?v=-2wca_0CpXY

### Drives will not auto-mount despite being BTRFS/ext4 (Requests authentication every boot to mount)

1. Mount the target disk(s).

2. Open Gnome Disks and navigate to the target disk.

3. Click on Additional Partition Options > Edit Mount Options.

4. Ensure "User Session Defaults" is FALSE and "Mount at system startup" is TRUE, then click "Ok"

5. Repeat for any additional disks. You can confirm this worked by checking your Fstab file and seeing that the appropriate UUIDs have been added. `sudo cat /etc/fstab`


