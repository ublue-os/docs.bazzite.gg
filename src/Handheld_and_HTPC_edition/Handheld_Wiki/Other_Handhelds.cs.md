---
title: Other Handhelds
---

# Další kapesní počítače

![generický handheld|348x158, 100%](../../img/generic_handheld.jpeg)

## Netestované kapesní počítače

!!! note

    U některých handheldů bylo potvrzeno, že spouštějí Bazzite, ale trpí chybějící podporou ovladačů pro Linux včetně chybějících zvukových ovladačů.

Netestované handheldy _by mohly fungovat_ s Bazzite, ale mohou se vyskytnout závažné problémy, které nejsou zdokumentovány.  Váš počet najetých kilometrů se může lišit v závislosti na netestovaném hardwaru. 

Bazzite **nemá** požadované nastavení pro jiné kapesní počítače, takže nastavení bude ručně provádět koncový uživatel pro různé funkce, pokud dokonce funguje správně na nepodporovaném zařízení.

### Nastavení HHD (pokud není na zařízení ve výchozím nastavení povoleno)

**Příkazy pro funkční HHD**:

```command
systemctl start hhd@yourusername
```

```command
systemctl enable hhd@yourusername
```

!!! important
    Nahraďte `yourusername` svým uživatelským jménem Bazzite.