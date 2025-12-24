<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=2647", "fetched_at": "2024-09-03 16:43:17.164020+00:00"}-->
<!-- ANCHOR_END: METADATA -->

# `bazzite-rollback-helper`

![Bazzite Rollback Helper Command|636x500](../../img/Bazzite_Rollback_Helper_Command.png)

!!! important

    Read the [rollback](./rolling_back_system_updates.md) and [rebasing](./rebase_guide.md) guides to understand what rebasing and rolling back on Bazzite entails.

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

### Options Available:

- `list` = List images from the last 90 days that can rebased to.
- `rollback` = Rollback to the previous deployment on the next reboot.
- `current` = Show information about your current deployment and image.
- `rebase` = Switch to another build, update branch, or a different Fedora image **at your own risk**.

### Usage

`bazzite-rollback-helper list` will list available bazzite images.

`bazzite-rollback-helper rebase <image-name:stable>` to rebase to an earlier image, update branch, or different Bazzite image (Desktop vs. Bazzite-Deck).  Find a version from the `list` command.

#### Rebasing to an older Bazzite image

**Example**: `bazzite-rollback-helper rebase stable-40.20240930.0`

Rebasing to an image will lock you to that OS image which means new features and security updates will no longer be applied until you rebase back to the Stable channel.

Get back to normal OS updates later after the bug has been squashed that prevents you from running the Stable branch:
`bazzite-rollback-helper rebase stable`

## Video Guide

https://www.youtube.com/watch?v=XvljabnzgVo

> ### Key Takeaways:
>
> **Updates**: Upgrades both system and installed software.
> **Rollbacks**: Return to a previous deployment after a bad system upgrade.
> **Rebasing**: Use the `bazzite-rollback-helper` command in the terminal.

<hr>

[**<-- Back to Updates, Rollback, and Rebasing Guide**](./index.md)
