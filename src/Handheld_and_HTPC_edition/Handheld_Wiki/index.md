---
title: Handheld Compatibility
---

# Handheld Compatibility

## SteamOS-like Functionality

>**Notice**: Bazzite uses [Handheld Daemon](https://github.com/hhd-dev/hhd/blob/master/readme.md) for proper handheld support currently. 

Bazzite-Deck images ship with [Steam Gaming Mode](../Steam_Gaming_Mode.md) which is intended to mimic the experience of SteamOS.  The goal is to have earlier support for most x86_64 handheld PCs before SteamOS and with the same benefits of the desktop version of Bazzite.

## Supported Handhelds

!!! attention

    This list is incomplete and does not indicate that unlisted handhelds do not work with Bazzite currently, but because we lack specific information regarding their post-installation setup, workarounds, and proper hardware support for Linux, they are unlisted here.

**All handhelds except for the Steam Deck make use of [Handheld Daemon](https://github.com/hhd-dev/hhd/blob/master/readme.md) for controls, TDP, etc.**

_Click the name of each hardware to view post-installation setup and known issues/workarounds._

- [**Steam Deck**](./Steam_Deck.md)
- [**Lenovo Handhelds**](./Lenovo_Legion_Go.md)
- [**ASUS Handhelds**](./ASUS_ROG_Ally.md)
- [**GPD Handhelds**](./GPD_Handhelds.md)
- [**OneXPlayer Handhelds**](./OneXPlayer_Handhelds.md)
- [**Ayn Handhelds**](./Ayn_Handhelds.md)
- [**Ayaneo Handhelds**](./Ayaneo_Handhelds.md)
- [**Other Handhelds**](./Other_Handhelds.md)

If your handheld isn't listed in the entries, then it does **not** necessarily mean that the device is unsupported. 

## HHD Setup

!!! attention

    HHD is intended and functional for handhelds that are **not** the Steam Deck.

>Read the [**HHD README**](https://github.com/hhd-dev/hhd/blob/master/readme.md) for more information.

1. Double press the 'side menu button' to access Handheld Daemon overlay in Steam Gaming Mode

2. Select the controller emulation and RGB color you want

!!! note

    Gyro functionality **requires** DualSense emulation

 ## TDP Controls

![TDP|690x431, 75%](../../img/TDP.jpeg)

There are a few options for TDP Controls that work with Bazzite:

- The [HHD-overlay](https://github.com/hhd-dev/hhd/blob/master/readme.md) supports TDP controls. (**Primary Supported Method**)
  - Also has a desktop app that is pre-installed, look for the Handheld Daemon app in Desktop Mode.
- [SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP) supports TDP, GPU, Power Governor, and among other settings.
  - Also has a [graphical application](https://github.com/aarron-lee/SimpleDeckyTDP-Desktop), but needs to be manually installed.
  - [PowerControl](https://github.com/mengmeet/PowerControl) supports TDP, GPU, and fan controls on select devices.

### How do I open the HHD Overlay?

![Overlay|690x431, 75%](../../img/HHD_Overlay.jpeg)
![RGB|690x431, 75%](../../img/HHD_RGB.jpeg)

Press, hold, or double-tap the Quick Access Menu button.

## Controller Information

For most handheld hardware, besides the Steam Deck, emulation of a DualSense controller is used for full functionality. Double tap or hold the side menu button to access settings for controller emulation including switching to an Xbox controller with reduced functionality.

If your device has paddles, you will want to use the DualSense Edge controller (**excluding the Ayn Loki**). It’s disabled by default because some games do not map it correctly.

Some games and emulators may need Steam Input **disabled** to work correctly with your controls.

### Desktop Controls

Virtual keyboard is Steam's keyboard, but needs to be setup in Steam's settings in Desktop Mode. There is **no default keybinding for Steam's on-screen keyboard** (Remap it to <kbd>**X**</kbd> or whatever you prefer).  Desktop controller layout may not exist by default if Steam doesn't setup your handheld controller properly. This can be fixed in Steam's controller settings

## Decky Setup

To install [Decky Loader](https://decky.xyz), open a host terminal and enter:

```bash
ujust setup-decky
```

You can access Decky Loader by pressing the 'side menu button', also known as the Quick Access Menu (QAM), once from within Steam Gamemode or Steam Big Picture Mode.

The Quick Access Menu is accessible from the keyboard with Control + 2, or with an external controller using Xbox/PS button + A/X.

### Decky Plugins

!!! attention

    Decky may break or uninstall after updates especially if there is an update.

Install optional [Decky plugins](https://plugins.deckbrew.xyz/) for your handheld. If you experience any major issues then it is recommended to uninstall Decky before reporting Bazzite bugs.

## Unsupported Handhelds

!!! note

    Certain handhelds have been confirmed to boot Bazzite, but are plagued by missing driver support for Linux including missing audio drivers.

Unsupported handhelds _could work_ with Bazzite, but there may be major issues encountered that are undocumented. If your handheld hardware is not listed, then you can still give Bazzite a try with our Bazzite-Deck image.

Your mileage may vary with untested hardware. Bazzite does **not** have the required setup for unsupported handheld, so setup will be manually done by the end-user for different functionality if it even works properly on the unsupported device.

## e-GPU Caveats:

- The same [GPU hardware requirements](/Gaming/Hardware_compatibility_for_gaming.md#steam-gaming-mode-requirements) that apply for Steam Gaming Mode also apply for e-GPUs.
  - Nvidia GPUs are **unsupported** but may work if rebasing to a Nvidia `-deck` image with a potential for outstanding bugs.

>[**General Linux e-GPU Guide + Script**](https://github.com/ewagner12/all-ways-egpu)
