---
title: Встановлення Arctis Manager
authors:
  - "@elegos"
  - "@ifeign"
  - "@rdamron"
tags:
  - Community
search:
  exclude: true
---

# Встановлення Arctis Manager

[![GitHub Release](https://img.shields.io/github/v/release/elegos/Linux-Arctis-Manager?label=Latest%20Release&color=brightgreen&logo=github&logoColor=white)](https://github.com/elegos/Linux-Arctis-Manager/releases)

## Призначення { #purpose }
Цей посібник пояснює, як встановити [**Linux-Arctis-Manager**](https://github.com/elegos/Linux-Arctis-Manager) (v2.0.4+) за допомогою Distrobox. Цей спосіб не потребує накладання пакетів чи тимчасового вимкнення режиму «лише для читання» кореневої файлової системи й водночас дає менеджеру потрібний доступ до обладнання та фонових служб. Список підтримуваних пристроїв і документацію для досвідчених користувачів дивіться в репозиторії за посиланням.

## Встановлення { #installation }

Щоб встановити, виконайте такий скрипт:

```bash
curl -LsSf https://raw.githubusercontent.com/elegos/Linux-Arctis-Manager/refs/heads/develop/scripts/distrobox.sh | sh
```

!!! note

    В операційних системах Linux на кшталт Bazzite (на основі образів, із кореневою файловою системою лише для читання) застосунок поводиться як звичайна встановлена програма, а не як ізольований контейнер. Оскільки Distrobox напряму монтує ваші `/home`, `/var` і `/etc`, менеджер може працювати з потрібними йому системними службами й файлами конфігурації.

!!! tip

    Щоб застосунок у системному лотку запускався автоматично після входу в систему:

    ```bash
    ln -sf ~/.local/share/applications/ArctisManagerSystray.desktop ~/.config/autostart/
    ```

## Видалення й очищення { #uninstall-cleanup }
1. Зупиніть і вимкніть службу:

   ```bash
   systemctl --user disable --now arctis-manager
   rm ~/.config/systemd/user/arctis-manager.service
   ```

2. Видаліть контейнер:
 
   ```bash
   distrobox-rm -f arctis-manager
   ```

3. Видаліть файли, що залишилися в хост-системі:

   ```bash
   # desktop menu entries
   rm -f ~/.local/share/applications/ArctisManager.desktop
   rm -f ~/.local/share/applications/ArctisManagerSystray.desktop
   rm -f ~/.config/autostart/ArctisManagerSystray.desktop

   # udev rules
   sudo rm -f /etc/udev/rules.d/91-steelseries-arctis.rules

   # user preferences and virtual environment
   rm -rf ~/.config/arctis_manager
   rm -rf ~/.local/share/pipx/venvs/linux-arctis-manager
   ```   
