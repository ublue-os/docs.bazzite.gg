---
title: Cardwire
---

# Cardwire

![Cardwire 界面截图|2224x1468, 25%](https://github.com/OpenGamingCollective/cardwire/raw/main/assets/org.opengamingcollective.cardwire.screenshot.png)

## 概述

Cardwire 通过 eBPF 和 LSM 触发器监听并按规则处理对显卡设备节点的调用请求，包括`/dev/dri/renderDX`、`/dev/dri/cardX`、sysfs 的 `config`、`nvidiaX`等各类显卡相关文件。

显卡被“阻挡”时，eBPF 会拦截所有对该设备的请求并返回 -ENOENT 错误代码，因此从调用程序的视角来看这块显卡并不存在。和常规的显卡控制方式相比这提供了一些独特优势：

-   程序启动更快：有些程序（尤其是 Electron 或 GTK 程序）总会尝试遍历所有显卡，这往往会导致程序浪费 3-4 秒的时间重新启动休眠状态的显卡；
-   省电：在系统调用层面拦截所有请求使得显卡可以始终停留在最低级的电源状态（D3cold）而不需要被唤醒，这在笔记本类的设备上有助于延长电池续航；
-   非侵入性：传统方法往往需要进行暂时禁用相关驱动或其他影响整个系统的操作，而 Cardwire 的配置方式的适用范围可以精细控制，开关也更方便。

!!! note "Cardwire 只支持 Wayland 桌面环境，不支持 X11。"

---

## 配置

Cardwire 可以通过自带的图形界面或命令行进行设置。

```console
CLI for cardwire GPU management

Usage: cardwire <COMMAND>

Commands:
set      Set to the desired mode
get      Get the current mode
list     Print the gpu list
gpu      Manage a specific GPU by its id
config   Manage daemon configuration
manager  Manager operations
debug    Debug operations
launch   Launch a program on the specified GPU
help     Print this message or the help of the given subcommand(s)

Options:
-h, --help     Print help
-V, --version  Print version
```

---

## 用法

如果需要一个 Steam 游戏总是在一块特定显卡上运行，则应设置以下 [Steam 启动选项](/Gaming/launch-options-env-variables.md)：

```bash
cardwire launch %command%
```

!!! note "Cardwire 不需要也不应该和`switcherooctl`、`envycontrol`或`supergfxctl`等其他显卡管理工具一起使用。"

> 参考 [Cardwire 官方文档](https://opengamingcollective.github.io/cardwire/)以获取更多信息。

---

## 项目官网

https://github.com/OpenGamingCollective/cardwire
