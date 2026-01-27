---
title: How to Use Modprobe Options in Bazzite
---

# How to Use Modprobe Options in Bazzite

## If you just plan to add options to a module, then you should consider using a karg!
Touching the initramfs system and modprobe will slow down your updates so all your updates will take several minutes longer. In most cases what you want to do in modprobe can be done with simple kernel arguments.

In this example lets change the below modprobe options into a karg (kernel argument):
```
options hid_apple fnmode=2
```
This would translate to the karg:
```
hid_apple.fnmode=2
```
To add this to grub we issue the command:
```
rpm-ostree kargs --append-if-missing="hid_apple.fnmode=2"
```
This lets you change the module option without editing the initramfs system and is a lot faster whenever you update the system as the kernel arguments are not regenerated on each update.

## Upstream Documentation on Modifying Kernel Arguments

Read the [**upstream Fedora documentation**](https://docs.fedoraproject.org/en-US/fedora-coreos/kernel-args/) on this topic for more information.
