---
title: Bazzite 掌機版概覽
---

# Bazzite 掌機版概覽

## 甚麼是 Bazzite 掌機版？

**一個適用於家庭劇院系統及掌機的 Bazzite 版本**。其旨在打造一個支援控制器操作的環境，並為使用者提供類似 Steam Deck 上 SteamOS 的「主機級」體驗。本系統同時適用於手持式裝置及家庭劇院電腦系統，且與 SteamOS 相似，包含許多 SteamOS 內建的套件，因此安裝完成後即可立即開始遊玩遊戲。

本文檔假設使用者已熟悉 SteamOS 及其運作方式，因而可能未涵蓋某些特定領域。若你對某些內容不熟悉，且無法在本文中找到相關資訊，請以「SteamOS」或「Steam Deck」作為關鍵字進行搜尋，以查閱你具體的問題。否則，請移玉步至我們的 [**論壇**](https://universal-blue.discourse.group/c/bazzite/5) 或 [**Discord**](https://discord.gg/f8MUghG5PB) 提出你的問題。

## 甚麼是 Steam 遊戲模式？

> 閱讀 [**Bazzite掌機版相容性分頁**](../Handheld_and_HTPC_edition/Handheld_Wiki/index.md) 以獲取關於在掌機上運行 Bazzite 掌機版的更多資訊！

![Steam Gaming Mode UI|690x430](../img/Steam_Gaming_Mode_UI.jpeg)

!!! note "請注意 Steam 遊戲模式對 [GPU 硬體規格](/Gaming/Hardware_compatibility_for_gaming) 的要求相較於傳統的桌面環境較為嚴苛。"

!!! 重要訊息

    Steam 測試版客戶端**不**受支援，請在報告 Bug 前切換回穩定版客戶端。

https://www.youtube.com/watch?v=zXK1CXUyzXQ
<sub>**由 [Linux For Everyone](https://www.youtube.com/@LinuxForEveryone) 創作的 Steam Deck UI 遊覽團**</sub>

Bazzite 運用 Steam 遊戲模式，而 Steam 遊戲模式正是 Steam Deck 上 SteamOS 的核心架構。 Steam 遊戲模式是一個以 Steam Big Picture 模式 UI/UX 為基礎、專為手把操作優化的簡潔介面。此精簡模式僅在背景執行最基本的運作，確保絕大部分的硬體資源都投入到正在遊玩的遊戲中。

[**Gamescope**](https://github.com/ValveSoftware/gamescope) 是 Steam 遊戲模式的核心組件，提供設定幀率上限、解析度縮放選項等功能。Steam 遊戲模式亦被稱為 gamepadUI 和 gamescope-session ，但為保持一致性，Bazzite 指南中通常會稱其為 Steam 遊戲模式。

### Steam 輸入

!!! 溫馨提示
        
    有些遊戲與模擬器或需要**關閉** Steam 輸入以正常運作。

> 你可以閱讀這篇 [Steam 指南](https://steamcommunity.com/sharedfiles/filedetails/?id=2804823261)，其中詳細介紹了 Steam Deck 的操作技巧與訣竅，但大部分資訊同樣適用於所有運行 Bazzite掌機版的裝置。

### 我應如何在實體鍵盤上打開側選單？

**Steam 主選單**: <kbd>Ctrl</kbd>/<kbd>Win</kbd>+<kbd>1</kbd>
**快速存取選單(QAM)**: <kbd>Ctrl</kbd>/<kbd>Win</kbd>+<kbd>2</kbd>

## Valve 的官方 SteamOS 指引

!!! info "其中的資訊未必全部適用於 Bazzite 掌機版"

Valve 針對 Steam Deck 撰寫了一份[**指引**](https://help.steampowered.com/en/faqs/view/7DD4-C618-182E-0E49)，其中或包含與 Bazzite 相關的資訊。
