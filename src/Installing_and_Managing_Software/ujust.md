---
title: ujust Commands
---

# `ujust` Commands

## Usage

![Shell Scripts (.sh)|96x96, 100%](../img/Shell_Scripts__sh.png)

!!! note

    Use the [Bazzite Portal](./Bazzite_Portal.md) application as a graphical interface for popular `ujust` commands.

`ujust` commands that automate tasks using scripts which can be utilized to for system configuration and maintenance. 

It also can install specialized software that ships with Bazzite as an installation script by the maintainers and contributors of the project.

!!! info 
  
    Please note that _some_ of the software that can be installed from `ujust` commands can add [**layered packages**](../rpm-ostree.md) to your installation which is generally not recommended, but is rather a compromise between ease of use and update stability. 
    
    Bazzite maintainers try to keep them updated to avoid breakages, though the general advise is still to keep as little layered packages as possible and to reset ostree if you encounter any difficulties with updates.

---

### Showing Available Commands

The following command show a list of available scripts:

```bash
ujust
```

![ujust command list|3041x1128, 25%](../img/ujust_command_list.png)

---

### Interactive Picker

The following command will show a TUI of `ujust` commands that you can choose to execute with arrow keys or mouse input:

!!! info "Using arguments or flags is not available when using this method. However, most commands provide an interactive mode when ran without arguments/flags."

```bash
ujust --choose
```

![ujust TUI|690x403](../img/ujust_TUI.png)

---

### Manually Entering Commands

**Find the command you want to use and enter**:

```bash
ujust <command>
```

You can search for specific commands by **entering**:

```bash
ujust | grep "<search keyword(s)>"
```

---

### Common Script Naming Style

- `install-`: Install programs that is otherwise difficult or impossible to set up with other methods.

!!! warning "Some of the applications avaliable to install as a `ujust` command can end up [layering packages](./rpm-ostree.md) to your system. Bazzite recommends keeping layered packages to a minimum."

- `get-`: Install Decky plugins, though some other function also use this prefix.
- `setup-`: Install program, provides uninstall and configuration options for after install.
- `configure-`: Configure something that came by default on the image.
  - If it must be installed first, then it will be prefixed with `setup-`.
- `toggle-`: Enables or disables a feature or setting.
  - Selection might be automatic or manual depending on implementation.
- `fix-`: Fixes, patches or workarounds for an issue.
- `distrobox-`: Distrobox exclusive verb intended to make container usage easier.
- `foo`: Replace this with whatever the command is called.
  - These are shortcuts that we have deemed necessary to not have a verb.
  - **Examples**: `ujust update` & `ujust enroll-secureboot-key`
  
---

## View each `ujust` script's source code

You may use the following command to view each script's source code:

```bash
ujust --show <command>
```

Alternatively, you may also find all local `ujust` scripts in
`/usr/share/ublue-os/just`

!!! note

    This directory also shows **hidden** `ujust` commands.

## `ujust` Script Overview

Below is a non-exhaustive list of common `ujust` scripts and their description. There are much more available which are viewable with `ujust --choose` as mentioned above.

---

### Maintenance Scripts

| Command | Description |
| --- | --- |
| `ujust update` | Updates system, flatpaks, and containers all at once |
| `ujust configure-grub` | Configures GRUB boot menu visibility |
| `ujust fix-reset-steam` | Reset the Steam folder back to a fresh state without removing games, music, saves, etc. Very useful if Steam is giving trouble or if you are getting a blank screen in Game Mode |
| `ujust fix-proton-hang` | Force terminates all processes related to wine and proton. Useful if you can't launch games after a game fails to close properly |
| `ujust bios` | Reboots straight into this device's BIOS/UEFI screen |
| `ujust restart-pipewire` | Crackling audio? Restarting Pipewire sometimes fixes that |
| `ujust enroll-secure-boot-key` | Enrolls the Nvidia driver & KMOD signing key for secure boot. You'll need this if you want to use Bazzite with Secure Boot enabled |
| `ujust clean-system` | Cleans up old unused podman images, volumes, flatpak packages, and rpm-ostree content |

---

### Configuration/Enable Scripts

| Command | Description |
| --- | --- |
| `ujust configure-waydroid` | A configuration helper for Waydroid. More information in [Waydroid Setup Guide](../Installing_and_Managing_Software/Waydroid_Setup_Guide.md) |
| `ujust setup-virtualization` | Setup and configure virtualization and VFIO |
| `ujust setup-sunshine` | Toggle Sunshine Game Streaming |
| `ujust setup-luks-tpm-unlock` | Enable auto LUKS unlock via TPM |
| `ujust setup-decky` | Install and configure Decky Loader |
| `ujust setup-boot-windows-steam` | Adds a script in Steam to boot Windows, which is useful for dual-boot setups |
| `ujust enable-tailscale` | Enables support for Tailscale |
| `ujust bazzite-cli` | Bazzite CLI mod for Bluefin-styled CLI enhancements. More information in [Bazzite Command Line Tools](../Advanced/bazzite-cli.md) |

---

### Troubleshooting Scripts

| Command | Description |
| --- | --- |
| `ujust logs-last-boot` | Shows all system logs from last boot |
| `ujust logs-this-boot` | Shows all system logs from this boot |
| `ujust device-info` | Gathers useful device information to a pastebin. This is very useful for providing information when creating support tickets. |

---

## Project Website

https://just.systems/man/en/
