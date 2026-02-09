---
title: Update Guide
---

# Update Guide

![System Updates|200x200, 100%](../../img/System_Updates.png)

!!! attention

    It is required to have **3% free storage of your total drive that Bazzite is installed on** to update properly.

## Updating Bazzite

!!! attention

    It is required to have **3% free storage of your total drive that Bazzite is installed on** to update properly.

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

### Terminal command to upgrade manually (all images):

```command
ujust update
```

## Do I have to reboot immediately after every system update?

**No**, but the **system upgrade will not apply until the next reboot**.  User-installed applications from Bazaar **will be upgraded without rebooting**.

- **Desktop images**: While your device is running, newer updates will still download in the background once a day, and will be waiting to be applied until the device is rebooted.
- **Bazzite-Deck images**: Updates will be checked daily and can be downloaded at your leisure.
  
## How do I view the changelog for each update?

Changelogs for each Bazzite can be found on [Github](https://github.com/ublue-os/bazzite/releases).

## How does upgrading to a new major version release work?

Bazzite should automatically update when our new builds based on that new major release is ready.

## Do I have to reboot after every system update?

**No**, but the system upgrade will not apply until the next reboot.

- Desktop images: While your device is running, newer updates will still download in the background once a day, and will be waiting to be applied until the device is rebooted.
- Bazzite-Deck images: Updates will be checked daily and can be downloaded at your leisure.
  - Users will need to apply system updates manually similarly to SteamOS.

## How do I view the changelog for each update?

Changelogs can be found on the [Github repository](https://github.com/ublue-os/bazzite/releases).

## How often is there a new Bazzite build?

Usually Bazzite is built twice a week which includes the new changes from us and from Fedora Linux.

## How does updating to a new Fedora major release work?

Bazzite should automatically update when our new builds based on that new major release are ready, and usually aims for the around the same day when the new Fedora Linux major release is out.
