---
authors:
  - "@nicknamenamenick"
tags:
  - Guide
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=574", "fetched_at": "2024-09-03 16:43:19.212243+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## Customizing KDE Plasma

KDE Plasma is the default Bazzite desktop environment and is highly customizable. One of the various customization that can be done is installing custom styles, cursors, and icons to your system with custom themes made by the community.  Themes installed through the **System Settings** are installed into `~/.local/share/plasma`; to uninstall them, you may need to manually delete the folders associated with the installed themes manually.

![Directory|401x207, 75%](../img/Directory.png)

## Manually Installing Themes (_Recommended_)

Step-by-step instructions to install custom themes on KDE Plasma.

1. Download the theme manually from the [KDE Store](https://store.kde.org/browse/)
2. Extracting the contents to `~/.local/share/plasma/` (you may need to make this directory)
3. Open the system settings and select your theme, style, cursor etc. as it now should appear

### Theme Extraction Locations

The location where specific KDE Plasma components will be extracted on the desktop.

#### Global Themes

Global themes are placed in `~/.local/share/plasma/look-and-feel/` (_you may need to make this directory_).

#### Plasma Themes

"Plasma themes" are placed in `~/.local/share/plasma/desktoptheme/` (_you may need to make this directory_).

#### Plasma Window Decorations

"Window decoration themes" are placed in `~/.local/share/aurorae/themes/` (_you may need to make this directory_).

#### SDDM (Login Manager) Themes

SDDM themes can be layered **at your own risk** if they are available as RPM packages using [`rpm-ostree`](/Installing_and_Managing_Software/rpm-ostree.md).

#### Icon / Cursor Themes

"Icon/Cursor themes" are placed in `~/.local/share/icons`

#### Application Permissions to Use Themes

Some Flatpaks need filesystem permissions for applications that have issues with cursor themes.

**Example**: (`~/.local/share/icons/:ro` in "Filesystem" in each problematic application or globally in Flatseal).

#### Themes that require `kvantum`

Some themes require [`kvantum`](https://github.com/tsujan/Kvantum/blob/master/Kvantum/README.md) to be installed on the host system.

Install it with this **command**:

```
rpm-ostree install kvantum
```
> [**Check out this external resource on KDE themes for more information**](https://itsfoss.com/properly-theme-kde-plasma/).

<hr>

## Customizing Other Desktops and Sessions

### Manage GNOME Extensions (`-gnome` Images)

The "Extension Manager" applicaton alllows for installing new extensions to GNOME and managing currently pre-installed extensions.  Proceed with caution as extensions can make your system unstable and if your desktop crashes then GNOME will disable all of the extensions on the next boot.

### Steam Gaming Mode Tweaks (`-deck` Images)
!!! warning
    Decky Loader will sometimes have issues with new Steam and Gamescope updates, and may need to be uninstalled temporarily.

Install [Decky Loader](https://decky.xyz/) then install [CSS Loader](https://docs.deckthemes.com/) to customize how Steam Gaming Mode looks. Be aware that third-party plugins may cause issues. Read Bazzite's [Steam Gaming Mode documentation](../Handheld_and_HTPC_edition/quirks.md) to resolve common issues if you run into them after using Decky Loader.

## **See also**:
- [KDE Plasma Documentation](https://docs.kde.org/stable5/en/plasma-desktop/plasma-desktop/index.html)
- [GNOME Documentation](https://help.gnome.org/users/gnome-help/stable/)
