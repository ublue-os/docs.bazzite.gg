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

[![GitHub Release](https://img.shields.io/github/v/release/elegos/Linux-Arctis-Manager?label=Latest%20Release&color=brightgreen&logo=github&logoColor=white)](https://github.com/elegos/Linux-Arctis-Manager/releases)

## Purpose
This guide walks you through installing [**Linux-Arctis-Manager**](https://github.com/elegos/Linux-Arctis-Manager) (v2.0.4+) using Distrobox. This method works without package layering or temporarily turning off the read-only root filesystem while providing the manager with necessary hardware access and background services. For a list of currently supported devices as well as advanced documentation, please check the linked repository.

## Installation 

Run the following script to install:

```bash
curl -LsSf https://raw.githubusercontent.com/elegos/Linux-Arctis-Manager/refs/heads/develop/scripts/distrobox.sh | sh
```

!!! note
    
    For Linux operating systems like Bazzite (image-based / read-only root filesystem), the app behaves like a native installation rather than an isolated container. Because Distrobox mounts your `/home`, `/var`, and `/etc` directly, the manager can interact with the system services and configuration files it needs to function.

### Enable Autostart (Optional)
To launch the system tray app automatically on login:

```bash
ln -sf ~/.local/share/applications/ArctisManagerSystray.desktop ~/.config/autostart/
```

## Uninstall / Cleanup
1. Stop and disable the service:

   ```bash
   systemctl --user disable --now arctis-manager
   rm ~/.config/systemd/user/arctis-manager.service
   ```

2. Remove the container:
 
   ```bash
   distrobox-rm -f arctis-manager
   ```

3. Remove leftover host files:

   ```bash
   # desktop menu entries
   rm -f ~/.local/share/applications/ArctisManager.desktop
   rm -f ~/.local/share/applications/ArctisManagerSystray.desktop
   rm -f ~/.config/autostart/ArctisManagerSystray.desktop

   # udev rules
   sudo rm -f /etc/udev/rules.d/91-steelseries-arctis.rules

   # user preferences and virtual environment
   rm -rf ~/.config/arctis_manager
   rm -rf ~/.local/share/pipx/venvs/linux-arctis-manager
   ```   
