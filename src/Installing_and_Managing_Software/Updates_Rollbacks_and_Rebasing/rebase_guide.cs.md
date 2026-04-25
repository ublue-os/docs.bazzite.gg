---
title: Rebase Guide
---

# Průvodce rebase

## Co je rebasing?

!!! warning

    Změna základu mezi různými prostředími plochy (např. KDE Plasma na GNOME) **může způsobit problémy** a není **podporována**.

Rebasing umožňuje uživatelům přepnout na jiný obraz **bez** nutnosti opětovné instalace a ztráty osobních souborů a dat aplikací.

>[**Doporučujeme použít nástroj Bazzite Rollback Helper**](./bazzite_rollback_helper.md).

## Scénáře rebase

- Pokud se u nejnovějšího sestavení Bazzite vyskytnou problémy, obnovte základ na konkrétní obrazy starších sestavení za posledních 90 dní.
- Rebase na jiné obrazy Fedora Atomic Desktop včetně jiných obrazů Bazzite.
  - **ne** rebase mezi různými desktopovými prostředími.

## Jak mohu přepínat mezi obrazy Bazzite?

**zadáním tohoto příkazu do hostitelského terminálu** zjistíte, na jakém kanálu nebo sestavení se nacházíte:

```command
rpm-ostree status
```

Zkontrolujte pod "**Deployments:**" a výstup by měl být podobný:
```
 ● ostree-image-signed:docker://ghcr.io/ublue-os/[*image*]:[*channel*]
```

Přepněte na jinou variantu Bazzite zadáním příkazu pro každý konkrétní obraz.

Otevřete terminál a **zadejte**:

```
rpm-ostree rebase <image>
```

### **Příklad**:

!!! warning

    Změna základu mezi různými prostředími plochy (např. KDE Plasma na GNOME) **může způsobit problémy** a není **podporována**.

```command
rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:stable
```

Pro přenastavení na KDE Plasma verzi obrazu Bazzite-Deck.

## Jak změním aktualizační větev Bazzite? (Stabilní, Testovací a Nestabilní)

Pro koncové uživatele jsou určeny dvě aktualizační větve:

- Stabilní (`:stable`)
  - Výchozí větev, která se používá v normálních instalacích Bazzite.
- [Testování (`:testing`)](https://github.com/ublue-os/bazzite/compare/main...testing)
  - Získejte před vydáním přehled budoucích sestavení Bazzite.
  - Často se mohou objevit chyby.
  - Povzbuzeni k rebase zpět na `:stable` po testování hlavní verze.

### Nestabilní větev

Toto je určeno pouze pro hlavní přispěvatele a správce Bazzite a používá se pro velké změny, které vyžadují časté testování. Nestabilní větev může zaostávat za aktualizacemi i ve stabilní větvi, protože testuje konkrétní velké změny a není to něco, co je postaveno podle plánu.

## Přepínání aktualizačních větví v herním režimu Steam
  
Obrazy Bazzite-Deck mohou přepínat větve v `Settings > System > OS Update Channel` v režimu hry Steam.

Pokud jste povolili **kanál pokročilé aktualizace**, objeví se další možnosti. Možnosti mapují následovně:

```
Stable (:stable)
Release Candidate (:testing)
Beta (:testing)
Beta Candidate (:unstable)
Main (:unstable)
```

### **Příklad**:

```command
rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite:testing
```

Pro **testovací** větev na image AMD/Intel Desktop.

## Přenastavení na starší sestavení

!!! attention

    Jakmile budete chtít upgradovat na nejnovější verzi, budete se muset vrátit zpět na `:stable`.

!!! warning

    Přechod na starší sestavení Bazzite nepřinese nové aktualizace, dokud neupgradujete zpět na `:stable`, což znamená, že nebudou existovat žádné aktualizace zabezpečení, dokud nepřejdete zpět do stabilní větve.

Stejně jako při návratu k předchozímu nasazení Bazzite mohou uživatelé také přejít na konkrétní sestavení Bazzite, která byla vytvořena za posledních 90 dní.  Všechna vaše uživatelská data zůstanou nedotčena, ale stejně jako ve výše uvedeném varování budete muset manuálně převést zpět na `:stable`, abyste aktualizovali systém, abyste obdrželi nejnovější sestavení.

Prohlédněte si seznam dostupných stabilních sestavení **zadáním**:

```command
skopeo list-tags docker://ghcr.io/ublue-os/bazzite | grep -- "stable-" | sort -rV
```

Změna na konkrétní sestavení vyžaduje, aby uživatelé otevřeli hostitelský terminál a **zadali**:

```command
rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/IMAGE-NAME:VERSION-YEARMONTHDAY
```

**Příklad**:

```command
rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:39-20240113
```

Pro _Jan. 13. 2024_ sestavení `bazzite-deck` (_Fedora 39_).

<small>_(Upozorňujeme, že toto sestavení již není dostupné, protože překročilo 90denní limit a používá se pouze jako příklad pro tuto dokumentaci.)_</small>