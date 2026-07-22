---
title: 桌面環境個人化、主題與其他設置
---

# 桌面環境個人化、主題與其他設置

!!! warning
    
    個人化插件及主題有機會降低系統穩定性，**安裝風險自負**！

## 在KDE Plasma上使用個人化主題

KDE Plasma是Bazzite的預設桌面環境，亦是Linux生態中包含最多個人化設置的桌面環境<small>(_當然，你也可以在自定義系統映像檔中遊玩各種窗口管理器(Window Manager)，它們有更多、更複雜的個人化設置_)</small>。你可以在Plasma的設定程式中安裝由社區製作的自定義主題、鼠標圖案、系統圖示。這些主題會被安裝於`~/.local/share/plasma`目錄下並自動管理和分類；但有的時候你需要人手將有問題的主題或插件移除。

![Directory|401x207, 75%](../img/Directory.png)

## 手動安裝系統主題

1. 在[**KDE Store**](https://store.kde.org/browse/)中下載主題的壓縮檔
2. 將其解壓縮至`~/.local/share/plasma/` <small>(_你或須手動創建此文件夾_)</small>
3. 打開系統設定，並選擇你的主題、應用程式風格、鼠標圖案、或其他個人化設置

## 個人化設置的解壓縮路徑

以下為各種個人化設置的存取位置<small>(_你或須手動創建這些文件夾_)</small>

-   Global Themes（全域主題）: `~/.local/share/plasma/look-and-feel/`
-   Plasma Themes（Plasma主題）: `~/.local/share/plasma/desktoptheme/`
-   Plasma Window Decorations（Plasma窗口裝飾）: `~/.local/share/aurorae/themes/`
-   Icon / Cursor Themes（鼠標圖案／系統圖示）: `~/.local/share/icons`
-   Sounds（系統音效）: `~/.local/share/sounds`
-   Login Screen（登入畫面設置）: Security & Privacy → Login Screen

!!! notice 
    
    Bazzite於更新至Fedora 44之後已轉用全新的KDE Display Manager作為登入管理器。

## Flatpak應用權限和主題

一些Flatpak應用程式需額外設置一些目錄的唯讀權限以使鼠標圖案於應用內生效。

**例子**： `~/.local/share/icons/:ro`

<hr>

## 其他桌面環境的個人化設置

上文提及，KDE Plasma是Linux中包含最多個人化設置的桌面環境，因此此指南主要包含Plasma的個人化設定。

### 管理 GNOME 插件 (`-gnome` 映像及更新頻道)

你可以在「Extension Manager」（插件管理器）中安裝及管理預安裝和新的插件。

!!! warning
    
    若GNOME崩潰，其所有插件會將被自動關閉。此外，GNOME一向對插件的支持都不太友好，其在各版本更新中有不少的機率使現有插件停止運作。

### Steam 遊戲模式個人化設置 (`-deck` 映像及更新頻道)
!!! warning

    Decky Loader 或許會因新Steam及Gamescope版本而出現問題，你或須將其暫時卸載。

安裝 [Decky Loader](https://decky.xyz/) 和 [CSS Loader](https://docs.deckthemes.com/) 以對Steam遊戲模式的介面進行個人化修改。 注意第三方插件有機會降低系統穩定性。你可於[此處](../Handheld_and_HTPC_edition/quirks.md)尋找常見問題的解決方法。

<hr>

## 桌面環境文檔及指南
- [**KDE Plasma 文檔**](https://docs.kde.org/stable5/en/plasma-desktop/plasma-desktop/index.html)
- [**GNOME 文檔**](https://help.gnome.org/users/gnome-help/stable/)
- [**Bazzite Steam遊戲模式指南**](../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)
