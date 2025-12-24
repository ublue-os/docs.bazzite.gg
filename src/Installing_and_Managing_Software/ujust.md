<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=2638", "fetched_at": "2024-09-03 16:43:04.643633+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## What is `ujust`?

![Shell Scripts (.sh)|96x96, 100%](../img/Shell_Scripts__sh.png)

Technically `ujust` is **not** a package format, but are convenience commands that automate tasks using scripts which can be utilized to install specific software. There are also commands for system configuration and maintenance included here, so run `ujust` commands **at your own risk.**  If an application is available to install via a `ujust` command but can also be obtained as a [Flatpak](/Installing_and_Managing_Software/Flatpak/), then it is recommended to use `ujust` command over installing the Flatpak version on Bazzite.

### Using `ujust`

![ujust command list|690x411](../img/ujust_command_list.png)

!!! note

    Use the Bazzite Portal application as a graphical interface for popular `ujust` commands.

Open a host terminal and **enter**:

```
ujust
```

<sub>This will output a list of available commands.</sub>

![ujust TUI|690x403](../img/ujust_TUI.png)

```
ujust --choose
```

This will show a terminal user interface of `ujust` commands that you can choose to execute with arrow keys or mouse input.

!!! attention

    Commands that require values or flags do not function with this method.

### Manually entering commands

**Find the command you want to use and enter**:

```
ujust <command>
```

You can search for specific commands by **entering**:

```
ujust | grep "<search keyword(s)>"
```

- `install-`: Install program, there is no configuration or uninstall commands at this time
- `get-`: Install an "extension" like Decky plugins, and if it is an extension then it can use `get-` too
- `setup-`: Install program, provides uninstall and configuration options for after install
- `configure-`: Configure something that came by default on the image
  - If it must be installed first, then it will be in `setup-`
- `toggle-`: Turns something on/off
  - Selection might be automatic or manual depending on implementation
- `fix-`: Fixes, patches or works around an issue
- `distrobox-`: Distrobox exclusive verb for useful Distrobox stuff
- `foo`: Replace this with whatever the command is called
  - These are shortcuts that we have deemed necessary to not have a verb
    - **Examples**: `ujust update` and `ujust enroll-secureboot-key`

### View each `ujust` script's source code

If you would like to see what each script does for each command then open a host terminal and **enter**:

```
ujust --show <command>
```

Alternatively, you can find the `ujust` commands locally in:
`/usr/share/ublue-os/just`

!!! note

    This directory also shows **hidden** `ujust` commands.

### Uninstalling applications installed through `ujust`

Most applications installed via a `ujust` script would have to be uninstalled manually. Follow the instructions found on the project's website or README file in the source code to uninstall it properly.

This **command** Shows layered packages that may be installed from `ujust`:

```
rpm-ostree status
```

### `ujust` script overview

These are just some of the common Bazzite ujust scripts, there are much more available which are viewable with `ujust --choose` as mentioned above

#### Maintenance Scripts

- **ujust update** - updates system, flatpaks, and containers all at once
- **ujust configure-grub** - Configures GRUB boot menu visibility
- **ujust fix-reset-steam** - Reset the Steam folder back to a fresh state without removing games, music, saves, etc. Very useful if Steam is giving trouble or if you are getting a blank screen in Game Mode
- **ujust fix-proton-hang** - Force terminates all processes related to wine and proton. Useful if you can't launch games after a game fails to close properly
- **ujust bios** - Reboots straight into this device's BIOS/EUFI screen
- **ujust restart-pipewire** - Crackling audio? Restarting Pipewire sometimes fixes that
- **ujust enroll-secure-boot-key** - Enrolls the Nvidia driver & KMOD signing key for secure boot. You'll need this if you want to use Bazzite with Secure Boot enabled
- **ujust clean-system** - Cleans up old unused podman images, volumes, flatpak packages and rpm-ostree content

#### Configuration/Enabling Scripts

- **ujust setup-waydroid** - a configuration helper for Waydroid. More information in [Waydroid Setup Guide](../Installing_and_Managing_Software/Waydroid_Setup_Guide.md)
- **ujust setup-virtualization** - setup and configure virtualization and vfio
- **ujust setup-sunshine** - toggle Sunshine Game Streaming host on or off
- **ujust setup-luks-tpm-unlock** - enable auto LUKS unlock via TPM
- **ujust setup-decky** - Install and configure Decky Loader
- **ujust setup-boot-windows-steam** - Adds a script in Steam to boot Windows which is useful for dual-boot setups
- **ujust enable-tailscale** - Enables support for Tailscale
- **ujust enable-supergfxctl** - Enable Supergfxctl, a GPU switcher for hybrid laptops
- **ujust bazzite-cli** - Bazzite CLI mod for Bluefin styled cli enhancements. More information in [Bazzite Command Line Tools](../Advanced/bazzite-cli.md)

#### Troubleshooting Scripts

- **ujust logs-last-boot** - Shows all messages from last boot
- **ujust logs-this-boot** - Shows all messages from this boot
- **ujust device-info** - Gathers useful device information to a pastebin. This is very useful for providing information when creating support tickets in the #Bazzite-Help section in Discord

## Project Website

https://just.systems/

<hr>


[**<-- Back to Installing and Managing Software on Bazzite**](./index.md)
