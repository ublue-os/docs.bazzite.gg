!!! info

    {# TODO: Write section explaining partition labeling requirements and procedure #}
    [`ublue-os-media-automount-udev`](https://github.com/ublue-os/packages/tree/main/packages/ublue-os-media-automount-udev) will handle automounting given the partition follows these conditions:

    - Uses BTRFS/ext4
    - Has a label/name

    In the scenario where the partition doesn't get mounted automatically under these conditions, then please follow the manual procedure,
    using [KDE partition manager](/Advanced/KDE_Partition_Manager_Auto_Mount_Guide.md) or [GNOME Disks](/Advanced/GNOME_Disks_Auto-Mount_Guide.md)
