---
title: Alternative Installation Guide
---

# Alternativní instalační průvodce

!!! warning

    Tato metoda může mít problémy s škálováním instalačního programu v závislosti na hardwaru, zejména pokud se jedná o hardware kapesního počítače.

## Rebasing z obrazu Fedora Atomic Desktop

Pokud se setkáte s problémy s instalací našeho ISO nebo spouštěcí jednotka, kterou máte pro Bazzite příliš malá, stáhněte si [Fedora Kinoite (**KDE Plasma**)](https://fedoraproject.org/atomic-desktops/kinoite/) nebo [Fedora Silverblue (**GNOME**)](https://fedoraproject.org/samozřejmě, které prostředí preferujete.

1. Nastavení instalace je podobné jako u Bazzite a zahrnuje stejný instalační program se stejnými pokyny, ale **nenastavujte** účet root, pokud je to v instalačním programu možnost.

2. Po instalaci nebudete na Bazzite, dokud nezadáte příkaz na našem webu, který se objeví v sekci ["**Existující uživatelé Fedora Atomic Desktop**"](https://download.bazzite.gg), když je stahování připraveno, nebo odkazem na [úplný seznam obrazů v FAQ](/General/FAQ/#bazzite-image-chart-example).

3. Otevřete terminál a zadejte tento příkaz a mějte na paměti, že tento proces nemá **žádný indikátor průběhu** a bude trvat dlouho.

4. Po dokončení rebase restartujte a Bazzite by měl být nainstalován po restartu a vaše uživatelské jméno a uživatelské heslo se přenesou z upstream Fedora Atomic Desktop do Bazzite.

5. Také vám **budou chybět výchozí aplikace Flatpak, pokud je nenainstalujete pomocí příkazu `ujust`** níže.

## Pokyny pro bezpečné spouštění při rebasování z upstream obrazů Fedora Atomic Desktop

Rebasing z Fedora Silverblue, Fedora Kinoite atd. na Bazzite.

Pokud rebasujete z obrazu Fedora Atomic Desktop a používáte Secure Boot, postupujte podle pokynů v [**SOUBORU Bazzite**](https://github.com/ublue-os/bazzite/blob/main/README.md#secure-boot).

## Nainstalujte předinstalované aplikace Flatpak

Otevřete terminál a **zadejte tento příkaz**:

```command
ujust _install-system-flatpaks
```

Vyberte vzdálený repozitář „**Flathub**”.  Pokud se zeptá na „Systém” nebo „Uživatel”, vyberte „**Systém**”, protože to je výchozí vzdálený repozitář pro Bazzite.

> **Tento příkaz se nainstaluje:**
>
> - [Aplikace Flatpak pro obrazy **KDE Plasma**](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/kinoite/usr/share/ublue-os/bazzite/flatpak/install)
> - [Aplikace Flatpak pro obrazy **GNOME**](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/silverblue/usr/share/ublue-os/bazzite/flatpak/install)

### Odebrat Fedora Flatpak Remote

Odeberte prosím vzdálený repozitář Fedora Flatpak pomocí aplikace Warehouse.  To **ne** odstraní uživatelská data.

## Změna základu na podepsaný obraz

Jakmile je vše správně nastaveno, měli byste z bezpečnostních důvodů předělat z **nepodepsaného obrazu** na **podepsaný obraz**, takže **zadejte tento příkaz** do hostitelského terminálu:

```command
ujust verify-image
``` 
Po dokončení příkazu restartujte zařízení.

## Video tutoriál

https://www.youtube.com/watch?v=0NKEfVvdiOs