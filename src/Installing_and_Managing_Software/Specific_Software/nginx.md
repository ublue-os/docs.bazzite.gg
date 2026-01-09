---
title: NGINX Web Server
---

# Setting Up A NGINX Web Server

## Preface

Use a [Quadlet service](../index.md#quadlet) to host a NGINX web server on Bazzite.

## Setup

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

![nginx welcome page|1296x400](../img/nginx_welcome.png)
<fix this>
