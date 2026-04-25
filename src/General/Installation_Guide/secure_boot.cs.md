---
title: Secure Boot Guide
tags:
  -  QR
search:
  exclude: true
---

# Průvodce bezpečným spouštěním

## Bazzite podporuje bezpečné spouštění

!!! note

    Klikněte na „Pokračovat ve spouštění“, pokud vaše zařízení nepodporuje zabezpečené spouštění nebo jej nechcete povolit.

!!! important

    Výzva k registraci používá anglické rozložení klávesnice QWERTY bez rozdílu od vaší skutečné hardwarové klávesnice. Jiná rozložení proto mohou kolidovat se znaky hesla (tj. `A` a `Q` jsou na rozloženích AZERTY zaměněny).

Bazzite podporuje Secure Boot, ale pro jeho použití je nutné zaregistrovat klíč Universal Blue, jinak ponecháte Secure Boot zapnutou v BIOSu, Bazzite se nespustí.

## Důležité poznámky k bezpečnému spouštění:

- Zadáním hesla se z bezpečnostních důvodů zaregistrují neviditelné znaky, takže neuvidíte, co píšete!
- Aktualizace BIOSu může znovu povolit Secure Boot a možná budete muset po aktualizaci postupovat podle **"Metody B"**, abyste vyřešili černou obrazovku při zavádění, která si stěžovala na načtení jádra jako prvního.
- Steam Deck **není** dodáván s povoleným bezpečným spouštěním a nedodává se s žádnými klíči zaregistrovanými ve výchozím nastavení, nepovolujte Secure Boot na vašem Steam Deck, pokud absolutně nevíte, co děláte.

## Chybová zpráva (pokud klíč **není** správně zaregistrován):

```
error: ../../grub-core/kern/efi/sb.c:182:bad shim signature.
error: ../../grub-core/loader/1389/efi/linux.c:256:you need to load the kernel first.

Press any key to continue...
```

Chcete-li to vyřešit, postupujte podle **metody B** níže, a pokud na ni narazíte, přejděte přes chybovou zprávu.

### **Metoda A** - Během způsobu instalace

![Nabídka bezpečného spouštění: Pokračovat ve spouštění / Zapsat MOK / Zapsat klíč z disku / Zapsat hash z disku|200x102, 100%](../../img/Secure_Boot.png 'Zabezpečené spouštění')

!!! note

    Tato obrazovka se objeví také při příštím spouštění, pokud povolíte zabezpečené spouštění, pokud bylo během instalace zakázáno.

Po opuštění instalačního programu Bazzite se objeví modrá obrazovka s možností zaregistrovat podepsané klíče.

`Enroll MOK`, pokud máte povoleno bezpečné spouštění. Pokud budete vyzváni k zadání hesla, **zadejte**:

```command
universalblue
```

V opačném případě `Continue boot`, pokud máte zakázáno Secure Boot nebo pokud není podporováno vaším hardwarem.

## **Metoda B** – Metoda po instalaci

**Před pokračováním v BIOSu zakažte Secure Boot** a poté jej znovu povolte **po registraci klíče**.

Pokud jste již Bazzite nainstalovali, pak **zadejte tento příkaz do hostitelského terminálu**:

```
ujust enroll-secure-boot-key
```

Pokud budete vyzváni k registraci požadovaného klíče, **zadejte heslo do hostitelského terminálu**:

```command
universalblue
```

**Zabezpečené spouštění můžete nyní znovu zapnout v systému BIOS.**
Pomocí následujícího příkazu nabootujete přímo do systému BIOS (pokud je podporován):

```command
ujust bios
```
## Dokončete registraci MOK při spuštění

Při příštím spuštění uvidíte modrou obrazovku MokManager:

1. Zvolte **Zapsat MOK**.
2. Až budete vyzváni k zadání hesla, zadejte:
    ```command
    universalblue
    ```

Po restartu je klíč zaregistrován a Secure Boot může zůstat povolený. Váš systém by se nyní měl normálně spustit pod Secure Boot.