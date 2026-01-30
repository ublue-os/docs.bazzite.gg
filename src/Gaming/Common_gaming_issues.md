---
authors:
  - "@nicknamenamenick"
  - "@m2Giles"
  - "@porkloin"
tags:
  - Troubleshooting
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=2658", "fetched_at": "2024-09-03 16:43:04.885968+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## Steam Logs

If you encounter issues with a game launching on Steam:

1. Open the game's properties and **enter this launch option**:
   `PROTON_LOG=1 %command%`

2. Launch the game

A log file should appear in your Home directory named after the game's application ID number.
You can use this log file for requesting support.

## Steam Games Not Launching

### NTFS Permissions

Make sure your games are **not** on a NTFS (Windows) partition. More information can be found [**here**](./Hardware_compatibility_for_gaming.md#unsupported-filesystems-for-secondary-drives).

### Multi-User WINE Quirks

!!! note

    Bazzite-Deck does not support multiple Linux user accounts, this information only applies to the Desktop edition of Bazzite.

Sometimes Steam games will completely refuse to launch on a secondary user account. This can be due to the ownership of the WINE prefix files. You might see an error like this in ` ~/.local/share/Steam/logs/console-linux.txt ` on the secondary user account:

```
wineserver: /SteamLibrary/steamapps/compatdata/377160/pfx is not owned by you
```

You can fix this by creating a separate Steam library folder to hold the prefix data for Proton and creating a symbolic link (_symlink_) for the other folders (like common game data).

```
USER2@bazzite: /mnt/ExtraStuff/USER2SteamLibrary/steamapps$ ls -la
total 32
drwxrwxr-x. 3 USER2 steamplayers 4096 Jan 29 15:19 .
drwxrwsr-x. 3 USER2 steamplayers 4096 Jan 29 16:13 ..
-rwxr-xr-x. 1 USER2 USER2         2287 Jan 29 15:19 appmanifest_377160.acf
lrwxrwxrwx. 1 USER2 USER2           51 Jan 29 15:10 common -> /mnt/ExtraStuff/USER1SteamLibrary/steamapps/common/
drwxr-xr-x. 3 USER2 USER2         4096 Jan 29 15:13 compatdata
lrwxrwxrwx. 1 USER2 USER2           56 Jan 29 15:12 shadercache -> /mnt/ExtraStuff/USER1SteamLibrary/steamapps/shadercache/
lrwxrwxrwx. 1 USER2 USER2           49 Jan 29 15:12 temp
lrwxrwxrwx. 1 USER2 USER2           53 Jan 29 15:12 workshop
```

Similarly copy or symlink the appmanifest files from each library for games to show up properly in each Steam library. 

## Native Linux Port Versus Windows Version

Some Linux ports may have missing functionality or worse performance than on the Windows version running through Proton. However, there are scenarios where using the native port exclusively is your only option, and may even be desirable.  If a Linux native game does not launch, then force the Legacy Runtime compatibility layer by going into the **game's properties** and selecting "**Compatibility**" then checking "**Force the use of a specific Steam Play compatibility tool**".

## Valve & Source Engine Game Problems

!!! note

    This only applies to specific games running on the [Source engine](https://www.pcgamingwiki.com/wiki/Engine:Source).

### Audio & Custom Content Bugs

!!! attention

    Do **not** attempt to follow this workaround until you run into issues with audio or the specific scenario mentioned below regarding _Left 4 Dead 2_.

Missing voice lines or custom content not loading in Source games? SELinux is blocking MP3 decoding and other middleware because it [executes heap memory](https://github.com/ValveSoftware/steam-for-linux/issues/43).

This has also been confirmed to cause issues joining and hosting custom maps in _Left 4 Dead 2_.

!!! warning

    Configuring SELinux is intended for advanced users and if used irresponsibly can break other components in your system and weaken the security of your device.

**At your own risk**

Open a host terminal and **enter these 4 commands**:

```command
sudo su
```

```command
cd /tmp
```

```command
ausearch -c 'hl2_linux' --raw | audit2allow -M my-hl2linux
```

```command
semodule -X 300 -i my-hl2linux.pp
```

Reboot your device

#### If you want to undo this change eventually:

**Disable or remove the module.**

##### Disable it:

```command
semodule -X 300 -d my-hl2linux
```

##### Remove and delete it:

```command
semodule -X 300 -r my-hl2linux
```

The `.pp` file should be in `/root` if you want to remove that.

### Source Games Not Launching

If a 32-bit Source 1 engine game is not opening due to [tmalloc libraries issues](https://github.com/ValveSoftware/csgo-osx-linux/issues/3229), then open a host terminal and **enter**:

Add the following as a **launch option** to the affected game in Steam:

```command
LD_PRELOAD=/usr/lib/libtcmalloc_and_profiler.so.4 %command%
```

Delete `libtcmalloc_minimal.so.x` in the game's bin folder if present.

If this fails to fix it, then try forcing Proton Experimental in the game's properties.


## Frame Rate Limiting Issues and Inconsistency

When using Gamescope, framerate limits can be applied in several ways. Unfortunately not all methods work for every enviroment, game, or hardware configuration.

Many inconsistencies can be observed, especially when applying framerate limits in desktop mode.

The tables below show the behavior of different framerate limiting methods.

### Steam Game Mode (Deck OS / Game Mode session)
| Method | Setup steps | Requires V-Sync On In-Game? | Change limit without restarting game? | Latency | Preferred | Notes |
|---|---|---|---|---|---|---|
| **Gamescope FPS limiter** | Use **Quick Access Menu > Performance > Framerate Limit** | No | Yes | Meh | **Preferred** | Automatically turns v-sync on at driver-level whenever the framerate cap is enabled. Additional latency will be introduced. |
| **MangoAPP (embedded)** | N/A - doesn't work at all. | - | - | - | – | Frame limiter settings from mangoapp are ignored in game mode/deck mode. Use the slider or external mangohud instead. |
| **MangoHUD (external)** | **Launch Options:** `MANGOHUD=1 %command%` | No | Yes | Meh | – | Set `fps_limit=0,30,60,120...` (0=no cap) in MangoHud.conf. May clash with MangoAPP. |
| **DXVK/VKD3D runtime frame limiter** | **DXVK (D3D8/9/10/11):** `DXVK_FRAME_RATE={fps} %command%`<br>**VKD3D-Proton (D3D12):** `VKD3D_FRAME_RATE={fps} %command%` | No | No | Best | – | Applies only to DXVK/VKD3D titles (no effect on native OpenGL or native Vulkan). |




### Desktop Mode (GNOME / KDE)
| Method | Setup steps | Requires V-Sync On In-Game? | Change limit without restarting game? | Latency | Preferred | Notes |
|---|---|---|---|---|---|---|
| **Gamescope FPS limiter** | **Launch Options**: `gamescope -r {fps} -- %command%` / `--framerate-limit {fps}` | Yes | Yes | Meh | – | Use `gamescopectl debug_set_fps_limit {fps}` to change the limiter value live without restarting. |
| **MangoAPP (embedded)** | **Launch Options:** `gamescope --mangoapp -- %command%` | Yes | Yes | Meh | – | Caps are sometimes not effective. Set `fps_limit=0,30,60,120...` (0=no cap) in MangoHud.conf (or via `MANGOHUD_CONFIG=...`). Add `show_fps_limit` to preset to see in game. Change with `ShiftL+F1`. |
| **MangoHUD (external)** | **Launch Options:** `MANGOHUD=1 gamescope -- %command%` | No | Yes | Meh | **Preferred** | Caps are almost always effective. Set `fps_limit=0,30,60,120...` (0=no cap) in MangoHud.conf (or via `MANGOHUD_CONFIG=...`). Add `show_fps_limit` to preset to see in game. Change with `ShiftL+F1`. |
| **DXVK/VKD3D runtime frame limiter** | **DXVK (D3D8/9/10/11):** `DXVK_FRAME_RATE={fps} %command%`<br>**VKD3D-Proton (D3D12):** `VKD3D_FRAME_RATE={fps} %command%` | No | No | Best | – | In-process/API-level caps; excellent timing, but you must restart to change. |


If your framerate limiter isn't working, the following steps can often help:

1. Disable adaptive sync/VRR or remove the `--adaptive-sync` flag from your gamescope args.
2. Set vsync in-game to "on".


<hr>

[**<-- Back to Gaming Guide**](./index.md)
