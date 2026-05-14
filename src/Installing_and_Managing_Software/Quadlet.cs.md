---
title: Quadlets (Services)
---

# Quadlet (služby)

![podman|385x358, 50%](../img/podman.png)

## Případy použití kvadletů

Quadlet je funkce [podman](https://podman.io/), která uživateli umožňuje spouštět kontejner jako jednotky [systemd](https://systemd.io/). Funguje pomocí deklarativní syntaxe jako [docker compose](https://docs.docker.com/compose/), ale integruje se do systemd a jako backend používá podman.

Quadlet lze použít pro aplikace zabalené jako kontejner, jako je například serverová aplikace. Můžete najít spoustu příkladů kontejnerizovaných aplikací z [Linux Server](https://docs.linuxserver.io/images/).

## Správa kvadletu

Quadlet lze spravovat jako kteroukoli jinou systemd službu pomocí níže uvedeného příkazu.

**Kontrola stavu kvadletu**
```sh
systemctl --user status <service>
```

**Zastavení kvadletu**
```sh
systemctl --user stop <service>
```

Další příkazy můžete vidět v [man systemctl](https://man.archlinux.org/man/systemctl.1) nebo [tldr systemctl](https://tldr.inbrowser.app/pages/linux/systemctl).

!!! note

    Při interakci se systemctl nepřidávejte příponu `.container`, jinak dojde k chybě.

### Umístění souborů kvadletů

Svůj kvadlet můžete umístit na tato místa seřazená podle priority:

- `$XDG_RUNTIME_DIR/containers/systemd/` - Obvykle se používá pro dočasné kvadlety
- `~/.config/containers/systemd/` - Doporučené umístění
- `/etc/containers/systemd/users/$(UID)`
- `/etc/containers/systemd/users/`

!!! note

    Pokud chcete, aby se vaše služba spustila, i když nejste přihlášeni, spusťte `loginctl enable-linger $USER` a spusťte ji automaticky.

### Spuštění kvadletu při spuštění

Možná budete chtít svůj kvadlet spouštět automaticky při spuštění, stačí do souboru kvadletu přidat instalační sekci, pokud chcete, aby se spouštěl automaticky. Většinu času je `default.target` to, co chcete, ale pokud potřebujete jiný cíl, můžete si o tom přečíst v dokumentaci systemd.

```
[Install]
WantedBy=default.target
```

### Převod Docker Compose na jednotku Quadlet

Zjistíte, že většina kontejnerizovaných aplikací na webu je vytvořena pomocí docker compose. Dokonce i Linux Server, který je propojen výše, má všechny kontejnery zdokumentované pomocí nového souboru. Takže jej budete muset nejprve převést, než jej spustíte jako kvadlet, naštěstí můžete použít [podlet](https://github.com/containers/podlet), který vám pomůže s převodem.

!!! note

    Ve výchozím nastavení vyžaduje kvadlet úplný název úložiště. Většina obrazů je v Docker Hubu, takže k němu přidejte `docker.io/` (např. „nginxinc/nginx-unprivileged“ se změní na „docker.io/nginxinc/nginx-unprivileged“).

### Spuštění Rootful Container jako Quadlet

I když v ideálním případě byste spouštěli všechny kontejnery pomocí rootless podman, bohužel ne všechny kontejnery s ním budou fungovat.  Použijte rootful podman pomocí jiné cesty kvadletu a spusťte pomocí root systemctl (bez `--user`).

Rootful Quadlet Cesty
- `/run/containers/systemd/` - Dočasný kvadlet
- `/etc/containers/systemd/` - Doporučené umístění
- `/usr/share/containers/systemd/` - Definovaný obraz

## Společný popis klíče kvadletu

| Možnost | Příklad | Popis |
| -------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Název kontejneru | Název kontejneru=nginx | Název kontejneru.                                                                   |
| Obraz | Image=docker.io/nginxinc/nginx-unprivileged | Obraz kontejneru, který chcete použít.                                                    |
| Automatická aktualizace | AutoUpdate=registr | Zdroj pro kontrolu aktualizací. Hodnota je buď `registry` nebo `local`.                   |
| PublishPort | PublishPort=8080:8080 | Přístav otevřen kontejnerem. (HOST_PORT:CONTAINER_PORT) |
| Svazek | Volume=/cesta/k/datům:/data:z | Propojte složku hostitele se složkou kontejneru. (HOST_FOLDER:CONTAINER_FOLDER:OPTION) |
| Síť | Síť=hostitel | Síť používaná kontejnerem. Hodnota může být `host`, `none` nebo uživatelsky definovaný název sítě |

!!! note

    Volba `z` ve svazku má zabránit selinuxu v blokování přístupu ke složce. Více si můžete přečíst [zde](https://docs.podman.io/en/stable/markdown/podman-run.1.html#volume-v-source-volume-host-dir-container-dir-options).

## Odstraňování problémů

Pokud váš kvadlet z nějakého důvodu není nalezen nebo se nespouští, můžete kontejnerovou jednotku ladit pomocí `/usr/libexec/podman/quadlet -dryrun` pro systémový kvadlet nebo `/usr/libexec/podman/quadlet -user -dryrun` pro uživatelský kvadlet.


## Příklady

Reálné příklady použití kvadletů.

### Hosting serveru Minecraft

!!! note

    Po vytvoření souboru nezapomeňte spustit `systemctl --user daemon-reload`

Dokumentace: https://docker-minecraft-server.readthedocs.io/en/latest
Soubor kvadletu:
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

    Pro objem použijte absolutní cestu, např. `/home/username/minecraft/data`.

### Webový server NGINX

Vytvořte soubor s názvem `~/.config/containers/systemd/nginx.container` s obsahem níže.
```
[Container]
ContainerName=nginx
Image=docker.io/nginxinc/nginx-unprivileged
AutoUpdate=registry
PublishPort=8080:8080
```

Uložte jej a spusťte níže uvedený kód.

```sh
systemctl --user daemon-reload
systemctl --user start nginx
xdg-open localhost:8080
```

### Plex Media Server

Dokumentace: https://github.com/plexinc/pms-docker
Soubor kvadletu:
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

    Seznam časových pásem naleznete [zde](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
!!! note

    Pro objem použijte absolutní cestu, např. `/home/username/plex/config`.
!!! note

    Pro svá média můžete připojit více svazků, např. `Volume=/path/to/media:/tv:z` a `Volume=/path/to/another/media:/movie:z`. Další informace naleznete v dokumentaci.


#### Video tutoriál
https://www.youtube.com/watch?v=xTVFmvyZGpg

### Server Samba

Dokumentace: https://github.com/ServerContainers/samba
Soubor kvadletu:
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

    Seznam časových pásem naleznete [zde](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
!!! note

    Pro objem použijte absolutní cestu, např. `/home/username/samba/guest`.

## Užitečné odkazy

- https://podman.io/
- https://docs.podman.io/en/stable/markdown/podman-systemd.unit.5.html
- https://www.redhat.com/en/blog/quadlet-podman