---
title: 基于 Bazzite 的自定义镜像
---

# 基于 Bazzite 的自定义镜像

## 使用场景

- 你想换掉一些 Bazzite 预装的程序，但又不想从头配置或和 Bazzite 偏离太远；
    - 比如：Bazzite 预装了 Waydroid 但不进行任何初始设置。如果你确定完全不需要其功能且想要省下这些空间，则可以将其移除；
    - 你需要在系统树中特定 RPM 打包的软件（比如 VPN），但又不想从头配置全新的镜像。（_抄作业一时爽，一直抄作业一直爽_）
    - 你有特定的个人习惯的软件组或配置想要自动应用，但也想更高效的接入上游的变化；
    - 你想使用 Bazzite 目前不提供的其他桌面环境或窗口管理器。
- 你想向 Bazzite 项目提交修改，因此在发起 PR 之前需要进行测试。
    - 在修复合并前测试硬件驱动或固件方面的变化，或其他实验性的功能。

## 推荐方法

### 选项 A - 模板镜像

Universal Blue 提供了[**万金油模板镜像**](https://github.com/ublue-os/image-template)。我们建议从这份模板出发来定义新的镜像，而非直接 Fork Bazzite 仓库。

#### 视频指南

https://www.youtube.com/watch?v=IxBl11Zmq5w

### Option B - Fork

如果你只想在 Bazzite 定义的基础上进行非常少量的变化，也可以考虑 **Fork**。我们建议在维护 Fork 时借助[**GitHub 的 Pull 工具**](https://github.com/apps/pull)来保证其能够及时更新。

### Option C - BlueBuild

[**BlueBuild**](https://blue-build.org/learn/universal-blue/) 曾经是 Universal Blue 自定义镜像的初始工具，但后来逐渐分离出来成为了单独的项目。BlueBuild 构建的镜像相关的问题应[直接提到上游](https://blue-build.org/community/)。
