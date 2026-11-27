---
title: Quadlet（系统服务）
---

# Quadlet（系统服务）

![podman|385x358, 50%](../img/podman.png)

## Quadlet 使用场景

Quadlet 是 [Podman](https://podman.io/) 提供的一个功能，允许用 [systemd](https://systemd.io/) 控制一个容器随系统启动并统一管理，其用法和 [Docker Compose](https://docs.docker.com/compose/) 相近，但和 systemd 集成程度更高，且对应 Podman 的后端而非 Docker。

Quadlet 最适合的场景是长期运行的服务包装成的容器。一些例子可以参考 [Linux Server](https://docs.linuxserver.io/images/)。

## Quadlet 配置

Quadlet 的配置方式和普通的 systemd 服务基本一致。

**查询 Quadlet 状态**
```sh
systemctl --user status <service>
```

**停止 Quadlet 容器**
```sh
systemctl --user stop <service>
```

[man systemctl](https://man.archlinux.org/man/systemctl.1) 和 [tldr systemctl](https://tldr.inbrowser.app/pages/linux/systemctl) 可以提供更多信息。

!!! note

    在`systemctl`指令中不要使用`.container`的后缀名，否则命令会出错。

### Quadlet 文件位置

以下目录都可以用来保存 Quadlet 文件。优先级从高到低：

- `$XDG_RUNTIME_DIR/containers/systemd/` - 一般用于临时文件
- `~/.config/containers/systemd/` - 通常推荐的位置
- `/etc/containers/systemd/users/$(UID)`
- `/etc/containers/systemd/users/`

!!! note

    如果你需要 Quadlet 在你没有登录用户时也能运行，则需要使用`loginctl enable-linger $USER`命令。

### 配置 Quadlet 在开机时运行

如果需要 Quadlet 在开机时运行，则需要在定义文件里增加`[Install]`部分。`default.target`适用于绝大多数情况，但 systemd 文档中也解释了其他的 target 及其对应用途。

```
[Install]
WantedBy=default.target
```

### 将 Docker Compose 文件转换成 Quadlet

目前 Docker Compose 的定义文件相对于 Quadlet 仍然更加常见，包括先前提到的 Linux Server 目前提供的也是 Compose 文件。如果需要转换，可以使用 [podlet](https://github.com/containers/podlet) 这一工具。

!!! note

    Quadlet 一般要求镜像名称提供完整路径。对于 Docker Hub，只需要在开头加上`docker.io/`（比如`nginxinc/nginx-unprivileged`改成`docker.io/nginxinc/nginx-unprivileged`）。

### 系统级运行 Quadlet（rootful）

虽然 Podman 一般常用于用户级的容器运行（rootless），但有些情况下也有需要在系统层面上运行的容器。这种情况下，需要`systemctl`控制全局配置（即不使用`--user`参数），且 Quadlet 的文件路径需要改变：

Rootful Quadlet 的文件路径
- `/run/containers/systemd/` - 临时文件
- `/etc/containers/systemd/` - 推荐位置
- `/usr/share/containers/systemd/` - 发行版预定义

## Quadlet 常用设置项

| 项目           | 示例                                        | 解释                                                                              |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------- |
| ContainerName | ContainerName=nginx                         | 容器名称。 |
| Image         | Image=docker.io/nginxinc/nginx-unprivileged | 容器对应镜像的路径。 |
| AutoUpdate    | AutoUpdate=registry                         | 检查更新的来源。一般是`registry`（从镜像来源查询）或`local`（只考虑本地保存的版本）。 |
| PublishPort   | PublishPort=8080:8080                       | 容器对外共享的端口，格式为`主机侧端口号:容器侧端口号`。 |
| Volume        | Volume=/path/to/data:/data:z                | 将主机上的目录绑定挂载到容器内，格式为`主机路径:容器内路径:挂载选项`。 |
| Network       | Network=host                                | 容器使用的虚拟网络。可以是`host`、`none`或提前定义并配置的网络名称。 |

!!! note

    `Volume`项下的`z`选项可以防止 SELinux 在一些配置下阻止容器访问绑定的目录。更多信息请参考 [Podman 的文档](https://docs.podman.io/en/stable/markdown/podman-run.1.html#volume-v-source-volume-host-dir-container-dir-options)。

## 故障排除

如果你的 Quadlet 文件无法启动容器，可以使用`/usr/libexec/podman/quadlet -dryrun`（rootful）或`/usr/libexec/podman/quadlet -user -dryrun`（rootless）命令进行文件语法的排查。

另外，抓取容器启动时的输出有时也会很有用。在启动命令中添加`--verbose`即可，比如`systemctl --user start --verbose myapp.service`。

## 示例

一些 Bazzite 用户常用的 Quadlet 场景。

### Minecraft 多人服务器

!!! note

    创建或更改 Quadlet 文件之后，应该运行`systemctl --user daemon-reload`以进行刷新。

文档：https://docker-minecraft-server.readthedocs.io/en/latest
Quadlet 文件：
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

    绑定文件夹的主机路径应为绝对路径，例如`/home/username/minecraft/data`。

### NGINX 网络服务

创建文件`~/.config/containers/systemd/nginx.container`并输入以下内容：
```
[Container]
ContainerName=nginx
Image=docker.io/nginxinc/nginx-unprivileged
AutoUpdate=registry
PublishPort=8080:8080
```

保存之后使用以下命令启动服务并打开浏览器访问：

```sh
systemctl --user daemon-reload
systemctl --user start nginx
xdg-open localhost:8080
```

### Plex 媒体服务器

文档：https://github.com/plexinc/pms-docker
Quadlet 文件：
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

    [此处](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)有时区名称的更多信息。
!!! note

    绑定文件夹的主机路径应为绝对路径，例如`/home/username/plex/config`。
!!! note

    如有需要可以绑定多个目录提供媒体文件，比如`Volume=/path/to/media:/tv:z`之后再定义`Volume=/path/to/another/media:/movie:z`。具体配置请参考官方文档。


#### 视频指南
https://www.youtube.com/watch?v=xTVFmvyZGpg

### Samba 服务器

文档：https://github.com/ServerContainers/samba
Quadlet 文件：
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

    [此处](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)有时区名称的更多信息。
!!! note

    绑定文件夹的主机路径应为绝对路径，例如`/home/username/samba/guest`。

## 其他资源

- https://podman.io/
- https://docs.podman.io/en/stable/markdown/podman-systemd.unit.5.html
- https://www.redhat.com/en/blog/quadlet-podman
