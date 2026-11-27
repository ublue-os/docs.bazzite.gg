---
title: Увімкнення TRIM на дисках із шифруванням LUKS
---

# Увімкнення TRIM на дисках із шифруванням LUKS

!!! warning "Дотримуйтеся цього посібника на власний розсуд."

Скористайтеся `lsblk`, щоб знайти назву тому LUKS (наприклад, `luks-5641321xc65c6`). Скопіюйте цю назву й виконайте:

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

Щоб перевірити ввімкнені прапорці, виконайте

```bash
sudo cryptsetup status <LUKS-volume-name>
```

!!! example

    ```bash
    sudo cryptsetup status luks-5641321xc65c6
    ```

---
