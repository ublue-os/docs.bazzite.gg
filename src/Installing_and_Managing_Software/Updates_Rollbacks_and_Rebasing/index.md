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

### How do I change the Bazzite's update branch? (Stable, Testing, and Unstable)

There are two update branches:

- Stable (`:stable`)
  - Default branch that's used in normal Bazzite installations.
- [Testing (`:testing`)](https://github.com/ublue-os/bazzite/compare/main...testing)
  - Get a sneak peak of future Bazzite builds before release.
  - Bugs may frequently appear.
  - Encouraged to rebase back to `:stable` after testing a major release.
    - It can be behind on certain updates for a long time.

## Rolling Back System Updates

![GRUB Menu|690x402](../../img/GRUB_Menu.png)

Swap back to a previous system update if there are major issues after updating via the GRUB menu or the `rpm-ostree rollback` command or using the Bazzite Rollback Helper.

### Bazzite Rollback Helper

<this needs to be in src>
<img width="919" height="606" alt="image" src="https://github.com/user-attachments/assets/fa57e61b-87b0-40cc-a6bd-e79e47481e94" />

Rollback to a Bazzite build within the last 90 days.

A command-line utility that assists with **rollbacks**, **rebasing**, and **outputs information on your current Bazzite image**.

## Using `bazzite-rollback-helper`
Open a host terminal and **enter**:

```command
bazzite-rollback-helper
```

There is also an **alias** which is less typing for those on handhelds or HTPC setups without a keyboard:

```command
brh
```

#### Options Available:

- `list` = List images from the last 90 days that can rebased to.
- `rollback` = Rollback to the previous deployment on the next reboot.
- `current` = Show information about your current deployment and image.
- `rebase` = Switch to another build, update branch, or a different Fedora image **at your own risk**.

#### Usage

`bazzite-rollback-helper list` will list available bazzite images.

`bazzite-rollback-helper rebase <image-name:stable>` to rebase to an earlier image, update branch, or different Bazzite image (Desktop vs. Bazzite-Deck).  Find a version from the `list` command.

#### Rebasing to an older Bazzite image

**Example**: `bazzite-rollback-helper rebase stable-40.20240930.0`

Rebasing to an image will lock you to that OS image which means new features and security updates will no longer be applied until you rebase back to the Stable channel.

Get back to normal OS updates later after the bug has been squashed that prevents you from running the Stable branch:
`bazzite-rollback-helper rebase stable`

#### Video Guide

https://www.youtube.com/watch?v=XvljabnzgVo

## Other Update Topics

### How do I save my **current** deployment?

You can pin your **current** deployment with this **command**:

```command
sudo ostree admin pin 0
```

Unpin saved **current** deployment:

```command
sudo ostree admin pin --unpin 0
```
