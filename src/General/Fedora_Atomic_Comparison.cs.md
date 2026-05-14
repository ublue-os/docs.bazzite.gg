---
title: Comparison of Bazzite and Fedora Atomic Desktop
---

# Srovnání Bazzite a Upstream Fedora Atomic Desktop

## Co je to Bazzite?

Bazzite je vlastní obraz [**Fedora Kinoite (KDE Plasma images)**](https://fedoraproject.org/atomic-desktops/kinoite/) nebo [**Fedora Silverblue (obrazy GNOME)**](https://fedoraproject.org/atomic-desktops/silverblue/), které jsou součástí [**rodiny Fedora Atomic Desktop**](https://fedoraproject.org/atomic-desktops/) s úpravami, které se snaží poskytnout uživatelsky přívětivý zážitek hned po vybalení se zaměřením na hry na PC.

## Klíčové rozdíly

Následuje seznam funkcí, se kterými se Bazzite dodává a které se liší od upstreamových operačních systémů Fedora Atomic Desktop:

### Méně nastavení po instalaci

- Lepší hardwarová podpora ihned po vybalení od PC hardwaru po periferní zařízení.
- Multimediální kodeky s plnou podporou zrychleného kódování a dekódování videa ihned po vybalení.
- Předinstalovaný software zaměřený na hry jako Steam a Lutris.
- Vzdálený repozitář Fedora Flatpak byl odstraněn ve prospěch používání repozitáře [**System Flathub**](https://flathub.org/), abyste měli ve výchozím nastavení přístup k více aplikacím.

### Snadné použití

- Pohodlné [**`ujust`**](/Installing_and_Managing_Software/ujust/) skripty od správců a přispěvatelů projektu.
- Režim hry Steam je nastaven po vybalení a automaticky se spouští na [**obrazech Bazzite-Deck**](/Handheld_and_HTPC_edition/Steam_Gaming_Mode/), které jsou určeny pro hraní z ruky a na gauči. 

### Vyrobeno s ohledem na vývojáře

- Homebrew je zamýšlený správce balíčků pro nástroje příkazového řádku.
- Kontejnery Distrobox poskytují přístup k dalším správcům balíčků pro stolní počítače Linux pro konkrétní aplikace nebo vývojová prostředí.
- [**Bazzite-DX varianta**](https://dev.bazzite.gg/) jako defacto Bazzite image pro vývoj softwaru.

### Extra vylepšení

- Podpora aplikací pro Android s [**Waydroid**](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md).
- Firefox již není součástí obrazu ve prospěch verze Flatpak.
  - Firefox lze nyní odinstalovat, protože není součástí obrazu
  - Může také přijímat aktualizace rychleji, protože se nespoléhá na aktualizace systému. 
- Sekundární disky naformátované jako BTRFS nebo Ext4 budou automaticky připojeny.
- Vylepšení desktopových prostředí včetně předinstalovaných rozšíření GNOME a motivů KDE Plasma.
- Návrat ke starším sestavením Bazzite za posledních 90 dní.