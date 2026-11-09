---
title: Словник і терміни
---

# Словник і терміни

## Загальне { #general }

-   **[[Desktop] Linux](https://www.ubuntudocs.com/bdesktop/)** <small>[резервна копія в Internet Archive](https://web.archive.org/web/20240813064251/https://www.ubuntudocs.com/bdesktop/)</small>: сімейство операційних систем, які мають багато спільних базових програм, зокрема [ядро Linux](https://www.kernel.org/), [systemd](https://systemd.io/) і [основні утиліти GNU](https://www.gnu.org/software/coreutils/).
-   **[Робоче середовище](https://uk.wikipedia.org/wiki/Середовище_робочого_столу)** (Desktop Environment): графічний інтерфейс користувача (UI) і досвід користування (UX) режиму робочого столу / настільних образів Bazzite. Також відоме як *DE*.
-   **[Fedora Linux](https://fedoraproject.org/)**: передова операційна система Linux, новий основний випуск якої виходить кожні 6 місяців.
-   **[Fedora Atomic Desktop](https://fedoraproject.org/atomic-desktops/)**: експериментальна версія Fedora Linux, створена, щоб бути надійною і відтворюваною. Два найпопулярніші варіанти — [Fedora Silverblue](https://fedoraproject.org/atomic-desktops/silverblue/) і [Fedora Kinoite](https://fedoraproject.org/atomic-desktops/kinoite/) — названо за робочими середовищами, які вони використовують (GNOME і KDE Plasma відповідно).
-   [«**Immutable**» («незмінна»)](https://blog.verbum.org/2020/08/22/immutable-%E2%86%92-reprovisionable-anti-hysteresis/): термін для операційних систем Linux, які не дотримуються традиційної структури файлової системи, де користувач із правами root може видалити будь-який файл. У випадку Bazzite [усе складніше](https://docs.fedoraproject.org/en-US/fedora-silverblue/technical-information/#filesystem-layout), і ширша спільнота Linux часто помилково вважає його «незмінним». Команда Bazzite **не** називала б Bazzite «незмінною» операційною системою.
-   [**Open Gaming Collective (OGC)**](https://github.com/OpenGamingCollective): робоча група організацій і окремих людей, які хочуть створити спільну основу для змін в ігрових компонентах на рівні першоджерел (upstream), що принесе користь усім проєктам Linux, орієнтованим на ігри.

## Образи Bazzite-Deck { #bazzite-deck-images }

-   **[Steam Deck](https://store.steampowered.com/steamdeck)**: портативний ігровий ПК від Valve, який працює на її власній операційній системі Linux, побудованій навколо [клієнта Steam](https://store.steampowered.com/about/download).
-   **[SteamOS](https://www.steamdeck.com/en/software)**: операційна система Linux від Valve на основі [Arch Linux](https://archlinux.org/), на якій працює Steam Deck.
-   **[Gamescope](https://github.com/ValveSoftware/gamescope)**: мікрокомпозитор, розроблений для SteamOS. Використовується для масштабування, фільтрації, обмеження частоти кадрів і підтримки HDR.
-   **[Ігровий режим Steam](https://github.com/OpenGamingCollective/gamescope-session)** (Steam Gaming Mode): сеанс, який запускає інтерфейс режиму Big Picture у Steam усередині Gamescope. Також відомий як *Game Mode*.

## Програмне забезпечення { #software }

-   **[Proton](https://github.com/ValveSoftware/Proton)**: шар сумісності для ігор, який підтримує Valve, щоб запускати ігри для Windows за допомогою [WINE](https://www.winehq.org/), [DXVK](https://github.com/doitsujin/dxvk), [VKD3D](https://github.com/HansKristian-Work/vkd3d-proton) та інших компонентів.
-   [**Vulkan**](https://www.vulkan.org/): кросплатформний відкритий стандарт графічного API, що походить від Mantle від AMD, як альтернатива DirectX, який є лише у Windows. Більшість застосунків у Linux (зокрема застосунки для Windows, запущені через Proton) використовують API Vulkan.
-   [**OpenGL**](https://www.opengl.org/): застарілий графічний API, який використовують, коли Vulkan недоступний. На нових відеокартах Intel ARC немає власного драйвера OpenGL, і застосунки OpenGL транслюються у Vulkan через [драйвер Zink Mesa Gallium](https://docs.mesa3d.org/drivers/zink.html).
- **[Flatpak](https://flatpak.org/)**: універсальні застосунки для Linux. Джерело за замовчуванням — [Flathub](https://www.flathub.org).
-   [**Контейнери**](https://www.redhat.com/en/topics/containers) : ізольовані середовища для програм.

## Технології в основі { #underlying-technology }

-   **[OSTree/libostree](https://ostreedev.github.io/ostree/introduction/)**: система оновлення, яку використовує Bazzite. Вона дає змогу відкочувати попередні оновлення системи або повністю перебазовуватися на інші образи.
-   **[InputPlumber](https://github.com/shadowblip/InputPlumber)**: відкрита служба маршрутизації і керування введенням для Linux. Вона може об'єднувати будь-яку кількість пристроїв введення (геймпади, миші, клавіатури) і перетворювати їхнє введення на різні формати віртуальних пристроїв.
-   **[OpenGamepadUI](https://github.com/ShadowBlip/OpenGamepadUI)**: вільний і відкритий лаунчер ігор та оверлей, створений для зручного керування геймпадом. Він має систему введення з геймпада, яка дає змогу перепризначати кнопки геймпада на дії миші й клавіатури.
-   **[Universal Blue](https://ublue.it)**: спільнота вільного ПЗ (FOSS), що спеціалізується на власних образах Fedora.
-   **[Завантажувальний образ контейнера](https://docs.fedoraproject.org/en-US/bootc/getting-started/)** (Bootable Container Image): програми й служби, упаковані в контейнер, який працює поверх наявної операційної системи (наприклад, Fedora), як спосіб постачати спеціалізовану операційну систему. Також відомий як [*власний образ*](../Advanced/creating_custom_image.md) (custom image).
-   **[Cloud-Native](https://aws.amazon.com/what-is/cloud-native/)**: автоматизоване збирання і розгортання програм. Дає такі можливості, як оновлення «по повітрю», кілька образів, що отримують ті самі оновлення з першоджерела, тощо. У випадку Bazzite кожне оновлення виконується на [GitHub](https://github.com/ublue-os/bazzite/).

!!! info

    [**Handheld Daemon (HHD)**](https://github.com/hhd-dev/hhd), який раніше відповідав за підтримку обладнання портативних пристроїв, роботу контролерів, енергоспоживання, RGB-підсвічування та інші функції, у випуску Bazzite 44 поступово замінюється на OpenGamepadUI і InputPlumber, як описано [тут](https://universal-blue.discourse.group/t/a-brighter-future-for-bazzite/11575)
