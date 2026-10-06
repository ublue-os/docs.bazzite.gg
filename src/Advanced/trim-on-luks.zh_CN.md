---
title: 在 LUKS 加密的分区上启用 TRIM
---

# 在 LUKS 加密的分区上启用 TRIM

!!! warning "该指南涉及系统底层的配置，请务必小心。"

用`lsblk`命令确定 LUKS 加密的分区的名称（一般类似于`luks-5641321xc65c6`）。复制该名称并粘贴到以下命令当中：

```bash
sudo cryptsetup refresh --perf-same_cpu_crypt --perf-submit_from_crypt_cpus
       --perf-no_read_workqueue --perf-no_write_workqueue
       --allow-discards --persistent <LUKS-volume-name>
```

!!! example

    ```bash
    sudo cryptsetup refresh --perf-same_cpu_crypt --perf-submit_from_crypt_cpus
        --perf-no_read_workqueue --perf-no_write_workqueue
        --allow-discards --persistent luks-5641321xc65c6
    ```

---

使用以下命令查询目前启用的功能：

```bash
sudo cryptsetup status <LUKS-volume-name>
```

!!! example

    ```bash
    sudo cryptsetup status luks-5641321xc65c6
    ```

---
