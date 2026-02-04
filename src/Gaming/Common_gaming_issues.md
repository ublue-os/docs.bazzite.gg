---
title: Common Gaming Issues
---

# Common Gaming Issues

### Native Linux Port Versus Windows Version

Some Linux ports may have missing functionality or worse performance than on the Windows version running through Proton. However, there are scenarios where using the native port exclusively is your only option, and may even be desirable.  

If a Linux native game does not launch, then force the **Legacy Runtime** compatibility layer by going into the **game's properties** and selecting "**Compatibility**" then checking "**Force the use of a specific Steam Play compatibility tool**" and selecting it.

### Denuvo Anti-Tamper DRM Locking Games

Games that use Denuvo Anti-Tamper DRM consider changing Proton versions as activating the game on different hardware which may cause you to get locked out of the game if you change the Proton version more than 5 times within a 24 hour period.

## Source 1 Engine Audio and Custom Content Bugs

!!! note

    This only applies to specific games running on the [Source engine](https://www.pcgamingwiki.com/wiki/Engine:Source).

!!! attention

    Do **not** attempt to follow this workaround until you run into issues with audio or the specific scenario mentioned below regarding _Left 4 Dead 2_.

Missing voice lines or custom content not loading in Source games? SELinux is blocking MP3 decoding and other middleware because it [**executes heap memory**](https://github.com/ValveSoftware/steam-for-linux/issues/43).

This has also been confirmed to cause issues joining and hosting custom maps in _Left 4 Dead 2_.

### The fix for audio/custom content issues:

!!! warning

    Configuring SELinux is intended for advanced users and if used irresponsibly can break other components in your system and weaken the security of your device.

Open a host terminal and **enter these 4 commands at your own risk**:

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

Reboot your device and test to see if the Source game still has issues.

### Undoing this change:

**Disable or remove the module.**

#### Disable the change:

```command
semodule -X 300 -d my-hl2linux
```

##### Remove and delete the change:

```command
semodule -X 300 -r my-hl2linux
```

The `.pp` file should be in `/root` if you want to remove that.

## Steam Games Not Launching

Steam games might not launch for a variety of reasons.

### Gathering Steam log files:

If you encounter issues with a game launching on Steam:

1. Open the game's properties and **enter this launch option**:
   `PROTON_LOG=1 %command%`

2. Launch the game

A log file should appear in your Home directory named after the game's application ID number.

### NTFS formatted drive permission issues:

Make sure your games are **not** on a NTFS (Windows) partition. More information can be found [**here**](./Hardware_compatibility_for_gaming.md#unsupported-filesystems-for-secondary-drives).

### Multi-user WINE quirks:

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
