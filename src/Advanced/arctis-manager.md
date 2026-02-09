---
title: Installing Arctis Manager
search:
  exclude: true
---

# Installing Arctis Manager

## Purpose

This guide will walk you through the steps to install and run Arctis Manager in Distrobox then run it automatically at startup.
This guide works with [Linux-Arctis-Manager](https://github.com/elegos/Linux-Arctis-Manager) v1.6.3.

## Add udev Rules on Host:
This will let arctis manager access the usb device without needing root.
```
cd /etc/udev/rules.d/
sudo wget https://raw.githubusercontent.com/elegos/Linux-Arctis-Manager/refs/heads/main/udev/91-steelseries-arctis.rules
sudo udevadm control --reload-rules
sudo udevadm trigger
```

## Create & Enter A Distrobox Container:
```
distrobox create arctis --additional-flags "--privileged" --additional-packages "pw-cli"
distrobox enter arctis
```

## Install RPM (Inside A Distrobox Container):
```
wget https://github.com/elegos/Linux-Arctis-Manager/releases/download/v1.6.3/arctis-manager-1.6.3-1.fc42.x86_64.rpm
sudo dnf install arctis-manager-1.6.3-1.fc42.x86_64.rpm
```

## Export App (Inside A Distrobox Container):
```
distrobox-export -b /usr/local/bin/arctis-manager -el "Arctis Manager"
```

## Exit Distrobox Container & Run From Host:
(Inside distrobox)
```
exit
```

### Test Arctis Manager(<kbd>CTRL</kbd>+<kbd>C</kbd> once it starts correctly).
```
arctis-manager
```

## Create A User SystemD Service & Find the Path to `arctis-manager`:
```
touch ~/.config/systemd/user/arctis-manager.service
which arctis-manager
```
Copy the output from the last command and place in the ExecStart line in arctis-manager.service

```
nano ~/.config/systemd/user/arctis-manager.service
```
### `arctis-manager.service`
```
[Unit]
Description=Arctis Manager
After=graphical-session.target
Wants=graphical-session.target

[Service] 
ExecStart=/home/<username>/.local/bin/arctis-manager
Restart=always
RestartSec=2

[Install] 
WantedBy=graphical-session.target
```

### Reload and Launch
```
systemctl --user daemon-reload
systemctl --user enable --now arctis-manager.service
```
