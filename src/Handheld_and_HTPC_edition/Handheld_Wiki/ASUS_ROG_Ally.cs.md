---
title: ASUS Handhelds
---

# Kapesní počítače ASUS

!!! disclaimer

    Tato wiki může obsahovat zastaralé informace.

## ASUS ROG Ally / ASUS ROG Ally X

![ally|603x500, 100%](../../img/ally.png)

### Obecné poznámky

- Podržením tlačítka Armory Crate (na boku) můžete přepnout do režimu myši
- Povolte nastavení Steam Power Button Handler v Handheld Daemon

### Volitelné vylepšení

- Upravte nastavení v Handheld Daemon.
- Upravte měřítko uživatelského rozhraní v Nastavení zobrazení.

### Známé problémy
- Změna napájení A/C někdy vede k zaseknutí TDP.
- Někteří uživatelé hlásí, že zvuk mikrofonu je zkomolený
  - Řešením je nastavit v nastavení hlasitost mikrofonu/vstupu na 10%-15%.
  - Pro Discord musíte také nastavit vstupní profil v nastavení Discord na zrušení hlasu.
- (Pouze Xbox Ally) Zvuk se přepíná z levého do pravého interního reproduktoru jako mono.
  - Toto je známý problém, který by měl být opraven v jádře 6.19
- Někteří uživatelé hlásí, že "Auto UMA" v biosu může způsobit pády v některých hrách.
  - Pokud se s tím setkáte, zkuste nastavit VRAM v biosu na **4 GB** nebo **8 GB**.
- Indikátor LED je ve výchozím nastavení na maximální jas a nelze jej změnit na žádném jiném operačním systému mimo Windows.
  - To souvisí s firmwarem.
  - To také ovlivňuje, kdy se spojenec nabíjí a spí.
- Ally **nepodporuje** držení tlačítka pro tlačítka Steam nebo QAM.
  - Steam Input ve výchozím nastavení nefungují.
    - Záměna tlačítka (tlačítek) Start/Select je řešením.
- Pozastavení se může přerušit, pokud je zakázáno SMT
- Ovladač otisků prstů nefunguje.
- Úložiště zobrazuje duplicitní disky.
  - Toto je vizuální chyba, **ne** pokuste se tuto jednotku formátovat!
- Zapnutí animace probuzení při probuzení z režimu spánku způsobí, že zařízení bude fungovat nepravidelně.
  - Žádné ovládací prvky mimo Steam.
  - Chybí horní a spodní panel Steamu.

#### Zvýšit CPU?

Ve výchozím nastavení zakázáno, aby se zabránilo nadměrnému odběru energie do zařízení.

Další informace o tom naleznete [**zde**](https://github.com/aarron-lee/SimpleDeckyTDP/blob/main/README.md#are-there-cpu-boost-controls).