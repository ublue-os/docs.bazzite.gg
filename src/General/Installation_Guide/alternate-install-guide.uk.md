---
title: Альтернативний посібник зі встановлення
---

# Альтернативний посібник зі встановлення

!!! warning

    З цим способом встановлювач може некоректно масштабуватися залежно від обладнання, особливо на портативних ПК.

## Перебазування з образу Fedora Atomic Desktop { #rebasing-from-a-fedora-atomic-desktop-image }

Якщо під час встановлення з нашого ISO-образу виникають проблеми або ваш завантажувальний носій замалий для Bazzite, завантажте [Fedora Kinoite (**KDE Plasma**)](https://fedoraproject.org/atomic-desktops/kinoite/) або [Fedora Silverblue (**GNOME**)](https://fedoraproject.org/atomic-desktops/silverblue/), залежно від того, яке робоче середовище вам більше до вподоби.

1. Встановлення схоже на встановлення Bazzite: той самий встановлювач і ті самі кроки, але **не** створюйте обліковий запис root, якщо встановлювач це пропонує.

2. Після встановлення у вас ще не буде Bazzite, доки ви не введете команду з нашого сайту. Вона з'являється в розділі [«**Existing Fedora Atomic Desktop Users**»](https://download.bazzite.gg), коли завантаження готове. Також її можна знайти в [повному списку образів у FAQ](../FAQ.md#bazzite-image-chart-example).

3. Відкрийте термінал і введіть цю команду. Майте на увазі, що цей процес **не показує прогресу** і триває довго.

4. Коли перебазування завершиться, перезавантажтеся. Після перезавантаження Bazzite має бути встановлено, а ваше ім'я користувача і пароль перейдуть з Fedora Atomic Desktop до Bazzite.

5. Також у вас **не буде стандартних Flatpak-застосунків, доки ви не встановите їх командою `ujust`**, наведеною нижче.

## Secure Boot під час перебазування з образів Fedora Atomic Desktop { #secure-boot-instructions-when-rebasing-from-upstream-fedora-atomic-desktop-images }

Перебазування з Fedora Silverblue, Fedora Kinoite тощо на Bazzite.

Якщо ви перебазовуєтеся з образу Fedora Atomic Desktop і використовуєте Secure Boot, дотримуйтеся інструкцій у [**README Bazzite**](https://github.com/ublue-os/bazzite/blob/main/README.md#secure-boot).

## Встановлення попередньо встановлених Flatpak-застосунків { #install-pre-installed-flatpak-applications }

Відкрийте термінал і **введіть цю команду**:

```command
ujust _install-system-flatpaks
```

Виберіть джерело «**Flathub**». Якщо запитають «System» чи «User», виберіть «**System**», бо саме це джерело Bazzite використовує за замовчуванням.

> **Ця команда встановлює:**
>
> - [Flatpak-застосунки для образів з **KDE Plasma**](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/kinoite/usr/share/ublue-os/bazzite/flatpak/install)
> - [Flatpak-застосунки для образів з **GNOME**](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/silverblue/usr/share/ublue-os/bazzite/flatpak/install)

### Видалення джерела Flatpak від Fedora { #remove-fedora-flatpak-remote }

Видаліть джерело Flatpak від Fedora за допомогою застосунку Warehouse. Ваші дані користувача при цьому **не** видаляться.

## Перебазування на підписаний образ { #rebasing-to-a-signed-image }

Коли все налаштовано, з міркувань безпеки варто перебазуватися з **непідписаного образу** на **підписаний**. Для цього **введіть цю команду** в терміналі основної системи:

```command
ujust verify-image
``` 
Після завершення команди перезавантажте пристрій.

## Відеоінструкція { #video-tutorial }

https://www.youtube.com/watch?v=0NKEfVvdiOs
