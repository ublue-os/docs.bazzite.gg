---
title: Bazzite與SteamOS
---

# Bazzite與SteamOS

## 甚麼是SteamOS？

**SteamOS** 是一個原為Steam Deck而設的作業系統。SteamOS 主要作為Steam 客戶端的載體存在，但亦附裝一個簡化版的 **KDE Plasma** 桌面環境供用戶安裝模組、模擬器等工具。這被稱爲Steam 桌面模式，但作為桌面系統使用時因其精簡化的配置或有不足。

## 甚麼是 Bazzite？

Bazzite 是一個由社區推動的Linux遊戲為本作業系統，旨在包含最新的驅動程式，提供各種各樣不同的風味版本（**桌面版**、**掌機版**、和**開發者版**）。Bazzite基於[**Fedora原子桌面**](https://fedoraproject.org/atomic-desktops/)而建立，使用原子化更新系統，坐享[獨特優勢](/General/FAQ/#bazzite-fedora)。<small>_優勢在我！_</small>

### Bazzite 對比於 SteamOS 的額外功能

-   支持與Windows雙啟動
-   支持運行在**絕大部分**X86-64架構的掌機之上，包括但不僅限於： 聯想 Legion Go/S、華碩 ROG Ally/X、OneXPlayer F1/G1/X1 variants、GPD Win 4/Mini/Max、Ayn Loki、微星 Claw 1st Gen AI7+/8+、Zotac Zone、Ayaneo Air/Geek/Next、Steam Deck LCD/OLED等
-   透過 LACT 支持超頻及修改風扇曲線
-   **超雄的更新系統**
  -   你無時無刻都可以回溯至上一版本
  -   在 Bazzite 掌機版，系統將於三次啟動失敗後自動回溯
  -   支持回溯至90日內的任意Bazzite映像
-   包含最新版本的系統包，包括但不僅限於：Linux內核、顯卡驅動程式和[Gamescope](https://github.com/ValveSoftware/gamescope)
-   更新版的桌面環境，提供基於 Wayland 協議的分數縮放、自適應同步、色彩管理功能
-   預安裝各種有用的小工具，如 Lutris、ScopeBuddy GUI、ProtonUp-Qt/ProtonPlus、Protontricks等
-   除KDE Plasma外，亦有GNOME桌面環境任君選擇
-   透過 Flatpak 支持的虛擬機和顯卡直通功能
-   透過[Waydroid](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md)安裝 Android 應用程式
-   透過 Bazzite Portal 簡化的 [Sunshine遊戲串流](/Advanced/sunshine/) 安裝流程
-   匯集於 **[Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal.md)** 的各種系統設置及常用功能
-   預設使用 BTRFS ，提供自動去重及全域壓縮 (SteamOS 使用 **Ext4**) 及提供內／外置硬盤及內存卡的自動掛載功能

### 為開發者而設的功能

-   預安裝Homebrew作為用戶層的命令行工具包管理器
-   預安裝Distrobox容器管理器，提供種類繁多的軟件包管理器
-   提供[**Bazzite-DX**](https://dev.bazzite.gg/)作為開發者向的專屬Bazzite映像

### 安全性優化

Bazzite 支持使用 LUKS 全碟加密、安全開機和TPM解密。此外，Bazzite 亦預設啟用 [SELinux (安全增強式Linux)](https://www.redhat.com/en/topics/linux/what-is-selinux) 系統。

安全開機在與Windows雙啟動的時候相當有用，如用以應付各種奇形怪狀的反作弊軟件。

>關於[**安全開機（Secure Boot）設置教學**](/General/Installation_Guide/secure_boot.md).
