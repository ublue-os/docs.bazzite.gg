---
title: Differences Between Bazzite & Upstream Fedora Atomic Desktop
---

Bazzite is a custom image of [**Fedora Kinoite (KDE Plasma images)**](https://fedoraproject.org/atomic-desktops/kinoite/) or [**Fedora Silverblue (GNOME images)**](https://fedoraproject.org/atomic-desktops/silverblue/) with modifications made to try and provide a user friendly experience out of the box with a focus on PC gaming.

## Key Differences:

- Better hardware support out of the box from PC hardware to peripheral devices.
- Fedora Flatpak remote removed in favor of using the [**System Flathub**](https://flathub.org/) remote for all applications.
- [**Homebrew**](/Installing_and_Managing_Software/Homebrew/) is the intended package manager for command-line tools.
- Convenient [**`ujust`**](/Installing_and_Managing_Software/ujust/) scripts by maintainers and contributors of the project.
- [**Distrobox**](/Installing_and_Managing_Software/Distrobox/) grants access to other Linux desktop package managers for specific applications or development environments.
- Multimedia codecs with full support for accelerated video encoding and decoding out of the box.
- Android application support with [**Waydroid**](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md).
- Firefox is no longer part of the image in favor of the Flatpak.
- Secondary drives that are BTRFS or EXT4 will be automatically auto-mounted.
- Tweaks to desktop environments including pre-installed GNOME extensions and KDE Plasma themes.
- Steam Gaming Mode is setup out of the box and auto-starts (for [**Bazzite-Deck images**](/Handheld_and_HTPC_edition/Steam_Gaming_Mode/) only).
- [**Rollback to older Bazzite builds within the last 90 days**](/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/bazzite_rollback_helper.md).
- Tons of gaming enhancements included.
