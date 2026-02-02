---
authors:
  - "@nicknamenamenick"
tags:
  -  Software
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=2636", "fetched_at": "2024-09-03 16:43:08.564302+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## What is Flatpak?

![Flatpak|100x100, 100%](../img/Flatpak.png)

Flatpak is a universal containerized package format that tries to sandbox applications through flexible permissions that the application has access to on your system.  It is the **primary method of installing applications on Bazzite** _(outside of the small selection of software available in the [Bazzite Portal or as a `ujust` command](./ujust.md))_  and is recommended to use Flatpak over other formats for most software when possible.

## Installing Flatpaks

![Screenshot of the Bazaar app store|1649x1274, 50%](../img/Bazaar.png)

Flatpaks can be installed via the Bazaar app store.

**Alternatively open a host terminal and enter**:

```
flatpak install <application>
```

## Flatpak Remotes

Flatpaks can be hosted anywhere, but by default Bazzite ships with the [Flathub](https://flathub.org/) system remote which is a centralized repository of Linux applications.

The Flathub App Store is the definitive Linux app store and several Linux operating systems ship it out of the box which means the software ecosystem is one of the largest in the Linux community.

## Manage Flatpaks

Manage Flatpaks with [Flatseal](https://github.com/tchx84/Flatseal) and [Warehouse](https://github.com/flattool/warehouse) which are both pre-installed.

### Flatseal

**Flatseal** is for changing [application permissions](https://github.com/tchx84/Flatseal/blob/92e675e5ad2129f2aabf324261570eef442494f6/DOCUMENTATION.md) if necessary.

Alternatively, use KDE Plasma's system settings which has application permissions to adjust as well on KDE Plasma images.

Sometimes a project's website or [Github repository](<https://github.com/flathub/com.discordapp.Discord/wiki/Rich-Precense-(discord-rpc)#flatpak-applications>) contain information on what permissions need to be changed to perform certain functionality.

### Warehouse

**Warehouse** is a utility that gives users a graphical interface to downgrade applications, add other Flatpak sources outside of Flathub, and backup application user data. Its also a helpful tool for installing Flatpaks outside of Flathub, **at your own risk**.

### Project Website

https://flatpak.org/

<hr>

[**<-- Back to Installing and Managing Software on Bazzite**](./index.md)
