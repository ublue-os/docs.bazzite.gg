---
title: Dictionary & Terminology
---

# Slovník a terminologie

## Obecné

- **[[Desktop] Linux](https://www.ubuntudocs.com/bdesktop/)**: Rodina operačních systémů, které sdílejí mnoho ze stejného základního softwaru včetně [linuxového jádra](https://www.kernel.org/), [systemd](https://systemd.io/) a [jádrových nástrojů GNU](https://www.gnu.org/).
- **[Prostředí pro stolní počítače](https://en.wikipedia.org/wiki/Desktop_environment)**: Grafické uživatelské rozhraní (UI) a uživatelské prostředí (UX) pro režim plochy / obrazy pro plochu pro Bazzite. Také známý jako *DE*.
- **[Fedora Linux](https://fedoraproject.org/)**: Špičkový operační systém Linux, který má každých 6 měsíců novou hlavní verzi.
- **[Fedora Atomic Desktop](https://fedoraproject.org/atomic-desktops/)**: Experimentální verze Fedora Linux vytvořená tak, aby byla co nejspolehlivější a reprodukovatelná. Dvě z nejpopulárnějších variant jsou známé jako [Fedora Silverblue](https://fedoraproject.org/atomic-desktops/silverblue/) a [Fedora Kinoite](https://fedoraproject.org/atomic-desktops/kinoite/) pro konkrétní desktopová prostředí, která používají (GNOME a KDE Plasma).
- ["**Immutable**"](https://blog.verbum.org/2020/08/22/immutable-%E2%86%92-reprovisionable-anti-hysteresis/): Termín popisující operační systémy Linux, které se neřídí tradičním rozložením souborového systému, kde může být každý jednotlivý soubor odstraněn uživatelem s právy root.  V případě Bazzite je více [než toto](https://docs.fedoraproject.org/en-US/fedora-silverblue/technical-information/#filesystem-layout) a z pohledu rozšířené linuxové komunity je často nesprávně považován za „neměnný“.  Tým Bazzite by **nepopsal** Bazzite jako „neměnný“ operační systém.
- [**Open Gaming Collective (OGC)**](https://github.com/OpenGamingCollective): Pracovní skupina pro organizace a jednotlivce se zájmem o poskytování rámce pro spolupráci pro upstream změny různých herních komponent, které budou přínosem pro všechny projekty zaměřené na linuxové hry.

## Obrazy Bazzite-Deck

- **[Steam Deck](https://store.steampowered.com/steamdeck)**: Herní kapesní počítač Valve, který využívá jejich vlastní operační systém s vlastním operačním systémem Linux založeným na [Steam klientovi](https://store.steampowered.com/about/download).
- **[SteamOS](https://www.steamdeck.com/en/software)**: Operační systém Linux společnosti Valve založený na [Arch Linux](https://archlinux.org/), na kterém běží Steam Deck.
- **[Gamescope](https://github.com/ValveSoftware/gamescope)**: Mikrokompozitor vyvinutý pro SteamOS.  Použití zahrnuje škálování, filtrování, omezení snímkové frekvence a podporu HDR.
- **[Steam Gaming Mode](https://github.com/KyleGospo/gamescope-session)**: Relace, která spouští uživatelské rozhraní Steam Big Picture Mode uvnitř Gamescope.  Také známý jako *Herní režim*.

## Software

- **[Proton](https://github.com/ValveSoftware/Proton)**: Vrstva kompatibility zaměřená na hry spravovaná společností Valve ke spouštění her pro Windows pomocí [WINE](https://www.winehq.org/), [DXVK](https://github.com/doitsujin/dxvk), [VKD3D](https://github.com/HansKristian-Work/vkd3d-proton) a další komponenty.
- [**Vulkan**](https://www.vulkan.org/): Multiplatformní, otevřené standardní grafické rozhraní API odvozené od AMD's Mantle jako alternativa k DirectX, které je exkluzivní pro Windows.
- [**OpenGL**](https://www.opengl.org/): Starší grafické rozhraní API, když Vulkan není k dispozici.
- **[Flatpak](https://flatpak.org/)**: Univerzální aplikace pro Linux.  Výchozí vzdálené úložiště je [Flathub](https://www.flathub.org).
– [**Kontejnery**](https://www.redhat.com/en/topics/containers) – Izolovaná prostředí pro software.

## Základní technologie

- **[OSTree/libostree](https://ostreedev.github.io/ostree/introduction/)**: Upgrade systému, který Bazzite využívá a který umožňuje vrátit předchozí aktualizace systému nebo zcela změnit základ na jiné obrazy.
- **[Handheld Daemon (HHD)](https://github.com/hhd-dev/hhd)**: Handheldový software s podporou hardwaru, který poskytuje funkce ovladače, využití energie, RGB a další.
- **[Universal Blue](https://ublue.it)**: Kolektiv FOSS, který se specializuje na vlastní obrazy Fedory.
- **[Obraz bootovatelného kontejneru](https://docs.fedoraproject.org/en-US/bootc/getting-started/)**: Software a služby jsou zabaleny v kontejneru, který běží nad stávajícím operačním systémem (jako je Fedora) jako prostředek k dodání specializovaného operačního systému.  Také známý jako [*vlastní obraz*](../Advanced/creating_custom_image.md).
- **[Cloud-Native](https://aws.amazon.com/what-is/cloud-native/)**: Vytváření a nasazování softwaru automatizovaným způsobem. Poskytuje funkce, jako jsou bezdrátové aktualizace, více obrazů, které obdrží stejné upgrady upstream atd. V případě Bazzite se každý jednotlivý upgrade provádí v [Github](https://github.com/ublue-os/bazzite/).