---
title: Bazzite 游戏入门
---

# Bazzite 游戏入门

## 趋势转变

在 Linux 上成体系的运行 Windows 游戏算是一个相对新的概念，但目前很多只面向 Windows 的游戏都已经可以在大致同等硬件配置的 Bazzite 上运行。虽然仍有些游戏存在一些障碍，但 Linux 有时也能提供更好的帧率或其他优势。

### Steam 游戏

Steam 通常是在 Bazzite 上运行 Windows 游戏最简单的方式，因为它自带了被称为 [**Proton**](/General/terms#software) 的兼容层。绝大多数单机游戏可以直接运行，但也有极少数游戏需要特定的配置调整。

有些游戏，尤其是需要联机功能的游戏，可能会需要更底层的硬件权限来实现反作弊等功能。这些功能在 Windows 上通常由专有的驱动程序实现，但 Linux 不支持这种驱动，因此这些游戏很可能只能在 Windows 上运行。

### 非 Steam 游戏

<small>_With this, we have included everything in the observable universe into Bazzite Docs, from Steam-Games... to Non Steam-Games. Q.E.D._</small>

Bazzite 预安装了 **Lutris** 以管理非 Steam 的游戏，它也同样提供 Proton/Wine 管理的功能。Bazaar 上也能找到 [**Faugus Launcher**](https://flathub.org/en/apps/io.github.Faugus.faugus-launcher)，提供相对更简洁的用户界面。对于通过 Epic Games Launcher、GOG 和 Amazon Games Launcher 运行的游戏，[**Heroic Games Launcher**](https://flathub.org/apps/com.heroicgameslauncher.hgl) 会更加合适。

在 Windows 上通过 Microsoft Store 安装的游戏**无法**在 Bazzite 上直接运行。如果你有 Game Pass Ultimate 订阅的话，可以通过 Xbox Cloud Gaming 配合 [**Greenlight**](https://github.com/unknownskl/greenlight) 或类似的客户端来进行云游戏。Fortnite 不需要订阅亦可用这种方式运行。[**一些在 Game Pass 上可用的暴雪战网游戏**](https://us.support.blizzard.com/en/help/article/000367382)可以通过 Lutris 直接安装。

游戏主机的模拟器通常可以在 Bazaar 上找到，或者通过 [**Retrodeck**](https://flathub.org/en/apps/net.retrodeck.retrodeck) 或 [**Emudeck**](https://www.emudeck.com/) 一类的项目进行集中管理。Bazzite Portal 也提供了一些相关的快捷脚本。

<hr>

## 其他资源

-   [**ProtonDB**](https://www.protondb.com/explore) - 玩家上传的 Linux 兼容性报告 
-   [**Are We Anti-Cheat Yet?**](https://areweanticheatyet.com/) - 记录一些热门游戏的反作弊组件及其 Linux 支持情况
-   [**Linux Gaming Wiki**](https://linux-gaming.kwindu.eu/index.php?title=Main_Page) - Linux 游戏的总指南，也提供一些有用的参考链接
-   [**PC Gaming Wiki**](https://www.pcgamingwiki.com/wiki/Home) - PC 游戏的总指南，也提供一些常见问题的修复指南和高级技巧
-   [**General Emulation Wiki**](https://emulation.gametechwiki.com/index.php/Main_Page) - 模拟器相关资源
-   [**Linux VR Adventures Wiki**](https://lvra.gitlab.io/) - 在 Linux 上运行虚拟现实（VR）游戏的相关信息
-   [**Linux VR Adventure Database**](https://db.vronlinux.org/) - 玩家上传的 Linux 端 VR 游戏的兼容性报告
