---
title: Homebrew
---

# Homebrew

## 甚麼是 Homebrew?

![Homebrew|332x500, 15%](../img/Homebrew.png)

!!! 溫馨提示

    絕大部分需要 root 權限的包皆需要 rootful Distrobox 容器或 `rpm-ostree` 疊加至系統樹。

Homebrew 是一個會將套件安裝至其專屬位置的軟件包管理工具。其主要用於命令列介面（CLI）／終端機介面（TUI）應用程式。Homebrew 亦可透過 `--cask` 參數安裝圖形化應用程式（GUI），但因 Linux 平台上對 Cask 的支援仍在開發中，其中大多皆僅適用於 macOS。你可以使用 Bold Brew 應用程式，或透過指令行執行以下指令來安裝 Brew 軟件。

開啟系統終端並輸入以下指令以安裝 Brew 軟件包：

```bash
brew install <package>
```

!!! 溫馨提示

    在多用戶或非一般的系統設置上，因其使用獨立的 `linuxbrew` 用戶組進行安裝，安裝 Homebrew 軟件包將需要使用 root 權限。

## Bold Brew

![bbrew|3164x2060, 25%](../img/bbrew-installed-screenshot.png)

[Bold Brew](https://bold-brew.com/) 提供一個指令行介面以安裝常用的 Brew 軟件包。

## 項目網誌

https://brew.sh/
