---
title: Post-Installation Setup
---

# Post-Installation Setup

## First Boot Setup

![Rollbacks|690x402, 50%](../../img/GRUB_Menu.png)

The first boot will show a screen showing your current and last deployment. It is important to note that the GRUB menu can be used to rollback Bazzite deployments if you encounter issues.

Read more about this in the [Updates, Rollback, and Rebasing documentation](../../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md).

It is important to configure the system settings on a first boot to personalize your desktop especially if you notice the scaling is incorrect on first-boot.

## Configure system settings

### Scaling Settings

![Display Settings (KDE Plasma)|690x370, 75%](../../img/KDE_Display_Settings.png)
**_KDE Plasma's System Settings application_**

![Display Settings (GNOME)|690x344, 75%](../../img/GNOME_Display_Settings.png)
**_GNOME's Settings application_**

Adjust the system settings to your preference.

### Changing Default Password
<sub> (If it wasn't changed in the installer) </sub>

![KDE Plasma's Change Password|584x500, 75%](../../img/change-pass.png)

Change it in the settings of Desktop Mode under the "User" category.

### Setting Up Steam Gaming Mode (Bazzite-Deck Only)

![Gaming Mode Setup|690x442, 50%](../../img/pLvHB1NAMlb3ghsR72q7l9Auj8B.jpeg)
^^^GET A NEW IMAGE THIS ONE IS BAD!

After completing all of the above, then your next boot will be in Steam Gaming Mode which requires additional setup for Steam.

>[Read the Bazzite-Deck documentation](<link>)

## Dual Boot Post-Configuration Setup

Show both your Windows and Bazzite installations in the GRUB menu to select from at boot by entering this **command into the terminal**:

```
ujust regenerate-grub
```

#### Bazzite as Primary Boot

If the `OS Boot Manager` has set `Windows Boot Manager` to be the first boot priority, then this may result in booting directly into Windows after the install instead of Bazzite. You may have to fix this in your BIOS settings.

Take note that the GRUB menu might not show up. In such case, spam the <kbd>↓</kbd> key when booting up.

#### Boot into Windows from Steam

Adds a script in Steam to boot into Windows.

```
ujust setup-boot-windows-steam
```

#### Expanding storage size in a Windows dual-boot scenario

!!! note

    This is for future reference after dual-booting for a while.

**Watch this video tutorial on how to expand the storage**:

https://www.youtube.com/watch?v=uy8mi1pAj8E

## Recommended Next Steps

### Configure your system with the Bazzite Portal application

<screenshot the bazzite portal>

### Install additional software with the Bazaar app store

![Screenshot of the Bazaar app store|1649x1274, 50%](../../img/Bazaar.png)

### Play video games

Enjoy using Bazzite!
