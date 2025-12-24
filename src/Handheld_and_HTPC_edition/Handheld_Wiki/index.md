<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=1038", "fetched_at": "2024-09-03 16:43:15.186486+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## Handheld Compatibility

!!! attention

    This list is incomplete and does not indicate that unlisted handhelds do not work with Bazzite currently, but because we lack specific information regarding their post-installation setup, workarounds, and proper hardware support for Linux, they are unlisted here.

**All handhelds except for the Steam Deck make use of [Handheld Daemon](https://github.com/hhd-dev/hhd/blob/master/readme.md) for controls, TDP, etc.**

_Click the name of each hardware to view post-installation setup and known issues/workarounds._

- [**Steam Deck**](./Steam_Deck.md)
- [**Lenovo Legion Go**](./Lenovo_Legion_Go.md)
- [**ASUS ROG Ally**](./ASUS_ROG_Ally.md)
- [**GPD Handhelds**](./GPD_Handhelds.md)
- [**OneXPlayer Handhelds**](./OneXPlayer_Handhelds.md)
- [**Ayn Handhelds**](./Ayn_Handhelds.md)
- [**Ayaneo Handhelds**](./Ayaneo_Handhelds.md)
- [**Other Handhelds**](./Other_Handhelds.md)

Feel free to add new entries or update current wiki pages for your handheld following our [**documentation guidelines**](https://github.com/bazzite-org/docs.bazzite.gg/blob/main/README.md#documentation-guidelines).


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

### Controller Information

For most handheld hardware, besides the Steam Deck, emulation of a DualSense controller is used for full functionality. Double tap or hold the side menu button to access settings for controller emulation including switching to an Xbox controller with reduced functionality.

If your device has paddles, you will want to use the DualSense Edge controller (**excluding the Ayn Loki**). It’s disabled by default because some games do not map it correctly.

Some games and emulators may need Steam Input **disabled** to work correctly with your controls.

Virtual keyboard is Steam's keyboard, but needs to be setup in Steam's settings in Desktop Mode. There is **no default keybinding for Steam's on-screen keyboard** (Remap it to <kbd>**X**</kbd> or whatever you prefer)

#### Desktop Controls

Desktop controller layout may not exist by default if Steam doesn't setup your handheld controller properly. This can be fixed in Steam's controller settings

![desktop_controls_step_1|588x500, 75%](../../img/handheld_desktop_controls_1.png)

![desktop_controls_step_2|690x431, 75%](../../img/handheld_desktop_controls_2.png)

![desktop_controls_step_3|690x431, 75%](../../img/handheld_desktop_controls_3.jpeg)

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

## e-GPU Caveats:

- The same [GPU hardware requirements](/Gaming/Hardware_compatibility_for_gaming.md#steam-gaming-mode-requirements) that apply for Steam Gaming Mode also apply for e-GPUs.
  - Nvidia GPUs are **unsupported** but may work if rebasing to a beta Nvidia `-deck` image.

### Recommended External Guide & Script:

Read this [guide](https://github.com/ewagner12/all-ways-egpu) for eGPU usage on Linux, and use the script at your own risk.

## Bazzite's Steam Gaming Mode Documentation

Check out the [Steam Gaming Mode documentation](../Steam_Gaming_Mode.md) for an in-depth guide on Steam Gaming Mode plus general fixes for common issues.

<hr>

← [**View all Bazzite documentation**](/index.md)
