---
title: Updates, Rollbacks, and Rebasing
---

# Updates, Rollbacks, and Rebasing

## Updates

Updates are automatic on Desktop images and manually done on Bazzite-Deck images, and both Bazzite variants upgrade everything at both a system-level and user-installed applications during the updating process.

> [**Updating Guide**](./updating_guide.md)

## Rollbacks

Swap back to a previous system update if there are major issues after updating via the GRUB menu or the `rpm-ostree rollback` command.

> [**Rollbacks Guide**](./rolling_back_system_updates.md)

## Rebasing

!!! important

    Do **not** rebase to a different desktop environment than the one you are currently using, please backup and reinstall instead.

Rebase to Bazzite builds from the last 90 days, change Bazzite update channels, swap between the Desktop and Bazzite-Deck images, or move completely to a different Fedora Atomic Desktop image.

> [**Rebase Guide**](./rebase_guide.md)

## Bazzite Rollback Helper Tool

Utility to assist with rolling back to older Bazzite images, changing update branches, or swapping to a different Bazzite image.

> [**Bazzite's Rollback Helper Utility Guide**](./bazzite_rollback_helper.md)
