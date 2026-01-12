---
title: Bazzite's Gaming Guide
---

# Bazzite's Gaming Guide

## Linux Gaming Introduction

Linux gaming being a viable competitor to Windows is a relatively new paradigm. Most Windows exclusive games can run on Bazzite using modern hardware. There are still some rough edges, but gaming on Linux does offer advantages on the appropriate hardware such as better frame-times than on Windows.

## Game Launchers

### Steam

Steam is the recommended way to play PC games on the Linux desktop as it ships with a compatability layer known as [Proton](https://steamcommunity.com/games/221410/announcements/detail/1696055855739350561).  If a game has a Linux port that isn't well maintained then it is recommended to try running the game through Proton in its Steam game properties.

![Cog Icon > Properties|690x284, 75%](../img/Steam_Setup_Cog.png)
![Compatibility tab|690x492, 75%](../img/Steam_Setup_Compat_Tab.png)

### Non-Steam Games

Non-Steam games can run on Bazzite. The most recommended method is Lutris for most non-Steam games. [**Faugus Launcher**](https://flathub.org/en/apps/io.github.Faugus.faugus-launcher) is an alternative to Lutris available in the Bazaar app store which may be favorable due to a simpler design. [**Heroic Games Launcher**](https://flathub.org/apps/com.heroicgameslauncher.hgl) is recommended over Lutris for games that were purchased from Epic Games Launcher, GOG, and Amazon Games Launcher.  

Games installed from the Microsoft Store do **not** run unless you use a Xbox Cloud Gaming client like [**Greenlight**](https://github.com/unknownskl/greenlight). Fortnite can also be played via this method **without** a Game Pass subscription.  There are also [**select titles available on Battle.net**](https://us.support.blizzard.com/en/article/000357106) which can be ran through Proton using Lutris. 

Console emulators should be installed from the Bazaar app store or using a setup script like [**Emudeck**](https://www.emudeck.com/).

### Lutris Setup

Lutris offers two methods to play Windows games on Bazzite.  Community-driven scripts or manually adding the executable.  It is **highly recommended to use the manual method** as some scripts are poorly maintained.

### Lutris Install Scripts

![Example of Lutris installers|623x500, 75%](../img/Lutris_Setup_Installers.png)

Lutris is game management software that doubles as a WINE front-end for Windows games. Several games and launchers can be installed by searching for the title and using one of the installer scripts for it. 

### Manually adding a Windows game to Lutris

![Add Locally Installed Game|632x496, 75%](../img/Lutris_Setup_Add_Local_Game.png)

![Lutris manually adding games example 1|690x213](../img/Lutris_Setup_Add_Local_Game_1.png)

However if your game is not listed or doesn't work with the provided script, then manually add the executable. It will need a [**prefix directory**](/Gaming/Managing_and_modding_games.md#non-steam-games-prefix-management) created somewhere, but by default it will use the `~/Games` directory for each game.

#### Lutris Shortcuts

![Lutris_Right_Click_Menu|421x447, 75%](../img/Lutris_Setup_Shortcut.png)

Right clicking a game on Lutris gives the option to add it as a non-Steam game (useful for Steam Gaming Mode), create a desktop shortcut, or an application menu shortcut.

<hr>

## Compatibility Layers & Managing Windows Games

Windows games need to run through a **compatibility layer** (like Proton) on Bazzite. KDE Plasma and GNOME images pre-install different, but similar compatibility layer managers.

<ProtonPlus screenshot>

Install and update to the latest [GE-Proton](https://github.com/GloriousEggroll/proton-ge-custom), [Luxtorpeda](https://github.com/luxtorpeda-dev/luxtorpeda), and other tools using ProtonPlus.

![Protontricks|660x500](../img/Protontricks.png)

Some games require [Protontricks](https://github.com/Matoking/protontricks) (pre-installed) or [Winetricks](https://github.com/Winetricks/winetricks) (for non-Steam games, included with Lutris) to function properly.

### Modding

**Steam Workshop is the most straightforward method to obtain mods**, but is not supported for every title and requires you to own the game on Steam. Some mod managers have Linux ports like [r2modman.](https://github.com/ebkr/r2modmanPlus).

Adding and replacing game files is still viable in both the game directory and prefix, but there may be some extra steps involved.  Some mods require a "WINE DLL OVERRIDE" environment variable in the Steam launch options.  For non-Steam Games, use Lutris to open "Wine Configuration" and select the "Libraries" tab to add new overrides.

!!! example

    **DirectInput8 DLL Override**: `WINEDLLOVERRIDES="dinput8=n,b" %command%`

#### What is a Proton (or Wine) Prefix?

It's the glue that holds everything together when you run a game through Proton and also is responsible for containing any of the files the game would drop outside of the installation folder.

!!! important

    This installation folder for **Steam games** is usually in: `.../steamapps/common/<game>`

Many PC games drop files in Windows folders like "My Documents" or "AppData" and both can be found in your prefix directory. This prefix directory may be useful for modding your games, backing up your saves, or configuration files.

![AppID|690x482, 75%](../img/Steam_AppID.png)

For games on Steam, they are located in your `~/.steam/root/steamapps/compatdata/` folder, and then the **AppID number of the game**:

- This ID by going into the game's properties on Steam in the games `Properties > Updates > App ID`
- Continue to `.../pfx/drive_c/` and wherever the game drops the file on Windows.

Non-Steam games can have the prefix folder anywhere you specify.  By default Lutris uses `~/Games` as the main folder.

<hr>

## Common Linux Gaming Issues

Issues that happen specifically in Linux gaming outside of Bazzite.

### Native Linux Port Versus Windows Version

Some Linux ports may have missing functionality or worse performance than on the Windows version running through Proton. However, there are scenarios where using the native port exclusively is your only option, and may even be desirable.  If a Linux native game does not launch, then force the Legacy Runtime compatibility layer by going into the **game's properties** and selecting "**Compatibility**" then checking "**Force the use of a specific Steam Play compatibility tool**".

### Denuvo Anti-Tamper DRM Locking Games

Games that use Denuvo Anti-Tamper DRM consider changing Proton versions as activiating the game on different hardware which may cause you to get locked out of the game if you change the Proton version more than 5 times within a 24 hour period.

### Steam Logs

If you encounter issues with a game launching on Steam:

1. Open the game's properties and **enter this launch option**:
   `PROTON_LOG=1 %command%`

2. Launch the game

A log file should appear in your Home directory named after the game's application ID number.

> **See also**: <link to common issues and resolutions and gaming mode quirks>

<hr>

## Advanced Gaming Tweaks

For those who like to tinker with specific environment variables, then please read the [**Advanced Gaming Guide**](/Advanced/gaming-advanced.md).

<hr>

## Useful External Resources

- [**ProtonDB**](https://www.protondb.com/explore) - User reports for game compatibility on Linux
- [**Are We Anti-Cheat Yet?**](https://areweanticheatyet.com/) - List of popular games utilizing anti-cheat software and if the game supports Linux
- [**PC Gaming Wiki**](https://www.pcgamingwiki.com/wiki/Home) - General information, workarounds, and enhancements for PC games
- [**General Emulation Wiki**](https://emulation.gametechwiki.com/index.php/Main_Page) - Emulation resources
- [**Linux VR Adventures Wiki**](https://lvra.gitlab.io/) - General information for running VR games on Linux
- [**Linux VR Adventure Database**](https://db.vronlinux.org/) - User reports for Virtual Reality (VR) game compatibility on Linux
