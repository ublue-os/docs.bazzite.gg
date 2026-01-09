---
title: Handheld Compatibility
---

# Handheld Compatibility

## SteamOS-like Functionality

>**Notice**: Bazzite uses [Handheld Daemon](https://github.com/hhd-dev/hhd/blob/master/readme.md) for proper handheld support currently. 

Bazzite-Deck images ship with [Steam Gaming Mode](<link that here>) which is intended to mimic the experience of SteamOS.  The goal is to have earlier support for most x86_64 handheld PCs before SteamOS and with the same benefits of the desktop version of Bazzite.

### Tips and Tricks

- [Lenovo Legion Go Linux Tips and Tricks](https://github.com/aarron-lee/legion-go-tricks)
- [GPD Win Linux Tips and Tricks](https://github.com/aarron-lee/gpd-win-tricks)

### Steam Deck BIOS Updates

It is recommended to enter `ujust enable-deck-bios-firmware-updates` in the terminal to receive Steam Deck BIOS updates.

## Desktop Controls

Virtual keyboard is Steam's keyboard, but needs to be setup in Steam's settings in Desktop Mode. There is **no default keybinding for Steam's on-screen keyboard** (Remap it to <kbd>**X**</kbd> or whatever you prefer).  Desktop controller layout may not exist by default if Steam doesn't setup your handheld controller properly. This can be fixed in Steam's controller settings

![desktop_controls_step_1|588x500, 75%](../../img/handheld_desktop_controls_1.png)

<retake this pic>

Make sure to **apply** the desktop controls when you select them.

## Decky Setup

To install [Decky Loader](https://decky.xyz), open a host terminal and enter:

```bash
ujust setup-decky
```

You can access Decky Loader by pressing the 'side menu button', also known as the Quick Access Menu (QAM), once from within Steam Gamemode or Steam Big Picture Mode.

The Quick Access Menu is accessible from the keyboard with Control + 2, or with an external controller using Xbox/PS button + A/X.

## Decky Plugins

!!! attention

    Decky may break or uninstall after updates especially if the Steam client or Gamescope is updated.

Install optional [Decky plugins](https://plugins.deckbrew.xyz/) for your handheld. If you experience any major issues then it is recommended to uninstall Decky before reporting Bazzite bugs.

## Unsupported Handhelds

!!! note

    Certain handhelds have been confirmed to boot Bazzite, but are plagued by missing driver support for Linux including missing audio drivers.

Unsupported handhelds _could work_ with Bazzite, but there may be major issues encountered that are undocumented. If your handheld hardware is not listed, then you can still give Bazzite a try with our Bazzite-Deck image.

Your mileage may vary with untested hardware. Bazzite does **not** have the required setup for unsupported handheld, so setup will be manually done by the end-user for different functionality if it even works properly on the unsupported device.

## Bazzite's Steam Gaming Mode Documentation

Check out the [Steam Gaming Mode documentation](../Steam_Gaming_Mode.md) for an in-depth guide on Steam Gaming Mode plus general fixes for common issues.
