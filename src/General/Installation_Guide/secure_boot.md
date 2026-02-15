---
title: Secure Boot Guide
---

# Secure Boot Guide

![Secure Boot menu: Continue boot / Enroll MOK / Enroll key from disk / Enroll hash from disk|690x378, 50%](../../img/Secure_Boot.jpeg 'Secure Boot')

## Secure Boot Notes and Gotchas

!!! note

    Skip this section if Secure Boot is not enabled or unsupported with your hardware.

!!! important

    The enrollment prompt uses a English QWERTY keyboard layout, indiscriminately of your actual hardware keyboard. Other layouts can therefore interfere with the characters of the password (i.e. `A` and `Q` are swapped on AZERTY layouts).

- Entering the password will register invisible characters for security purposes, so you will not be able to see what you are typing!

- Updating your BIOS may re-enable Secure Boot and you may have to follow **"Method B"** after updating it to resolve the black screen on boot complaining about loading the kernel first.

- The Steam Deck does **not** come with secure boot enabled and does not ship with any keys enrolled by default, do not enable Secure Boot on your Steam Deck unless you absolutely know what you're doing.

### Error message if key is **not** enrolled properly:

```
error: ../../grub-core/kern/efi/sb.c:182:bad shim signature.
error: ../../grub-core/loader/1389/efi/linux.c:256:you need to load the kernel first.

Press any key to continue...
```

![error: ../../grub-core/kern/efi/sb.c:182:bad shim signature. / error: ../../grub-core/loader/1389/efi/linux.c:256:you need to load the kernel first. / Press any key to continue...|613x63](../../img/load_the_kernel_first_error.jpeg 'load the kernel first error')

Select and follow **Method B** below to resolve this and move past the error message if you encounter it.

=== "Method A: During Installation Method"

    ![Secure Boot menu: Continue boot / Enroll MOK / Enroll key from disk / Enroll hash from disk|690x378, 50%](../../img/Secure_Boot.jpeg 'Secure Boot')
    
    !!! note

        This screen will also appear on the next boot if you enable Secure Boot if it was disabled during installation.

    A blue screen will appear giving the option to enroll the signed keys after leaving the Bazzite installer.

    `Enroll MOK` if you have secure boot enabled. If prompted to enter a password, then **enter**:

    ```command
    universalblue
    ```

    Otherwise `Continue boot` if you have Secure Boot disabled or if it is not supported with your hardware.

=== "Method B: After Installation Method"

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
    ... or mash the BIOS key <kbd>F2</kbd>/<kbd>Delete</kbd>,
    ... or mash the <kbd>↓</kbd> key and select **UEFI Firmware Settings** in grub.
    
### Complete MOK enrollment at boot

On the next boot, you will see the blue MokManager screen:

1.  Choose **Enroll MOK**.
2.  When prompted for a password, enter:
    ```command
    universalblue
    ```

After the reboot, the key is enrolled and Secure Boot can remain enabled. Your system should now boot normally under Secure Boot.

## Secure Boot Instructions for Upstream Fedora Atomic Desktop Images

>[**Read more about rebasing from upstream Fedora Atomic Desktop images**](/General/Installation_Guide/alternate-install-guide.md)

Rebasing from Fedora Silverblue, Fedora Kinoite, etc. to Bazzite.

If you're rebasing from a Fedora Atomic Desktop image and use Secure Boot, then follow our [README](https://github.com/ublue-os/bazzite/blob/main/README.md#secure-boot).
