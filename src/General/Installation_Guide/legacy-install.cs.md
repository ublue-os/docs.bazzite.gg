---
title: Legacy ISO Installation Guide
---

# Legacy ISO instalační příručka

## Pouze starší ISO

Tato příručka je pouze pro starší ISO, které jsou v současné době stále podporovány, protože nový instalátor nepodporuje ruční dělení a některé malé chyby, které se stále vyskytují v novém instalačním programu.

## Systémové požadavky

- Přečtěte si [**Průvodce kompatibilitou hardwaru**](/Gaming/Hardware_compatibility_for_gaming.md) pro systémové požadavky Bazzite.
- Secure Boot a Trusted Platform Module (TPM) jsou podporovány na většině hardwaru, ale musíte [**zaregistrovat náš klíč během instalace nebo po instalaci**](#secure-boot).
- [**Dual-booting-windows je také podporováno**](#dual-booting-windows).

### Požadavky na instalaci

- Způsob, jak stáhnout Bazzite ISO
  - Správce stahování (jako [**Motrix**](https://motrix.app/)), pokud přímé stahování pro Bazzite ISO selže nebo se stahuje příliš pomalu.
- 16GB+ spouštěcí médium, jako je flash disk
  – Software pro flashování ISO, jako je **Fedora Media Writer** ([**Windows/macOS**](https://github.com/FedoraQt/MediaWriter/releases) nebo [**Linux**](https://flathub.org/en/apps/org.fedoraproject.MediaWriter))
    - Ventoy **NENÍ** podporovaný software pro flashování Bazzite ISO.
- Fyzická kabelová klávesnice je **doporučena** a **vyžadována pro zařízení bez dotykové obrazovky**.
  - V opačném případě si vytvořte uživatelský účet s **uživatelským jménem** a **uživatelským heslem**, pokud máte klávesnici.

### Desktopová prostředí

Všechny obrazy přicházejí s výběrem [**KDE Plasma**](https://kde.org/plasma-desktop/) nebo [**GNOME**](https://www.gnome.org/) pro jejich desktopové prostředí.

[**Steam Gaming Mode**](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md) je volitelná doplňková relace k KDE Plasma nebo GNOME a je doporučena pro domácí kino PC (HTPC) a kapesní nastavení.

Více informací o rozdílech mezi variantami obrazů naleznete na [**Bazzite FAQ**](../../General/FAQ.md).

=== "KDE Plasma"

    #### KDE Plasma (výchozí)

    ![Snímek obrazovky plochy Bazzite s KDE Plasma|690x388, 75%](/img/KDE_Plasma_DE.png)

    - Výchozí rozhraní KDE Plasma má tradiční a známé rozložení
    - Vysoce přizpůsobitelné se spoustou nastavení
    - Qt framework
    - Populární linuxové distribuce jako SteamOS používají KDE Plasma

=== "GNOME"

    #### GNOME (obrazy `-gnome`)

    ![Snímek obrazovky plochy Bazzite s GNOME|690x388, 75%](/img/GNOME_DE.png)

    - Výchozí rozhraní GNOME má elegantní a dotykové rozložení
    - Jednoduché a stručné
    - GTK framework
    - Populární linuxové distribuce jako Ubuntu používají GNOME

=== "Steam Gaming Mode"

    #### Herní režim Steam (obrazy `-deck`)

    ![Herní režim|690x388, 75%](/img/Gaming_Mode.jpeg)

    !!! note

        Vaše zařízení se při spuštění automaticky spustí do relace herního režimu Steam a do režimu Desktop lze přistupovat z „**nabídky napájení**“ v režimu hry Steam.

    {% block desktop_envs_steam_notes %}

    - **Vyžaduje účet [Steam](https://store.steampowered.com/)**
    - Zahrnuto v [obrazech Bazzite-Deck](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)
    - Rozhraní je navrženo pro ruční a gaučové hraní
    - Přátelský k ovladači
    - Volba KDE Plasma nebo GNOME jako relace režimu plochy
    - Další funkce s [Decky pluginy](https://github.com/SteamDeckHomebrew/decky-loader) [(Zobrazit všechny pluginy)](https://plugins.deckbrew.xyz/)

    {% endblock %}

## 0. Zálohování dat

Než budete pokračovat v instalaci, nezapomeňte si zálohovat svá osobní data z disku, na který chcete Bazzite nainstalovat.

## 1. Stáhnout a flashovat starší ISO

- Stáhněte si [Bazzite](https://download.bazzite.gg) po výběru správného ISO pro váš hardware pomocí našeho nástroje Image Picker.
- Flash Bazzite na zaváděcí médium.
- Po flashování ISO vysuňte disk.

### Výpočet hash kontrolního součtu ISO SHA256

**Video tutoriál**:

https://www.youtube.com/watch?v=wUDbMJtR1sM

## 2. Boot Bazzite

- Připojte zaváděcí médium k zařízení a spusťte jej.
- Po připojení zařízení spusťte instalační program Bazzite.
- To závisí na hardwaru vaší základní desky, ale většinou to může být funkční klávesa jako <kbd>F9</kbd> nebo podobná.
  - Někdy potřebujete nahlédnout do manuálu, vyhledat své zařízení online nebo si přečíst klávesové zkratky, které se objeví při spouštění počítače.
    - Případně změňte nastavení systému BIOS tak, aby se spouštělo ze zaváděcího zařízení nejdříve před aktuálním úložištěm, ale toto se **nedoporučuje** ponechat zapnuté i po instalaci Bazzite.
- Ověřte správně médium a přejděte k instalačnímu programu.

### Ruční zařízení

Podržte tlačítko 'Snížit hlasitost' (<kbd>-</kbd>) a klikněte na tlačítko napájení, a když uslyšíte zvonění, uvolněte obě tlačítka a spustí se Boot Manager. Když se dostanete do spouštěcí nabídky, vyberte spouštěcí zařízení pro zavedení instalačního programu Bazzite.

## 3. Uvnitř instalačního média

!!! note "Instalace Bazzite bez fyzické klávesnice připojené k vašemu zařízení:"

    Pokud nemáte připojenou fyzickou klávesnici USB, **NE** nemačkejte** „_User Creation_“, protože tím odstraníte výchozí uživatelské jméno a heslo a nebudete moci zadat uživatelské jméno nebo heslo bez fyzické klávesnice.

    **výchozí uživatel**: `bazzite`
    **výchozí heslo**: `bazzite`

![Automatická konfigurace disku|690x497, 75%](../../img/anaconda_drive_configuration.png)

![Příklad uživatelského nastavení|690x359, 75%](../../img/anaconda_user_setup.png)

- Vyberte jazyk, region, rozložení klávesnice a časové pásmo.
- Vyberte jednotku, na kterou bude Bazzite nainstalován.
  - Odstraňte všechny diskové oddíly, které vám zbyly na disku **pokud není duální bootování na stejném disku**.
  - Doporučuje se použít konfiguraci automatického úložiště **pokud není duální bootování na stejném disku**.
- V případě potřeby můžete disk zašifrovat heslem.
  - **Pokud toto heslo ztratíte, nelze ho dešifrovat**.
  - K ODEMKNUTÍ ZAŘÍZENÍ JE POTŘEBA FYZICKÁ KABELOVÁ KLÁVESNICE!
- Nastavení uživatelského účtu.
  - Poskytněte administrátorská oprávnění a **nastavte uživatelské heslo**.
- Zahajte instalaci.
- Po dokončení instalace restartujte zařízení.

## Duální spouštění

!!! note

    Tuto část přeskočte, pokud plánujete nainstalovat Bazzite bez duálního spouštění Windows.

### Duální spouštění systému Windows

Pro duální spouštění Windows na **samostatných** discích použijte spouštěcí nabídku UEFI vaší základní desky, protože zavaděč GRUB nemusí správně rozpoznat každou spouštěcí položku.

### Videonávod

https://www.youtube.com/watch?v=KAt49B6rSFI

### Písemný návod

1. Instalace Bazzite se sdíleným diskem.
2. Instalace Bazzite na samostatný disk.

=== "Sdílený disk (automatické rozdělování)"

    1. (Ve Windows) Vypněte **Bitlocker šifrování** a **fastboot** a restartujte počítač.
    2. (Ve Windows) Změňte velikost oddílu Windows pomocí aplikace Správa disků, abyste měli dostatek místa pro Bazzite.
    Obvykle by to mělo vypadat nějak takto:
    ![](/img/dualbooting_partitions_windows.png)
    <i><small>Zdroj: [diskpart.com](https://www.diskpart.com/windows-10/windows-10-disk-management-0528.html)</small></i>
    3. Spusťte instalační program Bazzite s možností automatického rozdělení.
    4. Restartujte do Bazzite a spusťte `ujust regenerate-grub` v terminálu pro přidání Windows do GRUB.

=== "Sdílený disk (ruční rozdělení) [k dispozici pouze u starších verzí ISO]"

    1. (Ve Windows) Změňte velikost oddílu Windows pomocí aplikace Správa disků, abyste měli dostatek místa pro Bazzite.
    Obvykle by to mělo vypadat nějak takto:
    ![](/img/dualbooting_partitions_windows.png)
    <i><small>Zdroj: [diskpart.com](https://www.diskpart.com/windows-10/windows-10-disk-management-0528.html)</small></i>
    2. Spusťte instalační program Bazzite pomocí [manual partitioning](#manual-partitioning-instructions)
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

### Pokyny k ručnímu rozdělení

!!! warning "Tyto pokyny by měli používat pouze uživatelé, kteří spouštějí duální systém na stejném disku. V ostatních případech je preferováno automatické rozdělování."

!!! attention "Bazzite podporuje pouze souborový systém BTRFS pro `/`."

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

### Duální spouštění jiných operačních systémů Linux

!!! note 

    Duální bootování s **jinými distribucemi Linuxu**, zejména s **neatomovou Fedorou**, není oficiálně podporováno. Doporučuje se použít spouštěcí nabídku UEFI vaší základní desky nebo se zcela vzdát duálního spouštění, abyste předešli neočekávaným problémům. Pokud se něco pokazí, obnovte zavaděč Bazzite pomocí nástroje **Bootloader Restoring Tool** v Live ISO.

Pro obrazy Fedora Atomic Desktop na **stejném** disku: pro duální spouštění jiného **obrazu Fedora Atomic Desktop** (jako [Bluefin](https://projectbluefin.io/)) nainstalovaného spolu s Bazzite, musíte vytvořit další oddíl EFI a přepínat mezi nimi prostřednictvím spouštěcí nabídky UEFI vaší základní desky.

Pro duální spouštění na **samostatných** discích:

Použijte spouštěcí nabídku UEFI vaší základní desky, protože zavaděč GRUB nemusí správně rozpoznat každou spouštěcí položku.

## Zabezpečené spouštění

!!! note

    Tuto část přeskočte, pokud není zabezpečené spouštění povoleno nebo jej váš hardware nepodporuje.

!!! important

    Výzva k registraci používá anglické rozložení klávesnice QWERTY bez rozdílu od vaší skutečné hardwarové klávesnice. Jiná rozložení proto mohou kolidovat se znaky hesla (tj. `A` a `Q` jsou na rozloženích AZERTY zaměněny).

Bazzite podporuje Secure Boot, ale pro jeho použití je nutné zaregistrovat klíč Universal Blue, jinak ponecháte Secure Boot zapnutou v BIOSu, Bazzite se nespustí.

### Důležité poznámky k bezpečnému spouštění:

- Zadáním hesla se z bezpečnostních důvodů zaregistrují neviditelné znaky, takže neuvidíte, co píšete!
- Aktualizace BIOSu může znovu povolit Secure Boot a možná budete muset po aktualizaci postupovat podle **"Metody B"**, abyste vyřešili černou obrazovku při zavádění, která si stěžovala na načtení jádra jako prvního.
- Steam Deck **není** dodáván s povoleným bezpečným spouštěním a nedodává se s žádnými klíči zaregistrovanými ve výchozím nastavení, nepovolujte Secure Boot na vašem Steam Deck, pokud absolutně nevíte, co děláte.

### Chybová zpráva (pokud klíč **není** správně zaregistrován):

```
error: ../../grub-core/kern/efi/sb.c:182:bad shim signature.
error: ../../grub-core/loader/1389/efi/linux.c:256:you need to load the kernel first.

Press any key to continue...
```

Chcete-li to vyřešit, postupujte podle **metody B** níže, a pokud na ni narazíte, přejděte přes chybovou zprávu.

### **Metoda A** - Během způsobu instalace

![Nabídka bezpečného spouštění: Pokračovat ve spouštění / Zapsat MOK / Zapsat klíč z disku / Zapsat hash z disku|200x102, 100%](../../img/Secure_Boot.png 'Zabezpečené spouštění')

!!! note

    Tato obrazovka se objeví také při příštím spouštění, pokud povolíte zabezpečené spouštění, pokud bylo během instalace zakázáno.

Po opuštění instalačního programu Bazzite se objeví modrá obrazovka s možností zaregistrovat podepsané klíče.

`Enroll MOK`, pokud máte povoleno bezpečné spouštění. Pokud budete vyzváni k zadání hesla, **zadejte**:

```command
universalblue
```

V opačném případě `Continue boot`, pokud máte zakázáno Secure Boot nebo pokud není podporováno vaším hardwarem.

### **Metoda B** – Metoda po instalaci

**Před pokračováním v BIOSu zakažte Secure Boot** a poté jej znovu povolte **po registraci klíče**.

Pokud jste již Bazzite nainstalovali, pak **zadejte tento příkaz do hostitelského terminálu**:

```
ujust enroll-secure-boot-key
```

Pokud budete vyzváni k registraci požadovaného klíče, **zadejte heslo do hostitelského terminálu**:

```command
universalblue
```

**Zabezpečené spouštění můžete nyní znovu zapnout v systému BIOS.**
Pomocí následujícího příkazu nabootujete přímo do systému BIOS (pokud je podporován):

```command
ujust bios
```

### Dokončete registraci MOK při spuštění

Při příštím spuštění uvidíte modrou obrazovku MokManager:

1. Zvolte **Zapsat MOK**.
2. Až budete vyzváni k zadání hesla, zadejte:
    ```command
    universalblue
    ```

Po restartu je klíč zaregistrován a Secure Boot může zůstat povolený. Váš systém by se nyní měl normálně spustit pod Secure Boot.

## **Odstraňování problémů s instalací**:

Přečtěte si [**Troubleshooting Guide**](./troubleshoot_guide.md) nebo [**Alternative Installation Guide**](./alternate-install-guide.md), kde najdete zástupná řešení instalace.

## Po instalaci

Bazzite je nyní nainstalován. Přečtěte si [**Průvodce po instalaci**](./post-installation.md), kde najdete doporučené další kroky, nebo začněte hrát!