---
title: 启动选项与环境变量
---

# 启动选项与环境变量

## 前言

近几年 Linux 上的游戏运行已经比以往方便了很多。当然，对于需要一些特定运行选项或配置的情况，Bazzite 也同样支持。这部分指南将简单总结一些可以在 Bazzite 上进行的高级配置。

## DXVK、MangoHud 和 vkBasalt 的配置文件模板

![模板文件|690x334, 50%](../img/DXVK_Mango_VkBasalt_templ.png)

在 Bazzite 上可以利用这些模板文件快速创建一些常用工具所需要的配置文件。只需要在文件管理器的任意处右键点击即可。除此之外，也有 [**Mango Juice**](https://flathub.org/en/apps/io.github.radiolamp.mangojuice) 这样的程序提供配置 Mangohud 的图形界面。

## Steam 启动选项与实用工具

Steam 启动选项允许你向游戏传递环境变量、参数或额外命令。Bazzite 额外提供了一些实用程序和界面优化来帮助你完成一些常用操作，这在掌机上的效果尤其明显。

### 启动选项中的常用语法

Steam 游戏的启动选项通常都符合 `ENVIRONMENT_VARIABLES command_or_script %command% --arguments` 的模式。

- `%command%` 对应游戏的可执行文件本身，因此除了以下两种情况外，必须在启动选项中出现：
  - 启动选项为空，或只有`--arguments`的参数（比如`--wine-canonical-hole=SKIP_VOLATILE_CHECK`）；
  - 命令或脚本本身即可启动游戏且不需要经过 Steam。
- 环境变量应在 `%command%` 之前，但以下三种情况下可以省略：
  - 在 `~/.config/environment.d` 或其他全局变量的加载位置已经定义的值；
  - 在 Bazzite Portal 中已经定义的值（本质上就是上一条）；
  - `%command%` 前的命令或脚本会设置的环境变量。
- `%command%` 之后的参数被视为提供给游戏可执行文件本身。

**示例:**
```bash
PROTON_LOG=1 %command%                    # 启用 Proton 的日志
STEAMDECK=0 %command%                     # 禁用 Steam Deck 相关调整
PROTON_ENABLE_NGX_UPDATER=1 %command%     # 允许 Proton 覆盖 DLSS 组件以升级
%command% --in-process-gpu                # 在一些 Unity 游戏中修复启动时白屏的问题，%command% 可以省略
scb %command%                             # 用 ScopeBuddy （Gamescope 的辅助程序）启动游戏
```

### Proton 启动选项
<small>_觉得很眼熟吗？本章（的英文版）直接来自于 [Proton-CachyOS Wiki](https://wiki.cachyos.org/configuration/gaming/#environment-variables)。<del>你可能就是下一个！</del>_</small>

自定义 Proton 版本的往往自带比较激进的默认配置。具体情况请参考各个项目的官方文档。

- Proton-CachyOS
  - [Readme](https://github.com/CachyOS/proton-cachyos/blob/cachyos_main/README.md#proton-cachyos-config-options)
  - [Changelogs](https://github.com/CachyOS/proton-cachyos/blob/cachyos_main/CHANGELOG.md)
- Proton-EM
  - [Readme](https://github.com/Etaash-mathamsetty/Proton/blob/em-11-hdr/README.md)
  - [EM-ADDITIONS](https://github.com/Etaash-mathamsetty/Proton/blob/em-10-hdrtest/docs/EM-ADDITIONS.md)
  - [FSR4](https://github.com/Etaash-mathamsetty/Proton/blob/em-10-hdrtest/docs/FSR4.md)
  - [Wine-Wayland](https://github.com/Etaash-mathamsetty/Proton/blob/em-10-hdrtest/docs/CHANGES.md)

### Bazzite 提供的实用工具

Bazzite 针对一些常用的启动选项提供了一些捷径。

#### Steam Deck 模式开关

- **`sd0 %command%`** - `SteamDeck=0 %command%` 的简写形式
  - 关闭一些游戏针对 Steam Deck 的特殊配置
  - 用例：Expedition 33 在不进行该设置时默认采用面向 Steam Deck 的（比极低还低的）画质预设，并禁用绝大多数画质选项。

#### NVIDIA (dlss-swapper)

- **`dlss-swapper %command%`** - 用 NGX Updater 自动应用最新的 DLSS 配置
  - 本质为`PROTON_ENABLE_NGX_UPDATER=1 DXVK_NVAPI_DRS_SETTINGS=NGX_DLSS_SR_OVERRIDE=on,NGX_DLSS_RR_OVERRIDE=on,NGX_DLSS_FG_OVERRIDE=on,NGX_DLSS_SR_OVERRIDE_RENDER_PRESET_SELECTION=render_preset_latest,NGX_DLSS_RR_OVERRIDE_RENDER_PRESET_SELECTION=render_preset_latest %command%`的简写
- **`dlss-swapper-dll %command%`** - 同上，但跳过 NGX Updater

!!! info

    DLSS 并非一刀切的越新越好，因此 Bazzite 有意保留了这套配置，而非完全依赖较新的 `PROTON_DLSS_UPGRADE=1`（此功能在 Bazzite Portal 上亦有记载）。

#### 如何设置启动选项

1. 在 Steam 库中右键选择一个游戏
2. 选择**属性...**
3. 在**通用**一栏中，找到**启动选项**的输入框
4. 输入你需要的启动选项

![启动选项|833x594, 75%](../img/Steam_Launch_Options.png)

## 帧率限制相关问题

游戏模式（Gamescope）支持多种帧率限制的方式，但根据游戏与硬件配置，并非所有方法都稳定有效。

帧率限制的效果有时并不稳定，尤其是在桌面模式下。

以下列出了一些常用的帧率限制方法和对应表现。

=== "Steam 游戏模式（Gamescope 会话）"

    | 方法 | 如何设置 | 是否需要游戏内启用垂直同步？ | 不重启游戏能否生效？ | 对延迟的影响 | 是否推荐 | 备注 |
    |---|---|---|---|---|---|---|
    | **Gamescope 自带帧率限制** | Use **Quick Access Menu → Performance → Framerate Limit** | 否 | 是 | 相对较差 | **推荐** | Automatically enables v-sync at driver-level whenever the framerate cap is enabled. Additional latency will be introduced. |
    | **MangoAPP（Gamescope 集成）** | - | - | - | - | – | 默认会话无法添加需要的参数，因此不可用。 |
    | **MangoHUD（外部安装）** | **游戏启动选项**：`MANGOHUD=1 %command%` | 否 | 是 | 相对较差 | – | 在`MangoHud.conf` 中进行配置（`fps_limit=0,{fps}...`，0对应无限制），或使用 [MangoJuice](https://flathub.org/en/apps/io.github.radiolamp.mangojuice)。 |
    | **DXVK/VKD3D runtime frame limiter** | **DXVK(D3D8/9/10/11):** `DXVK_FRAME_RATE={fps} %command%`<br>**VKD3D(D3D12):** `VKD3D_FRAME_RATE={fps} %command%` | No | No | Generally Better | – | Applies only to DXVK/VKD3D titles (no effect on native OpenGL or Vulkan games). |

=== "桌面模式 （GNOME/KDE Plasma 桌面会话）"

    | 方法 | 如何设置 | 是否需要游戏内启用垂直同步？ | 不重启游戏能否生效？ | 对延迟的影响 | 是否推荐 | 备注 |
    |---|---|---|---|---|---|---|
    | **Gamescope 自带帧率限制** | **游戏启动选项**：`gamescope -r {fps} -- %command%`或`--framerate-limit {fps}` | 是 | 是* | 相对较差 | – | *`gamescopectl debug_set_fps_limit {fps}`可以不重启游戏应用新的限制值。 |
    | **MangoAPP（Gamescope 集成）** | **游戏启动选项**：`gamescope --mangoapp -- %command%` | 是 | 是 | 相对较差 | – | 限制有时无法生效。配置方式参考 MangoHUD。 |
    | **MangoHUD（外部安装）** | **游戏启动选项**：`MANGOHUD=1 %command%` | 否 | 是 | 相对较好 | **推荐** | 限制通常稳定生效。在`MangoHud.conf` 中进行配置（`fps_limit=0,{fps}...`，0对应无限制），或使用 [MangoJuice](https://flathub.org/en/apps/io.github.radiolamp.mangojuice)。 |
    | **DXVK/VKD3D 自带帧率限制** | **DXVK(D3D8/9/10/11):** `DXVK_FRAME_RATE={fps} %command%`<br>**VKD3D(D3D12):** `VKD3D_FRAME_RATE={fps} %command%` | 否 | 否 | 相对较好 | – | 只适用于需要转译的 DirectX 游戏，对本身是 OpenGL 或 Vulkan 的游戏无效。 |

如果限制配置没有生效，以下两步可能会有帮助：

- 禁用帧率自适应同步（Adaptive sync）和可变刷新率（VRR）；如果你的 Gamescope 启动参数中有`--adaptive-sync`，尝试移除。
- 在游戏内启动垂直同步（Vsync）。

!!! Note

    游戏内的延迟往往是个很复杂的问题，不同配置的情况可能天差地别。几乎不可能有一套解决一切问题的“完美”参数，而是需要用户根据自己的实际需求不断进行打磨与测试。
    
    除此之外，上游的 DXVK 和 VKD3D 自 3.0 版本起已经不再支持直接通过 `DXVK_FRAME_RATE` 环境变量来限制帧率，而是由 Proton 按自身需求进行调整。Valve 官方的 Proton 使用的是上游的 DXVK/VKD3D，因此如果你仍然需要在 DXVK/VKD3D 层面上限制帧率，则需要[特定的 Proton 版本](#proton-launch-options) 或用自定义版本的 DXVK 直接配合 Wine 运行，比如 [DXVK Low-Latency](https://github.com/netborg-afps/dxvk-low-latency).
    
    Proton-CachyOS 自带 DXVK-LL，因此支持 `PROTON_DXVK_LOWLATENCY=1`，是一个不错的出发点。

## 使用 ScopeBuddy 进一步调整启动选项

[**ScopeBuddy** 的文档](../Advanced/scopebuddy.md) 将会介绍在 Gamescope 上更进一步的启动选项管理。
