---
title: Home
hide:
  - navigation
---

# Getting Started with [Bazzite](https://bazzite.gg)

<div class="grid cards _bz" markdown>

- [:material-harddisk: **Installing Bazzite**](General/Installation_Guide/index.md){ style="font-size: 1.1rem" }

  Bazzite supports PC hardware from [most desktop and laptops][install_pc_laptop] to specialized models like the [Framework 13][frame_13] and [Framework 16][frame_16]. <br>

  Bazzite also supports controller-friendly hardware like [home theater PC setups][htpc] and a [multitude of handhelds][install_handheld]:

  - Lenovo Legion Go Handhelds
  - Asus ROG Ally Handhelds
  - GPD Handhelds
  - OneXPlayer Handhelds
  - Ayn Handhelds
  - Steam Deck (LCD and OLED)

- [:material-controller: **Playing Video Games**][gaming]{ style="font-size: 1.1rem" }

  Bazzite comes bundled with :fontawesome-brands-steam: [Steam](https://store.steampowered.com) and [Lutris](Gaming/Game_Launchers.md#lutris) to run all of your PC games<sup>1</sup> on multiple hardware configurations!

  It is also compatible with other tools like:

  - [Heroic Games Launcher](https://heroicgameslauncher.com/) for seamless Epic Games, GOG, and Amazon Games integration.
  - [Games and emulators from the built-in app store](https://flathub.org/apps/category/Game/1) that range from [osu!](https://flathub.org/apps/sh.ppy.osu) to [Minecraft](https://flathub.org/apps/org.prismlauncher.PrismLauncher).
  - ...And [more][run_win_game]!

  <small>\*<sup>1</sup> PC games that are known to work on the Linux desktop, visit [**ProtonDB**](https://protondb.com) and [**Are We Anti-Cheat Yet?**](https://areweanticheatyet.com) for more information</small>.

- [:material-download-circle: **Installing Software**][installing_software]{ style="font-size: 1.1rem" }

  <small>Order reflects the recommendation degree.</small>

  1. [`ujust`][ujust] to use Bazzite tailored installers.
     {style="list-style-type: decimal;"}
  2. [Flatpak][flatpak] for graphical apps.
     {style="list-style-type: decimal;"}
  3. [Homebrew][homebrew] for command-line apps.
     {style="list-style-type: decimal;"}
  4. [Quadlet][quadlet] for hosting services.
     {style="list-style-type: decimal;"}
  5. [Distrobox][distrobox] for access to most Linux package managers and as development toolboxes.
     {style="list-style-type: decimal;"}
  6. [Appimage][appimage] for portable apps found on the web.
     {style="list-style-type: decimal;"}

  There is also [package layering with `rpm-ostree`][rpm-ostree], but it is [advised to avoid using it if possible][rpm-ostree_caveats] since layered packages can break future upgrades until packages are removed.

- [:fontawesome-solid-circle-arrow-down: **Updates & Rollbacks**][updateindex]{ style="font-size: 1.1rem" }

  Hassle-free updates with protections against regressions. Rollback to the previous deployment or rebase to an earlier Bazzite build within the last 90 days without losing your personal files.

  - [Updating Guide][updates]
  - [Rollback System Updates][rollbacks]
    - [`bazzite-rollback-helper`][rollback-helper]
  - [Rebasing to Other Images][rebasing]

- [:fontawesome-brands-android: **Android Applications**][waydroid]{ style="font-size: 1.1rem" }

  Run Android applications in a container using [Waydroid](https://waydro.id/)!

  - Launch anything from productivity software to games.
  - ARM translation support for most applications.
  - Use your favorite streaming service without the limitations of DRM.
  - Install software through [Google Play Store](https://play.google.com/store/games) and [F-Droid](https://f-droid.org/).

- [:fontawesome-solid-handshake: **Contributing**][contrib]{ style="font-size: 1.1rem" }

  One of the strengths of Bazzite (inherited from [Universal Blue](https://universal-blue.org/)) is how easy it is to contribute.

  - Something seems broken? You might want to [report a bug](General/reporting_bugs.md).
  - Add new changes by testing them in a [custom image][customimage].
  - Editing current documentation and [adding translations](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/README.md#translate-documentation) are also appreciated.

</div>

[install_pc_laptop]: General/Installation_Guide/Installing_Bazzite_for_Desktop_or_Laptop_Hardware.md
[install_handheld]: General/Installation_Guide/Installing_Bazzite_for_Handheld_PCs.md
[deck]:  Handheld_and_HTPC_edition/Handheld_Wiki/Steam_Deck.md
[frame_13]: General/Installation_Guide/Installing_Bazzite_Framework_Laptop_13.md
[frame_16]: General/Installation_Guide/Installing_Bazzite_for_Framework_Laptop_16.md
[htpc]: General/Installation_Guide/Installing_Bazzite_for_HTPC_Setups.md
[ally]: Handheld_and_HTPC_edition/Handheld_Wiki/ASUS_ROG_Ally.md
[legion_go]: Handheld_and_HTPC_edition/Handheld_Wiki/Lenovo_Legion_Go.md
[ayn]: Handheld_and_HTPC_edition/Handheld_Wiki/Ayn_Handhelds.md
[onex]: Handheld_and_HTPC_edition/Handheld_Wiki/OneXPlayer_Handhelds.md
[gpd]: Handheld_and_HTPC_edition/Handheld_Wiki/GPD_Handhelds.md
[ayaneo]: Handheld_and_HTPC_edition/Handheld_Wiki/Ayaneo_Handhelds.md
[run_win_game]: Installing_and_Managing_Software/index.md#how-do-i-run-windows-applications
[enable_proton]: Gaming/Game_Launchers.md#enabling-proton-for-all-steam-games
[flatpak]: Installing_and_Managing_Software/Flatpak.md
[ujust]: Installing_and_Managing_Software/ujust.md
[rpm-ostree]: Installing_and_Managing_Software/rpm-ostree.md
[distrobox]: Installing_and_Managing_Software/Distrobox.md
[installing_software]: Installing_and_Managing_Software/index.md
[contrib]: CONTRIBUTE.md
[homebrew]: Installing_and_Managing_Software/Homebrew.md
[rpm-ostree_caveats]: Installing_and_Managing_Software/rpm-ostree.md#major-caveats-using-rpm-ostree
[steam_game_mode]: Handheld_and_HTPC_edition/Steam_Gaming_Mode.md#what-is-steam-gaming-mode
[appimage]: Installing_and_Managing_Software/AppImage.md
[updateindex]: Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md/
[updates]: Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/updating_guide.md/
[rollbacks]: Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rolling_back_system_updates.md/
[rebasing]: Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rebase_guide.md/
[rollback-helper]: Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/bazzite_rollback_helper.md/
[waydroid]: Installing_and_Managing_Software/Waydroid_Setup_Guide.md
[gaming]: Gaming/index.md
[quadlet]: Installing_and_Managing_Software/Quadlet.md
[otherhand]: Handheld_and_HTPC_edition/Handheld_Wiki/Other_Handhelds.md
[customimage]: Advanced/creating_custom_image.md
