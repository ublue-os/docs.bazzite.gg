---
title: Enabling TRIM on LUKS-Encrypted Drives
---

# Enabling TRIM on LUKS-Encrypted Drives

!!! warning "Follow this guide at your own discretion."

use `lsblk` to find the name of the LUKS volume (e.g.: `luks-5641321xc65c6`). Copy that name and run the following:

```bash
sudo cryptsetup refresh --perf-same_cpu_crypt --perf-submit_from_crypt_cpus \
       --perf-no_read_workqueue --perf-no_write_workqueue \
       --allow-discards --persistent <LUKS-volume-name>
```

!!! example

    ```bash
    sudo cryptsetup refresh --perf-same_cpu_crypt --perf-submit_from_crypt_cpus \
        --perf-no_read_workqueue --perf-no_write_workqueue \
        --allow-discards --persistent luks-5641321xc65c6
    ```

---

to check enabled flags, use

```bash
sudo cryptsetup status <LUKS-volume-name>
```

!!! example

    ```bash
    sudo cryptsetup status luks-5641321xc65c6
    ```

---
