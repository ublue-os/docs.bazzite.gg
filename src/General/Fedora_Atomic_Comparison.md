---
title: Comparison of Bazzite and Fedora Atomic Desktop
---

# Comparison of Bazzite & Upstream Fedora Atomic Desktop

## What is Bazzite?

Bazzite is a custom image of [**Fedora Kinoite (KDE Plasma images)**](https://fedoraproject.org/atomic-desktops/kinoite/) or [**Fedora Silverblue (GNOME images)**](https://fedoraproject.org/atomic-desktops/silverblue/) which are part of the [**Fedora Atomic Desktop family**](https://fedoraproject.org/atomic-desktops/) with modifications made to try and provide a user friendly experience out of the box with a focus on PC gaming.

## Key Differences

The following is a list of features Bazzite ships with that differs from upstream Fedora Atomic Desktop operating systems:

### Less Post-Installation Setup

- Better hardware support out of the box from PC hardware to peripheral devices.
- Multimedia codecs with full support for accelerated video encoding and decoding out of the box.
- Gaming-focused software pre-installed like Steam and Lutris.
- Fedora Flatpak remote removed in favor of using the [**System Flathub**](https://flathub.org/) remote to have access to more applications by default.

### Ease of Use

- Convenient [**`ujust`**](/Installing_and_Managing_Software/ujust/) scripts by maintainers and contributors of the project.
- Steam Gaming Mode is setup out of the box and auto-starts on [**Bazzite-Deck images**](/Handheld_and_HTPC_edition/Steam_Gaming_Mode/) which are intended for handheld and couch gaming. 

### Made with Developers in Mind

- Homebrew is the intended package manager for command-line tools.
- Distrobox containers grants access to other Linux desktop package managers for specific applications or development environments.
- [**Bazzite-DX variant**](https://dev.bazzite.gg/) as the defacto Bazzite image for software development.

### Extra Enhancements

- Android application support with [**Waydroid**](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md).
- Firefox is no longer part of the image in favor of the Flatpak version.
  - Firefox can now be uninstalled as it is not part of the image
  - It also can receive updates faster since it does not rely on system upgrades to update. 
- Secondary drives that are formatted as BTRFS or Ext4 will be automatically auto-mounted.
- Tweaks to desktop environments including pre-installed GNOME extensions and KDE Plasma themes.
- Rollback to older Bazzite builds within the last 90 days.
