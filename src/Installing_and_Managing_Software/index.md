---
title: Installing and Managing Applications
---

# Installing and Managing Applications

## Bazaar App Store (Flatpak) [Recommended for Most Apps]

![Bazaar|2840x2038, 50%](../img/Bazaar.jpg)

Flatpak is a universal containerized package format that tries to sandbox applications through flexible permissions that the application has access to on your system.  It is the **primary method of installing applications on Bazzite** and the most recommended way to install software over other formats outside of the few exceptions of software available in the Bazzite Portal which take priority. Flatpaks can be installed, upgraded, and uninstalled via the Bazaar app store.  The applications that are in Bazaar are from [Flathub](https://flathub.org/).

### Manage Flatpaks

Manage Flatpaks with [Flatseal](https://github.com/tchx84/Flatseal) and [Warehouse](https://github.com/flattool/warehouse) which are both pre-installed.

#### Flatseal

**Flatseal** is for changing [application permissions](https://github.com/tchx84/Flatseal/blob/92e675e5ad2129f2aabf324261570eef442494f6/DOCUMENTATION.md) if necessary. Alternatively, use KDE Plasma's system settings which has application permissions to adjust as well on KDE Plasma images.

Sometimes a project's website or [Github repository](<https://github.com/flathub/com.discordapp.Discord/wiki/Rich-Precense-(discord-rpc)#flatpak-applications>) contain information on what permissions need to be changed to perform certain functionality.

#### Warehouse

**Warehouse** is a utility that gives users a graphical interface to **downgrade applications**, install remote Flatpak sources outside of Flathub at your own risk, and backup application user data.

<hr>

## Homebrew (Command-Line Utilites)

<pic of bold brew>
    
!!! note

    Any package that requires root privileges will either need a rootful Distrobox container or has to be layered with `rpm-ostree`.

Homebrew is a package manager that installs packages into their own prefix. It is primarily used for command-line interface (CLI) and terminal user interface (TUI) applications. Homebrew can also install graphical applications using the `--cask` flag, but most are for macOS as support for casks on Linux is still developing. Use the Bold Brew application or the terminal using the command below to install packages.

Install packages in a host terminal with this **terminal command**:

```
brew install <package>
```

<hr>

## Bazzite Portal (`ujust` Commands)

<show screenshot of bazzite portal>

The Bazzite Portal application can install specialized software that ships with Bazzite as an installation script by the maintainers and contributors of the project.  Please note that _some_ of the software that can be installed from the Bazzite Portal can add layered packages to your installation which is generally not recommended.

Read the ujust page <link this>

<hr>

## Containers (Distrobox/Quadlet)

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=2640", "fetched_at": "2024-09-03 16:43:09.168054+00:00"}-->
<!-- ANCHOR_END: METADATA -->

### Distrobox Containers

![distrobox|510x413](../img/distrobox.png)

Run other minimal variants of popular Linux distributions in Bazzite inside of a container, and access each distribution's packages without any of their dependencies and libraries affecting the host machine.

- Containers are **not** virtual machines.
- Containers are intended to be **disposable** and may run into issues where they need to be recreated.
- Using this method to obtain software **requires knowledge of how traditional Linux operating systems install packages**.
  - Create a test container to familiarize yourself with basic Linux commands before diving in further.

Distrobox containers run sub-systems of other popular [Linux distributions](https://distrobox.it/compatibility/#containers-distros) with access to their package managers (`apt`, `dnf`, `pacman`, etc.) and their package formats (`.deb`/`.rpm`) and any additional repositories like the [AUR](https://aur.archlinux.org/). Distrobox containers can be used for both **development environments** and **installing applications that are not available in any of the other installation methods** which can be exclusive to specific package managers.

![i use arch btw|1022x822, 75%](../img/i_use_arch_btw.png)

<sub><sup>i use arch (in a container) btw.</sup></sub>

**Linux Distribution Examples**:

| OS                                  | Package Manager    | Search for Packages                                                       |
| ----------------------------------- | ------------------ | ------------------------------------------------------------------------- |
| [Fedora][fedora]                    | [`dnf`][dnf]       | [Fedora Packages][fedora_pkgs] / [COPR Packages][copr]                    |
| [Arch][arch]                  | [`pacman`][pacman] | [Arch Linux Packages][arch_pkgs] / [AUR Packages][aur_pkgs]               |
| [Debian][debian] / [Ubuntu][ubuntu] | [`apt`][apt]       | [Debian Packages][deb_pkgs] / [Ubuntu Packages][ubuntu_pkgs] ([PPA][ppa]) |
| [openSUSE][osuse]                   | [`zypper`][zypper] | [openSUSE Packages][osuse_pkgs]                                           |
| [Void][void]                  | [`xbps`][xbps]     | [Void Linux Packages][void_pkgs]                                          |
| [Alpine][alpine]              | [`apk`][apk]       | [Alpine Linux Packages][alpine_pkgs]                                      |

#### Distrobox Graphical Interface

![Distroshelf|970x752, 75%](../img/distroshelf_fixedcrop.png)

Distrobox containers can be created and managed graphically with [**DistroShelf**](https://github.com/ranfdev/DistroShelf) which is pre-installed.

#### Distrobox Video Guide

https://youtu.be/5m0YfIiypwA

[fedora]: https://fedoraproject.org/
[dnf]: https://docs.fedoraproject.org/en-US/quick-docs/dnf/
[fedora_pkgs]: https://packages.fedoraproject.org/index-static.html
[copr]: https://copr.fedorainfracloud.org/
[arch]: https://archlinux.org/
[pacman]: https://wiki.archlinux.org/title/Pacman
[arch_pkgs]: https://archlinux.org/packages/
[aur_pkgs]: https://aur.archlinux.org/packages?SB=l&SO=d
[debian]: https://www.debian.org/
[ubuntu]: https://ubuntu.com/
[apt]: https://ubuntu.com/server/docs/package-management
[deb_pkgs]: https://packages.debian.org/stable/
[ubuntu_pkgs]: https://packages.ubuntu.com/
[ppa]: https://launchpad.net/ubuntu/+ppas
[osuse]: https://get.opensuse.org/
[zypper]: https://documentation.suse.com/smart/systems-management/html/concept-zypper/index.html
[osuse_pkgs]: https://search.opensuse.org/packages/
[void]: https://voidlinux.org/
[xbps]: https://docs.voidlinux.org/xbps/index.html
[void_pkgs]: https://voidlinux.org/packages/
[alpine]: https://www.alpinelinux.org/
[apk]: https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper
[alpine_pkgs]: https://pkgs.alpinelinux.org/packages

### Quadlet

![podman|385x358, 50%](../img/podman.png)

Quadlet is a feature of [podman](https://podman.io/) that allows a user to run a container as [systemd](https://systemd.io/) units. It works by using a declarative syntax like [docker compose](https://docs.docker.com/compose/) but integrates to systemd and uses podman as a backend.

#### Quadlet Usecases

Quadlet can be used for application packaged as a container such as a server application. You can find a lot of examples of containerized applications from [Linux Server](https://docs.linuxserver.io/images/).

#### Managing Quadlet

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

#### Quadlet File Locations

You can put your quadlet in these locations sorted by priority:

- `$XDG_RUNTIME_DIR/containers/systemd/` - Usually used for temporary quadlet
- `~/.config/containers/systemd/` - Recommended location
- `/etc/containers/systemd/users/$(UID)`
- `/etc/containers/systemd/users/`

!!! note

    If you want your service to start even when you are not logged in, run `loginctl enable-linger $USER` to start it automatically.

#### Running Quadlet on Startup

You may want to run your quadlet automatically on startup, just add an install section to the quadlet file if you want it to autostart. Most of the time `default.target` is what you want but if you need other target you can read about that on systemd docs.

```
[Install]
WantedBy=default.target
```

#### Converting Docker Compose to Quadlet Unit

You will find that most of containerized apps in the web are built using docker compose. Even the Linux Server that is linked above has all containers documented using a compose file. So you will need to convert it first, before running it as quadlet, fortunately you can use [podlet](https://github.com/containers/podlet) to help you converting it.

!!! note

    By default quadlet require full repository name. Most images are in docker hub so add `docker.io/` (e.g "nginxinc/nginx-unprivileged" becomes "docker.io/nginxinc/nginx-unprivileged") to it.

#### Running Rootful Container as Quadlet

While ideally you would run all containers using rootless podman, sadly not all containers will work with it.  Use rootful podman by using a different quadlet path and run using root systemctl (without `--user`).

Rootful Quadlet Paths
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

#### Troubleshooting

If your quadlet for some reason isn't found or starting, you can debug the container unit using `/usr/libexec/podman/quadlet -dryrun` for system quadlet or `/usr/libexec/podman/quadlet -user -dryrun` for user quadlet.

#### Useful Links

- https://podman.io/=
- https://docs.podman.io/en/stable/markdown/podman-systemd.unit.5.html
- https://www.redhat.com/en/blog/quadlet-podman

<hr>

## AppImage (Portable Applications Downloaded from Trusted Source)

![AppImage|100x100, 100%](../img/AppImage.png)

AppImage is a universal package format that attempts to bundle every dependency that an application needs into one portable file. They can be installed by downloading any file with a `.AppImage` file extension and then giving it executable permissions in the file's properties so the application can run properly. Like Windows executable files, they are usually found on the project's website to download.

<hr>

## System-Level Package Layering (`rpm-ostree` Commands) [_**Not Recommended**_]

Add software on top of the Bazzite image.  Use as a last resort and specifically for packages that cannot be installed from Homebrew or ran inside of a container.  Layered packages can break system upgrades until removed due to dependency issues since the package will have to be updated with the rest of the image.  It also causes upgrades to take longer to run.

<link to rpm-ostree guide>

<hr>

## Other

Bazzite can also run Windows and Android applications too!

### Windows Executables

**Use a [WINE](https://www.winehq.org/) front-end**:

- [**Steam**](https://store.steampowered.com/) (_pre-installed_) has a Windows compatibility layer built-in.
- [**Lutris**](https://lutris.net/about) (_pre-installed_) for non-Steam PC games and non-gaming software.
- [**Faugus Launcher**](https://github.com/Faugus/faugus-launcher) (_Available in Bazaar_) as an alternative to Lutris.
- [**Heroic Games Launcher**](https://heroicgameslauncher.com/) (_Available in Bazaar_) for proper Epic Games, GOG, and Amazon Games integration.
- [**Greenlight**](https://flathub.org/en/apps/io.github.unknownskl.greenlight) (_Available in Bazaar_) for streaming Windows store games and Gamepass. <small>(**Streaming only**)</small>
- [**WineZGUI**](https://github.com/fastrizwaan/WineZGUI) (_Available in Bazaar_) for less complicated Windows applications that don’t require special considerations.

>Read the [**Bazzite Gaming Guide**](/Gaming/index.md) for more information on running Windows games on Linux.

### Android Apps

Follow the [**Waydroid Setup Guide**](./Waydroid_Setup_Guide.md) to install Android applications on Bazzite.

### Installing Specific Software

Tutorials on installing software like setting up [ZeroTier](<link guide>) to [hosting a Minecraft server](<link guide>) can be found in the [**Installing Specific Software Guides**](<link to index>)
