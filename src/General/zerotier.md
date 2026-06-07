---
title: "ZeroTier Setup"
authors:
  - "@Zeglius"
  - "@adokitkat"
  - "@Ruvonn"
tags:
  -  Community
search:
  exclude: true
---

# ZeroTier Setup

## Installing

!!! warning
    Setup requires package layering and is **not recommended**.
    
Add ZeroTier repository to yum by copying the following to the terminal (to paste copied text in the terminal: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>)

```sh
sudo tee >/dev/null /etc/yum.repos.d/zerotier.repo <<'EOF'
[zerotier]
name=ZeroTier, Inc. RPM Release Repository
baseurl=https://download.zerotier.com/redhat/fc/$releasever
enabled=1
gpgcheck=1
gpgkey=https://download.zerotier.com/contact@zerotier.com.gpg
EOF
```

Install ZeroTier One:

```sh
sudo rpm-ostree install zerotier-one
```

Reboot the system, and then enable ZeroTier service by running this command in the terminal:

```sh
sudo systemctl enable --now zerotier-one
```

## Uninstalling

Select, copy and paste the following to the terminal (pasting is <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>)

```sh
sudo systemctl disable zerotier-one.service
sudo rpm-ostree uninstall zerotier-one
```

Reboot, and run this at the terminal:

```sh
sudo rm -fv /etc/yum.repos.d/zerotier.repo
```

## Fix not seeing your teammates in games relying on broadcast, e.g., Warcraft III LAN

_(Route broadcast through the ZeroTier network interface)_

Get your ZeroTier network interface name by running: `ip a` (compare the IP addresses at the inet/inet6 entries to the ones in your ZeroTier web dashboard)

Add the route: `sudo ip route add 255.255.255.255 dev <INTERFACE_NAME>` (replace `<INTERFACE_NAME>` with the name you got from `ip a`, likely `ztbto7vntf`)

Note that this change will be ephemeral, so after a restart of your system you will have to add the route again.

If you want NetworkManager to automatically create the route as soon as the ZeroTier interface comes up run the following from your terminal:

```sh
sudo tee /etc/NetworkManager/dispatcher.d/99-zerotier-broadcast.sh >/dev/null <<'EOF' && sudo chmod 755 /etc/NetworkManager/dispatcher.d/99-zerotier-broadcast.sh && sudo systemctl restart zerotier-one.service
#!/bin/bash
INTERFACE=$1
ACTION=$2

# Check if the interface starts with "zt" and is coming UP
if [[ "$INTERFACE" =~ ^zt ]] && [ "$ACTION" = "up" ]; then
  ip route replace 255.255.255.255 dev "$INTERFACE"
fi
EOF
```
