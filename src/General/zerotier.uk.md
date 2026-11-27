---
title: "Налаштування ZeroTier"
authors:
  - "@Zeglius"
  - "@adokitkat"
  - "@Ruvonn"
tags:
  -  Community
search:
  exclude: true
---

# Налаштування ZeroTier

## Встановлення { #installing }

!!! warning
    Для налаштування потрібне накладання пакетів, і це **не рекомендовано**.
    
Додайте репозиторій ZeroTier до yum, скопіювавши в термінал таке (щоб вставити скопійований текст у термінал, натисніть <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>)

```sh
sudo tee >/dev/null /etc/yum.repos.d/zerotier.repo <<'EOF'
[zerotier]
name=ZeroTier, Inc. RPM Release Repository
baseurl=https://download.zerotier.com/redhat/fc/$releasever
enabled=1
gpgcheck=1
gpgkey=https://download.zerotier.com/contact@zerotier.com.gpg
EOF
```

Встановіть ZeroTier One:

```sh
sudo rpm-ostree install zerotier-one
```

Перезавантажте систему, а потім увімкніть службу ZeroTier такою командою в терміналі:

```sh
sudo systemctl enable --now zerotier-one
```

## Видалення { #uninstalling }

Виділіть, скопіюйте й вставте в термінал таке (вставлення — <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>)

```sh
sudo systemctl disable zerotier-one.service
sudo rpm-ostree uninstall zerotier-one
```

Перезавантажте систему й виконайте в терміналі:

```sh
sudo rm -fv /etc/yum.repos.d/zerotier.repo
```

## Як побачити товаришів по команді в іграх, що використовують широкомовну розсилку (наприклад, Warcraft III LAN) { #fix-not-seeing-your-teammates-in-games-relying-on-broadcast-eg-warcraft-iii-lan }

_(Спрямуйте широкомовну розсилку через мережевий інтерфейс ZeroTier)_

Дізнайтеся назву мережевого інтерфейсу ZeroTier командою `ip a` (порівняйте IP-адреси в записах inet/inet6 з тими, що у вебпанелі ZeroTier)

Додайте маршрут: `sudo ip route add 255.255.255.255 dev <INTERFACE_NAME>` (замініть `<INTERFACE_NAME>` назвою, яку ви отримали з `ip a`, найімовірніше на кшталт `ztbto7vntf`)

Зверніть увагу, що ця зміна тимчасова: після перезавантаження системи маршрут доведеться додати знову.

Якщо ви хочете, щоб NetworkManager автоматично створював маршрут, щойно з'являється інтерфейс ZeroTier, виконайте в терміналі:

```sh
sudo tee /etc/NetworkManager/dispatcher.d/99-zerotier-broadcast.sh >/dev/null <<'EOF' && sudo chmod 755 /etc/NetworkManager/dispatcher.d/99-zerotier-broadcast.sh && sudo systemctl restart zerotier-one.service
#!/bin/bash
INTERFACE=$1
ACTION=$2

# Check if the interface starts with "zt" and is coming UP
if [[ "$INTERFACE" =~ ^zt ]] && [ "$ACTION" = "up" ]; then
  ip route replace 255.255.255.255 dev "$INTERFACE"
fi
EOF
```
