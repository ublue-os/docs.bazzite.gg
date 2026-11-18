---
title: Bazaar 應用程式商店
---

# Bazaar 應用程式商店

![Screenshot of the Bazaar app store|1649x1274, 50%](../img/Bazaar.png)

## 前言

Bazaar 是 **在 Bazzite 上安裝應用程式的主要方式** _(除 [Bazzite Portal](./Bazzite_Portal.md) 或 [`ujust` 指令](./ujust.md)中提供的少量軟體外)_。嚴格來説，Bazaar 是一個提供 [Flathub](https://flathub.org/) 的 [Flatpak 包](https://flatpak.org/) 的前端。

## 甚麼是 Flatpak？

Flatpak ，又稱平包、胖包，是一種通用的容器化軟件包格式。其透過靈活的權限設定，將應用程式隔離在沙盒環境中，並限制其對系統的存取範圍。使用者可透過 Bazaar 應用商店，以圖形化介面安裝和升級 Flatpak 。

### 指令行安裝方法

```bash
flatpak install <application>
```

## 管理 Flatpak

你可使用預安裝的 [Flatseal](https://github.com/tchx84/Flatseal) 和 [Warehouse](https://github.com/flattool/warehouse) 管理 Flatpak。 此外，你亦可使用 KDE Plasma 自帶的 Application Permissions → Manage Flatpak Settings 管理 Flatpak。

### Flatseal

**Flatseal** 一般用於在必要時變更 [應用程式權限](https://github.com/tchx84/Flatseal/blob/92e675e5ad2129f2aabf324261570eef442494f6/DOCUMENTATION.md)。

項目的網站和 [GitHub](<https://github.com/flathub/com.discordapp.Discord/wiki/Rich-Precense-(discord-rpc)#flatpak-applications>) 或會提供相關資訊，說明為實現特定功能所需要更改的權限（如 Discord RPC）。

### Warehouse

**Warehouse** 一般用於 **管理應用程式版本**、切換或增加其他 Flatpak 包源，以及備份應用程式的使用者資料等。

## 項目網誌

https://github.com/kolunmi/bazaar
