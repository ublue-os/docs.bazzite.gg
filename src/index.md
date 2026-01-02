---
title: Home
hide:
  - navigation
---

# Getting Started with [Bazzite](https://bazzite.gg)

<div class="grid cards _bz" markdown>

- [:material-harddisk: **Installing Bazzite**](General/Installation_Guide/index.md){ style="font-size: 1.1rem" }

  Bazzite supports PC hardware from most modern desktop and laptops to specialized models like the Framework 13 and Framework 16. <br>

  Bazzite also supports controller-friendly hardware like [home theater PC setups][htpc] and a [multitude of handhelds][install_handheld]:

  - Lenovo Legion Go Handhelds
  - Asus ROG Ally Handhelds
  - GPD Handhelds
  - OneXPlayer Handhelds
  - Ayn Handhelds
  - Steam Deck (LCD and OLED)

- [:material-download-circle: **Installing Software**][installing_software]{ style="font-size: 1.1rem" }

  <small>Order reflects the recommendation degree.</small>

  1. [Bazaar App Store (**Flatpak**)][flatpak] for graphical apps.
     {style="list-style-type: decimal;"}
  2. [Homebrew][homebrew] for command-line apps.
     {style="list-style-type: decimal;"}
  3. [Quadlet][quadlet] for hosting services.
     {style="list-style-type: decimal;"}
  4. [Containers][distrobox] for access to most Linux package managers and as development toolboxes.
     {style="list-style-type: decimal;"}
  5. [Appimage][appimage] for portable software found on the web.
     {style="list-style-type: decimal;"}

  There is also software available as [`ujust` commands][ujust] and [layering system-level packages*][rpm-ostree].

  <sub>*Not recommended since it can break automatic updates until the package is removed from the image.</sub>
  
- [:fontawesome-solid-circle-arrow-down: **Updates & Rollbacks**][updateindex]{ style="font-size: 1.1rem" }

  Hassle-free updates with protections against regressions. Rollback to the previous deployment or rebase to an earlier Bazzite build within the last 90 days without losing your personal files.

  - [Updating Guide][updates]
  - [Rollback System Updates][rollbacks]
    - [`bazzite-rollback-helper`][rollback-helper]
  - [Rebasing to Other Images][rebasing]

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
[flatpak]: https://flathub.org/en
[ujust]: Installing_and_Managing_Software/ujust.md
[rpm-ostree]: Installing_and_Managing_Software/rpm-ostree.md
[distrobox]: Installing_and_Managing_Software/Distrobox.md
[installing_software]: Installing_and_Managing_Software/index.md
[contrib]: CONTRIBUTE.md
[homebrew]: https://formulae.brew.sh/formula/
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
