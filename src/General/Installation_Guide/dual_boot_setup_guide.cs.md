---
title: Dual Boot Preliminary and Post-Installation Setup Guide
tags:
  -  Obsolete
search:
  exclude: true
---

# Průvodce nastavením po instalaci a předběžném spouštění dvou systémů

!!! note

    Než budete pokračovat, přečtěte si nejprve [**Průvodce instalací**](./index.md) pro vaše zařízení.

1. Instalace Bazzite se sdíleným diskem.
2. Instalace Bazzite na samostatný disk.

=== "Sdílený disk (automatické rozdělování)"

    1. (Ve Windows) Vypněte **Bitlocker šifrování** a **fastboot** a restartujte počítač.
    2. (Ve Windows) Změňte velikost oddílu Windows pomocí aplikace Správa disků, abyste měli dostatek místa pro Bazzite.
    Obvykle by to mělo vypadat nějak takto:
    ![](/img/dualbooting_partitions_windows.png)]
    <i><small>Zdroj: [diskpart.com](https://www.diskpart.com/windows-10/windows-10-disk-management-0528.html)</small></i>
    3. Spusťte instalační program Bazzite s možností automatického rozdělení.
    4. Restartujte do Bazzite a spusťte `ujust regenerate-grub` v terminálu pro přidání Windows do GRUB.


=== "Sdílený disk (ruční rozdělení) [k dispozici pouze u starších verzí ISO]"

    1. (Ve Windows) Změňte velikost oddílu Windows pomocí aplikace Správa disků, abyste měli dostatek místa pro Bazzite.
    Obvykle by to mělo vypadat nějak takto:
    ![](/img/dualbooting_partitions_windows.png)
    <i><small>Zdroj: [diskpart.com](https://www.diskpart.com/windows-10/windows-10-disk-management-0528.html)</small></i>
    2. Spusťte instalační program Bazzite pomocí [manual partitioning](./manual_partitioning.md)
    3. Restartujte do Bazzite a spusťte `ujust regenerate-grub` v terminálu pro přidání Windows do GRUB.

=== "Samostatný disk"

    **Pokud je možné použít vyhrazený disk, doporučujeme tento způsob.**

    Nainstalujte Bazzite na samostatný interní nebo externí disk.

    1. Nainstalujte druhý operační systém na jednotku (například Windows).
    2. Nainstalujte Bazzite na **druhý** disk.
    3. Nastavte Bazzite jako **výchozí** v pořadí spouštění (volitelné).

    Pokud instalujete Windows jako druhý, měli byste odpojit jednotku Bazzite, abyste zabránili použití instalátoru Windows v používání jeho oddílu EFI.

    Pokud nemáte k dispozici interní disk, můžete také nainstalovat systém Windows na externí disk pomocí systému Windows-to-Go pomocí [Rufus](https://rufus.ie/en/) pro duální spouštění.

Pokud nainstalujete Windows po Bazzite, můžete obnovit zavaděč Bazzite pomocí nástroje **Bootloader Restoring Tool** v Live ISO.

## Pokyny k ručnímu rozdělení

!!! warning "Tyto pokyny by měli používat pouze uživatelé, kteří spouštějí duální systém na stejném disku. V ostatních případech je preferováno automatické rozdělování."

!!! warning "Bazzite podporuje pouze souborový systém BTRFS pro `/`."

Pokud potřebujete výukové video pro ruční dělení, podívejte se na tento [návod v časovém razítku 9:10](https://www.youtube.com/watch?v=JxPsKhJGTrs&t=550s).

1. Vyberte možnost Instalace
2. Vyberte `Advanced Custom(Blivet-GUI)` v části Konfigurace úložiště.
![Výběr ručního rozdělení](../../img/select_manual_partitioning.png)
3. Vytvořte následující oddíly a zařízení:
  - **/boot/efi**
    ![EFI oddíl](../../img/efi_partition.png)
    ```
    mount point: /boot/efi
    format:      EFI system partition
    size:        300MB
    ```
  - **/bota**
    ![spouštěcí oddíl](../../img/boot_partition.png)
    ```
    mount point: /boot
    format:      ext4
    size:        2GB
    ```
  - **oddíl btrfs**
    ![btrfs partition](../../img/btrfs_partition.png)
    ```
    mount point:
    format: btrfs
    size: [max]
    ```
  -**/**
    ![/ subvolume](../../img/root_subvolume.png)
    ```
    mount point: /
    format:      btrfs (subvolume)
    ```
  - **/var**
    ![/var subvolume](../../img/var_subvolume.png)
    ```
    mount point: /var
    format:      btrfs (subvolume)
    ```
  - **/var/home**
    ![/var/home subvolume](../../img/var_home_subvolume.png)
    ```
    mount point: /var/home
    format:      btrfs (subvolume)
    ```
4. Vyberte Hotovo
5. Vyberte Přijmout změny
6. Pokračujte v instalaci.

<hr/>

### Poznámka o duálním spouštění jiných distribucí

Pro obrazy Fedora Atomic Desktop na **stejném** disku:

- Chcete-li duální spouštění dalšího **obrazu Fedora Atomic Desktop** (jako [Bluefin](https://projectbluefin.io/)) nainstalovaného spolu s Bazzite, musíte vytvořit další oddíl EFI a přepínat mezi nimi prostřednictvím spouštěcí nabídky UEFI vaší základní desky.

Pro duální spouštění na **samostatných** discích:

- Použijte spouštěcí nabídku UEFI vaší základní desky, protože zavaděč GRUB nemusí správně rozpoznat každou spouštěcí položku.

!!! note 

    Duální bootování s **jinými distribucemi**, zejména **neatomovou Fedorou**, není oficiálně podporováno. Doporučuje se použít spouštěcí nabídku UEFI vaší základní desky nebo se zcela vzdát duálního spouštění, abyste předešli neočekávaným problémům. Pokud se něco pokazí, obnovte zavaděč Bazzite pomocí nástroje **Bootloader Restoring Tool** v Live ISO.

## Dual Boot Post-Configuration Setup

Zobrazte své instalace Windows i Bazzite v nabídce GRUB, ze které si můžete vybrat při spouštění, zadáním tohoto **příkazu do terminálu**:

```
ujust regenerate-grub
```

### Bazzite jako primární spouštěcí systém

Pokud `OS Boot Manager` nastavil `Windows Boot Manager` jako první prioritu spouštění, může to mít za následek zavádění systému přímo do Windows po instalaci namísto Bazzite. Možná to budete muset opravit v nastavení systému BIOS.

Pamatujte, že nabídka GRUB se nemusí zobrazit. V takovém případě spamujte při spouštění klávesu <kbd>↓</kbd>.

<hr>

### Spusťte systém Windows ze služby Steam

Přidá skript ve službě Steam pro spuštění systému Windows.

```
ujust setup-boot-windows-steam
```

## Rozšíření velikosti úložiště ve scénáři s duálním spouštěním systému Windows

!!! note

    Toto je pro budoucí použití po chvíli duálního spouštění.

**Podívejte se na tento videonávod o tom, jak rozšířit úložiště**:

https://www.youtube.com/watch?v=uy8mi1pAj8E