---
title: Словарь и терминология
---

# Словарь и терминология

## Общие понятия

-   **[[Desktop] Linux](https://www.ubuntudocs.com/bdesktop/)** <small>[Internet Archive Backup](https://web.archive.org/web/20240813064251/https://www.ubuntudocs.com/bdesktop/)</small>: Семейство операционных систем с общими базовыми компонентами, включая [ядро Linux](https://www.kernel.org/), [systemd](https://systemd.io/) и [основные утилиты GNU](https://www.gnu.org/software/coreutils/).
-   **[Desktop Environment](https://en.wikipedia.org/wiki/Desktop_environment)**: Окружение рабочего стола, то есть графический интерфейс (UI) и пользовательский опыт (UX) в режиме рабочего стола и Desktop-образах Bazzite. Также известно как *DE*.
-   **[Fedora Linux](https://fedoraproject.org/)**: Современная операционная система Linux, у которой новый крупный выпуск выходит каждые 6 месяцев.
-   **[Fedora Atomic Desktop](https://fedoraproject.org/atomic-desktops/)**: Экспериментальная версия Fedora Linux, созданная с упором на надежность и воспроизводимость. Два самых популярных варианта известны как [Fedora Silverblue](https://fedoraproject.org/atomic-desktops/silverblue/) и [Fedora Kinoite](https://fedoraproject.org/atomic-desktops/kinoite/). Они названы по используемым окружениям рабочего стола: GNOME и KDE Plasma соответственно.
-   ["**Immutable**"](https://blog.verbum.org/2020/08/22/immutable-%E2%86%92-reprovisionable-anti-hysteresis/): Термин для описания операционных систем Linux, которые не используют традиционную структуру файловой системы, где пользователь с правами root может удалить любой файл. В случае Bazzite [все сложнее](https://docs.fedoraproject.org/en-US/fedora-silverblue/technical-information/#filesystem-layout), и расширенное сообщество Linux часто ошибочно считает систему "immutable". Команда Bazzite **не** описывает Bazzite как "immutable"-операционную систему.
-   [**Open Gaming Collective (OGC)**](https://github.com/OpenGamingCollective): Рабочая группа для организаций и отдельных участников, заинтересованных в совместной работе над изменениями в основных игровых компонентах, которые принесут пользу всем Linux-проектам, ориентированным на игры.

## Образы Bazzite-Deck

-   **[Steam Deck](https://store.steampowered.com/steamdeck)**: Портативный игровой ПК от Valve, который использует собственную операционную систему Valve на базе Linux и [клиента Steam](https://store.steampowered.com/about/download).
-   **[SteamOS](https://www.steamdeck.com/en/software)**: Операционная система Valve на базе Linux, основанная на [Arch Linux](https://archlinux.org/), под управлением которой работает Steam Deck.
-   **[Gamescope](https://github.com/ValveSoftware/gamescope)**: Микрокомпозитор, разработанный для SteamOS. Используется для масштабирования, фильтрации, ограничения частоты кадров и поддержки HDR.
-   **[Steam Gaming Mode](https://github.com/bazzite-org/gamescope-session)**: Сеанс, в котором интерфейс Steam Big Picture Mode запускается внутри Gamescope. Также известен как *Game Mode*.

## Программы

-   **[Proton](https://github.com/ValveSoftware/Proton)**: Игровой слой совместимости, поддерживаемый Valve для запуска Windows-игр через [WINE](https://www.winehq.org/), [DXVK](https://github.com/doitsujin/dxvk), [VKD3D](https://github.com/HansKristian-Work/vkd3d-proton) и другие компоненты.
-   [**Vulkan**](https://www.vulkan.org/): Кроссплатформенный открытый стандарт графического API на основе AMD Mantle, альтернатива DirectX, доступному только в Windows. Большинство приложений в Linux, включая Windows-приложения, запущенные через Proton, используют API Vulkan.
-   [**OpenGL**](https://www.opengl.org/): Устаревший графический API для случаев, когда Vulkan недоступен. На новых видеокартах Intel ARC Graphics нет собственного драйвера OpenGL, поэтому приложения OpenGL переводятся в Vulkan через [Zink Mesa Gallium Driver](https://docs.mesa3d.org/drivers/zink.html).
- **[Flatpak](https://flatpak.org/)**: Универсальный формат приложений для Linux. Источник приложений по умолчанию - [Flathub](https://www.flathub.org).
-   [**Containers**](https://www.redhat.com/en/topics/containers) : Изолированные среды для программ.

## Базовые технологии

-   **[OSTree/libostree](https://ostreedev.github.io/ostree/introduction/)**: Система обновлений, которую использует Bazzite. Она позволяет откатывать предыдущие обновления системы или полностью переходить на другие образы.
-   **[InputPlumber](https://github.com/shadowblip/InputPlumber)**: Открытый демон маршрутизации и управления вводом для Linux. Он может объединять любое количество устройств ввода, например геймпады, мыши и клавиатуры, и преобразовывать их ввод в разные форматы виртуальных устройств.
-   **[OpenGamepadUI](https://github.com/ShadowBlip/OpenGamepadUI)**: Свободный лаунчер игр и оверлей с открытым исходным кодом, рассчитанный на управление с геймпада. В нем реализована система ввода с геймпада, которая позволяет переназначать ввод геймпада на ввод мыши и клавиатуры.
-   **[Universal Blue](https://ublue.it)**: FOSS-коллектив, который специализируется на пользовательских образах Fedora.
-   **[Bootable Container Image](https://docs.fedoraproject.org/en-US/bootc/getting-started/)**: Программы и службы упакованы в контейнер, который работает поверх существующей операционной системы, например Fedora, как способ доставки специализированной операционной системы. Также известен как [*пользовательский образ*](../Advanced/creating_custom_image.md).
-   **[Cloud-Native](https://aws.amazon.com/what-is/cloud-native/)**: Автоматизированная сборка и доставка программ. Дает возможности вроде обновлений по сети, нескольких образов, которые получают одни и те же актуальные обновления, и так далее. В случае Bazzite каждое обновление выполняется в [GitHub](https://github.com/ublue-os/bazzite/).

!!! info

    [**Handheld Daemon (HHD)**](https://github.com/hhd-dev/hhd), который раньше отвечал за поддержку оборудования портативных устройств, работу контроллера, энергопотребление, RGB и другие функции, постепенно выводится из Bazzite начиная с выпуска 44. Вместо него используются OpenGamepadUI и InputPlumber, как подробно описано [здесь](https://universal-blue.discourse.group/t/a-brighter-future-for-bazzite/11575)
