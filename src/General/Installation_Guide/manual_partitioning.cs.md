---
title: Manual Partitioning
tags:
  -  Obsolete
search:
  exclude: true
---

# Ruční dělení

!!! note
      
      Tato instalační příručka je pro **starší ISO** a aktualizovaná příručka pro nové ISO bude brzy k dispozici.

!!! warning "Tyto pokyny by měli používat pouze uživatelé, kteří spouštějí duální systém na stejném disku. V ostatních případech je preferováno automatické rozdělování."

!!! warning "Bazzite podporuje pouze souborový systém BTRFS pro `/`"

## Pokyny k ručnímu rozdělení

Pokud potřebujete výukové video pro ruční dělení, podívejte se na tento [návod v časovém razítku 9:10](https://www.youtube.com/watch?v=JxPsKhJGTrs&t=550s).

1. Vyberte možnost Instalace
2. Vyberte `Advanced Custom(Blivet-GUI)` v části Konfigurace úložiště.
![Výběr ručního rozdělení](../../img/select_manual_partitioning.png)
3. Vytvořte následující oddíly a zařízení:
  - **/boot/efi**
    ![EFI oddíl](../../img/efi_partition.png)
    ```
    mount point: /boot/efi
    format:      EFI system partition
    size:        300MB
    ```
  - **/bota**
    ![spouštěcí oddíl](../../img/boot_partition.png)
    ```
    mount point: /boot
    format:      ext4
    size:        2GB
    ```
  - **oddíl btrfs**
    ![btrfs partition](../../img/btrfs_partition.png)
    ```
    mount point:
    format: btrfs
    size: [max]
    ```
  -**/**
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
4. Vyberte Hotovo
5. Vyberte Přijmout změny
6. Pokračujte v instalaci.