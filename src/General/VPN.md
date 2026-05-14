---
title: "VPN Setup"
---

# VPN Setup

## Using functional VPN Flatpaks

VPN clients are usually not offered on the Bazaar app store as the Flatpak sandbox is too strict for most VPN clients to work as is which means they are not available in Bazaar to install. However examples of good VPN clients that are available in Bazaar:

- [Mozilla VPN](https://flathub.org/apps/org.mozilla.vpn)
- [ProtonVPN](https://flathub.org/apps/com.protonvpn.www)

## Tailscale

[Tailscale](https://tailscale.com) is included by default to provide VPN services for both desktop and development use cases. Read this [Tailscale guide](https://blog.6nok.org/tailscale-is-pretty-useful/) for common usage before proceeding.

- [Using Tailscale with Mullvad](https://tailscale.com/kb/1258/mullvad-exit-nodes) - Provides the best out of the box experience.
  - [Using Tailscale with Docker](https://tailscale.com/kb/1282/docker) - For development purposes.
  - `ujust toggle-tailscale` will remove the built in desktop integration if you prefer to use something else.
  - Tailscale's [YouTube channel](https://www.youtube.com/@Tailscale) has lots of great tips and tricks.
- Good VPNs provide Wireguard configuration files that can be imported directly into NetworkManager, check your VPN providers documentation for more information.
- Only as a last resort [layer the VPN with rpm-ostree](/Installing_and_Managing_Software/rpm-ostree/).

## Import VPN configuration files through Desktop Environment

This option may be good enough for you if you don't need special features provided by your VPN client, like kill-switches, split tunneling and other custom features not built-in to the VPN protocol. VPNs imported in this way can be toggled on and off at will.

=== "KDE Plasma"

    1\. Open System Settings
    2\. Navigate to the Networking Section and go into the "Wi-Fi & Internet" settings
    3\. Click the "+" button at the bottom

    <img src="/img/vpn_settings.png" alt="Settings page of Networking Settings" width="600" height="487" />

    4\. Select your downloaded configuration file

    <img src="/img/add_vpn.png" alt="Import VPN config file dialog" width="400" height="617" />

=== "GNOME"

    1\. Open Settings
    2\. Navigate to the Network section
    3\. Click the "+" button on the VPN section

    <img src="/img/vpn_settings_gnome.png" alt="Networking Settings page in GNOME" width="600" height="487" />

    4\. Choose "Import From file..."

    <img src="/img/add_vpn_file_gnome.png" alt="Import VPN config file dialog in GNOME" width="600" height="487" />

    5\. Select your downloaded configuration file.
