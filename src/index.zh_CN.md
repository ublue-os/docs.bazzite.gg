---
title: 首页
hide:
  - navigation
---

# Bazzite，启动！

<div class="grid cards _bz" markdown>

- [:material-harddisk: **安装 Bazzite**](General/Installation_Guide/index.md){ style="font-size: 1.1rem" }

  Bazzite 支持各种各样的台式机与笔记本，也包括较新的 [**Framework**](https://frame.work/) 等型号。 <br>

  除此之外 Bazzite 也支持面向手柄控制的家庭影院或掌机配置：
  
  - [**华硕**][ally]
  - [**联想**][legion_go]
  - [**GPD**][gpd]
  - [**OneXPlayer**][onex]
  - [**Ayn**][ayn]
  - [**Ayaneo**][ayaneo]
  - [**Steam Deck**][deck]
  - [**以及其他**][otherhand]

- [:material-controller: **游戏**][gaming]{ style="font-size: 1.1rem" }

  Bazzite 预装了 :fontawesome-brands-steam: [**Steam**](https://store.steampowered.com) 和 [**Lutris**](Gaming/Game_Launchers.md#non-steam-games) 保证各种硬件配置都能运行所有 PC 端游戏<sup>*</sup>。

  除此之外也兼容：

  - [**Heroic Games Launcher**](https://heroicgameslauncher.com/) 集成的 Epic Games、GOG 和 Amazon Games 商店。
  - 其他在 Linux 上原生运行的游戏，包括 [**osu!**](https://flathub.org/apps/sh.ppy.osu) 和 [**Minecraft**](https://flathub.org/apps/org.prismlauncher.PrismLauncher)。
  - ... [**以及其他**](https://flathub.org/en/apps/category/game/1)

  <small>*当然是指能在 Linux 上运行的 PC 游戏。[**ProtonDB**](https://protondb.com) 和 [**Are We Anti-Cheat Yet?**](https://areweanticheatyet.com) 提供了更多相关信息</small>。

- [:material-download-circle: **安装软件**][installing_software]{ style="font-size: 1.1rem" }

  <small>以下顺序对应推荐的优先级：</small>

  1. [**Bazzite Portal**][bazzite_portal] 对应 Bazzite 专门配置的安装流程。
     {style="list-style-type: decimal;"}
  2. [**Bazaar 应用商店（Flatpak）**][flatpak] 适用于绝大多数情况。
     {style="list-style-type: decimal;"}
  3. [**Homebrew**][homebrew] 适用于纯命令行的程序和工具。
     {style="list-style-type: decimal;"}
  4. [**Containers**][containers] 用于调用 Linux 包管理器（`apt`、`dnf`、`pacman` 等）、软件开发或服务部署等场景。
     {style="list-style-type: decimal;"}
  5. [**Appimage**][appimage] 作为自解压的便携程序。
     {style="list-style-type: decimal;"}

  [`rpm-ostree` 配置系统树][rpm-ostree]也是一种方法，但[**通常建议尽量避免**][rpm-ostree_caveats]，防止这些额外包的解析影响未来的系统更新。

- [:fontawesome-solid-circle-arrow-down: **更新与回滚**][updateindex]{ style="font-size: 1.1rem" }

  简单的更新流程，且配有防止问题回溯的机制。任何时候都可以回滚到 90 天内发布的 Bazzite 版本中，不会丢失个人文件。

  - [**更新指南**][updates]
  - [**回滚系统更新**][rollbacks]
  - [**切换到其他镜像**][rebasing]
  - [`bazzite-rollback-helper`][rollback-helper]

- [:fontawesome-brands-android: **Android 应用**][waydroid]{ style="font-size: 1.1rem" }

  通过 [**Waydroid**](https://waydro.id/) 即可在容器内运行 Android 应用。

  - 工具、办公软件、游戏等都有支持；
  - 绝大多数应用支持 ARM 转译；
  - 绕过一些串流软件的 DRM 问题；
  - 通过 [**Google Play 商店**](https://play.google.com/store/games) 和 [**F-Droid**](https://f-droid.org/) 安装更多软件。

- [:fontawesome-solid-handshake: **支持开发**][contrib]{ style="font-size: 1.1rem" }

  Bazzite（也包括其上级的 [Universal Blue](https://universal-blue.org/)）力求让所有人都可以参与开发。

  - 随时[**报告遇到的问题**](General/reporting_bugs.md)；
  - 通过[**自制镜像**][customimage]测试你的修改想法；
  - 当然也欢迎进一步充实文档或[**提供更多语言的翻译**](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/README.md#translate-documentation)。

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
