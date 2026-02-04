---
title: Manual Partitioning
---

# Manual Partitioning

!!! Note
      
      This installation guide is for the **legacy ISO** and an updated guide for the new ISOs will be coming soon.

!!! warning "Only users who are dual booting on the same drive should use these instructions. Automatic partitioning is preferred in other cases."

!!! warning "Bazzite only supports the BTRFS filesystem for `/`"

## Manual Partitioning Instructions

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
