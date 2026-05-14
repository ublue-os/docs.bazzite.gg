---
title: Booting Into Rescue and Emergency Modes
---

# Zavedení do záchranného a nouzového režimu

## Předmluva

Fedora již má vestavěný mechanismus (poskytovaný `systemd`) pro zavádění do záchranných/nouzových režimů.

Fedora (a tedy systémy Universal Blue) však během instalace nenastavují heslo `root`. Když je tedy dosaženo nouzového nebo záchranného režimu, uživateli se zobrazí chyba:

```
Cannot open access to console, the root account is locked.
```

??? note "Vylepšili jsme situaci pro všechny deriváty _Universal Blue_ pomocí inspirace z _Fedora CoreOS_."

    Nyní, když spouštíte systém do [nouzového](#booting-to-emergency-mode) nebo [rescue](#booting-to-rescue-mode) s uzamčeným účtem root, je uživateli namísto toho nabídnuta standardnější výzva:

```
Press Enter for maintenance
(or press Control-D to continue):
```

V tomto okamžiku stisknutím <kbd>Enter</kbd> přesunete uživatele do příslušného kořenového shellu. SELinux bude také aktivní v tomto režimu (pokud nebyl deaktivován jinou konfigurací), takže je to dobrý režim, který lze použít, pokud potřebujete resetovat heslo atd.

Další podrobnosti naleznete níže:

---

## Zavedení do nouzového režimu

Nouzový režim poskytuje minimální možné prostředí a umožňuje vám opravit váš systém i v situacích, kdy systém není schopen vstoupit do záchranného režimu. V nouzovém režimu systém připojí souborový systém `root` pouze pro čtení, nepokouší se připojit žádné jiné lokální souborové systémy, neaktivuje síťová rozhraní a spouští pouze několik základních služeb.

1. Stisknutím <kbd>Esc</kbd> na klávesnici přejděte do spouštěcí nabídky GRUB.
   A. Pokud stisknete <kbd>Esc</kbd> příliš mnohokrát, můžete skončit s výzvou `grub>`.
   b. Vraťte se do spouštěcí nabídky zadáním `exit` a stisknutím klávesy <kbd>Enter</kbd>
2. Vyberte požadované nasazení (horní položka je obecně správná) a upravte jej stisknutím <kbd>E</kbd> na klávesnici.
3. Šipkou dolů přejděte na řádek začínající `linux` a stisknutím <kbd>Ctrl</kbd>+<kbd>E</kbd> přejděte na konec řádku.
4. Na konec řádku přidejte slovo `emergency`.
   A. Ujistěte se, že mezi `emergency` a již existujícím textem je mezera.
   b. Místo `emergency` lze přidat ekvivalentní parametry `-b` a `systemd.unit=emergency.target`.
5. Stisknutím kláves <kbd>Ctrl</kbd>+<kbd>X</kbd> spusťte systém.

---

## Zavedení do záchranného režimu

Záchranný režim poskytuje pohodlné prostředí pro jednoho uživatele a umožňuje vám opravit váš systém v situacích, kdy není schopen dokončit běžný proces zavádění. V záchranném režimu se systém pokusí připojit všechny lokální souborové systémy a spustit některé důležité systémové služby, ale neaktivuje síťová rozhraní ani neumožní přihlášení více uživatelů do systému současně. Ve Fedoře je záchranný režim ekvivalentní režimu pro jednoho uživatele.

1. Stisknutím <kbd>Esc</kbd> na klávesnici přejděte do spouštěcí nabídky GRUB.
   A. Pokud stisknete <kbd>Esc</kbd> příliš mnohokrát, můžete skončit s výzvou `grub>`.
   b. Vraťte se do spouštěcí nabídky zadáním `exit` a stisknutím klávesy <kbd>Enter</kbd>
2. Vyberte požadované nasazení (horní položka je obecně správná) a upravte jej stisknutím <kbd>E</kbd> na klávesnici.
3. Šipkou dolů přejděte na řádek začínající `linux` a stisknutím <kbd>Ctrl</kbd>+<kbd>E</kbd> přejděte na konec řádku.
4. Na konec řádku přidejte slovo `single`.
   A. Ujistěte se, že mezi `single` a již existujícím textem je mezera.
   b. Místo `single` lze přidat ekvivalentní parametry `1`, `s`, `S` a `systemd.unit=rescue.target`.
5. Stisknutím kláves <kbd>Ctrl</kbd>+<kbd>X</kbd> spusťte systém.

---

## Root shell bez hesla! Jak to může být bezpečné?

Toto vylepšení je implementováno tak, že uživatel musí mít možnost upravovat příkazový řádek jádra. Pokud je váš bootloader (např. GRUB) nakonfigurován s heslem, které uživatelům brání v úpravě příkazového řádku jádra, nebude povoleno obcházení hesla pro uzamčený účet root. To je obzvláště důležité, protože režim `emergency` lze dosáhnout, když kontrola souborového systému selže při zavádění, nejen když je zadáno na příkazovém řádku jádra.

Vzhledem k této ochraně je tato vylepšená záchranná a nouzová metoda stejně bezpečná jako nastavení `init=/bin/bash` atd. Navíc je méně pravděpodobné, že uživatel touto metodou poškodí štítky SELinux.

---

## Resetovat zapomenuté uživatelské heslo

Zapomněli jste uživatelské heslo pro přihlášení?  Přečtěte si [Dokumentaci Fedory](https://docs.fedoraproject.org/en-US/fedora-silverblue/troubleshooting/#_resetting_passwords_in_rescue_mode) na toto téma.  Pamatujte, že výchozí heslo pro všechny nové instalace Bazzite je "**bazzite**", pokud jste je nenastavili během instalace.