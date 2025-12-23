---
authors:
  - "@asen23"
  - "@noelmiller"
tags:
  -  Software
preview:
  alpha: 70
  image: "../img/podman.png"
description: "Run services."
---

## What is Quadlet?

![podman|385x358, 50%](../img/podman.png)

Quadlet is a feature of [podman](https://podman.io/) that allows a user to run a container as [systemd](https://systemd.io/) units. It works by using a declarative syntax like [docker compose](https://docs.docker.com/compose/) but integrates to systemd and uses podman as a backend.

### Quick Example:

Create a file called `~/.config/containers/systemd/nginx.container` with content below.
```
[Container]
ContainerName=nginx
Image=docker.io/nginxinc/nginx-unprivileged
AutoUpdate=registry
PublishPort=8080:8080
```

Save it and run the code below.

```sh
systemctl --user daemon-reload
systemctl --user start nginx
xdg-open localhost:8080
```

![nginx welcome page|1296x400](../img/nginx_welcome.png)

## Use Cases

Quadlet can be used for application packaged as a container such as a server application. You can find a lot of examples of containerized applications from [Linux Server](https://docs.linuxserver.io/images/).

## Managing Quadlet

Quadlet can be managed like any other systemd service using below command.

Checking quadlet status
```sh
systemctl --user status nginx
```

Stopping quadlet
```sh
systemctl --user stop nginx
```

You can see more commands in [man systemctl](https://man.archlinux.org/man/systemctl.1) or [tldr systemctl](https://tldr.inbrowser.app/pages/linux/systemctl).

!!! note

    Do not add the `.container` suffix when you interact with systemctl or it will gives unit not found error

### Quadlet file location

You can put your quadlet in these location sorted by priority.
- `$XDG_RUNTIME_DIR/containers/systemd/` - Usually used for temporary quadlet
- `~/.config/containers/systemd/` - Recommended location
- `/etc/containers/systemd/users/$(UID)`
- `/etc/containers/systemd/users/`

!!! note

    If you want your service to start even when you are not logged in, run `loginctl enable-linger $USER` to start it automatically.

### Running Quadlet on Startup

You may want to run your quadlet automatically on startup, just add an install section to the quadlet file if you want it to autostart. Most of the time `default.target` is what you want but if you need other target you can read about that on systemd docs.
```
[Install]
WantedBy=default.target
```

For example:
```
[Container]
ContainerName=nginx
Image=docker.io/nginxinc/nginx-unprivileged
AutoUpdate=registry
PublishPort=8080:8080

[Install]
WantedBy=default.target
```

!!! note

    You don't need to run `systemctl enable` as the service file are generated. You also cannot run it anyway.

### Converting Docker Compose to Quadlet Unit

You will find that most of containerized apps in the web are built using docker compose. Even the Linux Server that is linked above has all containers documented using a compose file. So you will need to convert it first, before running it as quadlet, fortunately you can use [podlet](https://github.com/containers/podlet) to help you converting it.

!!! note

    By default quadlet require full repository name. Most image are in docker hub so you can just add `docker.io/` (e.g "nginxinc/nginx-unprivileged" become "docker.io/nginxinc/nginx-unprivileged")

### Running Rootful Container as Quadlet

While ideally you would run all containers using rootless podman, sadly not all containers will work with it. If you noticed in the beginning, this guide used nginx-unprivileged rather than the normal nginx, this is because it needs root to function. To use rootful podman, you will need to use different quadlet path and run using root systemctl (without `--user`).

Rootful Quadlet Path
- `/run/containers/systemd/` - Temporary quadlet
- `/etc/containers/systemd/` - Recommended location
- `/usr/share/containers/systemd/` - Image defined

### Common Quadlet Key Description
| Option        | Example                                     | Description                                                                              |
| ------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------- |
| ContainerName | ContainerName=nginx                         | Name of the container.                                                                   |
| Image         | Image=docker.io/nginxinc/nginx-unprivileged | Container image that you want to use.                                                    |
| AutoUpdate    | AutoUpdate=registry                         | Source to check for update. The value is either `registry` or `local`.                   |
| PublishPort   | PublishPort=8080:8080                       | Port opened by container. (HOST_PORT:CONTAINER_PORT)                                     |
| Volume        | Volume=/path/to/data:/data:z                | Link host folder with container folder. (HOST_FOLDER:CONTAINER_FOLDER:OPTION)            |
| Network       | Network=host                                | Network used by container. The value can be `host`, `none`, or user defined network name |

!!! note

    The `z` option in volume is to prevent selinux from blocking access to the folder. You can read more [here](https://docs.podman.io/en/stable/markdown/podman-run.1.html#volume-v-source-volume-host-dir-container-dir-options).

## Example

!!! note

    Don't forget to run `systemctl --user daemon-reload` after creating the file

### Minecraft Server

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

### Plex Server

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

    You can find the list of timezones [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
!!! note

    Use absolute path for volume, e.g `/home/username/plex/config`.
!!! note

    You can mount multiple volumes for your media, e.g `Volume=/path/to/media:/tv:z` and `Volume=/path/to/another/media:/movie:z`. Consult the documentation for more info.

#### Video Tutorial
https://www.youtube.com/watch?v=xTVFmvyZGpg

### Samba Server (Rootful)

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

    You can find a list of timezones [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
!!! note

    Use absolute path for volumes, e.g `/home/username/samba/guest`.

## Troubleshooting

If your quadlet for some reason isn't found or starting, you can debug the container unit using `/usr/libexec/podman/quadlet -dryrun` for system quadlet or `/usr/libexec/podman/quadlet -user -dryrun` for user quadlet.

## Project Website

https://podman.io/

### Useful Links
- https://docs.podman.io/en/stable/markdown/podman-systemd.unit.5.html
- https://www.redhat.com/en/blog/quadlet-podman

<hr>

[**<-- Back to Installing and Managing Software on Bazzite**](./index.md)
