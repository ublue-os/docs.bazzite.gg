---
title: Rollbacks
---

# Rollbacks

## Rolling Back Upgrades

Swap back to a previous system update if there are major issues after updating via the GRUB menu or the `rpm-ostree rollback` command or using the Bazzite Rollback Helper.

## How do I rollback a system update?

A rollback to the previous system deployment can be done by **entering this command in a host terminal**:

```command
rpm-ostree rollback
```

### Using the Bazzite Rollback Helper (`brh`) Utility

Rollback to an older Bazzite image from the last 90 days using the **[`brh` command](../Updates_Rollbacks_and_Rebasing/bazzite_rollback_helper.md)**.

### Before Booting Bazzite (GRUB)

![GRUB Menu with two deployments and UEFI Firmware Settings](../../img/GRUB_Menu.png)

!!! note

    Controls may vary with different handhelds or HTPC setups to navigate the menu and an external physical keyboard may be required to rollback in GRUB.

Rollback can also be done in the GRUB menu (which appears before booting into Bazzite) by choosing the previous boot entry before booting to the desktop. It shows your current (`:0`) and your previous (`:1`) deployments. Your personal files will **not** be affected by this, and you can still update to the newest builds after rolling back.

## How do I save my **current** deployment?

You can pin your **current** deployment with this **command**:

```command
sudo ostree admin pin 0
```

In a host terminal for a backup save state of your **current** deployment to rollback to if a new system update causes issues.

## How do I save my **previous** deployment?

You can pin your **previous** deployment with this **command**:

```command
sudo ostree admin pin 1
```

In a host terminal for a backup save state of your **previous** deployment to rollback if the current deployment has issues.

## How do I unpin a deployment if I saved it?

Unpin saved **current** deployment:

```command
sudo ostree admin pin --unpin 0
```

Unpin saved **previous** deployment:

```command
sudo ostree admin pin --unpin 1
```

View all deployment index numbers:

```command
rpm-ostree status -v
```

Unpin **saved** deployment:

```command
sudo ostree admin pin --unpin <index number>
```

## Application Update Downgrades

Read about the pre-installed Warehouse application to downgrade applications in the [**Bazaar App Store (Flatpak) documentation**](/Installing_and_Managing_Software/Flatpak.md#warehouse).
