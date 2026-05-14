---
title: Updates, Rollbacks, and Rebasing
---

# Aktualizace, vrácení změn a znovuzaložení

## Aktualizace

Aktualizace jsou automatické u obrazů Desktop a ručně se provádějí u obrazů Bazzite-Deck a obě varianty Bazzite upgradují vše na úrovni systému i aplikací nainstalovaných uživatelem během procesu aktualizace.

> [**Průvodce aktualizací**](./updating_guide.md)

## Vrácení zpět

Pokud po aktualizaci přes nabídku GRUB nebo příkaz `rpm-ostree rollback` dojde k závažným problémům, přejděte zpět na předchozí aktualizaci systému.

> [**Průvodce vrácením změn**](./rolling_back_system_updates.md)

## Rebasing

!!! important

    **ne** přestavujte na jiné desktopové prostředí, než jaké právě používáte, místo toho zálohujte a přeinstalujte.

Rebase to Bazzite builds z posledních 90 dnů, změna Bazzite aktualizačních kanálů, přepínání mezi obrazy Desktop a Bazzite-Deck, nebo úplně přejít na jiný obraz Fedora Atomic Desktop.

> [**Rebase Guide**](./rebase_guide.md)

## Pomocný nástroj Bazzite Rollback Helper

Pomůcka pro pomoc s návratem ke starším obrazům Bazzite, změnou větví aktualizací nebo přepnutím na jiný obraz Bazzite.

> [**Průvodce nástrojem Rollback Helper**](./bazzite_rollback_helper.md)