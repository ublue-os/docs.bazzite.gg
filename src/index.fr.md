---
title: Accueil
hide:
  - navigation
---

# Pour commencer

<div class="grid cards _bz" markdown>

- [:material-harddisk: **Installer Bazzite**](General/Installation_Guide/index.md){ style="font-size: 1.1rem" }

  Bazzite prend en charge le matériel PC, de la plupart des ordinateurs de bureau et portables modernes jusqu'aux modèles spécialisés comme [Framework](https://frame.work/). <br>

  Bazzite prend également en charge le matériel compatible avec les manettes, comme les PC home cinéma et nombreux appareils portables :
  
  - [Appareils portables Asus][ally]
  - [Appareils portables Lenovo][legion_go]
  - [Appareils portables GPD][gpd]
  - [Appareils portables OneXPlayer][onex]
  - [Appareils portables Ayn][ayn]
  - [Appareils portables Ayaneo][ayaneo]
  - [Steam Deck][deck]
  - [Autres appareils portables PC][otherhand]

- [:material-controller: **Jouer aux jeux vidéos**][gaming]{ style="font-size: 1.1rem" }

  Bazzite est fourni avec :fontawesome-brands-steam: [Steam](https://store.steampowered.com) and [Lutris](Gaming/Game_Launchers.md#non-steam-games) pour faire tourner tous vos jeux PC<sup>1</sup> sur de multiples configurations !

  Il est également compatible avec d'autres outils tels que :

  - [Heroic Games Launcher](https://heroicgameslauncher.com/) pour une intégration avec Epic Games, GOG et Amazon Games.
  - Jeux et émulateurs de la boutique d'applications intégrée, allant de  [osu!](https://flathub.org/apps/sh.ppy.osu) à [Minecraft](https://flathub.org/apps/org.prismlauncher.PrismLauncher).
  - ...et [bien plus !](https://flathub.org/en/apps/category/game/1)

  <small>\*<sup>1</sup> Pour vérifier la compatibilité des jeux avec Linux, rendez-vous sur [**ProtonDB**](https://protondb.com) et [**Are We Anti-Cheat Yet?**](https://areweanticheatyet.com) pour plus d'informations</small>.

- [:material-download-circle: **Installer des logiciels**][installing_software]{ style="font-size: 1.1rem" }

  <small>L'ordre correspond au niveau de recommandation.</small>

  1. [Portail Bazzite][ujust] pour utiliser les installateurs personnalisés de Bazzite.
     {style="list-style-type: decimal;"}
  2. [Bazaar App Store (Flatpak)][flatpak] pour la plupart des apps.
     {style="list-style-type: decimal;"}
  3. [Homebrew][homebrew] pour les apps et outils en ligne de commande.
     {style="list-style-type: decimal;"}
  4. [Containers][containers] pour accéder à la plupart des gestionnaires de paquets Linux (`apt`, `dnf`, `pacman`, etc.), comme boîtes à outils de développement, et pour les services d'hébergement.
     {style="list-style-type: decimal;"}
  5. [Appimage][appimage] pour les apps portables trouvées sur le Web.
     {style="list-style-type: decimal;"}

  Il existe également le [package layering avec `rpm-ostree`][rpm-ostree], mais il est [recommandé de l'éviter si possible][rpm-ostree_caveats] car les "layered packages" peuvent empêcher les mises à jour futures tant qu'ils n'ont pas été supprimés.

- [:fontawesome-solid-circle-arrow-down: **Mises à jour & Restauration**][updateindex]{ style="font-size: 1.1rem" }

  Des mises à jour en toute simplicité, avec des protections contre les régressions. Revenez à la version précédente ou effectuez un "rebase" vers une version antérieure de Bazzite datant de moins de 90 jours sans perdre vos fichiers personnels.

  - [Guide de mise à jour][updates]
  - [Restauration des mises à jour système][rollbacks]
  - ["Rebase" vers d'autres images][rebasing]
  - [`bazzite-rollback-helper`][rollback-helper]

- [:fontawesome-brands-android: **Applications Android**][waydroid]{ style="font-size: 1.1rem" }

  Exécutez des applications Android dans un conteneur grâce à [Waydroid](https://waydro.id/) !

  - Lancez tout ce que vous voulez, des logiciels de productivité aux jeux.
  - Prise en charge de la traduction ARM pour la plupart des applications.
  - Utilisez votre service de streaming préféré sans restrictions DRM.
  - Installez des apps via [Google Play Store](https://play.google.com/store/games) et [F-Droid](https://f-droid.org/).

- [:fontawesome-solid-handshake: **Contribuer**][contrib]{ style="font-size: 1.1rem" }

  L'un des atouts de Bazzite (hérité de [Universal Blue](https://universal-blue.org/)) est sa facilité de contribution.

  - Quelque chose ne fonctionne pas ? Vous pouvez [signaler un bug](General/reporting_bugs.md).
  - Ajoutez de nouvelles fonctionnalités en les testant dans une [image personnalisée][customimage].
  - - Nous encourageons également la modification de la documentation actuelle et l'[ajout de traductions](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/README.md#translate-documentation).

</div>

[deck]:  Handheld_and_HTPC_edition/Handheld_Wiki/Steam_Deck.md
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
[contrib]: https://universal-blue.org/contributing.html
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
[containers]: Installing_and_Managing_Software/Containers.md
