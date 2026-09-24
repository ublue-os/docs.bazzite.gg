---
title: Главная
hide:
  - navigation
---

# Начало работы

<div class="grid cards _bz" markdown>

- [:material-harddisk: **Установка Bazzite**](General/Installation_Guide/index.md){ style="font-size: 1.1rem" }

  Bazzite поддерживает ПК-оборудование: от большинства современных настольных компьютеров и ноутбуков до специализированных моделей вроде [**Framework**](https://frame.work/). <br>

  Bazzite также поддерживает оборудование, удобное для управления с контроллера, включая домашние медиацентры на базе ПК и множество портативных устройств:
  
  - [**Портативные устройства Asus**][ally]
  - [**Портативные устройства Lenovo**][legion_go]
  - [**Портативные устройства GPD**][gpd]
  - [**Портативные устройства OneXPlayer**][onex]
  - [**Портативные устройства Ayn**][ayn]
  - [**Портативные устройства Ayaneo**][ayaneo]
  - [**Steam Deck**][deck]
  - [**Другие портативные ПК**][otherhand]

- [:material-controller: **Игры**][gaming]{ style="font-size: 1.1rem" }

  Bazzite поставляется с :fontawesome-brands-steam: [**Steam**](https://store.steampowered.com) и [**Lutris**](Gaming/Game_Launchers.md#non-steam-games), чтобы запускать все ваши игры для ПК<sup>1</sup> на разных конфигурациях оборудования!

  Система также совместима с другими инструментами, например:

  - [**Heroic Games Launcher**](https://heroicgameslauncher.com/) для удобной интеграции Epic Games, GOG и Amazon Games.
  - Игры и эмуляторы из встроенного магазина приложений: от [**osu!**](https://flathub.org/apps/sh.ppy.osu) до [**Minecraft**](https://flathub.org/apps/org.prismlauncher.PrismLauncher).
  - ...И [**многое другое!**](https://flathub.org/en/apps/category/game/1)

  <small>*Игры для ПК, которые, как известно, работают на десктопном Linux. Подробнее см. на [**ProtonDB**](https://protondb.com) и [**Are We Anti-Cheat Yet?**](https://areweanticheatyet.com)</small>.

- [:material-download-circle: **Установка программ**][installing_software]{ style="font-size: 1.1rem" }

  <small>Порядок отражает степень рекомендации.</small>

  1. [**Портал Bazzite**][bazzite_portal] для использования установщиков, адаптированных под Bazzite.
     {style="list-style-type: decimal;"}
  2. [**Магазин приложений Bazaar (Flatpak)**][flatpak] для большинства приложений.
     {style="list-style-type: decimal;"}
  3. [**Homebrew**][homebrew] для приложений и инструментов командной строки.
     {style="list-style-type: decimal;"}
  4. [**Контейнеры**][containers] для доступа к большинству менеджеров пакетов Linux (`apt`, `dnf`, `pacman` и т. д.), использования в качестве сред разработки и размещения сервисов.
     {style="list-style-type: decimal;"}
  5. [**Appimage**][appimage] для портативных приложений из интернета.
     {style="list-style-type: decimal;"}

  Есть и [наслоение пакетов через `rpm-ostree`][rpm-ostree], но [**по возможности рекомендуется его избегать**][rpm-ostree_caveats], поскольку добавленные таким способом пакеты могут ломать будущие обновления, пока их не удалят.

- [:fontawesome-solid-circle-arrow-down: **Обновления и откаты**][updateindex]{ style="font-size: 1.1rem" }

  Обновления без лишних сложностей и с защитой от регрессий. Можно откатиться к предыдущему развертыванию или перейти на более раннюю сборку Bazzite за последние 90 дней без потери личных файлов.

  - [**Руководство по обновлению**][updates]
  - [**Откат системных обновлений**][rollbacks]
  - [**Переход на другие образы**][rebasing]
  - [`bazzite-rollback-helper`][rollback-helper]

- [:fontawesome-brands-android: **Приложения Android**][waydroid]{ style="font-size: 1.1rem" }

  Запускайте приложения Android в контейнере с помощью [**Waydroid**](https://waydro.id/)!

  - Запускайте что угодно: от программ для работы до игр.
  - Поддержка трансляции ARM для большинства приложений.
  - Используйте любимый стриминговый сервис без ограничений DRM.
  - Устанавливайте программы через [**Google Play Store**](https://play.google.com/store/games) и [**F-Droid**](https://f-droid.org/).

- [:fontawesome-solid-handshake: **Участие в проекте**][contrib]{ style="font-size: 1.1rem" }

  Одна из сильных сторон Bazzite, унаследованная от [Universal Blue](https://universal-blue.org/), в том, что участвовать в проекте очень легко.

  - Что-то выглядит сломанным? Можно [**сообщить об ошибке**](General/reporting_bugs.md).
  - Добавляйте новые изменения, тестируя их в [**пользовательском образе**][customimage].
  - Правки текущей документации и [**добавление переводов**](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/README.md#translate-documentation) тоже приветствуются.

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
