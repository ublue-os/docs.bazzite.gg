---
title: 系统启动时显示详细日志
---

# 系统启动时显示详细日志

## 适用场景

如果你需要在设备启动时确定服务的启动状态，可以配置 Plymouth （在启动时显示图形界面的组件）以默认显示日志。

![Plymouth](../img/plymouth.png)

## 修改 Plymouth 配置

```command
sudo plymouth-set-default-theme details
```

或者手动在`/etc/plymouth/plymouthd.conf`中配置对应内容。

## 重新生成 Initramfs 并重启

```command
sudo rpm-ostree initramfs --enable --reboot
```
