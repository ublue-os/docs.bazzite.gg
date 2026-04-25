---
title: Installing Bazzite on Steam Deck Hardware
tags:
  -  Obsolete
search:
  exclude: true
---

# Instalace Bazzite na hardware Steam Deck

![image|690x332](../../img/image.jpeg)

!!! note
      
      Tato instalační příručka je pro **starší ISO** a aktualizovaná příručka pro nové ISO bude brzy k dispozici.

## Bazzite na Steam Deck

### Stav

Bazzite funguje správně na modelech Steam Deck LCD a Steam Deck OLED.

<hr>

## Předinstalace

> Předpoklady a kroky před instalací Bazzite.

#### Požadavky na instalaci

!!! note

    Bazzite vyžaduje stabilní připojení k internetu bez omezení šířky pásma.

{% include 'installer_requirements.md' %}
- Volitelné: Fyzická klávesnice (bez jedné bude vaše uživatelské jméno `bazzite` a heslo `bazzite`)

{% include 'desktop_envs.md' %}

!!! warning

    XHCI musí být nastaven jako režim USB pro Steam Deck, aby se naše ISO spustilo! Pokud je nastaveno na DRD, změňte jej v nastavení BIOSu.
    Více informací naleznete [zde](https://github.com/ublue-os/bazzite/issues/808#issuecomment-1963141866).

<hr>

## Průvodce instalací

> Část průvodce, která vyžaduje největší úsilí.

### 1. Stáhněte si a flashujte Bazzite

- Stáhněte si [Bazzite](https://download.bazzite.gg) po výběru Steam Deck ISO pomocí našeho nástroje Image Picker.
- Flash Bazzite na zaváděcí médium.
- Vysunout pohon.

### 2. Zavedení instalačního média

Hold the 'Volume Down' (<kbd>-</kbd>) button and click the Power Button, and when you hear the chime, let go of both buttons, and you'll be booted into the Boot Manager.

Když se dostanete do spouštěcí nabídky, vyberte spouštěcí zařízení pro zavedení instalačního programu Bazzite.

### 3. Instalační program

!!! note "Instalace bez klávesnice"

    If you do not have a usb physical keyboard connected, do **NOT** press "_User Creation_", since it will remove the default username and password, and you will be unable to type a username or password without a physical keyboard.

    **výchozí uživatel**: `bazzite`
    **výchozí heslo**: `bazzite`

![Instalační program|690x348](../../img/uHKqd8F4nxZryfP8ebBz1DIbNVv.png)

<!--![Installer](../../img/zfpz6EXcBqQ6jxho1O9jLLSRUE9.png)-->

![Automatická konfigurace disku|690x497, 75%](../../img/anaconda_drive_configuration.png)

![Příklad uživatelského nastavení|690x359, 75%](../../img/anaconda_user_setup.png)

- Vyberte jazyk, region, rozložení klávesnice a časové pásmo.
- Vyberte jednotku, na kterou bude Bazzite nainstalován.
  - Odstraňte všechny oddíly, které vám na disku zůstaly.
  - Doporučuje se použít konfiguraci automatického úložiště.
- V případě potřeby můžete disk zašifrovat heslem.
  - **Pokud toto heslo ztratíte, nelze ho dešifrovat**.
  - **K ODEMKNUTÍ ZAŘÍZENÍ JE VYŽADOVÁNA FYZICKÁ KABELOVÁ KLÁVESNICE!**
- Nastavení uživatelského účtu. (Pokud nemáte fyzickou, přeskočte tento krok a zahajte instalaci)
  - Poskytněte administrátorská oprávnění a **nastavte uživatelské heslo**.
- Zahajte instalaci.
- Po dokončení instalace restartujte zařízení.

## Po instalaci

> Jemné doladění před hraním.

### Nabídka GRUB

![Rollbacks|690x402, 50%](../../img/GRUB_Menu.png)

Při prvním spuštění se zobrazí obrazovka s aktuálním a posledním nasazením. Je důležité poznamenat, že nabídku GRUB lze použít k vrácení zpět nasazení Bazzite, pokud narazíte na problémy.

Přečtěte si o tom více v [dokumentaci k aktualizacím, vrácení změn a rebasingu](../../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md).

### Přihlaste se do služby Steam a restartujte zařízení

Přihlaste se do služby Steam a poté **restartujte** zařízení, až dokončíte nastavení zařízení během procesu prvního spouštění.

#### Nastavení herního režimu Steam

![Nastavení herního režimu|690x442, 50%](../../img/pLvHB1NAMlb3ghsR72q7l9Auj8B.jpeg)

Po dokončení všech výše uvedených kroků bude vaše další spuštění v herním režimu Steam, který vyžaduje další nastavení pro Steam.

> [Přečtěte si další informace o herním režimu Steam][Steam_Gaming_Mode]

### Konfigurace nastavení systému pro KDE Plasma a GNOME

![Nastavení zobrazení (KDE Plasma)|690x370, 75%](../../img/KDE_Display_Settings.png)
**_Aplikace Nastavení systému KDE Plasma_**

![Nastavení zobrazení (GNOME)|690x344, 75%](../../img/GNOME_Display_Settings.png)
**_aplikace Nastavení GNOME_**

Je důležité nakonfigurovat nastavení systému při prvním spuštění, abyste si přizpůsobili plochu, zejména pokud si všimnete, že při prvním spuštění je škálování nesprávné.

### Instalace dalšího softwaru

[Dokumentace k instalaci a správě aplikací](../../Installing_and_Managing_Software/index.md) je užitečná, abyste se naučili, jak nainstalovat další software na Bazzite.


### Změna výchozího hesla
<sub> (Pokud to nebylo změněno v instalačním programu) </sub>

![KDE Plasma's Change Password|584x500, 75%](../../img/change-pass.png)

Změňte jej v nastavení režimu plochy v kategorii „Uživatel“.

### Výpočet hash kontrolního součtu ISO SHA256

https://www.youtube.com/watch?v=wUDbMJtR1sM

<hr>

## Problémy s instalací Bazzite?

Prohlédněte si [Průvodce odstraňováním problémů s instalací](./troubleshoot_guide.md).

<hr>

**Viz také:** [Upstream Manual Partitioning Guide](https://docs.fedoraproject.org/en-US/fedora-silverblue/installation/#manual-partition) & [Režim hry Steam][Steam_Gaming_Mode]

<-- [**Zobrazit veškerou dokumentaci Bazzite**](../../index.md)

[Steam_Gaming_Mode]: ../../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md