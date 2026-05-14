---
title: Game Launchers
---

# Game Launchers

## **Steam Setup**

Steam can run Windows games on Linux. It utilizes a wide range of projects and patches all packed into a piece of software built-in to Steam called [**Proton**](https://github.com/ValveSoftware/Proton) for Windows compatibility.

### Forcing A Specific Proton / Steam Play Tool Version

#### Important Notes

- Games with a Linux port will be used by default on Desktop images.
- Valve selects the default runner on _Handheld/HTPC_ images. 
- Some games run better with a specific version of Proton or forcing the Linux runtime to run the Linux port.

Run that specific version by going into the game's **Properties** > **Compatibility** > **Force the use of a specific Steam Play compatibility tool**

#### Image Example
![Cog Icon > Properties|690x284, 75%](../img/Steam_Setup_Cog.png)
![Compatibility tab|690x492, 75%](../img/Steam_Setup_Compat_Tab.png)


## **Non-Steam Games**

**It is recommended to use [Lutris](https://lutris.net/games?q=&ordering=-popularity&paginate_by=100) for _most_ non-steam games**.  There are edge cases with specific launchers and games that have a better working alternative than Lutris, but Lutris is the most supported option for PC games outside of Steam on Bazzite outside of special scenarios.

### Lutris Setup

Lutris offers two methods to play Windows games on Bazzite.  Community-driven scripts or manually adding the executable.  It is **highly recommended to use the manual method** as some scripts are poorly maintained.

### Manually adding a Windows game to Lutris

![Add Locally Installed Game|632x496, 75%](../img/Lutris_Setup_Add_Local_Game.png)

![Lutris manually adding games example 1|690x213](../img/Lutris_Setup_Add_Local_Game_1.png)

However if your game is not listed or doesn't work with the provided script, then manually add the executable. It will need a [**prefix directory**](./Managing_and_modding_games.md) created, but by default it will use the `~/Games` directory for each game.


### Lutris Install Scripts

![Example of Lutris installers|623x500, 75%](../img/Lutris_Setup_Installers.png)

Lutris is game management software that doubles as a WINE front-end for Windows games. Several games and launchers can be installed by searching for the title and using one of the installer scripts for it. 

#### Lutris Shortcuts

![Lutris_Right_Click_Menu|421x447, 75%](../img/Lutris_Setup_Shortcut.png)

Right clicking a game on Lutris gives the option to add it as a non-Steam game (useful for Steam Gaming Mode), create a desktop shortcut, or an application menu shortcut.

## Other Game Launchers

Bazaar can install other game launchers like [**Heroic Games Launcher**](https://flathub.org/en/apps/com.heroicgameslauncher.hgl) (for GOG/Epic/Amazon games) or alternate frontends like [**Faugus**](https://flathub.org/en/apps/io.github.Faugus.faugus-launcher).
