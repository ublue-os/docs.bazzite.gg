---
title: Update Guide
---

# Update Guide

![System Updates|200x200, 100%](../../img/System_Updates.png)

## Updating Bazzite

!!! attention

    It is required to have 3% free storage of your total drive that Bazzite is installed on to update properly.

Bazzite updates all of the changes made specifically in Bazzite itself, updates from Fedora's base packages upstream, graphic drivers, and user software installed from Bazaar.

### Desktop Images

- System updates happen **automatically daily** on a schedule and when the hardware is not under heavy use, like playing video games.
    - There is a check in-place to only update the image when your CPU, battery, and RAM usage meets certain requirements.
- Updates will be downloaded in the background and will **apply on the next reboot** and should contain the newest build of Bazzite.
    - An upgrade can be forced with the System Update tool at your own convenience.
- Updates upgrade system packages, Steam, and installed applications when available. 

### Bazzite-Deck Images

- Updates can be managed in Steam Gaming Mode **manually** by the user.
  - Open: **Steam Menu** > **Settings** > **System** > **Check for Updates** > **Apply**
    - **Reboot** to apply system upgrades.
- Updates upgrade system packages, Steam, and installed applications when available.

### Terminal Command (Manually Upgrade) [All Images):

```command
ujust update
```

## Do I have to reboot immediately after every system update?

**No**, but the **system upgrade will not apply until the next reboot**.  User-installed applications from Bazaar **can be upgraded without rebooting**.

- **Desktop images**: While your device is running, newer updates will still download in the background once a day, and will be waiting to be applied until the device is rebooted.
- **Bazzite-Deck images**: Updates will be checked daily and can be downloaded at your leisure similar to how SteamOS handles upgrades.

## How do I view the changelog for each update?

Changelogs for each Bazzite can be found on [Github](https://github.com/ublue-os/bazzite/releases).

## Metered / Limited Network Connections & Data Caps

!!! note
    This is an unsupported configuration since updates are expected to be running daily for both the operating system and applications.

Open the System Settings of your desktop environment and turn on the setting relating to a metered connection (Data caps or incur charges).  This setting will **pause** automatic updates for Bazzite.
