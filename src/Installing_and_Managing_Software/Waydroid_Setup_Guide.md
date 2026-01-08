---
authors:
  - "@nicknamenamenick"
  - "@Gecked-Deck"
  - "@KyleGospo"
  - "@storyaddict"
  - "@castrojo"
  - "@aarron-lee"
  - "@wxllow"
  - "@SuperRiderTH"
tags:
  - Guide
  - Software
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=32", "fetched_at": "2024-09-03 16:43:06.740654+00:00"}-->
<!-- ANCHOR_END: METADATA -->

![Google Play Store|650x500](../img/Google_Play_Store.jpeg)

!!! attention

    Waydroid does **not** work on Nvidia hardware.

## What is Waydroid?

![Waydroid](../img/Waydroid.jpeg)

[Waydroid](https://waydro.id/) is an Android container that runs on Linux. Bazzite users can run Android applications using this method.

## First Time Setup

Open a host terminal and **enter this command to setup Waydroid**:

```bash
ujust setup-waydroid
```

### Initialize Waydroid

Waydroid requires users to initialize it for the first time which can be done by selecting:
`Initialize Waydroid`

Make sure this worked by entering this **command**:

```bash
/usr/bin/waydroid-launcher
```

This will launch Waydroid for the first time.

### Configure Waydroid

> Customize your Waydroid container

#### Part 1: Stop Waydroid Session

Waydroid needs to stop running to configure properly.

Open a host terminal and enter this **command**:

```command
waydroid session stop
```

#### Part 2: Configuration

Open a host terminal and enter this **command**:

```
ujust setup-waydroid
```

Selecting `Configure Waydroid` will allow users to install additional Android tweaks with the [Waydroid Extras Scripts.](https://github.com/casualsnek/waydroid_script#waydroid-extras-script)

1. Select Android version you have installed. To find installed Android version, start Waydroid, open Settings app then go to "About This Phone". Your Android version will be 11 or 13.
2. Select items to install

##### Available Waydroid Extras:

- [GApps](https://github.com/opengapps/opengapps/wiki/FAQ) (Default Android applications including the **Google Play Store)** or [microG](https://microg.org/) (Free alternatives to Google applications)

- ARM Translation (_libndk_ or _libhoudini_. _libhoudini_ offers better overall compatibility compared to _libndk_. Some games may run on only one of _libhoudini_ or _libndk_.  On Android 11, _libhoudini_ will run significantly slower than _libndk_ if you have AMD CPU. **Do not install both of them at the same time. If you need to switch, uninstall your current translation layer before installing new one.**)

- [Magisk](https://github.com/topjohnwu/Magisk) (Android power user suite)

- [Logitech Smartdock Support](https://support.logi.com/hc/en-us/articles/360023201574-What-is-SmartDock) (SmartDock hardware support)

- [F-Droid Privileged Extension](https://f-droid.org/packages/org.fdroid.fdroid.privileged/) (Proper [F-Droid](https://f-droid.org/en/packages/) support)

- [`widevine`](https://widevine.com/) (Support for video streaming DRM)

### Get Google Device ID to Get Certified (**GApps**)

![Waydroid_DeviceID|690x182](../img/Waydroid_DeviceID.png)

1. Launch Waydroid
   (**Waydroid must be running**)

2. After selecting your current Android version, select `Get Google Device ID to Get Certified` especially if you plan to use the Google Play Store (**GApps**).

3. Follow the instructions in the terminal output.

After verification has happened, it will usually take a while before your device is Google Play certified.

## Waydroid Helper application

![Waydroid_Helper|400x400](../img/Waydroid_Helper.png)

[waydroid-helper](https://github.com/waydroid-helper/waydroid-helper) is a GUI app that enables more advanced configuration and control over your waydroid installations.

To install it, run the following `ujust` command:

```bash
ujust setup-waydroid helper
```

You can alternatively go directly to their [releases](https://github.com/waydroid-helper/waydroid-helper/releases) and install the latest AppImage via GearLever.

## Add as a Non-Steam Shortcut

> This is useful for [Bazzite images that use Steam Gaming Mode.](../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)

Make sure to add `/usr/bin/waydroid-launcher` to Steam as a non-Steam game for Waydroid to work properly in Steam Gaming Mode.

![Waydroid Launcher add to steam|960x540](../img/waydroid_launcher_add_to_steam.jpg)

### Enable Multi-Touch Support

To use multi-touch gestures in Waydroid while running under Steam Gaming Mode, you need to enable "Touchscreen Native Support" in Steam's controller settings:

1. Within your Waydroid shortcut, go to **Controller Settings**.
2. Go to **Edit Layout** > **Action Sets** > **Default**.
3. Select **Add Always-On command**.
4. Under **System**, select the **Touchscreen Native Support** command.

![Waydroid Launcher Steam Multi-Touch|640x400](../img/waydroid_launcher_steam_multitouch.jpg)

<hr>

## Disable Inputs to Waydroid When Unfocused

Waydroid has an [issue](https://github.com/waydroid/waydroid/issues/135) where it will register inputs from controllers, keyboards, and other input devices even when the window is not focused.

Disable this functionality:

!!! note

    Waydroid must be running!

In a host terminal, **run this command**:

```command
waydroid prop set persist.waydroid.uevent false
```

If you ever want to undo this change, run the same steps but set `true` instead of `false` with the same command.

## Mouse Clicks to Touch Input

Some applications do not expect mouse clicks and only respond to touchscreen taps.

!!! note

    Waydroid must be running!

You can use this command in a host terminal to enable this per-application:

```command
waydroid prop set persist.waydroid.fake_touch "PACKAGE_NAME_HERE"
```

!!! note

    Package names are usually in the format of "com.example.appname".
    You can find the package name for the application at the bottom of the "App info" page in the Settings app.

    Wildcards are also supported, so "com.rovio.*" would apply to all games by Rovio.

    An example for the app "Fate/Grand Order" would be:
    `waydroid prop set persist.waydroid.fake_touch "com.aniplex.fategrandorder.en"`

The application inside of Waydroid needs to be restarted for the changes to take effect.

!!! warning

    Only set specific applications with this command!
    Setting this globally to the system using a wildcard can cause irregular behavior with the mouse cursor.

To revert these changes, use the following command in a host terminal:

```command
waydroid prop set persist.waydroid.fake_touch ""
```

## Resolution & Density Options

This is intended for users who have issues with Waydroid's resolution, scaling, or running Waydroid nested. This is **optional**.

Open a host terminal and enter the following **commands**:

```bash
sudoedit /etc/default/waydroid-launcher
```

```bash
sudoedit /etc/default/steamos-nested-desktop
```

Save the text files when done.

## Waydroid Hybrid Graphics Fix

This is only intended for users who have multiple GPUs in their hardware who experience graphical corruptions in Waydroid.

**Enter in a host terminal**:

```
ujust setup-waydroid
```

Then `Select GPU for Waydroid` which will give the option on what GPU to utilize for Waydroid to fix graphical corruptions.

## Reset Waydroid

!!! warning

    You will lose all of your Waydroid data.

If you experience issues or want a fresh Waydroid container, then select `Reset Waydroid` after **entering**:

```
ujust setup-waydroid
```

### Project Website

https://waydro.id/

<hr>

**See also**: [Upstream documentation](https://docs.waydro.id/)

<-- [**View all Bazzite documentation**](../index.md)
