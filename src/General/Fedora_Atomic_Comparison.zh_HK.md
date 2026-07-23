---
title: Bazzite與Fedora原子化發行版
---

# Bazzite與Fedora原子化發行版

## 甚麼是Bazzite？

Bazzite是一個基於[**Fedora原子桌面**](https://fedoraproject.org/atomic-desktops/)的系統映像。其中，KDE和GNOME的原生映像又分別稱為[**Fedora Kinoite**](https://fedoraproject.org/atomic-desktops/kinoite/)和[**Fedora Silverblue**](https://fedoraproject.org/atomic-desktops/silverblue/)。Bazzite在基於Fedora原子化發行版的基礎上額外作出修改，旨在提供一個更容易上手的體驗。

## 主要差異

以下為Bazzite與上游Fedora原子化發行版的主要差別：

### 更精簡的安裝後設置

-   提供更全面的硬件支援，從外部設備到核心部件都更加「開箱即用」的體驗
-   預安裝各種多媒體系統包，你毋須額外設置便可使用硬件加速編／解碼
-   預安裝各種熱門啟動器，如Steam、Lutris等
-   移除為人詬病的Fedora Flatpak，使用[Flathub官方倉庫](https://flathub.org/)

### 更高的易用性

-   常用的設置和功能皆匯集於[Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal/)介面和[**`ujust`**](/Installing_and_Managing_Software/ujust/)命令行工具當中
-   在[**Bazzite-Deck映像**](/Handheld_and_HTPC_edition/Steam_Gaming_Mode/)中預先為你設置好Steam遊戲模式

### 為開發者而設

-   預安裝Homebrew作為用戶層的命令行工具包管理器
-   預安裝Distrobox容器管理器，提供種類繁多的軟件包管理器
-   提供[**Bazzite-DX**](https://dev.bazzite.gg/)作為開發者向的專屬Bazzite映像

### 額外功能

-   透過[**Waydroid**](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md)支持運行Android應用程式
-   取消Firefox系統包，改為可卸載、更新更頻密的Flatpak版本
-   自動掛載任何BTRFS或Ext4格式的次要硬盤
-   附帶額外桌面環境插件和主題
-   支持回溯至90日內的任意Bazzite映像
