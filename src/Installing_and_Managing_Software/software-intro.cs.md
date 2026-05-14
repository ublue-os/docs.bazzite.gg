---
title: Introduction to Installing Software on Bazzite
---

# Úvod do instalace softwaru na Bazzite

## Formáty balíčků pro Linux
**Formáty balíčků seřazené od nejvíce doporučených po nejméně doporučené pro každodenní použití**:

1. [**Bazzite Portal (`ujust` Commands)**](./ujust.md) (_Convenience Commands_) – Vlastní skripty spravované přispěvateli Bazzite & Universal Blue, které mohou také nainstalovat malou podmnožinu aplikací. <small>(Toto má přednost před ostatními formáty, ale protože lze nainstalovat pouze malou sadu softwaru, je považováno za rozšíření nastavení na úrovni systému na rozdíl od obchodu s aplikacemi.)</small>
2. [**Bazaar App Store (Flatpak)**](./Flatpak.md) (_Graphical Applications_) – Univerzální formát balíčku využívající model založený na oprávněních a měl by být používán pro většinu grafických aplikací, **je to primární způsob získávání softwaru na Bazzite**.
3. [**Homebrew**](./Homebrew.md) (_Nástroje příkazového řádku_) – Instalujte aplikace určené ke spuštění uvnitř terminálu (CLI/TUI).
4. [**Kontejnery**](./Containers.md) – Spouštějte aplikace v izolovaném prostředí, abyste se vyhnuli problémům se závislostmi.
    4a. [**Distrobox Containers**](./Distrobox.md) (_Linux Packages & Development Workflows_) – Přístup k většině správců balíčků Linuxu pro software, který nepodporují Flatpak a Homebrew, a pro použití jako vývojové boxy.
    4b. [**Quadlet**](./Quadlet.md) (_Services_) – Spouštějte kontejnerizované aplikace jako [službu systemd](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-managing_services_with_systemd_Sect-Services).
5. [**AppImage**](./AppImage.md) (_Portable Graphical Applications_) – Přenosný univerzální formát balíčků, který závisí na konkrétních hostitelských knihovnách na systémové úrovni, obvykle získaný z webových stránek projektu.
6. [**`rpm-ostree`**](./rpm-ostree.md) (_Balíčky na úrovni systému_) – Vrstva balíčků Fedora na systémové úrovni (**nedoporučuje se, použijte jako poslední možnost**)

## Nelinuxové formáty

Bazzite může také spouštět aplikace pro Windows a Android.  Upozorňujeme, že ne veškerý software určený pro Windows a Android poběží na Bazzite.

### Spustitelné soubory systému Windows

**Použijte rozhraní [WINE](https://www.winehq.org/)**:

- [**Steam**](https://store.steampowered.com/) (_předinstalovaný_) má vestavěnou vrstvu kompatibility se systémem Windows.
- [**Lutris**](https://lutris.net/about) (_předinstalovaný_) pro počítačové hry mimo Steam a neherní software.
- [**Faugus Launcher**](https://github.com/Faugus/faugus-launcher) (_K dispozici v Bazaar_) jako alternativa k Lutris.
- [**Heroic Games Launcher**](https://heroicgameslauncher.com/) (_K dispozici v Bazaar_) pro správnou integraci Epic Games, GOG a Amazon Games.
- [**Greenlight**](https://flathub.org/en/apps/io.github.unknownskl.greenlight) (_K dispozici v Bazaar_) pro streamování her z Windows Store a Gamepass. <small>(**Pouze streamování**)</small>
- [**WineZGUI**](https://github.com/fastrizwaan/WineZGUI) (_K dispozici v Bazaar_) pro méně komplikované aplikace Windows, které nevyžadují zvláštní ohledy.

>Přečtěte si [**Bazzite Gaming Guide**](/Gaming/index.md), kde najdete další informace o spouštění her pro Windows na Linuxu.

### Aplikace pro Android

Při instalaci aplikací pro Android na Bazzite postupujte podle [**Waydroid Setup Guide**](./Waydroid_Setup_Guide.md).

## Scénáře doporučení formátu balíčku

!!! note
        
        Vezměte prosím na vědomí, že pouze malý výběr softwaru je k dispozici k instalaci na portálu Bazzite, takže není uveden.

![Strom rozhodnutí o instalaci softwaru](../img/software-install-decision-tree-light.svg#only-light)
![Strom rozhodnutí o instalaci softwaru](../img/software-install-decision-tree-dark.svg#only-dark)

| **Formát balíčku** | **Grafická aplikace (GUI)** | **Příkazový řádek / balíček na úrovni systému** |
|--------------------|---------------------------------|---------------------------------------
| **Bazaar App Store (Flatpak)** | Primární metoda pro získání grafických aplikací. | Nedoporučuje se pro aplikace nebo nástroje příkazového řádku. |
| **Homebrew** | Pouze několik aplikací (např. VSCode přes [Universal Blue cask](https://github.com/ublue-os/homebrew-tap)) se doporučuje nainstalovat graficky. | Důrazně se doporučuje pro nástroje příkazového řádku. |
| **Kontejnery (Distrobox / Quadlet)** | Pokud není k dispozici v Bazaar, nainstalujte obecný balíček pro Linux do kontejneru Distrobox a exportujte jej. Pro služby vytvořte kvadlet. | Doporučeno, pokud balíček Homebrew neexistuje. |
| **AppImage** | Najděte AppImage online na vlastní nebezpečí z důvěryhodného zdroje. Pro správnou integraci systému použijte Gear Lever (k dispozici v Bazaar). | — |
| **Vrstvení balíků** | Pokud žádná z výše uvedených možností nefunguje, vrstvěte balíček na vlastní nebezpečí. | Vrstva pouze v případě, že nefunguje žádná jiná možnost. |
| **Ostatní** | Některý software se dodává jako `.tar.gz` se spustitelným souborem. *Může* to běžet na Bazzite poté, co ho uděláte spustitelným ve vlastnostech souboru. Případně použijte rozhraní Wine (např. Lutris) pro verze Windows. Waydroid může fungovat, pokud existuje port Android. | — |
| **[Vlastní obraz](../Advanced/creating_custom_image.md)** | — | Určeno pro alternativní desktopová prostředí nebo software pro neobvyklý hardware; může být vyžadován vlastní obraz Bazzite.  |