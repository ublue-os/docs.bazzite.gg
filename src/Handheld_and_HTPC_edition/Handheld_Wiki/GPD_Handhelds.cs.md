---
title: GPD Handhelds
---

# Handheldy GPD

!!! disclaimer

    Tato wiki může obsahovat zastaralé informace.

## GPD Win 4

![gpdwin4|690x328, 100%](../../img/gpdwin4.jpeg)


### Obecné informace a volitelné vylepšení

- Upravte RGB pomocí režimu Steam Gaming v Handheld Daemon
- Upravte měřítko uživatelského rozhraní v Nastavení zobrazení
- Nastavte limit nabíjení v HHD pomocí Handheld Daemon
- Zařízení GPD mají také fyzický přepínač, který můžete přepnout, abyste povolili samostatný režim plochy/myši.

### Známé problémy

- Suspend-resume plně funguje na 6800u Win 4 po deaktivaci skeneru otisků prstů, ale existuje několik uživatelských zpráv o 7840u a novějších modelech, které mají pouze částečně funkční pozastavení-obnovení.
  - Zdá se, že je to velmi podobné/souvisí s problémem pozastavení na GPD WM2 7840u a novějších zařízeních, více podrobností [zde](https://gitlab.freedesktop.org/drm/amd/-/issues/3154)
- Hry mohou někdy výchozí rozlišení 800p.
  - Ručně změňte rozlišení pro každou hru v `Steam Settings > Properties > Game Resolution` na `Native` nebo jiné vyšší rozlišení.
- Tlačítka Zpět může být nutné ručně přemapovat, než budou použitelná.
  - Ručně přemapujte tlačítka zpět, jak je popsáno v hhd docs [zde](https://github.com/hhd-dev/hhd?tab=readme-ov-file#extra-steps-gpd-win-devices)
    – Pokud potřebujete vizuálního průvodce, podívejte se na toto [video](https://www.youtube.com/watch?v=lnNfMY9kzjk).

### Externí zdroj

Další informace najdete v [GPD Win Tips and Tricks guide](https://github.com/aarron-lee/gpd-win-tricks), který obsahuje užitečné skripty pro tento handheld.

## GPD Win Max 2

![placeholder_gpdwinmax2|407x312, 100%](../../img/GPD_Win_Max_2.png)


### Volitelné vylepšení
- Nastavení režimu Steam Gaming **Zobrazení**, která se doporučuje změnit:
  - `Use Native Color Temperature` - Povoleno
- Zařízení GPD mají také fyzický přepínač, který můžete přepnout, abyste povolili samostatný režim plochy/myši
- Upravte RGB pomocí režimu Steam Gaming v Handheld Daemon
- Upravte měřítko uživatelského rozhraní v Nastavení zobrazení
- Nastavte limit nabíjení v HHD pomocí Handheld Daemon

### Známé problémy

- Suspend-resume funguje na modelu WM2 6800u po vypnutí skeneru otisků prstů, ale 7840u a novější modely mají pouze částečně funkční pozastavení-obnovení.
  - Přečtěte si o problému [zde](https://gitlab.freedesktop.org/drm/amd/-/issues/3154), kde najdete podrobnosti o problémech s pozastavením a obnovením u novějších zařízení WM2.
- Pokud nainstalujete svůj operační systém na m2 2230 SSD do slotu pro sekundární disk, může to způsobit problémy s pozastavením.
  - OS byste měli nainstalovat pouze na primární interní SSD.
- Hry mohou někdy výchozí rozlišení 800p
  - Ručně změňte rozlišení pro každou hru v `Steam Settings > Properties > Game Resolution` na `Native` nebo jiné vyšší rozlišení.
- Gyro je nefunkční.
- Tlačítka Zpět může být nutné ručně přemapovat, než budou použitelná.
  - Ručně přemapujte tlačítka zpět, jak je popsáno v hhd docs [zde](https://github.com/hhd-dev/hhd?tab=readme-ov-file#extra-steps-gpd-win-devices)
    – Pokud potřebujete vizuálního průvodce, podívejte se na toto [video](https://www.youtube.com/watch?v=lnNfMY9kzjk).

### Externí zdroj

Další informace najdete v [GPD Win Tips and Tricks guide](https://github.com/aarron-lee/gpd-win-tricks), který obsahuje užitečné skripty pro tento handheld.