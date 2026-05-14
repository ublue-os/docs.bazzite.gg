---
title: Common Gaming Issues
---

# Běžné problémy s hraním

### Nativní port pro Linux versus verze pro Windows

Některé linuxové porty mohou mít chybějící funkce nebo horší výkon než na verzi Windows běžící přes Proton. Existují však scénáře, kdy je použití výhradně nativního portu vaší jedinou možností a může být dokonce žádoucí.  

Pokud se nativní hra pro Linux nespustí, vynuťte vrstvu kompatibility **Legacy Runtime** tak, že přejdete do **vlastností hry** a vyberete „**Kompatibilita**“ a poté zaškrtnete „**Vynutit použití konkrétního nástroje kompatibility Steam Play**“ a vyberete jej.

### Zamykání her přes Denuvo Anti-Tamper DRM

Hry, které používají Denuvo Anti-Tamper DRM, považují změnu verze Protonu za aktivaci hry na jiném hardwaru, což může způsobit, že se ze hry dostanete, pokud změníte verzi Protonu více než 5krát během 24 hodin.

## Chyby zvuku a vlastního obsahu zdroje 1

!!! note

    To platí pouze pro konkrétní hry běžící na [zdrojovém enginu](https://www.pcgamingwiki.com/wiki/Engine:Source).

!!! attention

    **Nezkoušejte postupovat podle tohoto řešení, dokud nenarazíte na problémy se zvukem nebo na konkrétní scénář uvedený níže ohledně _Left 4 Dead 2_.**

Chybí hlasové linky nebo se nenačítá vlastní obsah ve hrách Source? SELinux blokuje dekódování MP3 a další middleware, protože [**spouští kód v haldové paměti**](https://github.com/ValveSoftware/steam-for-linux/issues/43).

Bylo také potvrzeno, že to způsobuje problémy s připojením a hostováním vlastních map v _Left 4 Dead 2_.

### Oprava problémů se zvukem/vlastním obsahem:

!!! warning

    Konfigurace SELinuxu je určena pro pokročilé uživatele a pokud je používána nezodpovědně, může rozbít ostatní komponenty ve vašem systému a oslabit zabezpečení vašeho zařízení.

Otevřete hostitelský terminál a **zadejte tyto 4 příkazy na vlastní nebezpečí**:

```command
sudo su
```

```command
cd /tmp
```

```command
ausearch -c 'hl2_linux' --raw | audit2allow -M my-hl2linux
```

```command
semodule -X 300 -i my-hl2linux.pp
```

Restartujte zařízení a otestujte, zda má hra Source stále problémy.

### Vrácení této změny:

**Zakažte nebo odeberte modul.**

#### Zakázat změnu:

```command
semodule -X 300 -d my-hl2linux
```

##### Odebrat a smazat změnu:

```command
semodule -X 300 -r my-hl2linux
```

Soubor `.pp` by měl být v souboru `/root`, pokud jej chcete odstranit.

## Hry na Steamu se nespouštějí

Hry na Steamu se nemusí spustit z různých důvodů.

### Shromažďování souborů protokolu Steam:

Pokud narazíte na problémy se spuštěním hry na Steamu:

1. Otevřete vlastnosti hry a **zadejte tuto možnost spuštění**:
   `PROTON_LOG=1 %command%`

2. Spusťte hru

Ve vašem domovském adresáři by se měl objevit soubor protokolu pojmenovaný podle ID aplikace hry.

### Problémy s oprávněním k jednotce naformátované na NTFS:

Ujistěte se, že vaše hry **nejsou** na oddílu NTFS (Windows). Další informace naleznete [**zde**](./Hardware_compatibility_for_gaming.md#unsupported-filesystems-for-secondary-drives).

### WINE pro více uživatelů:

!!! note

    Bazzite-Deck nepodporuje více uživatelských účtů Linuxu, tyto informace se týkají pouze desktopové edice Bazzite.

Někdy hry Steam zcela odmítnou spustit na sekundárním uživatelském účtu. To může být způsobeno vlastnictvím souborů s předponou WINE. V ` ~/.local/share/Steam/logs/console-linux.txt ` na sekundárním uživatelském účtu se může zobrazit podobná chyba:

```
wineserver: /SteamLibrary/steamapps/compatdata/377160/pfx is not owned by you
```

Můžete to opravit vytvořením samostatné složky knihovny Steam, která bude obsahovat data prefixu pro Proton, a vytvořením symbolického odkazu (_symlink_) pro ostatní složky (jako jsou běžná herní data).

```
USER2@bazzite: /mnt/ExtraStuff/USER2SteamLibrary/steamapps$ ls -la
total 32
drwxrwxr-x. 3 USER2 steamplayers 4096 Jan 29 15:19 .
drwxrwsr-x. 3 USER2 steamplayers 4096 Jan 29 16:13 ..
-rwxr-xr-x. 1 USER2 USER2         2287 Jan 29 15:19 appmanifest_377160.acf
lrwxrwxrwx. 1 USER2 USER2           51 Jan 29 15:10 common -> /mnt/ExtraStuff/USER1SteamLibrary/steamapps/common/
drwxr-xr-x. 3 USER2 USER2         4096 Jan 29 15:13 compatdata
lrwxrwxrwx. 1 USER2 USER2           56 Jan 29 15:12 shadercache -> /mnt/ExtraStuff/USER1SteamLibrary/steamapps/shadercache/
lrwxrwxrwx. 1 USER2 USER2           49 Jan 29 15:12 temp
lrwxrwxrwx. 1 USER2 USER2           53 Jan 29 15:12 workshop
```

Podobně zkopírujte nebo symbolicky propojte soubory appmanifest z každé knihovny, aby se hry správně zobrazovaly v každé knihovně Steam.