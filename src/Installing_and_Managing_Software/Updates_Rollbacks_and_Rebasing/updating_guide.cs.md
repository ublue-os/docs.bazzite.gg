---
title: Update Guide
---

# Průvodce aktualizací

![Aktualizace systému|200x200, 100%](../../img/System_Updates.png)

## Aktualizace Bazzite

!!! attention

    Ke správné aktualizaci je nutné mít 3 % bezplatného úložiště z celkového disku, na kterém je Bazzite nainstalován.

Bazzite aktualizuje všechny změny provedené konkrétně v samotném Bazzite, aktualizace ze základních balíčků Fedory upstream, grafické ovladače a uživatelský software nainstalovaný z Bazaaru.

### Obrazy na ploše

- Aktualizace systému probíhají **automaticky denně** podle plánu a když není hardware příliš vytížen, jako je hraní videoher.
    - Na místě je zaškrtnuto, aby se obraz aktualizoval pouze tehdy, když využití procesoru, baterie a RAM splňuje určité požadavky.
- Aktualizace se budou stahovat na pozadí a **budou platit při příštím restartu** a měly by obsahovat nejnovější sestavení Bazzite.
    - Upgrade lze vynutit pomocí nástroje Aktualizace systému podle vlastního uvážení.
- Aktualizuje balíčky upgradu systému, Steam a nainstalované aplikace, pokud jsou k dispozici. 

### Obrazy Bazzite-Deck

- Aktualizace může uživatel spravovat v herním režimu Steam **ručně**.
  – Otevřít: **Nabídka Steam** > **Nastavení** > **Systém** > **Zkontrolovat aktualizace** > **Použít**
    - **Restartujte** pro použití upgradů systému.
- Aktualizuje balíčky upgradu systému, Steam a nainstalované aplikace, pokud jsou k dispozici.

### Příkaz terminálu (ručně upgradovat) [Všechny obrazy):

```command
ujust update
```

## Musím po každé aktualizaci systému okamžitě restartovat?

**Ne**, ale **upgrade systému se uplatní až při příštím restartu**.  Uživatelem nainstalované aplikace přes Bazaar **lze upgradovat bez restartu**.

- **Obrazy na ploše**: Když je vaše zařízení spuštěno, novější aktualizace se budou stále stahovat na pozadí jednou denně a budou čekat na použití, dokud nebude zařízení restartováno.
- **Obrazy Bazzite-Deck**: Aktualizace budou denně kontrolovány a můžete si je stáhnout ve svém volném čase, podobně jako SteamOS zpracovává upgrady.

## Jak zobrazím seznam změn pro každou aktualizaci?

Changelogy pro každý Bazzite lze nalézt na [Github](https://github.com/ublue-os/bazzite/releases).

## Měřená/omezená síťová připojení a datové limity

!!! note
    Toto je nepodporovaná konfigurace, protože se očekává, že aktualizace budou spouštěny denně pro operační systém i aplikace.

Otevřete nastavení systému na ploše a zapněte nastavení týkající se měřeného připojení (datové limity nebo poplatky).  Toto nastavení **pozastaví** automatické aktualizace pro Bazzite.