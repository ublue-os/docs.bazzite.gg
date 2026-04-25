---
title: Frequently Asked Questions
---

# Často kladené otázky (FAQ)

## Pro koho je Bazzite určen?

Bazzite je pro ty, kteří hledají operační systém, který splňuje jedno z následujících kritérií:

- Desktopový operační systém navržený pro hraní her inspirovaný SteamOS, který má ve srovnání s jinými desktopovými operačními systémy Linux poměrně nízkou údržbu.
- Správný frontend pro herní počítač na gauči s přívětivým ovládáním.
- Alternativa ke kapesním počítačům založeným na Windows, kde je preferováno prostředí podobné SteamOS a SteamOS v současné době nefunguje dobře nebo postrádá funkčnost na hardwaru kapesního počítače.
- Zážitek podobný SteamOS na kapesních počítačích SteamOS (jako je Steam Deck nebo Lenovo Legion Go S SteamOS Edition) s novějšími systémovými balíčky a alternativními desktopovými prostředími se stejným přístupem operačního systému založeného na obrazech pro stabilitu.

## Jaký obraz Bazzite používám?

Web [Bazzite](https://bazzite.gg/#image-picker) nabízí zjednodušený způsob výběru správného obrazu, který bude vybrán na základě hardwaru, desktopového prostředí a začlenění herního režimu Steam, pokud jej hardware podporuje.

Bazzite nabízí více obrazů, ale většina obrazů bude následovat _jednu z těchto **tří variant**_:

- **Varianta 1**: Obrazy Bazzite, které **nemají** herní režim Steam a dostávají automatické aktualizace denně s předinstalovanými herními balíčky.
- **Varianta 2**: Obrazy Bazzite, které se automaticky spouštějí do herního režimu Steam (jako SteamOS) a jsou určeny pro nastavení orientovaná na ovladače.
- **Varianta 3**: Obrazy Bazzite, které jsou určeny pro vývoj softwaru.

### 1. Desktopová verze

<sub>(**Varianta 1**)</sub>

**Na těchto konkrétních obrazech není herní režim Steam!**

Určeno speciálně pro stolní počítače a notebooky se zaměřením na hraní her, které je ovlivněno režimem plochy SteamOS a bezúdržbovou povahou ChromeOS. Operační systém Fedora Atomic Desktop (Kinoite/Silverblue) zaměřený na hry.  Steam a další herní nástroje jsou součástí základního operačního systému. Systém lze vrátit zpět díky spolehlivé stabilní základně Fedora Linux. Většina moderního PC hardwaru by měla být kompatibilní mimo specifické ovladače, které nefungují dobře na desktopovém Linuxu.  [Flathub](https://flathub.org/) je po vybalení povolen, takže všechny aplikace, které byste našli na SteamOS, jsou dostupné na Bazzite.  Aktualizace systému a aplikací se automaticky stahují na pozadí a ve výchozím nastavení se aplikují při restartu.

### [2. Bazzite-Deck Edition](../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)

<sub>(**Varianta 2**)</sub>

"**Steam Gaming Mode**" je předinstalovaný a jeho funkce jsou plně funkční pro podporovaný hardware. Tato verze Bazzite se spouští přímo do relace herního režimu Steam a je určena pro handheldy a scénáře hraní na gauči. Zahrnuje také relaci režimu pracovní plochy. Aktualizace systému a aplikací jsou ručně upgradovány v režimu Steam Gaming Mode a aplikovány při restartu.

### [3. Bazzite-DX (Developer eXperience Edition)](https://dev.bazzite.gg/)

<sub>(**Varianta 3**)</sub>

Verze Bazzite, která se speciálně stará o vývoj softwaru. Není instalován přes ISO; místo toho na něj přejdete změnou báze z aktuálního obrazu na obraz Bazzite-DX.

#### Příklad tabulky obrazů Bazzite

!!! note

    To nezahrnuje všechny obrazy Bazzite.

Ověřte svůj obraz Bazzite zadáním tohoto **příkazu** do terminálu:

```
rpm-ostree status
```

!!! important

    Každý obraz Bazzite by měl začínat `ostree-image-signed:docker://ghcr.io/ublue-os/...`.
    <sub> `...` je zástupný symbol pro skutečný název obrazu, na který lze odkazovat v tabulce níže. </sub>

| Obraz | Desktopové prostředí | Herní režim Steam | Hardware | Vydání |
| ---------------------------- | -------------------- | ------------------ | ----------------------------------------- | -------------- |
| `bazzite` | KDE Plasma          | Ne | AMD/Intel GPU | Desktop |
| `bazzite-nvidia` | KDE Plasma | Ne | GPU Nvidia | Desktop |
| `bazzite-nvidia-open` | KDE Plasma | Ne | GPU Nvidia (novější GPU Nvidia) | Desktop |
| `bazzite-gnome` | GNOME | Ne | AMD/Intel GPU | Desktop |
| `bazzite-gnome-nvidia` | GNOME | Ne | GPU Nvidia | Desktop |
| `bazzite-gnome-nvidia-open` | GNOME | Ne | GPU Nvidia (novější GPU Nvidia) | Desktop |
| `bazzite-deck` | KDE Plasma | Ano | GPU AMD/Intel Arc | Bazzite-Deck |
| `bazzite-deck-nvidia` | KDE Plasma | Ano | GPU Nvidia (novější GPU Nvidia) | Bazzite-Deck |
| `bazzite-deck-nvidia-gnome` | GNOME | Ano | GPU Nvidia (novější GPU Nvidia) | Bazzite-Deck |
| `bazzite-deck-gnome` | GNOME | Ano | GPU AMD/Intel Arc | Bazzite-Deck |

## SteamOS je založen na Arch Linuxu, tak proč používat Fedora Atomic Desktop?

SteamOS přijímá aktualizace balíčků a ovladačů méně často, a to i přes postupné vydání.  Bazzite bude následovat cyklus vydávání aktualizací Fedory, což znamená brzký přístup k novým aktualizacím ovladače grafické karty a kernelu ve srovnání se SteamOS.  Fedora Linux a Universal Blue v současné době podporují specifickou „atomickou“ implementaci pro správu více obrazů, které mohou přijímat všechny stejné aktualizace najednou, což je na rozdíl od odvozené distribuce Linuxu.  **Cílem Bazzite je mít operační systém připravený ke hře po jeho instalaci**.

### Jaké jsou výhody používání Fedora Atomic Desktop jako základny?

Vzhledem k tomu, že Bazzite je vlastní image Fedory Atomic Desktop, využívá pro účely stability kořenové soubory pouze pro čtení a je vytvořen jako [**obraz bootovatelného kontejneru**](https://containers.github.io/bootable/), který má výhody jako:

- Nízké riziko nezavedení systému
- V případě potřeby vrácení aktualizací systému a možnost připnout aktuální nasazení jako záložní stav uložení bez ztráty uživatelských dat.
- Hladký proces upgradu z hlavních vydání Fedory.
- Zaměřte se na kontejnerové aplikace, které nenarušují váš hostitelský systém.

> Podívejte se na [**domovskou stránku Universal Blue**](https://universal-blue.org), kde najdete další informace o tom, co tento projekt umí.

## Jsou ovladače grafické karty AMD a Intel předinstalované?

**Ano** a jsou aktualizovány během aktualizace systému, když jsou k dispozici nové ovladače. Není možné je ručně aktualizovat samostatně, protože jsou součástí obrazu.

### Jsou ovladače grafické karty Nvidia předinstalované?

**Ano, na obrazech Nvidia** a jsou aktualizovány během aktualizace systému, když jsou k dispozici nové ovladače. Není možné je ručně aktualizovat.
- Starší obraz (`-nvidia`) podporuje architektury Pascal, Maxwell a Volta (GTX 900, GTX 1000, Nvidia Titan V, GTX 750 (TI) a GTX 745).
- Moderní obraz (`-nvidia-open`) podporuje každou kartu Nvidia od architektury Turing a novější (GTX 16 a všechny karty RTX).

#### Bude přidána podpora pro mnohem starší grafické karty Nvidia?

V současné době se neplánuje podpora Kepler a starších architektur (většina karet GTX 700 a starších), protože je již **nepodporují** upstream ovladače Nvidia.
- Stále můžete nainstalovat Bazzite pomocí open-source ovladače nouveau.
    - Výkon a stabilita tohoto ovladače však zaostává za oficiálními ovladači Nvidia.
- V Bazzite **není možné** ručně nainstalovat proprietární ovladače Nvidia pro vaši starší kartu.
- Budete potřebovat jinou distribuci Linuxu, která to umožňuje, pokud chcete pro svůj GPU používat proprietární ovladače Nvidia.

### Co když změním hardware?

Většina hardwarových změn by **neměla** vyžadovat žádný ruční zásah mimo očekávání od konkrétního hardwaru, který by byl agnostik operačního systému.  Pokud však přecházíte z nebo na GPU Nvidia, pak bude nutné [rebasing](../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/brh.md) jako ruční zásah pro získání příslušných grafických ovladačů.

## Hry pro Windows tvrdí, že moje grafické ovladače jsou zastaralé, jak je mohu aktualizovat?

![](/../img/gpu_driver_warning.png)
Hry pro Windows nemohou správně detekovat grafické ovladače pro Linux.
- Protože se čísla verzí mezi ovladači pro Windows a Linux liší, hry vás občas upozorní na zastaralé ovladače.
- **Jakékoli takové varování můžete bezpečně ignorovat.**
- [Další podrobnosti naleznete zde.](#are-amd-and-intel-graphics-card-drivers-pre-installed)

## Podporuje Bazzite CSM/Legacy Boot?

Ne. Oznámení s pokyny pro vypnutí CSM se zobrazí, když instalační program detekuje spouštění staršího systému BIOS: ![CSM](../img/csm.webp)

## Mohu používat AMD Fluid Motion Frames?

**Ano**, ale pouze pokud to hra podporuje. Není k dispozici globálně pro každou hru jako ve Windows, ale:
* Mohou existovat jednotlivé herní mody nebo [Decky pluginy](https://github.com/xXJSONDeruloXx/Decky-Framegen), které napodobují podobné funkce.
* Pokud vlastníte [Lossless Scaling](https://store.steampowered.com/app/993090/Lossless_Scaling/) na Steamu, můžete nastavit vrstvu LSFG Vulkan pomocí příkazu terminálu `ujust get-lsfg`.

## Mohu motivovat svůj GRUB/bootloader?
Bazzite nepodporuje motivy bootloaderu (GRUB) a jejich použití může způsobit kritické problémy, jako je například nenabootování systému. Před nahlášením problémů prosím odstraňte všechny motivy GRUB.

## Mohu změnit název hostitele svého zařízení?

!!! note

    Názvy hostitelů musí být **méně než 20 znaků** kvůli omezení s kontejnery Distrobox.

Otevřete terminál a zadejte následující **příkaz**

```
hostnamectl hostname <hostname>
```

Zadejte název hostitele, kde je `<hostname>`.


## Nainstaloval jsem Windows, ale Bazzite se nespustí { id="windows-bootloader-override" }

Flash Bazzite Live ISO na flash disk a spusťte **Bazzite Bootloader Restoration Tool**.

## Mohu ve své aktuální instalaci přepnout na jiné pracovní prostředí?

<sub> (Příklad: Přechod z KDE Plasma do GNOME nebo naopak) </sub>

**Nedoporučuje se přepínat mezi desktopovými prostředími**, protože konfigurační soubory mají různé standardy, **které obvykle vedou k nefunkčním instalacím po přenastavení na jiný obraz Bazzite s nainstalovaným jiným desktopovým prostředím**.

## Mohu nainstalovat _toto_ desktopové prostředí nebo _takový_ správce oken?

Vytvořte si svůj vlastní [vlastní obraz založený na Bazzite](/Advanced/creating_custom_image.md) pomocí změny prostředí plochy nebo samostatného správce oken, kterou chcete.

## Co je `:0` a `:1` v nabídce GRUB při spouštění?

To umožňuje uživatelům vrátit zpět špatný upgrade systému výběrem předchozího nasazení.

- `:0` = Aktuální nasazení/nejnovější aktualizace
- `:1` = Předchozí nasazení/aktualizace.

Rozmístění lze také připnout k vrácení pro budoucí použití, takže `:2`, `:3` atd. mohou také existovat, pokud pro ně máte úložný prostor.

## Proč se tomu říká Bazzite?

[Fedora Linux's Atomic Desktops](https://fedoraproject.org/atomic-desktops/) původně dodržovaly schéma pojmenování založené na [minerály.](https://fedoraproject.org/kinoite/) Bazzite je minerál, který je známý tím, že je silný, lehký a je [modrý](https://universal-blue.org/).

## Chci Bazzite na zařízení, kde videohry nejsou prioritou

Universal Blue nabízí dva další operační systémy pro stolní počítače podobné Bazzite, ale bez zaměření na PC hry. I když oba mohou stále spouštět videohry, obsahují méně předinstalovaného herního softwaru a optimalizací. Všechny tři projekty sdílejí zdroje a vývoj, často se na nich podílejí stejní přispěvatelé:

- [**Aurora**](https://getaurora.dev/), pokud chcete desktopové prostředí **KDE Plasma**
- [**Bluefin**](https://projectbluefin.io/), pokud chcete desktopové prostředí **GNOME**.

## Mám otázky nebo obavy, které nelze zodpovědět v dokumentaci

!!! note

    Nejprve vyhledejte příslušná klíčová slova v dokumentaci Bazzite, než budete pokračovat v dalších krocích.

Důrazně vás žádáme, abyste to [nahlásili nástroji pro sledování problémů](https://github.com/ublue-os/bazzite/issues).  Mějte na paměti, že určité oblasti a témata jsou mimo naši kontrolu, zejména pokud jde o problémy s ovladači Nvidia, kompatibilitu her nebo jiné problémy, které sužují moderní linuxový desktop bez ohledu na to, zda používáte Bazzite nebo jiný operační systém Linux.