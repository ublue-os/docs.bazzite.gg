---
title: Ayaneo Handhelds
---

# Kapesní počítače Ayaneo

!!! disclaimer

    Funkce spánku vyžaduje aktualizaci systému BIOS.

## Ayaneo Geek 1S

![photo_5875160389711413569_y|663x500, 100 %](../../img/Ayaneo_Geek_1S.jpeg)

### Známé problémy

- Pozastavení zařízení vyžaduje nejnovější aktualizaci systému BIOS.
  - Hlášení problémů s ovladačem při probuzení hlásila nekonzistenci. Zdá se, že povolení "úplné počáteční podpory usb" v Bios má vliv na to, jak často se problém vyskytuje.
- V BIOSu chybí možnost velikosti VRAM, protože je řízena aplikací AYASPACE pod Windows. Velikost vyrovnávací paměti UMA můžete změnit pomocí [Smokeless_UMAF](https://github.com/DavidS95/Smokeless_UMAF), ale tato metoda má svá vlastní rizika.

### Funkční HHD

```
sudo systemctl enable --now hhd@$(whoami)
```

### Podpora e-GPU:

- Jsou podporovány skříně e-GPU Thunderbolt 3/4 a USB4 přes USB4.
  - **AMD**:
    - Automatické přepínání při spouštění pomocí [all-ways-egpu](https://github.com/ewagner12/all-ways-egpu/tree/main) funguje dobře pomocí metody 2 a 3 při spouštění, bohužel metoda 1 není podporována.
      - Skript je třeba nainstalovat pomocí [Steam Deck/Uživatelská instalace](https://github.com/ewagner12/all-ways-egpu/blob/main/README.md#steamosbazziteuser-installation).
    - Žádný problém při bootování s připojeným eGPU. Testováno na RX 6800 a nejsou potřeba žádné parametry jádra, protože Bazzite nyní ve výchozím nastavení povoluje potřebný argument (amdgpu .ppfeaturemask).
      - Podle mého testování je stále potřeba používat `rpm-ostree kargs --append-if-missing=pci=nommconf` (nebo upravovat příkazový řádek jádra pomocí `rpm-ostree kargs –editor`), protože některé aplikace jinak nemusí fungovat správně.
    - Některé karty AMD vyžadují nastavení správného limitu pro takty GPU a paměti, jedná se o známý problém, který se vyskytuje také na stolních počítačích. Doporučuji nainstalovat LACT a nastavit správné limity pro kartu.
  - **NVIDIA**: momentálně netestováno, ale _může_ fungovat s variantou bazzite „-nvidia-deck“.

### Externí zdroj

Podívejte se na [původní vlákno](https://universal-blue.discourse.group/t/ayaneo-geek-1s-2s-linux-bazzite-support-is-already-almost-there-lets-add-them-to-the-officially-supported-devices/1046), kde najdete další informace a aktualizace o tomto zařízení.

Ayaneo Geek 1s je (od dubna 2025) jediný kapesní počítač Ryzen 7000, který dosud neobdržel aktualizaci EC, která prodlužuje výdrž baterie. Můžete sledovat a nahlásit [v tomto vláknu neshod](https://discord.com/channels/717181357109018694/1301507866754289745).