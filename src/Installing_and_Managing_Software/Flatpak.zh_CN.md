---
title: Bazaar 应用商店
---

# Bazaar 应用商店

![Bazaar 应用商店的截图|1649x1274, 50%](../img/Bazaar.png)

## 目的

Bazaar 是 **Bazzite 主要支持的应用程序安装平台** _(除非是 [Bazzite Portal](./Bazzite_Portal.md) 或[`ujust`命令](./ujust.md)提供快捷安装的软件)_，其本质为预配置了 [Flathub](https://flathub.org/) 为软件源的 [Flatpak](https://flatpak.org/) 的图形化前端。我们推荐绝大多数可用的应用程序都通过 Bazaar 安装。

## Flatpak 是什么？

Flatpak 是一个自带沙盒和权限管理的通用化的软件包格式。Bazzite 选择 Flatpak 作为**安装应用程序的主要方式**。Bazaar 应用商店提供了图形化的 Flatpak 管理。

### 命令行操作

在终端输入：

```
flatpak install <application>
```

## Flatpak 管理

Bazzite 预装了 [Flatseal](https://github.com/tchx84/Flatseal) 和 [Warehouse](https://github.com/flattool/warehouse) 两个工具方便 Flatpak 的管理。

### Flatseal

**Flatseal** 提供修改 Flatpak [权限配置](https://github.com/tchx84/Flatseal/blob/92e675e5ad2129f2aabf324261570eef442494f6/DOCUMENTATION.md)的图形化界面。

一些提供 Flatpak 包的项目可能会在其官网或[代码仓库](<https://github.com/flathub/com.discordapp.Discord/wiki/Rich-Precense-(discord-rpc)#flatpak-applications>)中提供一些有关特定功能需要的非默认权限的信息。

### Warehouse

**Warehouse** 提供 Flatpak 安装与管理的图形界面，可以用于**已安装 Flatpak 的降级**等。如果使用 Flathub 之外的软件源，应注意风险，并做好相关备份。

## 项目官网

https://github.com/kolunmi/bazaar
