---
title: Comparison of Bazzite and SteamOS
---

# Srovnání Bazzite a SteamOS

## Co je SteamOS?

**SteamOS** je operační systém původně navržený pro Steam Deck. SteamOS je operační systém pro klienta Steam a také obsahuje základní desktopové prostředí s **KDE Plasma**, které uživatelům umožňuje např. instalovat mody a emulátory, ale může být omezeno pro použití na desktopu.

## Co je to Bazzite?

Bazzite je komunitně řízený linuxový herní operační systém, který obsahuje nejnovější ovladače pro Linux a různé varianty (**Desktop (Bazzite)**, **Handheld/HTPC (Bazzite-Deck)** a **Developer eXperience (Bazzite-DX)**). Je založen na [**Fedora Linux**](https://fedoraproject.org/) a obsahuje [**atomový aktualizační systém**](https://github.com/bootc-dev/bootc), který zajišťuje, že předchozí aktualizace bude vždy k dispozici, pokud se něco pokazí.

Je také navržen pro každodenní používání se zaměřením na **hry**, **multimédia** a **vývoj**.  Navíc, protože Bazzite dodává nejnovější ovladače, můžete si být jisti, že pokud vaše zařízení může fungovat na Linuxu, bude fungovat i v Bazzite.  Bazzite podporuje GPU **AMD**, nejnovější **Nvidia** a **Intel**. Bazzite také dobře funguje pro kapesní zařízení **Lenovo**, **Asus**, **Ayn**, **GPD** a **OneXPlayer**.

### Extra vylepšení na Bazzite ve srovnání se SteamOS

- Vynikající podpora **dual-boot** s **Windows**.
- Funguje na **většině** kapesních počítačů založených na x86: Lenovo Legion Go/S, ASUS ROG Ally/X, varianty OneXPlayer F1/G1/X1, GPD Win 4/Mini/Max, Ayn Loki, MSI Claw 1st Gen AI7+/8+, Zotac Zone, Ayaneo Steck Air/Geek LCD/OLENext Deck/Geek
- Podpora pro ladění desktopových GPU a ventilátorů.
- **Fearless Update**
  - Vždy máte přístup k **předchozí verzi** prostřednictvím bootloaderu.
  - U kapesních počítačů se Bazzite automaticky vrátí zpět na předchozí verzi po 3 neúspěšných spuštěních.
  - K dispozici jsou **aktualizace za posledních 90 dní** a můžete se snadno vrátit k jakékoli verzi pomocí jednoduchého příkazu nebo prostřednictvím Handheld Daemon.
- Dodává **nejnovější dostupný software** včetně **linuxového jádra**, **grafických ovladačů** a [**Gamescope**](https://github.com/ValveSoftware/gamescope).
- Užitečný **software související s hraním**, jako je **Lutris, Umu-Launcher, ProtonUp-QT, Protontricks** a další.
- Přístup do prostředí **GNOME** jako alternativa k KDE Plasma.
- Po vybalení podpora pro **virtualizaci** a **průchod GPU**.
- **Aplikace pro Android** lze nainstalovat pomocí [Waydroid](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md).
- **Sunshine** je předinstalovaný, což vám umožní snadno streamovat vaše hry.
- [`ujust`](/Installing_and_Managing_Software/ujust.md) praktické skripty pro nastavení softwaru a vylepšení, jako je bezpečné spouštění a další software.
- Používá formát disku **BTRFS** s **deduplikací** a **kompresí** (SteamOS používá **Ext4**) a podporuje **automatické připojení** jak pro **interní disky**, tak pro **SD ​​karty**.

### Každodenní používání

- Systémové balíčky jsou často aktualizovány.
- Wayland se používá v režimu plochy, což zajišťuje správné škálování pro displeje s vysokým DPI.
- Většina balíčků pro stolní počítače se řídí životním cyklem Fedory, s výjimkou případů, kdy existuje chyba, kdy je balíček selektivně zadržen nebo opraven dříve než Fedora.

### Pro vývojáře

- Přístup k více správcům balíčků a úložištím v kontejnerech pomocí [Distrobox](https://distrobox.it).
- [Homebrew](https://brew.sh/) je předinstalovaný pro balíčky příkazového řádku.
- [Layer](/Installing_and_Managing_Software/rpm-ostree.md) Balíčky Fedory do systému, které přežijí mezi aktualizacemi systému.
– Další informace naleznete v části [Vývoj](https://dev.bazzite.gg).

### Vylepšení zabezpečení

Bazzite podporuje LUKS Disk Encryption, Secure Boot a TPM odemknutí šifrovaného disku. Bazzite má také [SELinux (Security Enhanced Linux)](https://www.redhat.com/en/topics/linux/what-is-selinux) povolený a předkonfigurovaný ve výchozím nastavení.

Podpora Secure Boot je také užitečná pro duální spouštění se systémem Windows, protože je vyžadována pro určitý software proti cheatům. Další informace naleznete v [**Příručce bezpečného spouštění**](/General/Installation_Guide/secure_boot.md).