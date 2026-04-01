---
title: Installing Arctis Manager
authors:
  - "@elegos"
  - "@ifeign"
  - "@rdamron"
tags:
  - Community
search:
  exclude: true
---

# Installing Arctis Manager

## Purpose
This guide walks you through installing [**Linux-Arctis-Manager**](https://github.com/elegos/Linux-Arctis-Manager) (v2.0.4+) using Distrobox. This method works without package layering or temporarily turning off the read-only root filesystem while providing the manager with necessary hardware access and background services. For a list of currently supported devices as well as advanced documentation, please check the linked repository.

## Installation 

Run the following script to install:

```bash
curl -LsSf https://raw.githubusercontent.com/elegos/Linux-Arctis-Manager/refs/heads/develop/scripts/distrobox.sh | sh
```
> [!NOTE]
>
> For Linux operating systems like Bazzite (image-based / read-only root filesystem), the app behaves like a native installation rather than an isolated container. Because Distrobox mounts your `/home`, `/var`, and `/etc` directly, the manager can interact with the system services and configuration files it needs to function.

### Enable Autostart (Optional)
To launch the system tray icon automatically on login, copy its desktop entry to your autostart folder:

```bash
cp ~/.local/share/applications/ArctisManagerSystray.desktop ~/.config/autostart/
```

### Verification (Optional)
To verify the daemon is running and can see your device, run this on your host:

```bash
lam-cli devices list
```

