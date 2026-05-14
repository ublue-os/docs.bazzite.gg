# Resetujte zapomenuté uživatelské heslo

!!! important

    Tato metoda je pouze v případě, že jste zapomněli své aktuální uživatelské heslo! Změna aktuálního hesla by měla být provedena prostřednictvím desktopového prostředí.

!!! warning

    Postupujte podle tohoto návodu **podle vlastního uvážení**, protože pokusem o cokoliv z toho můžete rozbít svůj systém.

![Upravte příkaz pro nejnovější zaváděcí položku|690x351](../img/Edit_the_command_for_the_latest_boot_entry.png)

1. Restartujte zařízení.
2. Stisknutím <kbd>Esc</kbd> na klávesnici přejděte do spouštěcí nabídky GRUB.
   A. Pokud stisknete <kbd>Esc</kbd> příliš mnohokrát, můžete skončit s výzvou `grub>`.
   b. Vraťte se do spouštěcí nabídky zadáním `exit` a stisknutím klávesy <kbd>Enter</kbd>
3. Upravte poslední nasazení stisknutím <kbd>E</kbd> na klávesnici.

![Boot with init=/bin/bash|689x359](../img/Boot_with_init_bin_bash.jpeg)

Upravte výzvu GRUB a připojte `init=/bin/bash` na řádek začínající `linux`.

![Reboot|689x359](../img/Reset_Password_Reboot.jpeg)

Pokračujte v zavádění pomocí <kbd>Ctrl</kbd>+<kbd>X</kbd>

Jakmile jste v příkazovém řádku GRUB:

1. Dočasně připojte SELinux

   `mount -t selinuxfs selinuxfs /sys/fs/selinux`

2. Načtěte zásady SELinux

   `/sbin/load_policy`

3. Zadejte své nové heslo (např. `passwd bazzite`)

   `passwd [INSERT USERNAME HERE]`

4. Synchronizace

   `sync`

5. Restartujte

   `/sbin/reboot -ff`

![Příkazy|690x334](../img/Reset_Password_Commands.png)

Vaše uživatelské heslo by nyní mělo být resetováno.

> Děkujeme [Colinu Waltersovi](https://github.com/cgwalters) za [řešení](https://github.com/ublue-os/main/issues/469#issuecomment-1885264886).

## Nefunguje?

Mnoho uživatelů zapomíná kroky týkající se SELinuxu kvůli starým zvykům. Pokud jste vytvořili vše kromě výše uvedených kroků SELinux, pak bude soubor `/etc/shadow` nečitelný nebo nedostupný jakýmkoli procesem.

Dobrým způsobem, jak zkontrolovat, zda je `/etc/shadow` ve špatné konfiguraci SELinux, je provést následující příkaz:

`ls -Z /etc/shadow`

![ls -Z /etc/shadow|690x334](../img/Unlabeled_Etc_Shadow.png)

Měli byste si také všimnout _unlabeled_t_ na vaší straně.
Nyní musíte opravit štítek na `/etc/shadow` příkazem níže:

`restorecon -v /etc/shadow`

A pak znovu zkontrolujte výsledek pomocí `ls -Z /etc/shadow`, což by mělo vést k:

`system_u:object_r:shadow_t:s0   /etc/shadow`

Nyní je systém připraven a můžete jej restartovat pomocí `/sbin/reboot -ff`.