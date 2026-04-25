---
title: Rollbacks
---

# Vrácení zpět

## Rolling Back Upgrade

Pokud se po aktualizaci prostřednictvím nabídky GRUB nebo příkazu `rpm-ostree rollback` nebo pomocí Bazzite Rollback Helper vyskytnou závažné problémy, přejděte zpět na předchozí aktualizaci systému.

## Jak vrátím aktualizaci systému?

Návrat k předchozímu nasazení systému lze provést **zadáním tohoto příkazu do hostitelského terminálu**:

```command
rpm-ostree rollback
```

### Použití nástroje Bazzite Rollback Helper (`brh`).

Vraťte se zpět ke staršímu obrazu Bazzite za posledních 90 dní pomocí **[příkazu `brh`](../Updates_Rollbacks_and_Rebasing/bazzite_rollback_helper.md)**.

### Před spuštěním Bazzite (GRUB)

![Nabídka GRUB|690x402](../../img/GRUB_Menu.png)

!!! note

    Ovládací prvky se mohou lišit v závislosti na různých kapesních počítačích nebo nastaveních HTPC pro navigaci v nabídce a pro návrat do GRUB může být vyžadována externí fyzická klávesnice.

Vrácení zpět lze také provést v nabídce GRUB (která se zobrazí před zavedením do Bazzite) výběrem předchozí položky spouštění před zavedením na plochu. Zobrazuje vaše aktuální (`:0`) a vaše předchozí (`:1`) nasazení. Vaše osobní soubory to **nebude** ovlivněno a po návratu můžete stále aktualizovat na nejnovější verze.

## Jak uložím své **aktuální** nasazení?

Své **aktuální** nasazení můžete připnout pomocí tohoto **příkazu**:

```command
sudo ostree admin pin 0
```

V hostitelském terminálu pro záložní stav uložení vašeho **aktuálního** nasazení, ke kterému se můžete vrátit, pokud nová aktualizace systému způsobí problémy.

## Jak uložím své **předchozí** nasazení?

Své **předchozí** nasazení můžete připnout pomocí tohoto **příkazu**:

```command
sudo ostree admin pin 1
```

V hostitelském terminálu pro záložní stav uložení vašeho **předchozího** nasazení pro vrácení zpět, pokud má aktuální nasazení problémy.

## Jak mohu uvolnit nasazení, pokud jsem ho uložil?

Odepnout uložené **aktuální** nasazení:

```command
sudo ostree admin pin --unpin 0
```

Odepnout uložené **předchozí** nasazení:

```command
sudo ostree admin pin --unpin 1
```

Zobrazit všechna čísla indexů nasazení:

```command
rpm-ostree status -v
```

Odepnout **uložené** nasazení:

```command
sudo ostree admin pin --unpin <index number>
```

## Downgrady aktualizace aplikace

Přečtěte si o předinstalované aplikaci Warehouse pro downgrade aplikací v [**dokumentaci Bazaar App Store (Flatpak)**](/Installing_and_Managing_Software/Flatpak.md#warehouse).