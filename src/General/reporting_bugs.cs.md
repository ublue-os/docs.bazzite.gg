---
title: Report Bugs
---

# Hlášení chyb

## Odešlete hlášení o chybách na příslušné místo

Nahlaste chyby zaznamenané s Bazzite v našem [**sledovači problémů**](https://github.com/ublue-os/bazzite/issues)! Nedoporučujeme hlásit chyby na diskusních fórech, protože zprávy se mohou ztratit nebo je nemusí přispěvatelé Bazzite prohlížet tak často jako nástroj pro sledování problémů.

## **Návod k šabloně vydání Bazzite**

![Hlášení o chybě|690x174](../img/Hlášení_chyby.png)

![Šablona|690x436](../img/Šablona_hlášení chyb.png)

## Před nahlášením aktualizujte Bazzite

Někdy jsou chyby opraveny během upgradů, takže před odesláním hlášení zkuste aktualizovat a restartovat zařízení, abyste zjistili, zda problém přetrvává i mezi aktualizacemi.

>Přečtěte si, jak aktualizovat Bazzite pro vaše zařízení:
>[**Průvodce aktualizací**](../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/updating_guide.md)

## Nezapomeňte připojit systémové protokoly

Otevřete hostitelský terminál a **zadejte**:

```
ujust device-info
```

Připojte odkaz, který vydává pro systémové protokoly.

## Zažít pád systému?

```command
ujust logs-last-boot
```
Zkopírujte výstup do zprávy o chybě.