---
title: Secure Boot Guide
tags:
  -  QR
search:
  exclude: true
---

# Secure Boot Guide

## What is Secure Boot?

Secure Boot is a security feature that checks your bootloader and operating system really come from Bazzite and haven't been tampered with before letting them start. Future anti-cheats will require it to be enabled. Your PC already trusts Microsoft's keys, but not the Universal Blue key that Bazzite is signed with, so you need to enroll that key once.

Terminology: 

* MOK (Machine Owner Key): a key you choose to trust on top of the ones your PC shipped with. Universal Blue's key is added as a MOK.
* MokManager: the blue screen at boot where you confirm the enrollment by choosing Enroll MOK and entering universalblue.
* Shim: a small bootloader signed by Microsoft that your PC trusts out of the box. It checks Bazzite against your enrolled MOKs.

## Important Secure Boot Notes:

- Entering the password will register invisible characters for security purposes, so you will not be able to see what you are typing!
- Updating your BIOS may re-enable Secure Boot and you may have to follow **"Method B"** after updating it to resolve the black screen on boot complaining about loading the kernel first.
- The Steam Deck does **not** come with secure boot enabled and does not ship with any keys enrolled by default, do not enable Secure Boot on your Steam Deck unless you absolutely know what you're doing.

## Error Message (if key is **not** enrolled properly):

```
error: ../../grub-core/kern/efi/sb.c:182:bad shim signature.
error: ../../grub-core/loader/i386/efi/linux.c:256:you need to load the kernel first.

Press any key to continue...
```

Follow **Method B** below to resolve this and move past the error message if you encounter it.

### **Method A** - During Installation Method

![Secure Boot menu: Continue boot / Enroll MOK / Enroll key from disk / Enroll hash from disk](../../img/Secure_Boot.png 'Secure Boot')

!!! note

    This screen will also appear on the next boot if you enable Secure Boot if it was disabled during installation.

A blue screen will appear giving the option to enroll the signed keys after leaving the Bazzite installer.

`Enroll MOK` if you have secure boot enabled. If prompted to enter a password, then **enter**:

```command
universalblue
```

Otherwise `Continue boot` if you have Secure Boot disabled or if it is not supported with your hardware.

## **Method B** - After Installation Method

**Disable Secure Boot in the BIOS before proceeding**, and then re-enable it **after enrolling the key**.

If you have already installed Bazzite then **enter this command in a host terminal**:

```
ujust enroll-secure-boot-key
```

If prompted to enroll the required key, then **enter the password in the host terminal**:

```command
universalblue
```

**You can now turn Secure Boot back on in the BIOS.**
Use the following command to boot straight into your system's BIOS (if supported):

```command
ujust bios
```
## Complete MOK enrollment at boot

On the next boot, you will see the blue MokManager screen:

1.  Choose **Enroll MOK**.
2.  When prompted for a password, enter:
    ```command
    universalblue
    ```

After the reboot, the key is enrolled and Secure Boot can remain enabled. Your system should now boot normally under Secure Boot.
