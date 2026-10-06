---
title: Homebrew
---

# Homebrew

## Homebrew 是什么？

![Homebrew|332x500, 15%](../img/Homebrew.png)

!!! note

    Homebrew 不适合安装需要 Root 权限才能运行的工具。建议改用 rootful Distrobox 容器，或使用`rpm-ostree`。

Homebrew 是一个主要面向 macOS 的包管理器，通常适用于命令行程序的安装。它默认使用一个非系统级的路径作为根目录，因此不受系统目录只读的影响。Homebrew 通过其 Cask 组件也支持一些图形化程序的安装，但目前 Linux 上的支持仍在开发。Bazzite 预装了 Bold Brew 作为控制 Homebrew 的实用工具，但也可以直接在命令行操作：

```
brew install <package>
```

!!! note

    对于多用户或一些比较特殊的用户配置：如果 Homebrew 配置了`linuxbrew`这一用户，则很有可能需要使用`sudo`才能控制 Homebrew。

## Bold Brew

![bbrew|3164x2060, 25%](../img/bbrew-installed-screenshot.png)

[Bold Brew](https://bold-brew.com/) 是一个方便安装常用的 Homebrew 包的 TUI 程序。

## 字体

Homebrew 也可以用于安装字体。请参考 [Homebrew 提供的列表](https://formulae.brew.sh/cask-font/)以查找需要的字体。通过此方法安装的字体会保存到`~/.local/share/fonts`。

- Microsoft 字体：

Homebrew 提供绝大多数 Microsoft 字体，有时在一些文档出现兼容性问题时可能会很有用。

但请注意，这当中有些字体可能仍为 Microsoft 专有，因此可能存在版权问题。
根据 Microsoft UK 曾表明过的立场，如果你拥有或购买了以下任意产品，则你拥有使用这些字体的权利：

- Microsoft PowerPoint Viewer（免费产品，但已不再提供）
- **可能包含** PowerPoint 移动版（免费产品）
- Microsoft Office（任意 Windows 或 Mac 版）

`font-microsoft-office`包包含了 Calibri、Cambria、Candara、Consolas、Constantia 和 Corbel，其他字体则必须单独安装。使用以下指令可以同时安装所有相关字体：

```
brew tap colindean/fonts-nonfree && brew install --cask font-microsoft-office font-microsoft-aptos font-arial font-arial-black font-courier-new font-times-new-roman font-georgia
```

## 项目官网

https://brew.sh/
