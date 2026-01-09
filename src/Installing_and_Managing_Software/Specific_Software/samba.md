---
title: Samba Server
---

# Setting Up A Samba Server

## Preface

Use a [Quadlet service](../index.md#quadlet) to host a Samba server on Bazzite.

## Setup

Documentation: https://github.com/ServerContainers/samba
Quadlet File:
```
# /etc/containers/systemd/samba.container
[Container]
Environment=ACCOUNT_username=password
# Protected share with write access
Environment="SAMBA_VOLUME_CONFIG_protected=[My Share]; path=/shares/protected; valid users = username; guest ok = no; read only = no; browseable = yes"
# Open share with readonly access
Environment="SAMBA_VOLUME_CONFIG_guest=[Guest Share]; path=/shares/guest; guest ok = yes; browseable = yes"
Image=ghcr.io/servercontainers/samba:smbd-only-latest
AutoUpdate=registry
Network=host
Volume=/path/to/protected:/shares/protected:z
Volume=/path/to/guest:/shares/guest:z

# Remove if you don't want autostart
[Install]
WantedBy=default.target
```
!!! note

    You can find list of timezone [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
!!! note

    Use absolute path for volume, e.g `/home/username/samba/guest`.
