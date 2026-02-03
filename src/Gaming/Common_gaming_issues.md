---
title: Common Gaming Issues
---

# Common Gaming Issues

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

<hr>

[**<-- Back to Gaming Guide**](./index.md)
