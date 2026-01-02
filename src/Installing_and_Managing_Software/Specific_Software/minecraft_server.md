---
title: Minecraft Server Hosting Guide
---

# Minecraft Server Hosting Guide

## Preface

Using a [Quadlet service] <link to quadlet service subsection on installaing and managing apps doc>

!!! note

    Don't forget to run `systemctl --user daemon-reload` after creating the file

Documentation: https://docker-minecraft-server.readthedocs.io/en/latest
Quadlet File:
```
# ~/.config/containers/systemd/minecraft.container
[Container]
ContainerName=minecraft
Environment=EULA=TRUE
Image=docker.io/itzg/minecraft-server
AutoUpdate=registry
PublishPort=25565:25565
Volume=/path/to/data:/data:z

# Remove if you don't want autostart
[Install]
WantedBy=default.target
```
!!! note

    Use absolute path for volume, e.g `/home/username/minecraft/data`.
