---
title: Home
hide:
  - navigation
---

# Getting Started with [Bazzite](https://bazzite.gg)

<div class="grid cards _bz" markdown>

- [:material-harddisk: **Installing Bazzite**](General/Installation_Guide/index.md){ style="font-size: 1.1rem" }

  Bazzite supports PC hardware from most modern desktop and laptops to specialized models like the Framework 13 and Framework 16. <br>

  Bazzite also supports controller-friendly hardware like [home theater PC setups][htpc] and a [multitude of handhelds][handheld]:

  - Lenovo Legion Go Handhelds
  - Asus ROG Ally Handhelds
  - GPD Handhelds
  - OneXPlayer Handhelds
  - Ayn Handhelds
  - Steam Deck

- [:material-download-circle: **Installing Software**][installing_software]{ style="font-size: 1.1rem" }

  <small>Order reflects the order of recommended method.</small>

  1. [Bazaar App Store (**Flatpak**)][flatpak] for graphical apps, install most software this way.
     {style="list-style-type: decimal;"}
  2. [Homebrew][homebrew] for command-line apps.
     {style="list-style-type: decimal;"}
  3. [Containers][containers] for access to most Linux package managers (`apt`, `dnf`, `pacman`, etc.), as development toolboxes, and for hosting services.
     {style="list-style-type: decimal;"}   
  4. [Appimage][appimage] for portable apps found on the web.
     {style="list-style-type: decimal;"}

  There is also software available as [`ujust` commands found in the Bazzite Portal application][ujust] which is the preferred way to obtain certain software and takes precedence over the list above. Users can also [layer system-level packages][rpm-ostree] as the **least recommended method of obtaining most software** since it can break automatic updates until the package is removed from the image.</sub>
  
- [:material-update: **Updates & Rollbacks**][updateindex]{ style="font-size: 1.1rem" }

  Hassle-free updates with protections against regressions. Rollback to the previous deployment or rebase to an earlier Bazzite build within the last 90 days without losing your personal files.

  Read about the [`bazzite-rollback-helper`][rollback-helper] tool for rolling back system upgrades or changning the update stream.

</div>

[handheld]: Handheld_and_HTPC_edition/Handheld_Wiki/index.md
[htpc]: Handheld_and_HTPC_edition/Steam_Gaming_Mode.md
[ally]: Handheld_and_HTPC_edition/Handheld_Wiki/ASUS_ROG_Ally.md
[run_win_game]: Installing_and_Managing_Software/index.md#how-do-i-run-windows-applications
[flatpak]: https://flathub.org/en
[ujust]: Installing_and_Managing_Software/ujust.md
[rpm-ostree]: Installing_and_Managing_Software/rpm-ostree.md
[containers]: https://distrobox.it/
[installing_software]: Installing_and_Managing_Software/index.md
[homebrew]: https://formulae.brew.sh/formula/
[steam_game_mode]: Handheld_and_HTPC_edition/Steam_Gaming_Mode.md
[appimage]: https://appimage.org/
[updateindex]: Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md/
[rollback-helper]: Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/bazzite_rollback_helper.md/
[waydroid]: Installing_and_Managing_Software/Waydroid_Setup_Guide.md
[gaming]: Gaming/index.md
