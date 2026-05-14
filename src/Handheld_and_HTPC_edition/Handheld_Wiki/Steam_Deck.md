---
title: Steam Deck
---

# Steam Deck

## Steam Deck (LCD & OLED Models)

![Steam Deck LCD|690x348, 100%](../../img/Steam_Deck_LCD.jpeg)

### BIOS Updates
It is recommended to enter `ujust enable-deck-bios-firmware-updates` in the terminal to receive Steam Deck BIOS updates.

### Why Bazzite over SteamOS?

Both SteamOS and Bazzite use Steam Gaming Mode and share packages between each other, but what about differences under the hood?  Bazzite should have most of the functionality from SteamOS with Steam Gaming Mode working as intended.

- It should function nearly identical to SteamOS.
  - The Quick Access Menu (QAM) which is accessed with the <kbd>...</kbd> button on Steam Deck is functional for TDP, framerate limiting, scaling, etc. like on SteamOS.
  - The same popular third-party software like [Decky Loader](https://decky.xyz/), [Emudeck](https://www.emudeck.com/), [RetroDeck](https://retrodeck.net/), etc. should install and function properly.
- Reaping the benefits of [Fedora Atomic Desktop](https://fedoraproject.org/atomic-desktops/):
  - Layer Fedora packages to the image without losing them between updates/reboots.
  - Roll back system updates from the last 90 days.
  - Alternate desktop environments available.
- Bazzite includes newer versions of base packages than SteamOS which means Bazzite is always ahead of SteamOS in terms of Steam Gaming Mode and Desktop Mode features.
  - Newer package upgrades including the Linux kernel and drivers.
  - Regressions may occur more often since Bazzite upgrades base packages faster than SteamOS does.

>If you want to see a more in-depth comparison, read our [**SteamOS comparison guide**](/General/SteamOS_Comparison.md).

### Known Issues

- (Steam Deck OLED) The brightness is not properly restored when changing refresh rate.
- (Steam Deck OLED) MangoHUD does not report GPU clocks.
