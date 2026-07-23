---
title: 首頁
hide:
  - navigation
---

# Bazzite，啟動！

<div class="grid cards _bz" markdown>

- [:material-harddisk: **安裝Bazzite**](General/Installation_Guide/index.md){ style="font-size: 1.1rem" }

  Bazzite可以運行於絕大部分x86-64架構的桌機和筆記本之上。此外，Bazzite亦有針對於特定設備的支持，例如 [Framework](https://frame.work/)。 <br>

  Bazzite亦支持以控制器為主要交互方式的系統和設備，如家庭劇院（HTPC）以及各式各樣的掌機：
  
  - [華碩ROG Ally系列][ally]
  - [聯想Legion Go系列][legion_go]
  - [GPD掌機][gpd]
  - [OneXPlayer掌機][onex]
  - [Ayn掌機][ayn]
  - [Ayaneo掌機][ayaneo]
  - [Steam Deck][deck]
  - [其他x86-64架構的掌機][otherhand]

- [:material-controller: **遊玩及安裝遊戲**][gaming]{ style="font-size: 1.1rem" }

  :fontawesome-brands-steam: [Steam](https://store.steampowered.com) 和 [Lutris](Gaming/Game_Launchers.md#non-steam-games) 都已經預先安裝於Bazzite系統之中，為你打造一個裝完即玩嘅體驗！<sup>1</sup>

  此外，Bazzite亦兼容其他遊戲啟動器：

  - [Heroic Games Launcher](https://heroicgameslauncher.com/)為你提供無縫遊玩Epic遊戲的體驗
  - 可於內設應用程式商店安裝的遊戲啟動器，例如[osu!](https://flathub.org/zh-Hant/apps/sh.ppy.osu)和[Minecraft](https://flathub.org/zh-Hant/apps/org.prismlauncher.PrismLauncher)
  - ...以及[其他遊戲！](https://flathub.org/zh-Hant/apps/category/game/1)

  <small>\*<sup>1</sup> 大多數電腦游戲都可以透過Wine/Proton運行於Linux之上，詳情請參考 [**ProtonDB**](https://protondb.com)、[**Are We Anti-Cheat Yet?**](https://areweanticheatyet.com)和[**Can We Tux?**](https://tux.red/)</small>

- [:material-download-circle: **安裝軟件**][installing_software]{ style="font-size: 1.1rem" }

  <small>註：由上之下的次序代表各種安裝途徑的推介先序</small>

  1. [Bazzite Portal][bazzite_portal]使用Bazzite推薦的安裝方式
     {style="list-style-type: decimal;"}
  2. [Bazaar 應用程式商店 (Flatpak)][flatpak]包含大部份應用程式
     {style="list-style-type: decimal;"}
  3. [Homebrew][homebrew]包含各種指令行軟件及工具
     {style="list-style-type: decimal;"}
  4. [Distrobox容器][containers]提供各大Linux發行版的安裝包管理器(如`apt`、`dnf`、`pacman`等等)，通常用於開發工具和網頁寄存（Web Hosting）
     {style="list-style-type: decimal;"}
  5. [Appimage][appimage]作為「綠色軟體」的載體
     {style="list-style-type: decimal;"}

  此外，你亦可使用Bazzite系統內建的[`rpm-ostree`疊加套件到系統樹上][rpm-ostree]，但如非必要，我們並[不推介使用這個方法][rpm-ostree_caveats]。

- [:fontawesome-solid-circle-arrow-down: **系統更新與回溯**][updateindex]{ style="font-size: 1.1rem" }

  Bazzite使用Fedora原子化更新系統，每次更新皆為啟動一個完整的唯讀系統映像檔。若更新後，你的系統出現異常，你可以回溯至90日內的任意一個系統映像檔，而你的個人檔案皆不會受影響。

  - [更新指南][updates]
  - [系統回溯][rollbacks]
  - [切換更新頻道][rebasing]
  - [Bazzite更新助手(`bazzite-rollback-helper`)][rollback-helper]

- [:fontawesome-brands-android: **Android應用程式**][waydroid]{ style="font-size: 1.1rem" }

  你可以在[Waydroid](https://waydro.id/)內運行Android的應用程式!

  - 運行由辦公軟件和手機遊戲之間的任意應用程式
  - 支持於大部分應用程式上的自動ARM架構轉譯
  - 在毋須擔憂DRM限制的情況下使用各種串流軟件
  - 透過[Google Play Store](https://play.google.com/store/games)和[F-Droid](https://f-droid.org/)安裝軟件

- [:fontawesome-solid-handshake: **合作與貢獻**][contrib]{ style="font-size: 1.1rem" }

  Bazzite從上游[Universal Blue](https://universal-blue.org/)帶來的一大特點是其開源貢獻的簡易性

  - 新系統壞了？你可以在[這裡提交Bug報告](General/reporting_bugs.md)
  - 在[自定義映像][customimage]裏測試你的修改
  - 幫助我們更新**Bazzite 指南**和[加入翻譯文檔](https://github.com/ublue-os/docs.bazzite.gg/blob/main/README.md#translate-documentation)！

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
