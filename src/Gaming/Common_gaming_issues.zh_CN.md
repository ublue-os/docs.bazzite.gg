---
title: 游戏常见问题
---

# 游戏常见问题

## 选择 Linux 原生版还是 Windows 版？

有些游戏的 Linux 原生版可能会少一些功能或在性能上弱于通过 Proton 运行 Windows 版，但也有些游戏可能只能使用原生版，需要具体游戏具体分析。

如果一个游戏提供了 Linux 原生版但它无法正常启动，可以尝试强制使用 **Legacy Runtime** 兼容性工具。在 Steam 的**游戏属性**下的**兼容性**菜单勾选 **Force the use of a specific Steam Play compatibility tool** 即可选择它。

!!! warning "Counter Strike 2 **必须**使用 Linux 原生版运行（在 Steam 的游戏配置中禁用**Force the use of a specific Steam Play compatibility tool**）。运行 Proton 版的 CS2 可能会导致账户被 VAC 封禁。"

## Denuvo 防篡改保护的游戏

Denuvo 会将 Proton 版本的切换视为在新硬件上激活游戏，因此如果在 24 小时内切换超过 5 次将会导致激活失败，无法启动游戏。等待 24 小时后即可再次尝试。

---

## Source 1 引擎的音频或自定义内容

!!! note

    本章节只针对基于 [Source 引擎](https://www.pcgamingwiki.com/wiki/Engine:Source) 的游戏的相关问题。

!!! attention

    除非你确实碰到了这些音频或 _Left 4 Dead 2_ 相关的问题，否则不需要，也不应该执行这些步骤。

在 Source 引擎的游戏中发现音频或自定义内容无法加载？问题在于 SELinux 阻止了 MP3 的解码以及其他一些组件的正常运行。本质原因是 Source 引擎在执行这些操作时[**将堆内存作为代码执行**](https://github.com/ValveSoftware/steam-for-linux/issues/43)了。Bazzite 基于 Fedora，因此默认启动 SELinux，这和基于 Arch Linux 的 SteamOS 不同。

在 _Left 4 Dead 2_ 中自定义地图房间的创建和加入失败也可能是这个问题。

### 音频或自定义内容的修复

!!! 警告

    SELinux 配置仅适合进阶用户操作。作为安全相关的内核底层组件，错误的配置可能会影响系统其他功能的正常运行，并降低系统安全性。

为了修复这些音频和自定义内容的问题，必须通过解析已有的`hl2_linux`触发的 SELinux 安全日志，生成并加载一个 SELinux 模块，以将这些操作加入允许运行的白名单。

<del>当你醒来，你会发现一切都变了......</del>

=== "生成并安装策略模块"

    ```bash
    sudo -i
    cd /tmp
    ausearch -c 'hl2_linux' --raw | audit2allow -M my-hl2linux
    semodule -X 300 -i my-hl2linux.pp
    ```
    如果没有解决，请尝试重启。

=== "禁用策略模块"

    ```bash
    semodule -X 300 -d my-hl2linux
    ```

=== "移除策略模块"

    ```bash
    semodule -X 300 -r my-hl2linux
    ```
    生成模块的步骤会把对应的 `.pp` 文件生成在 `/root/` 目录下，如有需要可以手动删除。

---

## Steam 游戏无法启动

Steam 游戏无法启动也有很多种情况。以下列出一些可能导致游戏立刻关闭或崩溃的问题（**开始游戏**按钮短暂显示**停止**之后很快跳回**开始游戏**）。

### `gamemoderun`

!!! note

      这里讨论的不是 Bazzite 掌机版（bazzite-deck）提供的**游戏模式**。 而是向操作系统申请各种优化以提升游戏性能的工具 (Feral) GameMode。

ProtonDB 上经常有用户建议将启动选项设定为`gamemoderun %command%`，但在 Bazzite 上这很可能导致游戏无法正常启动。

我们建议直接将它移除，原因有三：<small>_人有五名，代价有三个......_</small>

-   Bazzite 不预安装 GameMode，也不计划支持；
-   GameMode 在较新硬件上带来的性能提升非常有限；
-   有些极端情况下甚至会导致性能损失。

It might work if you layer the `gamemode` package, but this is **NOT** supported.

### NTFS 文件系统下的权限问题

**不要把游戏安装在 NTFS 文件系统的分区上**。Windows 创建的宗卷通常是 NTFS 文件系统。[**此处**](./Hardware_compatibility_for_gaming.md#unsupported-filesystems-for-secondary-drives)提供了更多信息。

### 多用户环境下使用 Wine

!!! note

    Bazzite 掌机版（bazzite-deck）不支持多个 Linux 用户的配置，因此本章节只适用于桌面版。

有时如果你从另一个 Linux 用户启动 Steam 游戏，可能会出错。一个常见的原因似乎是 Wine Prefix 文件的所有权问题，其典型标志为新用户的` ~/.local/share/Steam/logs/console-linux.txt`下类似于这样的错误:

```
wineserver: /SteamLibrary/steamapps/compatdata/377160/pfx is not owned by you
```

一种解决方法是创建一个公用的 Steam library 来保存 Proton 需要的 Prefix 数据，并通过符号链接（_symlink_）将其他对应文件夹也映射到下面。

```console
USER2@bazzite: /mnt/ExtraStuff/USER2SteamLibrary/steamapps$ ls -la
total 32
drwxrwxr-x. 3 USER2 steamplayers 4096 Jan 29 15:19 .
drwxrwsr-x. 3 USER2 steamplayers 4096 Jan 29 16:13 ..
-rwxr-xr-x. 1 USER2 USER2         2287 Jan 29 15:19 appmanifest_377160.acf
lrwxrwxrwx. 1 USER2 USER2           51 Jan 29 15:10 common -> /mnt/ExtraStuff/USER1SteamLibrary/steamapps/common/
drwxr-xr-x. 3 USER2 USER2         4096 Jan 29 15:13 compatdata
lrwxrwxrwx. 1 USER2 USER2           56 Jan 29 15:12 shadercache -> /mnt/ExtraStuff/USER1SteamLibrary/steamapps/shadercache/
lrwxrwxrwx. 1 USER2 USER2           49 Jan 29 15:12 temp
lrwxrwxrwx. 1 USER2 USER2           53 Jan 29 15:12 workshop
```

进一步的话，可以复制或链接各个库下的 appmanifest 文件，以保证每个 Steam library 都能看到游戏。

---

## 生成 Proton 日志

如果通过 Proton 运行游戏时遇到问题，可以用以下步骤生成日志文件。

1.  在 Steam 或 其他启动器的启动选项里配置[环境变量](/Gaming/launch-options-env-variables) `PROTON_LOG=1 %command%`；
2.  再次启动游戏；
3.  你的用户目录（`/home/[用户名]`）下应该会生成一个名字包含游戏的 Steam ID 命名的`.log`文件，类似于`steam-{App ID}.log`。

在寻求支持或向 Valve 提供错误报告时，通常会需要这个文件。
