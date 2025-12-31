---
title: Plex Media Server Guide
---

# Plex Media Server Guide

## Preface

Using a Quadlet service...

Documentation: https://github.com/plexinc/pms-docker
Quadlet File:
```
# ~/.config/containers/systemd/plex.container
[Container]
ContainerName=plex
Environment=TZ=Your/TimeZone
Image=docker.io/plexinc/pms-docker
AutoUpdate=registry
Network=host
Volume=/path/to/config:/config:z
Volume=/path/to/transcode:/transcode:z
Volume=/path/to/media:/data:z

# Remove if you don't want autostart
[Install]
WantedBy=default.target
```
!!! note

    You can find list of timezones [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
!!! note

    Use absolute path for volume, e.g `/home/username/plex/config`.
!!! note

    You can mount multiple volumes for your media, e.g `Volume=/path/to/media:/tv:z` and `Volume=/path/to/another/media:/movie:z`. Consult the documentation for more info.


## Video Tutorial
https://www.youtube.com/watch?v=xTVFmvyZGpg
