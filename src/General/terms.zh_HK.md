---
title: 用語和詞庫
---

# 用語和詞庫

## 泛用詞彙

-   [[桌面]Linux](https://www.ubuntudocs.com/bdesktop/) <small>[Internet Archive備份](https://web.archive.org/web/20240813064251/https://www.ubuntudocs.com/bdesktop/)</small>：一個包含並共享許多相同核心軟體（包括 [Linux 內核](https://www.kernel.org/)與 [GNU核心工具組](https://www.gnu.org/software/coreutils/)）的作業系統家族。
-   [桌面環境](https://zh.wikipedia.org/wiki/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83) <small>[Arch 維基頁面](https://wiki.archlinuxcn.org/wiki/%E6%A1%8C%E9%9D%A2%E7%8E%AF%E5%A2%83)</small>：在 Steam 桌面模式和 Bazzite 桌面版的使用者介面與體驗（UI&UX），又稱 *DE* 。
-   [Fedora Linux](https://fedoraproject.org/zh-Hant/)：一個具前瞻性的 Linux 作業系統發行版，其每6個月就會推出一個新版本。
-   [Fedora原子桌面](https://fedoraproject.org/zh-Hant/atomic-desktops/)：一個基於 Fedora Linux 並使用原子更新技術的官方分支。其中兩個最受歡迎、且最常用的版本為[**Fedora Kinoite**](https://fedoraproject.org/zh-Hant/atomic-desktops/kinoite/)和[**Fedora Silverblue**](https://fedoraproject.org/zh-Hant/atomic-desktops/silverblue/)，分別為KDE和GNOME桌面環境的原生版本。
-   [不可變作業系統](https://blog.verbum.org/2020/08/22/immutable-%E2%86%92-reprovisionable-anti-hysteresis/)：一個用以形容使用非傳統檔案系統佈局的桌面 Linux 系統的名詞。實際上， [Bazzite 系統並非完全不可變](https://docs.fedoraproject.org/zh_Hant/atomic-desktops/technical-information/)，而 Bazzite 亦不希望人們使用「不可變作業系統」來形容 Bazzite。
-   [Open Gaming Collective／OGC／開放遊戲聯盟](https://github.com/OpenGamingCollective)：一個由各組織與社區成員所組成的工作小組，旨在為各類遊戲為本組件提供予上游的變更設立一個協作框架，使所有以 Linux 遊戲為核心的開源專案受益。

## 關於 Bazzite 掌機版

-   [Steam Deck](https://store.steampowered.com/steamdeck)： Valve 的掌機／遊戲機。其使用並運行 Valve 基於 Linux，並為 [Steam 客戶端](https://store.steampowered.com/about/download)而設的 SteamOS 作業系統。
-   [SteamOS 作業系統](https://www.steamdeck.com/zh-tw/software)： 由Valve 推出的、基於 [Arch Linux](https://archlinux.org/) 的、Steam Deck使用的 Linux 作業系統。
-   [Gamescope](https://github.com/ValveSoftware/gamescope)： 為 SteamOS 而設的微型合成器。擁有多種功能，如全屏縮放、縮放濾鏡、幀率限制器、高動態範圍(HDR)等。
-   [Steam 遊戲模式](https://github.com/bazzite-org/gamescope-session)： 一個在 Gamescope 上運行 Steam Big Picture 模式介面的工具，又稱*Game Mode*。

## 關於 Bazzite 的常用軟件

- **[Proton](https://github.com/ValveSoftware/Proton)**： 一個由 Valve 維護，基於[WINE](https://www.winehq.org/)，並匯合各種工具如[DXVK](https://github.com/doitsujin/dxvk)和[VKD3D](https://github.com/HansKristian-Work/vkd3d-proton)的相容性轉譯層。
- [**Vulkan**](https://www.vulkan.org/)： 一個源自 AMD Mantle 的跨平台、開放標準低層圖形API，用以替代僅限 Windows 系統使用的 DirectX。絕大部分的 Linux 軟件（包括使用 Proton 轉譯層的 Windows 軟件）皆使用 Vulkan 圖形API。
- [**OpenGL**](https://www.opengl.org/)： 源於 Vulkan 尚未普及年代的傳統圖形API。在新 Intel ARC 顯卡上已不設 OpenGL 的原生驅動程式，而採用 [Zink 轉譯層](https://docs.mesa3d.org/drivers/zink.html)轉譯至 Vulkan。
- **[Flatpak](https://flatpak.org/)** <small>_又稱胖包、平包_</small>： Linux 通用安裝包格式，預設的安裝包源為 [Flathub](https://www.flathub.org)。
- [**Containers**](https://www.redhat.com/en/topics/containers)：容器，一個獨立、不受主系統影響的運行環境，常用於開發環境。

## 關於 Bazzite 所使用的底層技術

-   **[系統樹/OSTree/libostree](https://ostreedev.github.io/ostree/introduction/)**: Bazzite 使用的原子化更新系統，包含各式各樣如系統回溯、切換更新頻道的功能。
-   **[InputPlumber](https://github.com/shadowblip/InputPlumber)**: 一個適用於 Linux 的開源輸入源路由與控制程式。它可用於整合任意數量的輸入裝置如遊戲手柄、滑鼠和鍵盤，並將其輸入轉換為各種虛擬裝置格式。
-   **[OpenGamepadUI](https://github.com/ShadowBlip/OpenGamepadUI)**: 一個自由、開源、為提供原生手柄操作體驗而設的遊戲啟動器和介面。其包括將手柄輸入重新映射為滑鼠與鍵盤輸入的功能。
-   **[Universal Blue](https://ublue.it)**: 一個自由且開源，專為製作自定義 Fedora 映像的組織。
-   **[可啟動的容器映像(Bootable Container Image)](https://docs.fedoraproject.org/en-US/bootc/getting-started/)**: 於已有容器映像上安裝軟件和系統服務的系統映像，且將其作為一完整操作系統分發並啟動的技術，又稱 [*自定義映像*](../Advanced/creating_custom_image.md).
-   **[雲端原生(Cloud-Native)](https://aws.amazon.com/what-is/cloud-native/)**: 在雲端設立的自動化編譯、建設和分發工具，這對於基於一個共同系統映像方法多種不同映像版本的 Bazzite 有奇效。
在 Bazzite 中，所有的映像皆於[Github](https://github.com/ublue-os/bazzite/)上編譯、建設和分發。
