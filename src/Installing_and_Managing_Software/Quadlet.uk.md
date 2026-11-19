---
title: Quadlet (служби)
---

# Quadlet (служби)

![podman|385x358, 50%](../img/podman.png)

## Для чого потрібен Quadlet { #quadlet-usecases }

Quadlet — функція [podman](https://podman.io/), яка дає змогу запускати контейнер як модулі [systemd](https://systemd.io/). Він використовує декларативний синтаксис, схожий на [docker compose](https://docs.docker.com/compose/), але інтегрується із systemd і працює на основі podman.

Quadlet можна використовувати для застосунків, упакованих у контейнер, наприклад серверних. Багато прикладів застосунків у контейнерах можна знайти на [Linux Server](https://docs.linuxserver.io/images/).

## Керування Quadlet { #managing-quadlet }

Quadlet можна керувати як будь-якою іншою службою systemd за допомогою команд нижче.

**Перевірка стану Quadlet**
```sh
systemctl --user status <service>
```

**Зупинення Quadlet**
```sh
systemctl --user stop <service>
```

Більше команд — у [man systemctl](https://man.archlinux.org/man/systemctl.1) або [tldr systemctl](https://tldr.inbrowser.app/pages/linux/systemctl).

!!! note

    Не додавайте суфікс `.container`, коли працюєте із systemctl, інакше виникне помилка.

### Де зберігати файли Quadlet { #quadlet-file-locations }

Файли Quadlet можна розміщувати в таких теках (від найвищого пріоритету до найнижчого):

- `$XDG_RUNTIME_DIR/containers/systemd/` — зазвичай для тимчасових Quadlet
- `~/.config/containers/systemd/` — рекомендоване розташування
- `/etc/containers/systemd/users/$(UID)`
- `/etc/containers/systemd/users/`

!!! note

    Якщо служба має запускатися навіть тоді, коли ви не ввійшли в систему, виконайте `loginctl enable-linger $USER`, щоб вона запускалася автоматично.

### Запуск Quadlet під час завантаження системи { #running-quadlet-on-startup }

Щоб Quadlet запускався автоматично під час завантаження системи, просто додайте до файлу Quadlet розділ Install. Здебільшого вам потрібен `default.target`, але якщо потрібна інша ціль, про неї можна прочитати в документації systemd.

```
[Install]
WantedBy=default.target
```

### Перетворення Docker Compose на модуль Quadlet { #converting-docker-compose-to-quadlet-unit }

Більшість застосунків у контейнерах в інтернеті описано через docker compose. Навіть на згаданому вище Linux Server усі контейнери описано файлами compose. Тож перш ніж запускати застосунок як Quadlet, його треба перетворити. На щастя, у цьому допоможе [podlet](https://github.com/containers/podlet).

!!! note

    За замовчуванням Quadlet потребує повної назви репозиторію. Більшість образів розміщено на Docker Hub, тож додайте до назви `docker.io/` (наприклад, «nginxinc/nginx-unprivileged» стає «docker.io/nginxinc/nginx-unprivileged»).

### Запуск контейнера з правами root як Quadlet { #running-rootful-container-as-quadlet }

В ідеалі всі контейнери варто запускати через podman без прав root, але, на жаль, не всі контейнери так працюють. Щоб використовувати podman із правами root, розмістіть Quadlet в іншій теці й запускайте його через systemctl від root (без `--user`).

Теки для Quadlet із правами root
- `/run/containers/systemd/` — тимчасові Quadlet
- `/etc/containers/systemd/` — рекомендоване розташування
- `/usr/share/containers/systemd/` — визначені образом

## Опис основних ключів Quadlet { #common-quadlet-key-description }

| Параметр        | Приклад                                     | Опис                                                                              |
| ------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------- |
| ContainerName | ContainerName=nginx                         | Назва контейнера.                                                                   |
| Image         | Image=docker.io/nginxinc/nginx-unprivileged | Образ контейнера, який ви хочете використовувати.                                                    |
| AutoUpdate    | AutoUpdate=registry                         | Джерело для перевірки оновлень. Значення — `registry` або `local`.                   |
| PublishPort   | PublishPort=8080:8080                       | Порт, який відкриває контейнер. (ПОРТ_ХОСТА:ПОРТ_КОНТЕЙНЕРА)                                     |
| Volume        | Volume=/path/to/data:/data:z                | Зв'язує теку хоста з текою контейнера. (ТЕКА_ХОСТА:ТЕКА_КОНТЕЙНЕРА:ПАРАМЕТР)            |
| Network       | Network=host                                | Мережа, яку використовує контейнер. Значення — `host`, `none` або назва мережі, створеної користувачем |

!!! note

    Параметр `z` у Volume потрібен, щоб SELinux не блокував доступ до теки. Докладніше [тут](https://docs.podman.io/en/stable/markdown/podman-run.1.html#volume-v-source-volume-host-dir-container-dir-options).

## Вирішення проблем { #troubleshooting }

Якщо ваш Quadlet чомусь не вдається знайти або він не запускається, перевірте модуль контейнера командою `/usr/libexec/podman/quadlet -dryrun` для системних Quadlet або `/usr/libexec/podman/quadlet -user -dryrun` для Quadlet користувача.

Щоб одразу бачити журнал під час запуску Quadlet, додайте прапорець `--verbose`, наприклад: `systemctl --user start --verbose myapp.service`

## Приклади { #examples }

Приклади використання Quadlet із практики.

### Сервер Minecraft { #minecraft-server-hosting }

!!! note

    Не забудьте після створення файлу виконати `systemctl --user daemon-reload`

Документація: https://docker-minecraft-server.readthedocs.io/en/latest
Файл Quadlet:
```
# ~/.config/containers/systemd/minecraft.container
[Container]
ContainerName=minecraft
Environment=EULA=TRUE
Image=docker.io/itzg/minecraft-server
AutoUpdate=registry
PublishPort=25565:25565
Volume=/path/to/data:/data:z

# Remove if you don't want autostart
[Install]
WantedBy=default.target
```
!!! note

    Для Volume вказуйте абсолютний шлях, наприклад `/home/username/minecraft/data`.

### Вебсервер NGINX { #nginx-web-server }

Створіть файл `~/.config/containers/systemd/nginx.container` з таким вмістом.
```
[Container]
ContainerName=nginx
Image=docker.io/nginxinc/nginx-unprivileged
AutoUpdate=registry
PublishPort=8080:8080
```

Збережіть його й виконайте команди нижче.

```sh
systemctl --user daemon-reload
systemctl --user start nginx
xdg-open localhost:8080
```

### Медіасервер Plex { #plex-media-server }

Документація: https://github.com/plexinc/pms-docker
Файл Quadlet:
```
# ~/.config/containers/systemd/plex.container
[Container]
ContainerName=plex
Environment=TZ=Your/TimeZone
Image=docker.io/plexinc/pms-docker
AutoUpdate=registry
Network=host
Volume=/path/to/config:/config:z
Volume=/path/to/transcode:/transcode:z
Volume=/path/to/media:/data:z

# Remove if you don't want autostart
[Install]
WantedBy=default.target
```
!!! note

    Список часових поясів можна знайти [тут](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
!!! note

    Для Volume вказуйте абсолютний шлях, наприклад `/home/username/plex/config`.
!!! note

    Можна підключити кілька томів для медіафайлів, наприклад `Volume=/path/to/media:/tv:z` і `Volume=/path/to/another/media:/movie:z`. Докладніше — у документації.


#### Відеоінструкція { #video-tutorial }
https://www.youtube.com/watch?v=xTVFmvyZGpg

### Сервер Samba { #samba-server }

Документація: https://github.com/ServerContainers/samba
Файл Quadlet:
```
# /etc/containers/systemd/samba.container
[Container]
Environment=ACCOUNT_username=password
# Protected share with write access
Environment="SAMBA_VOLUME_CONFIG_protected=[My Share]; path=/shares/protected; valid users = username; guest ok = no; read only = no; browseable = yes"
# Open share with readonly access
Environment="SAMBA_VOLUME_CONFIG_guest=[Guest Share]; path=/shares/guest; guest ok = yes; browseable = yes"
Image=ghcr.io/servercontainers/samba:smbd-only-latest
AutoUpdate=registry
Network=host
Volume=/path/to/protected:/shares/protected:z
Volume=/path/to/guest:/shares/guest:z

# Remove if you don't want autostart
[Install]
WantedBy=default.target
```
!!! note

    Список часових поясів можна знайти [тут](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
!!! note

    Для Volume вказуйте абсолютний шлях, наприклад `/home/username/samba/guest`.

## Корисні посилання { #useful-links }

- https://podman.io/
- https://docs.podman.io/en/stable/markdown/podman-systemd.unit.5.html
- https://www.redhat.com/en/blog/quadlet-podman
