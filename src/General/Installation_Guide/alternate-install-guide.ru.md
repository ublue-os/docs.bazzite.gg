---
title: Альтернативное руководство по установке
---

# Альтернативное руководство по установке

!!! warning

    При этом способе на некоторых устройствах у установщика могут возникать проблемы с масштабом интерфейса, особенно на портативных ПК.

## Переход на другой образ с Fedora Atomic Desktop

Если у вас возникают проблемы с установкой нашего ISO или загрузочный носитель слишком мал для Bazzite, скачайте [Fedora Kinoite (**KDE Plasma**)](https://fedoraproject.org/atomic-desktops/kinoite/) или [Fedora Silverblue (**GNOME**)](https://fedoraproject.org/atomic-desktops/silverblue/) в зависимости от того, какое окружение рабочего стола вам нужно.

1. Процесс установки похож на Bazzite и использует тот же установщик с теми же инструкциями, но **не** настраивайте учетную запись root, если установщик предлагает такой вариант.

2. После установки это еще не будет Bazzite. Чтобы перейти на Bazzite, введите команду с нашего сайта: она появится в разделе ["**Existing Fedora Atomic Desktop Users**"](https://download.bazzite.gg), когда загрузка будет готова. Также можно свериться с [полным списком образов в FAQ](/General/FAQ/#bazzite-image-chart-example).

3. Откройте терминал и введите эту команду. Учтите, что у процесса **нет индикатора выполнения** и он займет много времени.

4. Перезагрузитесь, когда переход на другой образ завершится. После перезагрузки Bazzite должна быть установлена, а ваше имя пользователя и пароль пользователя перенесутся из основной Fedora Atomic Desktop в Bazzite.

5. Также у вас **не будет стандартных приложений Flatpak, пока вы не установите их командой `ujust`** ниже.

## Инструкции для Secure Boot при переходе с базовых образов Fedora Atomic Desktop

Переход с Fedora Silverblue, Fedora Kinoite и других подобных систем на Bazzite.

Если вы переходите на другой образ с Fedora Atomic Desktop и используете Secure Boot, следуйте инструкциям из [**README Bazzite**](https://github.com/ublue-os/bazzite/blob/main/README.md#secure-boot).

## Установка предустановленных приложений Flatpak

Откройте терминал и **введите эту команду**:

```command
ujust _install-system-flatpaks
```

Выберите удаленный репозиторий "**Flathub**". Если появится выбор между "System" и "User", выберите "**System**", потому что это удаленный репозиторий по умолчанию в Bazzite.

> **Эта команда устанавливает:**
>
> - [приложения Flatpak для образов **KDE Plasma**](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/kinoite/usr/share/ublue-os/bazzite/flatpak/install)
> - [приложения Flatpak для образов **GNOME**](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/silverblue/usr/share/ublue-os/bazzite/flatpak/install)

### Удаление репозитория Fedora Flatpak

Удалите репозиторий Fedora Flatpak через приложение Warehouse. Это **не** удалит пользовательские данные.

## Переход на подписанный образ

Когда все будет настроено правильно, из соображений безопасности перейдите с **неподписанного образа** на **подписанный образ**. Для этого **введите эту команду** в терминале основной системы:

```command
ujust verify-image
```
После завершения команды перезагрузите устройство.

## Видеоинструкция

https://www.youtube.com/watch?v=0NKEfVvdiOs
