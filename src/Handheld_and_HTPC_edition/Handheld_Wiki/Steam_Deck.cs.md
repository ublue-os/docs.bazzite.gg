---
title: Steam Deck
---

# Steam Deck

## Steam Deck (LCD a OLED modely)

![Steam Deck LCD|690x348, 100%](../../img/Steam_Deck_LCD.jpeg)

### Aktualizace systému BIOS
Chcete-li dostávat aktualizace BIOSu Steam Deck, doporučujeme do terminálu zadat `ujust enable-deck-bios-firmware-updates`.

### Proč Bazzite přes SteamOS?

SteamOS i Bazzite používají herní režim Steam a sdílejí balíčky mezi sebou, ale co rozdíly pod kapotou?  Bazzite by měl mít většinu funkcí ze SteamOS s herním režimem Steam fungujícím podle plánu.

- Mělo by fungovat téměř stejně jako SteamOS.
  - Nabídka rychlého přístupu (QAM), která je přístupná pomocí tlačítka <kbd>...</kbd> na Steam Decku, je funkční pro TDP, omezení snímkové rychlosti, škálování atd. jako na SteamOS.
  – Stejný populární software třetích stran jako [Decky Loader](https://decky.xyz/), [Emudeck](https://www.emudeck.com/), [RetroDeck](https://retrodeck.net/) atd. by se měl nainstalovat a fungovat správně.
– Sklízení výhod [Fedora Atomic Desktop](https://fedoraproject.org/atomic-desktops/):
  - Vrstvení balíčků Fedory do obrazu bez jejich ztráty mezi aktualizacemi/rebooty.
  - Vrátit aktualizace systému za posledních 90 dní.
  - K dispozici jsou alternativní desktopová prostředí.
- Bazzite obsahuje novější verze základních balíčků než SteamOS, což znamená, že Bazzite je vždy napřed před SteamOS, pokud jde o funkce Steam Gaming Mode a Desktop Mode.
  - Novější aktualizace balíčků včetně linuxového jádra a ovladačů.
  - K regresím může docházet častěji, protože Bazzite upgraduje základní balíčky rychleji než SteamOS.

>Pokud chcete vidět podrobnější srovnání, přečtěte si našeho [**srovnávacího průvodce SteamOS**](/General/SteamOS_Comparison.md).

### Známé problémy

- (Steam Deck OLED) Jas není správně obnoven při změně obnovovací frekvence.
- (Steam Deck OLED) MangoHUD nehlásí takt GPU.