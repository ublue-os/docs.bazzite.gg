---
title: "ZeroTier Setup"
authors:
  - "@Zeglius"
tags:
  -  Community
search:
  exclude: true
---

# Nastavení ZeroTier

## Instalace

!!! warning
    Instalace vyžaduje vrstvení balíčků a **nedoporučuje se**.
    
Přidejte úložiště ZeroTier do yum zkopírováním následujícího textu do terminálu (pro vložení zkopírovaného textu do terminálu: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>)

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

Nainstalujte ZeroTier One:

```sh
sudo rpm-ostree install zerotier-one
```

Restartujte systém a poté povolte službu ZeroTier spuštěním tohoto příkazu v terminálu:

```sh
sudo systemctl enable --now zerotier-one
```

## Odinstalování

Vyberte, zkopírujte a vložte následující do terminálu (vložení je <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>V</kbd>)

```sh
sudo systemctl disable zerotier-one.service
sudo rpm-ostree uninstall zerotier-one
```

Restartujte a spusťte toto na terminálu:

```sh
sudo rm -fv /etc/yum.repos.d/zerotier.repo
```

## Opravte, že nevidíte své spoluhráče ve hrách

_(Nastavit směrování přes síťové rozhraní ZeroTier)_

Získejte název svého síťového rozhraní ZeroTier spuštěním: `ifconfig -a` (porovnejte IP adresu s adresou na vašem webovém panelu ZeroTier)

Přidejte trasu: `sudo route add -host 255.255.255.255 dev <interface name>`