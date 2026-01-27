---
title: Using Swap for Additional Memory or Hibernation
---

# Using Swap for Additional Memory or Hibernation

## Purpose

This guide will walk you through the steps to create a swapfile on a BTRFS filesystem, which can be used for additional memory or hibernation.

Bazzite-Deck images already support hibernation via Handheld Daemon using a dynamic swap file (`General -> Hibernate`). In addition, all Bazzite images use zram by default to provide additional memory.

Use this guide if you want to create a persistent swapfile instead of zram for more uncompressed memory, or if you want to use hibernation via the desktop environment. 

## Create the Swapfile

First, create a subvolume for the swapfile. This ensures that if you decide to use snapshots, the swapfile will not be included in them. You should also fix the SELinux context of the swapfile directory.
```bash
sudo btrfs subvolume create /var/swap
sudo semanage fcontext -a -t var_t /var/swap
sudo restorecon /var/swap
```

Then, create the swapfile itself. In this example, we create a 26GB swapfile. Again, you need to fix the SELinux context of the swapfile itself.
```bash
SIZE=26G
sudo btrfs filesystem mkswapfile --size $SIZE /var/swap/swapfile
sudo semanage fcontext -a -t swapfile_t /var/swap/swapfile
sudo restorecon /var/swap/swapfile
```

Load the swapfile to verify it works with:
```bash
sudo swapon /var/swap/swapfile
```

## Adding it to fstab
Now, you need to add your swapfile to `/etc/fstab` to make it persistent:
```
sudo cp /etc/fstab /etc/fstab.bak
sudo nano /etc/fstab
```

!!! attention
    Be careful when you edit the fstab file **otherwise your system will no longer start**! In this case, the previous image can be used to boot.

Add the following **line of code** to fstab:

```
/var/swap/swapfile none swap defaults,nofail 0 0
```

## Disable zram
Finally, you need to disable zram to enable hibernation to work properly. For this, you can zero out the zram-generator configuration file. This prevents Bazzite updates from restoring it.
```
echo "" | sudo tee /etc/systemd/zram-generator.conf
```

Finally, reboot your device to apply the changes made above.

## Reverting Changes and Restoring zram
To revert the changes and restore zram, first remove the swapfile entry from `/etc/fstab`. Then, re-enable zram by copying the original configuration file back:
```
sudo cp /usr/etc/systemd/zram-generator.conf /etc/systemd/zram-generator.conf
```
