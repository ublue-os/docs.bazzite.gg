---
title: Show Detailed Init Logs During Boot
---

# Show Detailed Init Logs During Boot

## Purpose

See the init log show if services are functional when your device boots.

![Plymouth](../img/plymouth.png)

## 1 - Change Initramfs Theme to Enable Detailed Init Logs:

```command
sudo plymouth-set-default-theme details
```

Alternatively, create `/etc/plymouth/plymouthd.conf` manually

## 2 - Regenerate Initramfs & Reboot to Enable Theme Change

```command
sudo rpm-ostree initramfs --enable --reboot
```
