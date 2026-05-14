---
title: Domů
hide:
  - navigation
---

# Jak začít

<div class="grid cards _bz" markdown>

- [:material-harddisk: **Instalace Bazzite**](/General/Installation_Guide/index.md){ style="font-size: 1.1rem" }

  Bazzite funguje na většině moderních desktopů a notebooků, včetně speciálních modelů jako [Framework](https://frame.work/). <br>

  Bazzite podporuje také zařízení s kontrolery. Jako domácí PC kino nebo řada ručních zařízení:

  - [Asus Handhelds][ally]
  - [Lenovo Handhelds][legion_go]
  - [GPD Handhelds][gpd]
  - [OneXPlayer Handhelds][onex]
  - [Ayn Handhelds][ayn]
  - [Ayaneo Handhelds][ayaneo]
  - [Steam Deck][deck]
  - [Ostatní PC Handhelds][otherhand]

- [:material-controller: **Hraní her**][gaming]{ style="font-size: 1.1rem" }

  Bazzite přichází rovnou s :fontawesome-brands-steam: [Steamem](https://store.steampowered.com) a [Lutrisem](/Gaming/Game_Launchers.md#non-steam-games), takže si zahraješ prakticky cokoliv<sup>1</sup> na různých konfiguracích!

  Je také kompatibilní s nástroji jako:

  - [Heroic Games Launcher](https://heroicgameslauncher.com/) — Epic Games, GOG a Amazon Games.
  - Hry a emulátory přímo z obchodu od [osu!](https://flathub.org/apps/sh.ppy.osu) po [Minecraft](https://flathub.org/apps/org.prismlauncher.PrismLauncher).
  - ...a [spoustu dalšího!](https://flathub.org/en/apps/category/game/1)

  <small>\*<sup>1</sup> Hry, o kterých je známo, že na Linuxu běží, jsou v přehledu na [**ProtonDB**](https://protondb.com) a [**Are We Anti-Cheat Yet?**](https://areweanticheatyet.com)</small>.

- [:material-download-circle: **Instalace softwaru**][installing_software]{ style="font-size: 1.1rem" }

  <small>Seřazeno podle doporučené priority.</small>

  1. [Bazzite Portal][ujust] k použití instalátorů přizpůsobených pro Bazzite.
     {style="list-style-type: decimal;"}
  2. [Obchod Bazaar (Flatpak)][flatpak] pro většinu aplikací.
     {style="list-style-type: decimal;"}
  3. [Homebrew][homebrew] nástroje a aplikace pro příkazový řádek.
     {style="list-style-type: decimal;"}
  4. [Kontejnery][containers] pro přístup ke správcům balíčků (`apt`, `dnf` `pacman`, a další), vývojové toolboxy a pro hostování služeb.
     {style="list-style-type: decimal;"}
  5. [AppImage][appimage] přenosné aplikace stažené odkudkoliv z webu.
     {style="list-style-type: decimal;"}

  Existuje také [vrstvení balíčků přes `rpm-ostree`][rpm-ostree], ale [je doporučeno se tomu vyhnout, pokud je to možné][rpm-ostree_caveats] jelikož vrstvené balíčky můžou rozbít budoucí aktualizace, dokud nejsou odstraněny.

- [:fontawesome-solid-circle-arrow-down: **Aktualizace a Rollback**][updateindex]{ style="font-size: 1.1rem" }

  Bezproblémové aktualizace s ochranou vrácení se zpět. Vrať se k předchozímu nasazení nebo proveď rebase na dřívější build Bazzite z posledních 90 dnů, aniž bys přišel o své soubory.

  - [Jak aktualizovat][updates]
  - [Vrácení aktualizace][rollbacks]
  - [Přechod na jiný obraz (Rebase)][rebasing]
  - [`bazzite-rollback-helper`][rollback-helper]

- [:fontawesome-brands-android: **Aplikace pro Android**][waydroid]{ style="font-size: 1.1rem" }

  Spouštěj androidové aplikace v kontejneru díky [Waydroid](https://waydro.id)!

  - Spusť cokoli od her, až po produktivitu.
  - Podpora překladu ARM pro většinu aplikací.
  - Streamovací služby bez potíží s DRM.
  - Instalace přes [Google Play Store](https://play.google.com/store/games) nebo [F-Droid](https://f-droid.org/).

- [:fontawesome-solid-handshake: **Jak přispět**][contrib]{ style="font-size: 1.1rem" }

  Bazzite (a [Universal Blue](https://universal-blue.org/), ze kterého vychází) si zakládá na tom, aby přispívání bylo co nejjednodušší.

  - Narazil jsi na chybu? [Nahlaš ji](General/reporting_bugs.md).
  - Nové funkce testuj ve [vlastním obrazu][customimage].
  - Vítány jsou i úpravy dokumentace a [překlady](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/README.md#translate-documentation).

</div>

[deck]: /Handheld_and_HTPC_edition/Handheld_Wiki/Steam_Deck.md
[ally]: /Handheld_and_HTPC_edition/Handheld_Wiki/ASUS_ROG_Ally.md
[legion_go]: /Handheld_and_HTPC_edition/Handheld_Wiki/Lenovo_Legion_Go.md
[ayn]: /Handheld_and_HTPC_edition/Handheld_Wiki/Ayn_Handhelds.md
[onex]: /Handheld_and_HTPC_edition/Handheld_Wiki/OneXPlayer_Handhelds.md
[gpd]: /Handheld_and_HTPC_edition/Handheld_Wiki/GPD_Handhelds.md
[ayaneo]: /Handheld_and_HTPC_edition/Handheld_Wiki/Ayaneo_Handhelds.md
[flatpak]: /Installing_and_Managing_Software/Flatpak.md
[ujust]: /Installing_and_Managing_Software/ujust.md
[rpm-ostree]: /Installing_and_Managing_Software/rpm-ostree.md
[installing_software]: /Installing_and_Managing_Software/index.md
[contrib]: https://universal-blue.org/contributing.html
[homebrew]: /Installing_and_Managing_Software/Homebrew.md
[rpm-ostree_caveats]: /Installing_and_Managing_Software/rpm-ostree.md#major-caveats-using-rpm-ostree
[appimage]: /Installing_and_Managing_Software/AppImage.md
[updateindex]: /Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md
[updates]: /Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/updating_guide.md
[rollbacks]: /Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rolling_back_system_updates.md
[rebasing]: /Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rebase_guide.md
[rollback-helper]: /Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/bazzite_rollback_helper.md
[waydroid]: /Installing_and_Managing_Software/Waydroid_Setup_Guide.md
[gaming]: /Gaming/index.md
[otherhand]: /Handheld_and_HTPC_edition/Handheld_Wiki/Other_Handhelds.md
[customimage]: /Advanced/creating_custom_image.md
[containers]: /Installing_and_Managing_Software/Containers.md