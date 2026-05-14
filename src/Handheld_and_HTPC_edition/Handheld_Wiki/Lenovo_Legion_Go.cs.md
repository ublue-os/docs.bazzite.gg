---
title: Lenovo Handhelds
---

# Handheldy Lenovo

!!! disclaimer

    Tato wiki může obsahovat zastaralé informace.

## Lenovo Legion Go

![legion_go|690x387, 100%](../../img/legion_go.jpeg)

### Volitelné vylepšení
- Nakonfigurujte překrytí HHD jeho otevřením pomocí <kbd>Legion R</kbd>
- Upravte měřítko uživatelského rozhraní v Nastavení zobrazení

### Známé problémy

- Překrytí výkonu může hlásit nepřesnou spotřebu energie.
- Adaptivní/automatický jas displeje je momentálně nefunkční.
  - Ruční posuvník jasu v uživatelském rozhraní Steam funguje bez problémů.
- Firmware systému BIOS a řadiče **doporučujeme** aktualizovat v systému Windows.

### Aktualizace systému BIOS přeruší klíč Secure Boot

![secure-boot|603x500, 100%](../../img/secure-boot.png)

Přečtěte si naši [Průvodce bezpečným spouštěním](/General/Installation_Guide/secure_boot.md#method-b-after-installation-method) a znovu zaregistrujte klíč po aktualizaci systému BIOS, pokud ponecháte funkci Secure Boot povolenou, což je výchozí nastavení pro toto zařízení.

!!! info

    Od července 2025 fungují externí monitory dobře. Externí displej lze nastavit na příslušné nativní rozlišení a obnovovací frekvenci.

    ![legion-go-ext-display|690x387, 100%](../../img/legion_go_ext_display.jpeg)

    Bez dalších oprav nabízí interní displej pouze své nativní rozlišení se správným poměrem stran. Lze zvolit jiná rozlišení, ale většina obrazovky zůstane prázdná.

    ![legion-go-resolutions|690x387, 100%](../../img/legion_go_resolutions.png)
    ![legion-go-int-display-alternative-resolution|690x387, 100%](../../img/legion_go_int_display_alternative_resolution.jpg)



Pokud vaše obrazovka nezobrazuje správný výstup nebo vypadá zrnitě, hlučně nebo zvláštně barevně, budete muset **vstoupit do [TTY session](/Handheld_and_HTPC_edition/quirks.md#tty-if-you-cannot-access-desktop-mode) a zadat tento příkaz**:

```
rm ~/.config/kwin*
```

Případně do něj **ssh a zadejte tento příkaz**:

```
mv ~/.config/kwinoutputconfig.json ~/.config/kwinoutputconfig.json.old
```

## Externí zdroj

Další informace najdete v [Průvodci tipy a triky Legion Go](https://github.com/aarron-lee/legion-go-tricks), který obsahuje užitečné skripty pro tento kapesní počítač.