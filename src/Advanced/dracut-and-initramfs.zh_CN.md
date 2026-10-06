---
title: 在 Bazzite 中配置 modprobe
---

# 在 Bazzite 中配置 modprobe

## 如果你只是需要为一个模块提供选项，建议使用 `rpm-ostree kargs`
修改 initramfs 和 modprobe 配置会明显拉长所有更新需要的时间，通常可达数分钟。绝大多数情况下，modprobe 相关的修改可以通过内核参数来实现。

作为示范，接下来将以下的 modprobe 选项转换为内核参数：
```
options hid_apple fnmode=2
```
对应的内核参数：
```
hid_apple.fnmode=2
```
使用以下命令使其在每次启动时生效：
```
rpm-ostree kargs --append-if-missing="hid_apple.fnmode=2"
```
因为内核参数不像 initramfs 需要随系统更新重新生成，所以该方法不会影响更新时间。

## 关于内核参数的上游文档

有关该问题的更多信息，请参考[**上游 Fedora CoreOS 的文档**](https://docs.fedoraproject.org/en-US/fedora-coreos/kernel-args/)。
