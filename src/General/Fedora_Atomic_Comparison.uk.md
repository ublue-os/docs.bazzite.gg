---
title: Порівняння Bazzite і Fedora Atomic Desktop
---

# Порівняння Bazzite і Fedora Atomic Desktop з першоджерела

## Що таке Bazzite? { #what-is-bazzite }

Bazzite — власний образ [**Fedora Kinoite (образи з KDE Plasma)**](https://fedoraproject.org/atomic-desktops/kinoite/) або [**Fedora Silverblue (образи з GNOME)**](https://fedoraproject.org/atomic-desktops/silverblue/), які входять до [**сімейства Fedora Atomic Desktop**](https://fedoraproject.org/atomic-desktops/). Його змінено так, щоб він був зручним одразу після встановлення, з акцентом на іграх на ПК.

## Основні відмінності { #key-differences }

Нижче наведено можливості Bazzite, якими він відрізняється від операційних систем Fedora Atomic Desktop з першоджерела:

### Менше налаштувань після встановлення { #less-post-installation-setup }

- Краща підтримка обладнання одразу після встановлення, від компонентів ПК до периферійних пристроїв.
- Мультимедійні кодеки з повною підтримкою апаратного кодування й декодування відео одразу після встановлення.
- Попередньо встановлене програмне забезпечення для ігор, як-от Steam і Lutris.
- Джерело Flatpak від Fedora видалено на користь системного джерела [**Flathub**](https://flathub.org/), щоб за замовчуванням було доступно більше застосунків.

### Простота використання { #ease-of-use }

- Часто використовувані інструменти й ярлики, які супровідники та учасники проєкту зібрали у зручному інтерфейсі [Bazzite Portal](../Installing_and_Managing_Software/Bazzite_Portal.md) і скриптах [**`ujust`**](../Installing_and_Managing_Software/ujust.md).
- Ігровий режим Steam налаштовано одразу, і він запускається автоматично на [**образах Bazzite-Deck**](../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md), призначених для портативних пристроїв і гри з дивана.

### Створено з думкою про розробників { #made-with-developers-in-mind }

- Homebrew — основний менеджер пакетів для інструментів командного рядка.
- Контейнери Distrobox дають доступ до менеджерів пакетів інших дистрибутивів Linux для окремих застосунків або середовищ розробки.
- [**Варіант Bazzite-DX**](https://dev.bazzite.gg/) — фактично основний образ Bazzite для розробки програмного забезпечення.

### Додаткові переваги { #extra-enhancements }

- Підтримка Android-застосунків через [**Waydroid**](../Installing_and_Managing_Software/Waydroid_Setup_Guide.md).
- Firefox більше не входить до образу, замість нього використовується версія з Flatpak.
  - Тепер Firefox можна видалити, бо він не є частиною образу
  - Також він може швидше отримувати оновлення, бо не залежить від оновлень системи.
- Додаткові диски у форматі BTRFS або Ext4 монтуються автоматично.
- Зміни в робочих середовищах, зокрема попередньо встановлені розширення GNOME і теми KDE Plasma.
- Відкат до старіших збірок Bazzite за останні 90 днів.
