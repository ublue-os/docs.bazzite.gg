---
title: Managing and Modding Games
---

# Managing and Modding Games

## Compatibility Layers & Managing Windows Games

![Proton Plus|1797x1412, 43%](../img/proton-plus.png)
![Cog Icon > Properties|690x284, 75%](../img/Steam_Setup_Cog.png)
![Compatibility tab|690x492, 75%](../img/Steam_Setup_Compat_Tab.png)

Windows games need to run through a **compatibility layer** (like Proton) on Bazzite. Install and update to the latest [GE-Proton](https://github.com/GloriousEggroll/proton-ge-custom), [Luxtorpeda](https://github.com/luxtorpeda-dev/luxtorpeda), and other tools using ProtonPlus.

## Protontricks

![Protontricks|660x500](../img/Protontricks.png)

Some games require [Protontricks](https://github.com/Matoking/protontricks) (pre-installed) or [Winetricks](https://github.com/Winetricks/winetricks) (for non-Steam games, included with Lutris) to function properly by installing Windows DLLs into the prefix.

### What is a Proton (or Wine) Prefix?

It's the glue that holds everything together when you run a game through Proton and also is responsible for containing any of the files the game would drop outside of the installation folder.

!!! important

    This installation folder for **Steam games** is usually in: `.../steamapps/common/<game>`

Many PC games drop files in Windows folders like "My Documents" or "AppData" and both can be found in your prefix directory. This prefix directory may be useful for modding your games, backing up your saves, or configuration files.

![AppID|690x482, 75%](../img/Steam_AppID.png)

For games on Steam, they are located in your `~/.steam/root/steamapps/compatdata/` folder, and then the **AppID number of the game**:

- This ID by going into the game's properties on Steam in the games `Properties > Updates > App ID`
- Continue to `.../pfx/drive_c/` and wherever the game drops the file on Windows.

Non-Steam games can have the prefix folder anywhere you specify.  By default Lutris uses `~/Games` as the main folder.

## Modding

**Steam Workshop is the most straightforward method to obtain mods**, but is not supported for every title and requires you to own the game on Steam. Some mod managers have Linux ports like [r2modman](https://github.com/ebkr/r2modmanPlus).

Adding and replacing game files is still viable in both the game directory and prefix, but there may be some extra steps involved.  Some mods require a "WINE DLL OVERRIDE" environment variable in the Steam launch options.  For non-Steam Games, use Lutris to open "Wine Configuration" and select the "Libraries" tab to add new overrides.

!!! example

    **DirectInput8 DLL Override**: `WINEDLLOVERRIDES="dinput8=n,b" %command%`
