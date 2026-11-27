---
title: Looking Glass
---

# Встановлення Looking Glass

## СПЕРШУ ПРОЧИТАЙТЕ! { #read-first }
[Looking-Glass](https://looking-glass.io/) — дуже експериментальний проєкт, і він ще не готовий до повноцінного використання!
Тому офіційних пакетів `looking-glass-client` поки немає. <br>
З цієї причини ми не пакуємо й не постачаємо `looking-glass-client`, а лише надаємо робочу конфігурацію й правила SELinux, щоб ним можна було користуватися в Bazzite.
Проте модуль ядра `kvmfr` ми пакуємо й постачаємо в образі системи, тож про будь-які проблеми з модулем `kvmfr` у Bazzite повідомляйте в нашому Discord або на GitHub і обов'язково згадайте @HikariKnight.

Звернутися безпосередньо до Looking-Glass ми порадимо лише тоді, коли проблема не пов'язана з пакуванням і налаштуванням модуля `kvmfr`.

## Увімкнення модуля KVMFR { #enabling-the-kvmfr-module }
Увімкнути модуль kvmfr можна такою командою:

```bash
ujust setup-virtualization kvmfr
```

## Збирання клієнта Looking-Glass { #compiling-looking-glass-client }
Створіть distrobox `fedora:latest`, у якому будемо збирати програму. Скористайтеся командою нижче, а коли вас запитають, який образ використати, виберіть образ за замовчуванням: я перевірив, що з ним цей посібник працює.
Цей distrobox треба створити вручну без прапорця `--nvidia`, який наш ujust додає автоматично для апаратного прискорення: а тут він нам якраз не потрібен: без нього пакет `cmake-data` встановиться успішно.

!!! note

    Якщо у вас не найновіша версія Fedora, замініть `latest` на номер своєї версії, щоб уникнути проблем із версіями залежностей.

```bash
distrobox create -i "fedora:latest" -n "tmp-lookingglass"
```
Якщо ви хочете використовувати для цього окрему домашню теку, створіть теку, яка стане домашньою текою цього контейнера, і виконайте натомість таку команду:
```bash
distrobox create -i "fedora:latest" -n "tmp-lookingglass" -H "/path/to/new/home"
```
Увійдіть у контейнер командою `distrobox enter tmp-lookingglass`

Дотримуйтеся [документації першоджерела](https://looking-glass.io/docs/rc/build/#installing-build-dependencies). Залежності для збирання у Fedora можна знайти [тут](https://looking-glass.io/wiki/Installation_on_other_distributions), також варто встановити залежності, зазначені для **користувачів PipeWire**.
Оскільки ми збиратимемо для **Wayland**, а не X11, вам також знадобиться пакет `libdecor-devel`

Коли дійдете до запуску `cmake`, скористайтеся командою:
```
cmake -DENABLE_WAYLAND=1 -DENABLE_X11=0 -DENABLE_PULSEAUDIO=0 -DENABLE_PIPEWIRE=1 ..
```
Ця команда вимкне підтримку X11 і PulseAudio, але ввімкне PipeWire і Wayland. Так ви уникнете проблем, бо Bazzite не постачає залежностей X11 для `looking-glass`.

Скопіюйте зібраний файл `looking-glass-client` у `/run/host/home/$USER/.local/bin/`
Якщо ви дотримувалися документації looking-glass, це можна зробити такими командами.
```bash
mkdir /run/host/home/$USER/.local/bin
cp ./looking-glass-client /run/host/home/$USER/.local/bin/
```
Перевірте, чи працює `looking-glass-client` у хост-системі із запущеною віртуальною машиною.

Вийдіть із контейнера й виконайте команду нижче, щоб видалити контейнер, у якому ми збирали клієнт Looking-Glass.
```bash
distrobox stop tmp-lookingglass ; distrobox rm tmp-lookingglass
```
