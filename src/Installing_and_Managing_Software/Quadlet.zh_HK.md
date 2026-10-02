---
title: Quadlets (系統服務)
---

# Quadlet (系統服務)

![podman|385x358, 50%](../img/podman.png)

## 為甚麼要用 Quadlet？

Quadlet 是一個由 [podman](https://podman.io/) 提供、將容器以[systemd](https://systemd.io/) 系統服務運行的功能。其 Declarative 語法與 [docker compose](https://docs.docker.com/compose/) 相似，但對於 Systemd 系統集成，且使用 Podman 作為後端。

Quadlet 可以將一個程式作為伺服器服務容器般使用。詳情請閱 [Linux Server 鏡像](https://docs.linuxserver.io/images/)

---

## 管理 Quadlet

Quadlet 可以常用的 Systemd 語法進行管理。

檢索 Quadlet 服務運行詳情：

```bash
systemctl --user status <service>
```

終止 Quadlet 服務：

```bash
systemctl --user stop <service>
```

> 你可以在 [`man systemctl`](https://man.archlinux.org/man/systemctl.1) 或 [tldr systemctl](https://tldr.inbrowser.app/pages/linux/systemctl) 中查看更多 Systemd 語法。

!!! note "溫馨提示"

    不要使用 `.container` 後綴，否則 Systemctl 會報錯。

---

### Quadlet 檔案位置

你可將你的 Quadlet 檔放置在下列位置（優先度由高至低）：

- `$XDG_RUNTIME_DIR/containers/systemd/` - 常用於臨時、測試、一次性的 Quadlet
- `~/.config/containers/systemd/` - 推薦位置
- `/etc/containers/systemd/users/$(UID)`
- `/etc/containers/systemd/users/`

!!! note "溫馨提示"

    如你欲將服務設為無視用戶登入狀態地自啟動，你可以使用 `loginctl enable-linger $USER` 指令。

---

### 自啟動 Quadlet

如你欲將 Quadlet 服務設為自啟動，你可以於 Quadlet 設定檔中添加 `[Install]` 段落。在大部分情況下，你可以使用 `default.target`。如需使用其他自啟動的 `target`，請參閱 [systemd Arch維基](https://wiki.archlinux.org/title/Systemd)。

!!! example "例子"

    ```
    [Install]
    WantedBy=default.target
    ```

---

### 由 Docker Compose 轉換至 Quadlet Unit

大部分容器化的軟件皆使用 Docker Compose。在這些情況下，你可以使用 [podlet](https://github.com/containers/podlet) 將其轉譯至 Quadlet 檔。

!!! note "溫馨提示"

    Quadlet 預設使用 Full Repository Name。大部分的容器鏡像皆使用 Docker Hub ，因此你可在鏡像名稱前添加 `docker.io/` 以獲得 Full Repository Name。（如 `nginxinc/nginx-unprivileged` 變為 `docker.io/nginxinc/nginx-unprivileged`）

---

### 使用 Quadlet 運行有 Root 權限的容器

!!! info "理論上，容器應無需使用 Root 權限。"

將啟動及安裝指令中移除 `--user` 及將 Quadlet 設定檔移動至以下位置即可給予 Quadlet Root 權限。

可供使用的 Quadlet 設定檔位置

- `/run/containers/systemd/` - 臨時位置，重啟後將被移除
- `/etc/containers/systemd/` - **建議位置**
- `/usr/share/containers/systemd/` - 鏡像內建（不可用）

## 常用 Quadlet 設定檔語法

| Option        | Example                                     | Description                                                                              |
| ------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------- |
| ContainerName | ContainerName=nginx                         | Name of the container.                                                                   |
| Image         | Image=docker.io/nginxinc/nginx-unprivileged | Container image that you want to use.                                                    |
| AutoUpdate    | AutoUpdate=registry                         | Source to check for update. The value is either `registry` or `local`.                   |
| PublishPort   | PublishPort=8080:8080                       | Port opened by container. (HOST_PORT:CONTAINER_PORT)                                     |
| Volume        | Volume=/path/to/data:/data:z                | Link host folder with container folder. (HOST_FOLDER:CONTAINER_FOLDER:OPTION)            |
| Network       | Network=host                                | Network used by container. The value can be `host`, `none`, or user defined network name |

!!! note "溫馨提示"

    The `z` option in volume is to prevent selinux from blocking access to the folder. You can read more [here](https://docs.podman.io/en/stable/markdown/podman-run.1.html#volume-v-source-volume-host-dir-container-dir-options).

## 疑難排解

如你的 Quadlet 無法正常啟動，你可使用 `/usr/libexec/podman/quadlet -dryrun` (Root 權限) 或 `/usr/libexec/podman/quadlet -user -dryrun` （無 Root 權限）。

此外，你亦可在 `systemctl` 指令中添加 `--verbose` 以顯示日誌輸出。

---

## 範例

!!! example "以下為一些常用的 Quadlet 設定檔範例"

    ### Minecraft Server Hosting

    !!! note

        Don't forget to run `systemctl --user daemon-reload` after creating the file

    Documentation: https://docker-minecraft-server.readthedocs.io/en/latest
    Quadlet File:
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

        Use absolute path for volume, e.g `/home/username/minecraft/data`.

    ---

    ### NGINX Web Server

    Create a file called `~/.config/containers/systemd/nginx.container` with content below.
    ```
    [Container]
    ContainerName=nginx
    Image=docker.io/nginxinc/nginx-unprivileged
    AutoUpdate=registry
    PublishPort=8080:8080
    ```

    Save it and run the code below.

    ```sh
    systemctl --user daemon-reload
    systemctl --user start nginx
    xdg-open localhost:8080
    ```

    ---

    ### Plex Media Server

    Documentation: https://github.com/plexinc/pms-docker
    Quadlet File:
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

        You can find list of timezones [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    !!! note

        Use absolute path for volume, e.g `/home/username/plex/config`.
    !!! note

        You can mount multiple volumes for your media, e.g `Volume=/path/to/media:/tv:z` and `Volume=/path/to/another/media:/movie:z`. Consult the documentation for more info.


    #### Video Tutorial
    https://www.youtube.com/watch?v=xTVFmvyZGpg
    
    ---

    ### Samba Server

    Documentation: https://github.com/ServerContainers/samba
    Quadlet File:
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

        You can find list of timezone [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    !!! note

        Use absolute path for volume, e.g `/home/username/samba/guest`.

---

## 常用連結

- https://podman.io/
- https://docs.podman.io/en/stable/markdown/podman-systemd.unit.5.html
- https://www.redhat.com/en/blog/quadlet-podman

---
