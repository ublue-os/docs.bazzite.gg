---
title: Головна
hide:
  - navigation
---

# Початок роботи

<div class="grid cards _bz" markdown>

- [:material-harddisk: **Встановлення Bazzite**](General/Installation_Guide/index.md){ style="font-size: 1.1rem" }

  Bazzite підтримує більшість сучасних настільних комп'ютерів і ноутбуків, а також спеціалізовані моделі, як-от [**Framework**](https://frame.work/). <br>

  Bazzite також підтримує обладнання, зручне для керування контролером, зокрема ПК для домашнього кінотеатру та безліч портативних консолей:
  
  - [**Портативні консолі Asus**][ally]
  - [**Портативні консолі Lenovo**][legion_go]
  - [**Портативні консолі GPD**][gpd]
  - [**Портативні консолі OneXPlayer**][onex]
  - [**Портативні консолі Ayn**][ayn]
  - [**Портативні консолі Ayaneo**][ayaneo]
  - [**Steam Deck**][deck]
  - [**Інші портативні ПК**][otherhand]

- [:material-controller: **Ігри**][gaming]{ style="font-size: 1.1rem" }

  Bazzite постачається разом зі :fontawesome-brands-steam: [**Steam**](https://store.steampowered.com) і [**Lutris**](Gaming/Game_Launchers.md#non-steam-games), щоб запускати всі ваші ігри для ПК<sup>1</sup> на різних конфігураціях обладнання!

  Він також сумісний з іншими інструментами, як-от:

  - [**Heroic Games Launcher**](https://heroicgameslauncher.com/) для зручної інтеграції з Epic Games, GOG та Amazon Games.
  - Ігри та емулятори з вбудованого магазину застосунків — від [**osu!**](https://flathub.org/apps/sh.ppy.osu) до [**Minecraft**](https://flathub.org/apps/org.prismlauncher.PrismLauncher).
  - ...І [**багато іншого!**](https://flathub.org/en/apps/category/game/1)

  <small>*Ігри для ПК, які працюють на Linux. Докладніше дивіться на [**ProtonDB**](https://protondb.com) і [**Are We Anti-Cheat Yet?**](https://areweanticheatyet.com)</small>.

- [:material-download-circle: **Встановлення програм**][installing_software]{ style="font-size: 1.1rem" }

  <small>Порядок відповідає тому, наскільки ми рекомендуємо кожен спосіб.</small>

  1. [**Bazzite Portal**][bazzite_portal] — інсталятори, підготовлені спеціально для Bazzite.
     {style="list-style-type: decimal;"}
  2. [**Магазин застосунків Bazaar (Flatpak)**][flatpak] — для більшості застосунків.
     {style="list-style-type: decimal;"}
  3. [**Homebrew**][homebrew] — для програм та інструментів командного рядка.
     {style="list-style-type: decimal;"}
  4. [**Контейнери**][containers] — для доступу до більшості менеджерів пакетів Linux (`apt`, `dnf`, `pacman` тощо), як середовища для розробки та для запуску сервісів.
     {style="list-style-type: decimal;"}
  5. [**Appimage**][appimage] — для портативних програм, знайдених в інтернеті.
     {style="list-style-type: decimal;"}

  Також є [накладання пакетів через `rpm-ostree`][rpm-ostree], але [**за можливості цього варто уникати**][rpm-ostree_caveats], оскільки накладені пакети можуть ламати майбутні оновлення, доки їх не видалити.

- [:fontawesome-solid-circle-arrow-down: **Оновлення та відкати**][updateindex]{ style="font-size: 1.1rem" }

  Оновлення без клопотів і з захистом від регресій. Повертайтеся до попереднього розгортання або перебазовуйтеся на ранішу збірку Bazzite за останні 90 днів, не втрачаючи особистих файлів.

  - [**Посібник з оновлення**][updates]
  - [**Відкат оновлень системи**][rollbacks]
  - [**Перебазування на інші образи**][rebasing]
  - [`bazzite-rollback-helper`][rollback-helper]

- [:fontawesome-brands-android: **Android-застосунки**][waydroid]{ style="font-size: 1.1rem" }

  Запускайте Android-застосунки в контейнері за допомогою [**Waydroid**](https://waydro.id/)!

  - Запускайте що завгодно — від офісних програм до ігор.
  - Підтримка трансляції ARM для більшості застосунків.
  - Користуйтеся улюбленими стрімінговими сервісами без обмежень DRM.
  - Встановлюйте програми з [**Google Play Store**](https://play.google.com/store/games) і [**F-Droid**](https://f-droid.org/).

- [:fontawesome-solid-handshake: **Участь у проєкті**][contrib]{ style="font-size: 1.1rem" }

  Одна з переваг Bazzite (успадкована від [Universal Blue](https://universal-blue.org/)) — те, як легко долучитися до проєкту.

  - Щось не працює? Можливо, варто [**повідомити про помилку**](General/reporting_bugs.md).
  - Пропонуйте нові зміни, перевіряючи їх у [**власному образі**][customimage].
  - Також ми вдячні за редагування документації та [**додавання перекладів**](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/README.md#translate-documentation).

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
[bazzite_portal]: Installing_and_Managing_Software/Bazzite_Portal.md
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
