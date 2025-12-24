---
title: Alternative Installation Guide
---

!!! warning

    This method may have scaling issues with the installer depending on the hardware especially if it is a handheld PC.

## Rebasing from a Fedora Atomic Desktop Image

If you experience issues with installing our ISO or the bootable drive you have is too small for Bazzite, then download the [Fedora Kinoite (**KDE Plasma**)](https://fedoraproject.org/atomic-desktops/kinoite/) or [Fedora Silverblue (**GNOME**)](https://fedoraproject.org/atomic-desktops/silverblue/) depending on which desktop environment you prefer.

1. The installation setup is similar to Bazzite and includes the same installer with the same instructions, but do **not** set a root account if its an option in the installer.

2. Once installed, you will not be on Bazzite until you enter the command found on our website that appears under ["**Existing Fedora Atomic Desktop Users**" section](https://download.bazzite.gg) when the download is ready or by referencing the [full image list in the FAQ](/General/FAQ/#bazzite-image-chart).

3. Open the terminal and enter this command, and keep in mind this process has **no progress indicator** and will take a long time.

4. Reboot when the rebase has finished, and Bazzite should be installed after rebooting and your username as well as the user password will carry over from the upstream Fedora Atomic Desktop to Bazzite.

5. You will also be **missing the default applications**.

## Install Pre-Installed Flatpak Applications

Open the terminal and **enter this command**:

```command
ujust _install-system-flatpaks
```

Choose the "Flathub" remote.  If it asks for "System" or "User" then choose "**System**" since that is the default remote for Bazzite.

> **This command installs:**
>
> - [Flatpak applications for **KDE Plasma** images](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/kinoite/usr/share/ublue-os/bazzite/flatpak/install)
> - [Flatpak applications for **GNOME** images](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/silverblue/usr/share/ublue-os/bazzite/flatpak/install)

## Rebasing to a signed image

Once everything is setup properly, then you should rebase from the **unsigned image** to the **signed image** for security reasons, so **enter this command** in the host terminal:

```command
rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/<IMAGE>
```

Replace **`<IMAGE>`** with the image you're using.

### Video Tutorial

https://www.youtube.com/watch?v=0NKEfVvdiOs
