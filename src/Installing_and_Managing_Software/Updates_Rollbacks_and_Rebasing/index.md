---
title: Updates, Rollbacks, and Rebasing
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=36", "fetched_at": "2024-09-03 16:43:15.473615+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## Updates

![System Updates|200x200, 100%](../../img/System_Updates.png)

!!! attention

    It is required to have **3% free storage of your total drive that Bazzite is installed on** to update properly.

### How do updates work?

Bazzite updates all of the changes made specifically in Bazzite itself, updates from Fedora's base packages upstream, graphic drivers, and user software.

#### Desktop Images

System updates happen **automatically daily** on a schedule and when the hardware is not under heavy use, like playing video games.  There is a check in-place to only update the image when your CPU, battery, and RAM usage meets certain requirements. Updates will be downloaded in the background and will **apply on the next reboot** and should contain the newest build of Bazzite.  An upgrade can be forced with the System Update tool at your own convenience.

#### Bazzite-Deck Images

- Updates can be managed in Steam Gaming Mode **manually** by the user.
  - Open: **Steam Menu** > **Settings** > **System** > **Check for Updates** > **Apply**
    - **Reboot** to apply system upgrades.
- Updates upgrade system packages, Steam, containers and installed applications when available.

### Do I have to reboot immediately after every system update?

**No**, but the **system upgrade will not apply until the next reboot**.  User-installed applications from Bazaar **will be upgraded without rebooting**.

- **Desktop images**: While your device is running, newer updates will still download in the background once a day, and will be waiting to be applied until the device is rebooted.
- **Bazzite-Deck images**: Updates will be checked daily and can be downloaded at your leisure.
  
### How do I view the changelog for each update?

Changelogs for each Bazzite can be found on [Github](https://github.com/ublue-os/bazzite/releases).

### How does upgrading to a new major version release work?

Bazzite should automatically update when our new builds based on that new major release is ready.

## Rollbacks

Swap back to a previous system update if there are major issues after updating via the GRUB menu or the `rpm-ostree rollback` command.

> [**Rollbacks Guide**](./rolling_back_system_updates.md)


### Bazzite Rollback Helper Tool

Utility to assist with rolling back to older Bazzite images, changing update branches, or swapping to a different Bazzite image.

> [**Bazzite's Rollback Helper Utility Guide**](./bazzite_rollback_helper.md)

## Rebasing

!!! important

    Do **not** rebase to a different desktop environment than the one you are currently using, please backup and reinstall instead.

Rebase to Bazzite builds from the last 90 days, change Bazzite update channels, swap between the Desktop and Bazzite-Deck images, or move completely to a different Fedora Atomic Desktop image.

> [**Rebase Guide**](./rebase_guide.md)

<hr>

← [**View all Bazzite documentation**](../../index.md)
