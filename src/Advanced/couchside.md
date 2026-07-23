---
title: Setting Up Couchside
authors:
  - "@emerytech"
tags:
  - Community
search:
  exclude: true
---

# Setting Up Couchside

[![GitHub Release](https://img.shields.io/github/v/release/emerytech/couchside?label=Latest%20Release&color=brightgreen&logo=github&logoColor=white)](https://github.com/emerytech/couchside/releases)

## Purpose

[**Couchside**](https://couchside.tv) turns your phone into the dashboard, remote console, and
game controller for a Bazzite HTPC or handheld — so you can drive the box from the couch even
when the TV is showing a black screen. It pairs a native iOS & Android app with a small,
dependency-free Python service that runs on the box.

From your phone you can:

- See **live vitals** — CPU temperature, load, memory, disk, uptime, systemd service health, and
  (on handhelds) battery.
- **Fix a wedged session without a keyboard** — restart the display session when gamescope drops
  to a black screen, flip between Game Mode and Desktop, reboot, or power off.
- **Read the logs** and pull a live frame of the box's actual screen.
- **Launch games** from your Steam library as a cover-art grid.
- Pick up a **virtual Xbox 360 controller**, a trackpad, or a TV-style remote.

It is **LAN-only** — no cloud, no accounts, no analytics. The box-side agent is free and open
source (MIT); the companion phone app is on the App Store and Google Play.

!!! note

    Couchside runs as a `systemd --user` service under your own desktop account, using standard
    Bazzite facilities (`uinput` for the virtual controller, `steamos-session-select` /
    `gamescope` for the Game Mode ↔ Desktop handoff). It needs **no `rpm-ostree` layering** and
    does **not** touch the read-only root filesystem.

## Installation

Run the following in a terminal on the box to install the agent:

```bash
curl -fsSL https://couchside.tv/install.sh | bash
```

The installer sets up the user service and shows a **pairing QR code** on the box's screen (on a
fresh install it walks you through pairing there). Then:

1. Install the **Couchside** app on your phone from the [App Store](https://apps.apple.com/us/app/id6786884115)
   or [Google Play](https://play.google.com/store/apps/details?id=com.ets3d.rescueremote).
2. Open the app, tap **Scan for boxes**, and either scan the QR or enter the **6-digit PIN** the
   box shows on its own screen.

!!! tip

    Both the box and the phone must be on the **same local network**. Pairing needs no IP
    addresses or tokens typed by hand — the PIN shown on the box's screen is the whole handshake.

!!! note "How it stays safe"

    The agent only ever runs an exact, audited **allowlist** of actions — nothing the phone
    sends becomes an arbitrary command. Access is a single bearer token, generated on the box at
    install time and stored locally; it is never sent to any server off your LAN.

## Uninstall

To remove the agent (it asks before deleting the token):

```bash
curl -fsSL https://couchside.tv/install.sh | bash -s -- --uninstall
```

## More

- Website & setup walkthrough: [couchside.tv](https://couchside.tv/#how)
- Source (agent is MIT): [github.com/emerytech/couchside](https://github.com/emerytech/couchside)
- Per-release notes: [couchside.tv/updates](https://couchside.tv/updates/)
