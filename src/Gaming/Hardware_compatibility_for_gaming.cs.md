---
title: Hardware Compatibility for Linux Gaming
---

# Hardwarová kompatibilita pro hry Linux

## Minimální systémové požadavky

- **Architektura**: x86_64
- **Firmware**: UEFI (CSM/Starší boot [**UNSUPPORTED**](../General/FAQ.md#does-bazzite-support-csmlegacy-boot))
- **Procesor (CPU)**: 2GHz čtyřjádrový procesor nebo lepší
- **Systémová paměť (RAM)**: 8 GB
- **Grafika**: Grafická karta, která může využívat Vulkan 1.3 nebo vyšší, moderní GPU AMD fungují nejlépe
- **Úložiště**: 50 GB volného místa na interním **pevném disku (SSD)**
  - **Doporučené úložiště**: 120 GB volného místa na interním **pevném disku (SSD)**
  - **Externí úložiště a sekundární disky**: Všechny disky musí být naformátovány jako **BTRFS (SSD)** nebo **Ext4 (jednotky pevného disku [HDD])** (_prosím zálohujte soubory a po instalaci je přeformátujte_)
- **Síť**: Stabilní připojení k internetu bez omezení šířky pásma (_není vyžadováno pro instalaci_)
- **Další poznámky**: Některá periferní zařízení **nejsou** kompatibilní s Bazzite:
  – **Příklad adaptéru Wi-Fi** – [seznam **známých kompatibilních** adaptérů USB Wi-Fi](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md)

>[**Web Hardware pro Linux**](https://linux-hardware.org/?view=computers) je dobrým ukazatelem toho, jak dobře je OEM hardware podporován na ploše Linuxu.

### Požadavky na herní režim Steam

!!! note

    Tyto specifické požadavky se vztahují pouze na [obrazy Bazzite-Deck](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md), které jsou dodávány se všemi staženími ISO pro handheld Bazzite.

- Moderní AMD GPU
  - Řada RX 4xx a vyšší
    - Podporovány jsou také integrované GPU 600M/700M
- GPU Intel Arc jsou podporovány s **menšími výhradami** ve srovnání s hardwarem AMD
- Podpora GPU Nvidia je podporována s [**hlavními upozorněními**](/Handheld_and_HTPC_edition/quirks/#nvidia-gpu-exclusive-issues-with-steam-gaming-mode) ve srovnání s hardwarem AMD, který je mimo kontrolu správců Bazzite
– Vyžaduje účet [**Steam**](https://store.steampowered.com/).
  - Registraci účtu lze provést po instalaci, pokud jej ještě nemáte


>[**Web Hardware pro Linux**](https://linux-hardware.org/?view=computers) je dobrým ukazatelem toho, jak dobře je OEM hardware podporován na ploše Linuxu.

### Kompatibilní kapesní počítače

[**Handheld Wiki**](../Handheld_and_HTPC_edition/Handheld_Wiki/index.md) uvádí testované handheldy se správnou podporou pro Steam Deck, ASUS ROG Ally, Lenovo Legion Go a několik dalších handheldů.

<hr>

## GPU kompatibilní s Vulkan

!!! attention

    Linuxové hraní je silně závislé na kompatibilním hardwaru s Vulkanem.

### Zobrazení verze Vulkan vašeho GPU

Pokud používáte zařízení se starším nebo slabším GPU, které nepodporuje **Vulkan 1.3 nebo novější**, pak musíte použít starší sestavení Proton a Wine, jako je **Proton/WINE 6** nebo starší.  Zkontrolujte, kterou verzi Vulkan vaše GPU používá, zadejte toto do **terminálu**:

```command
vulkaninfo | grep 'Instance Version'
```

- Pokud má výstup méně než `1.3` v `Vulkan Instance Version:` nebo nefunguje vůbec, narazíte na problémy včetně nehratelných her a horšího výkonu.
- Opravdu stará zařízení se možná budou muset uchýlit k překladu OpenGL, který funguje hůře, má problémy s grafikou atd.

![Vulkan Command](https://github.com/user-attachments/assets/ccca14ca-3001-4aa6-bf47-e0dcbdb73936)

>Zkuste použít [**Proton-Sarek**](https://github.com/pythonlover02/Proton-Sarek), pokud máte hardware, který může využívat Vulkan 1.1, ale ne novější verze Vulkan. Lze jej nainstalovat pomocí ProtonPlus.

### GPU bez podpory Vulkan

Pokud však vaše GPU Vulkan vůbec nepodporuje, musíte použít starší verzi Protonu (Proton 3, 4 nebo 5) a použít tuto **možnost spuštění pro většinu her Steam**:

```command
PROTON_USE_WINED3D=1 %command%
```

To bude používat překlad OpenGL na rozdíl od Vulkanu.

<hr>

## Systémy souborů úložiště

!!! note

    Bazzite automaticky připojí sekundární disky, které jsou ve výchozím nastavení naformátovány jako Ext4 nebo BTRFS.

**BTRFS je výchozí a doporučený souborový systém pro Bazzite**.  Všechny sekundární disky, na kterých plánujete hrát videohry, by měly být **zálohovány a přeformátovány na Ext4 nebo BTRFS, disk však při provádění této operace ztratí všechna data**.  Pro správné formátování jednotek na vlastní riziko můžete použít [**Disky GNOME**](../Advanced/Auto-Mounting_Secondary_Drives.md).

### Nepodporované systémy souborů pro sekundární disky


!!! CRITICAL

NTFS a exFAT/FAT32 NEJSOU PODPOROVÁNY. OBA SOUBOROVÉ SYSTÉMY MOHOU A BUDOU VÉST K PORUŠENÍ DAT POD LINUXEM. NEPOUŽÍVEJTE JE!
    winBTRFS POD WINDOWS MÁ STÁLE CHYBY A TAKÉ NENÍ ŘEŠENÍM. 
    
    V SOUČASNOSTI NEEXISTUJE ŽÁDNÝ SPOLEHLIVÝ SOUBOROVÝ SYSTÉM MEZI PLATFORMY, KTERÝ LZE SDÍLET S WINDOWS A LINUXEM.

!!! warning

    Přeformátováním sekundárních interních/externích disků ztratíte všechna svá data.
    
!!! info
    
    Chcete-li zakázat NTFS upozornění, spusťte ujust _disable-ntfs-service. ** TOTO UDĚLEJTE POUZE V PŘÍPADĚ, ŽE VÍTE, CO DĚLÁTE. TOTO NEZABRÁNÍ ZTRÁTĚ DAT, POUZE TO VYPNE VAROVÁNÍ.**


#### NTFS

Pokud přicházíte ze systému Windows a plánujete hrát na sekundárním disku s již nainstalovanými hrami, s politováním vám musíme oznámit, že souborový systém NTFS je **nepodporován** pro hraní počítačových her na Bazzite.

Hraní her mimo NTFS způsobuje různé problémy, mimo jiné včetně **her se vůbec nespustí** a nakonec povede k **poškození dat** a **trvalé ztrátě dat**!

#### exFAT a FAT32

FAT32 a exFAT jsou **nepodporovány**. Oba souborové systémy **nepodporují symbolické odkazy**, které jsou vyžadovány pro správnou funkci prefixů Protonu.  Existují však scénáře, kdy je karta microSD naformátována na exFAT _v některých případech může fungovat_, ale tato metoda není podporována, protože správci Bazzite neplánují vyhovět.

### Sdílení her pomocí systému Windows Dual-Boot

Nainstalujte neoficiální ovladač [WinBtrfs](https://github.com/maharmstone/btrfs) do instalace Windows **na vlastní nebezpečí**. Před instalací ovladače v systému Windows si přečtěte veškerou dokumentaci související s tímto projektem.

#### Video tutoriál

https://www.youtube.com/watch?v=h6fc-3CCXbA