---
title: Bazzite軟件安裝概覽
---

# Bazzite軟件安裝概覽

## 安裝 Linux 軟件
**推薦軟件安裝方法，由夯到拉**:

1. [**Bazzite Portal (`ujust` 指令)**](./Bazzite_Portal.md) (_常用指令_) - 由 Bazzite 及 Universal Blue 貢獻者維護的自訂腳本，亦包括安裝一小部分的應用程式。<small>(此格式應當優先於其他格式，但由於僅能安裝少量軟體，因此應被視為系統層級設定的延伸，而非應用程式商店。)</small>
2. [**Bazaar 應用程式商店**](./Flatpak.md) (_圖形化應用程式_) - 應用商店前端，供用戶安裝一種適用於大多數圖形化應用程式，通稱為「平包」、「胖包」的通用軟件包，**為 Bazzite 上取得軟件的主要方式**。
3. [**Homebrew**](./Homebrew.md) (_指令行工具_) - 供安裝於系統終端中交互的指令行程式。
4. [**容器**](./Containers.md) - 供軟件獨立運行的虛擬系統環境。
    4a. [**Distrobox Containers**](./Distrobox.md) (_傳統 Linux 包管理與開發_) - 提供多數 Linux 發行版的包管理器，適用於不支援 Flatpak 和 Homebrew 的軟體，以及作開發環境用途。
    4b. [**Quadlet**](./Quadlet.md)  (_服務_) - 將容器以 [systemd 服務](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-managing_services_with_systemd#sect-Managing_Services_with_systemd-Services)的方式運行。
5. [**AppImage**](./AppImage.md) (_ Portable 應用程式／綠色軟體_) - 一種通常可從軟件網站發放並取得的可攜式通用套件格式。
6. [**`rpm-ostree`**](./rpm-ostree.md) (_系統層包_) - 疊加 Fedora 安裝包至系統樹上（不建議，僅作為後備安裝方法使用）。

## 安裝非 Linux 軟件

Bazzite 亦可運行 Windows 和 Android 應用程式。註：並非所有 Windows 和 Android 軟體都能在 Bazzite 上運行。

### Windows 軟件

**使用 [WINE](https://www.winehq.org/) ／ Proton 前端**:

- [**Steam**](https://store.steampowered.com/) (_預安裝_) 內建 Windows 相容層。
- [**Lutris**](https://lutris.net/about) (_預安裝_) 適用於非 Steam 的 PC 遊戲及非遊戲軟體。
- [**Faugus Launcher**](https://github.com/Faugus/faugus-launcher) (_可在 Bazaar 中取得_)，Lutris 的另一選擇，更簡潔、更直白。
- [**Heroic Games Launcher**](https://heroicgameslauncher.com/) (_可在 Bazaar 取得_)，用於與 Epic Games、GOG 及 Amazon Games 進行完善的整合。
- [**Greenlight**](https://flathub.org/en/apps/io.github.unknownskl.greenlight) (_可在 Bazaar 中取得_)，用於串流 Windows 商店及 Game Pass 的遊戲。<small>(**僅限遊戲串流**)</small>
- [**WineZGUI**](https://github.com/fastrizwaan/WineZGUI) (_可在 Bazaar 取得_)，適用於無需特別考量且較為簡單的 Windows 應用程式。

> 詳情請閱 [Bazzite 遊戲指南](/Gaming/index.md)。

### Android 應用程式

閱讀 [Waydroid 設置教程](./Waydroid_Setup_Guide.md)以於 Bazzite 上安裝 Android 應用程式。

## 軟件安裝流程圖

!!! 溫馨提示
        
    Bazzite Portal 僅提供安裝少量軟體，故未包括在以下圖表中。

![Software Installation Decision Tree](../img/software-install-decision-tree-light.svg#only-light)
![Software Installation Decision Tree](../img/software-install-decision-tree-dark.svg#only-dark)


| **安裝方法** | **圖像介面應用程式 (GUI)** | **指令行程式／系統包** |
|--------------------|----------------------------------|------------------------------------------|
| **Bazaar 應用程式商店 (Flatpak)** | 推薦且主要的安裝方式 | 不推介（程式運行環境則不在此限） |
| **Homebrew** | 宜安裝少量不適合 Flatpak 沙盒化環境的程式（如通過 [Universal Blue cask](https://github.com/ublue-os/homebrew-tap) 安裝的 VS Code） | 推薦且主要的安裝方式 |
| **容器 (Distrobox)** | 若軟件不在 Bazaar (Flathub) 上發佈，你可以在 Distrobox 內安裝傳統 Linux 安裝包（如提供） | 若軟件不在 Homebrew 上發佈，你可以在 Distrobox 內安裝傳統 Linux 安裝包（如提供） |
| **AppImage** | 從互聯網上尋找並下載 AppImage 執行檔（請自行承擔該風險！）， 你可使用 **Gear Lever** 以將其添加之啟動菜單中。 | — <small>_（誰家好人會用 AppImage 發指令行工具啊？！）_</small> |
| **疊加包至系統樹** | 若上述方法皆無法安裝你的軟件，你可以嘗試疊加至系統樹（請自行承擔該風險！）。 | ← 同左 |
| **獨立 Linux 執行檔** | 一些軟件會以`.tar.gz`壓縮包的形式發放執行檔。 若該執行檔支持 Linux，你或可於 Bazzite 上直接運行它（請參考軟件自身的運行指引）。 若其指引包含在某 Linux 發行版的步驟，你或可透過 Distrobox 運行它。 | ← 同左 |
| **非 Linux 軟件** | 你可使用 WINE／Proton 前端（Windows 程式）或 Waydroid（Android 程式）以運行軟件。 | — |
| **[自定義映像](../Advanced/creating_custom_image.md)** | — | 供安裝一整個桌面環境或窗口管理器及其他的大量系統包。  |
