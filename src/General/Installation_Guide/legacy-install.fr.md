---
title: Guide d'installation de l'ISO "Legacy"
---

# Guide d'installation de l'ISO "Legacy"

## ISOs "Legacy" seulement

Ce guide concerne uniquement les ISO "Legacy" qui sont encore prises en charge à l'heure actuelle, car le nouvel installateur ne prend pas en charge le partitionnement manuel et présente encore quelques bugs.

## Configuration requise

- Consultez le [**Guide de compatibilité matérielle**](/Gaming/Hardware_compatibility_for_gaming.md) pour connaître la configuration requise pour Bazzite.
- Secure Boot et le module TPM (Trusted Platform Module) sont pris en charge sur la plupart des configurations, mais vous devez [**enregistrer notre clé pendant ou après l'installation**](#secure-boot).
- [**Le Dual Boot avec Windows est également pris en charge**](#dual-booting-windows).

### Installer Requirements

- Un moyen de télécharger l'ISO de Bazzite
  - Un gestionnaire de téléchargement (comme [**Motrix**](https://motrix.app/)) si le téléchargement direct de l'ISO de Bazzite échoue ou est trop lent.
- Un support de démarrage d'au moins 16 Go, comme un clef USB
  - Le démarrage à partir d'une carte SD ou microSD peut fonctionner, mais tous les firmwares ne le prennent pas en charge.
- L'un des programmes suivants pour flasher/démarrer l'ISO :
  - **Fedora Media Writer (recommandé)** ([Windows/macOS](https://github.com/FedoraQt/MediaWriter/releases), [Linux](https://flathub.org/en/apps/org.fedoraproject.MediaWriter))
  - **Rufus** ([Windows](https://rufus.ie/))
  - **Ventoy** ([Windows, Linux](https://www.ventoy.net/)) (remarque : Ventoy nécessite [**des étapes supplémentaires pour que le Secure Boot fonctionne**](https://www.ventoy.net/en/doc_secure.html))
- Un clavier physique filaire est **recommandé** et **requis pour les appareils sans écran tactile**.
  - Sinon, créez un compte utilisateur avec un **nom d'utilisateur** et un **mot de passe** si vous disposez d'un clavier.

### Environnements de bureau

Toutes les versions proposent le choix entre [**KDE Plasma**](https://kde.org/plasma-desktop/) et [**GNOME**](https://www.gnome.org/) comme environnement de bureau.

[**Le mode jeu Steam**](../../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md) est une option permettant de lancer une session en plus de KDE Plasma ou GNOME.

Vous trouverez plus d'informations sur la [**FAQ de Bazzite**](../../General/FAQ.md) concernant les différences entre les variantes d'images.

=== "KDE Plasma"

    #### KDE Plasma (par défaut)

    ![Capture d'écran du bureau Bazzite exécutant KDE Plasma|690x388, 75 %](/img/KDE_Plasma_DE.png)

    - L'interface par défaut de KDE Plasma présente une disposition classique et familière
    - Hautement personnalisable grâce à de nombreux paramètres
    - Framework Qt
    - Des distributions Linux populaires telles que SteamOS utilisent KDE Plasma

=== "GNOME"

    #### GNOME (images "-gnome")

    ![Capture d'écran du bureau Bazzite sous GNOME|690x388, 75 %](/img/GNOME_DE.png)

    - L'interface par défaut de GNOME a une mise en page élégante et adaptée au tactile
    - Simple et concise
    - Framework GTK
    - Les distributions Linux populaires telles qu'Ubuntu utilisent GNOME

=== "Mode Jeu Steam"

    #### Mode Jeu Steam (images "-deck")

    ![Mode Jeu|690x388, 75%](/img/Gaming_Mode.jpeg)

    !!! note

        Votre appareil démarrera automatiquement en mode Jeu Steam au lancement, et vous pourrez accéder au mode Bureau depuis le "**menu d'alimentation**" en mode Jeu Steam.

    {% block desktop_envs_steam_notes %}

    - **Nécessite un compte [Steam](https://store.steampowered.com/)**
    - Inclus dans les [images Bazzite-Deck](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md)
    - L'interface est conçue pour le jeu sur console portable et salon
    - Compatible avec les manettes
    - Choix entre KDE Plasma ou GNOME pour le mode bureau
    - Fonctionnalités supplémentaires avec les [plugins Decky](https://github.com/SteamDeckHomebrew/decky-loader) [(Voir tous les plugins)](https://plugins.deckbrew.xyz/)

    {% endblock %}

## 0. Sauvegarde

Assurez-vous de sauvegarder vos données personnelles stockées sur le disque sur lequel vous prévoyez d'installer Bazzite avant de procéder à l'installation.

## 1. Télécharger et flasher l'ISO Legacy

- Téléchargez [Bazzite](https://download.bazzite.gg) après avoir sélectionné l'ISO adaptée à votre configuration à l'aide de notre outil Image Picker.
- Falshez Bazzite sur votre support de démarrage.
- Éjectez le support une fois l'ISO flashé.

### Calcul de la signature SHA256 de l'ISO

**Tutoriel vidéo** :

https://www.youtube.com/watch?v=wUDbMJtR1sM

## 2. Démarrer Bazzite

- Connectez votre support de démarrage à votre appareil et démarrez à partir de celui-ci.
- Une fois l'appareil connecté, démarrez le programme d'installation Bazzite.
- Cela dépend de la configuration de votre carte mère, mais il s'agit généralement d'une touche comme <kbd>F9</kbd> ou similaire.
  - Vous devrez peut-être consulter le manuel, rechercher votre appareil en ligne ou lire les raccourcis clavier qui s'affichent au démarrage de votre PC.
    - Vous pouvez également modifier les paramètres du BIOS pour démarrer d'abord avec votre périphérique de démarrage avant votre stockage actuel, mais il n'est **pas recommandé** de laisser cette option activée après l'installation de Bazzite.
- Vérifiez que le support est valide et passez à l'installateur.

### Appareils portables

Maintenez enfoncé le bouton "Volume bas" (<kbd>-</kbd>) et cliquez sur le bouton d'alimentation. Lorsque vous entendez un signal sonore, relâchez les deux boutons et vous accéderez au "Boot Manager". Une fois dans le "Boot Menu", sélectionnez votre périphérique de démarrage pour lancer le programme d'installation de Bazzite.

## 3. À l'intérieur de l'installateur

!!! note "Installation de Bazzite sans clavier physique connecté à votre appareil :"

    Si aucun clavier USB n'est connecté, n'appuyez **PAS** sur "_User Creation_", car cela supprimera le nom d'utilisateur et le mot de passe par défaut, et vous ne pourrez pas saisir de nom d'utilisateur ni de mot de passe sans clavier physique.

    **Utilisateur par défaut** : `bazzite`
    **Mot de passe par défaut** : `bazzite`

![Automatic drive configuration|690x497, 75%](../../img/anaconda_drive_configuration.png)

![User setup example|690x359, 75%](../../img/anaconda_user_setup.png)

- Sélectionnez votre langue, votre région, la disposition du clavier et le fuseau horaire.
- Sélectionnez le disque sur lequel Bazzite sera installé.
  - Supprimez toutes les partitions restantes sur le disque **sauf en cas de dual boot sur le même disque**.
  - Il est recommandé d'utiliser la configuration automatique du stockage **sauf en cas de dual boot sur le même disque**.
- Vous pouvez, si vous le souhaitez, chiffrer le disque à l'aide d'un mot de passe.
  - **Si vous perdez ce mot de passe, le disque ne pourra pas être déchiffré**.
  - UN CLAVIER PHYSIQUE FILAIRE EST NÉCESSAIRE POUR DÉVERROUILLER L'APPAREIL !
- Créez un compte utilisateur.
  - Attribuez-lui des privilèges d'administrateur et **définissez un mot de passe utilisateur**.
- Lancez l'installation.
- Redémarrez votre appareil une fois l'installation terminée.

### Dual-Booting Windows

!!! note

    Ignorez cette section si vous prévoyez d'installer Bazzite sans Dual Boot Windows.

Pour effectuer un dual boot avec Windows sur des disques **distincts**, utilisez le menu de démarrage UEFI de votre carte mère, car le bootloader GRUB risque de ne pas reconnaître correctement chaque entrée de démarrage.

### Guide vidéo

https://www.youtube.com/watch?v=KAt49B6rSFI

### Guide étape par étape

1. Installation de Bazzite sur un disque partagé.
2. Installation de Bazzite sur un disque séparé.

=== "Disque partagé (partition automatique)"

    1. (Sur Windows) Désactivez le **chiffrement BitLocker** et **fastboot**, puis redémarrez.
    2. (Sur Windows) Redimensionnez la partition Windows à l'aide de l'application Gestion des disques afin de disposer de suffisamment d'espace pour Bazzite.
    En général, cela devrait ressembler à ceci :
    ![](/img/dualbooting_partitions_windows.png)
    <i><small>Source : [diskpart.com](https://www.diskpart.com/windows-10/windows-10-disk-management-0528.html)</small></i>
    3. Lancez le programme d'installation de Bazzite avec l'option de partition automatique.
    4. Redémarrez sous Bazzite et exécutez `ujust regenerate-grub` dans le terminal pour ajouter Windows au menu GRUB.

=== "Disque partagé (partitionnement manuel) [Disponible uniquement pour l'ISO Legacy]"

    1. (Sous Windows) Redimensionnez la partition Windows à l'aide de l'application Gestion des disques afin de disposer de suffisamment d'espace pour Bazzite.
    En général, cela devrait ressembler à ceci :
    ![](/img/dualbooting_partitions_windows.png)
    <i><small>Source : [diskpart.com](https://www.diskpart.com/windows-10/windows-10-disk-management-0528.html)</small></i>
    2. Lancez le programme d'installation de Bazzite en utilisant le [partitionnement manuel](#manual-partitioning-instructions)
    3. Redémarrez sous Bazzite et exécutez `ujust regenerate-grub` dans le terminal pour ajouter Windows au menu GRUB.

=== "Disque dédié"

    **Lorsque l'utilisation d'un disque dédié est possible, cette méthode est recommandée.**

    Installez Bazzite sur un disque interne ou externe dédié.

    1. Installez l'autre système d'exploitation sur un disque (comme Windows).
    2. Installez Bazzite sur un **second** disque.
    3. Définissez Bazzite comme **par défaut** dans les priorités de démarrage (facultatif).

    Si vous installez Windows ensuite, vous devez déconnecter le disque Bazzite pour empêcher le programme d'installation de Windows d'utiliser sa partition EFI.

    Vous pouvez également installer Windows sur un disque externe avec Windows-to-Go à l'aide de [Rufus](https://rufus.ie/en/) pour le Dual Boot si vous ne disposez pas d'un disque interne.

Si vous installez Windows après Bazzite, vous pouvez restaurer le bootloader de Bazzite à l'aide du **Bootloader Restoring Tool** inclus dans l'ISO Live.

### Instructions pour le partitionnement manuel

!!! warning : "Seuls les utilisateurs qui utilisent un Dual Boot sur le même disque doivent suivre ces instructions. Dans les autres cas, il est préférable d'opter pour le partitionnement automatique."

!!! attention "Bazzite ne prend en charge que le système de fichiers BTRFS pour `/`."

Si vous avez besoin d'une vidéo explicative sur le partitionnement manuel, regardez ce [tutoriel à partir de 9 min 10 s](https://www.youtube.com/watch?v=JxPsKhJGTrs&t=550s).

1.  Sélectionnez la destination d'installation
2.  Sélectionnez `Advanced Custom (Blivet-GUI)` sous "Storage Configuration".
![Selecting manual partitioning](../../img/select_manual_partitioning.png)
3.  Créez les partitions et périphériques suivants :
  - **/boot/efi**
    ![EFI partition](../../img/efi_partition.png)
    ```
    mount point: /boot/efi
    format:      EFI system partition
    size:        300MB
    ```
  - **/boot**
    ![boot partition](../../img/boot_partition.png)
    ```
    mount point: /boot
    format:      ext4
    size:        2GB
    ```
  - **btrfs partition**
    ![btrfs partition](../../img/btrfs_partition.png)
    ```
    mount point:
    format: btrfs
    size: [max]
    ```
  - **/**
    ![/ subvolume](../../img/root_subvolume.png)
    ```
    mount point: /
    format:      btrfs (subvolume)
    ```
  - **/var**
    ![/var subvolume](../../img/var_subvolume.png)
    ```
    mount point: /var
    format:      btrfs (subvolume)
    ```
  - **/var/home**
    ![/var/home subvolume](../../img/var_home_subvolume.png)
    ```
    mount point: /var/home
    format:      btrfs (subvolume)
    ```
4.  Sélectionnez "Done"
5.  Sélectionnez "Accept Changes"
6.  Poursuivez l'installation.

### Dual-boot avec d'autres systèmes d'exploitation Linux

!!! Remarque 

    Le dual boot avec d'**autres distributions Linux**, en particulier **Fedora non-atomic**, n'est pas officiellement pris en charge. Il est recommandé d'utiliser le menu de démarrage UEFI de votre carte mère ou de renoncer complètement au dual boot afin d'éviter tout problème inattendu. Si un problème survient, restaurez le BootLoader de Bazzite à l'aide de l'**outil de restauration du BootLoader** disponible dans l'ISO Live.

Pour les images Fedora Atomic Desktop sur le **même** disque : pour effectuer un dual boot avec une autre **image Fedora Atomic Desktop** (comme [Bluefin](https://projectbluefin.io/)) installée parallèlement à Bazzite, vous devez créer une partition EFI supplémentaire et basculer entre les deux via le menu de démarrage UEFI de votre carte mère.

Pour un dual boot sur des disques **distincts** :

Utilisez le menu de démarrage UEFI de votre carte mère, car le BootLoader GRUB risque de ne pas reconnaître correctement chaque entrée de démarrage.

## Secure Boot

!!! note

    Ignorez cette section si le Secure Boot n'est pas activé ou n'est pas pris en charge par votre matériel.

!!! important

    L'invite d'enregistrement utilise une disposition de clavier QWERTY anglais, quelle que soit la disposition réelle de votre clavier. D'autres dispositions peuvent donc interférer avec les caractères du mot de passe (par exemple, les touches `A` et `Q` sont inversées sur les dispositions AZERTY).

Bazzite prend en charge le Secure Boot, mais la clef Universal Blue doit être enregistrée pour pouvoir l'utiliser ; sinon, le maintien du Secure Boot activé dans votre BIOS empêchera Bazzite de démarrer.

### Remarques importantes concernant le Secure Boot

- Pour des raisons de sécurité, la saisie du mot de passe s'effectue à l'aide de caractères invisibles ; vous ne pourrez donc pas voir ce que vous tapez !
- La mise à jour de votre BIOS peut réactiver le Secure Boot et vous devrez peut-être suivre la **« Méthode B »** après la mise à jour pour résoudre le problème d'écran noir au démarrage signalant que le noyau doit être chargé en premier.
- Le Steam Deck n'est **pas** livré avec le Secure Boot activé et ne contient aucune clé enregistrée par défaut. N'activez pas le Secure Boot sur votre Steam Deck à moins d'être absolument certain de ce que vous faites.

### Message d'erreur (si la clé n'est **pas** correctement enregistrée)

```
error: ../../grub-core/kern/efi/sb.c:182:bad shim signature.
error: ../../grub-core/loader/1389/efi/linux.c:256:you need to load the kernel first.

Press any key to continue...
```

Suivez la **méthode B** ci-dessous pour résoudre ce problème et ignorer le message d'erreur si celui-ci s'affiche.

### **Méthode A** - Procédure pendant l'installation

![Menu Secure Boot : Continue boot / Enroll MOK / Enroll key from disk / Enroll hash from disk](../../img/Secure_Boot.png)

!!! note

    Cet écran s'affichera également au prochain démarrage si vous activez le Secure Boot alors qu'il était désactivé pendant l'installation.

Un écran bleu s'affichera, vous proposant d'enregistrer les clés signées après avoir quitté le programme d'installation de Bazzite.

`Register MOK` si le Secure Boot est activé. Si vous êtes invité à saisir un mot de passe, **saisissez** :

```command
universalblue
```

Sinon, `Continue boot` si le Secure Boot est désactivé ou s'il n'est pas pris en charge par votre matériel.

### **Méthode B** - Méthode après installation

**Désactivez le Secure Boot dans le BIOS avant de continuer**, puis réactivez-le **après avoir enregistré la clé**.

Si vous avez déjà installé Bazzite, **saisissez cette commande dans un terminal hôte**

```
ujust enroll-secure-boot-key
```

Si vous êtes invité à enregistrer la clé requise, **saisissez le mot de passe dans le terminal hôte** :

```command
universalblue
```

**Vous pouvez désormais réactiver le Secure Boot dans le BIOS.**
Utilisez la commande suivante pour démarrer directement dans le BIOS de votre système (si cette fonctionnalité est prise en charge) :

```command
ujust bios
```

### Effectuer l'enregistrement du MOK au démarrage

Au prochain démarrage, l'écran bleu de MokManager s'affichera :

1.  Sélectionnez **Enroll MOK**.
2.  Lorsque le mot de passe vous est demandé, saisissez :
    ```command
    universalblue
    ```

Après le redémarrage, la clé est enregistrée et le Secure Boot peut rester activé. Votre système devrait désormais démarrer normalement sous Secure Boot.

## **Dépannage de l'installation**

Consultez le [**Guide de dépannage**](./troubleshoot_guide.md) ou le [**Guide d'installation alternative**](./alternate-install-guide.md) pour connaître les solutions de dépannage de l'installation.

## Après l'installation

Bazzite est désormais installé. Consultez le [**Guide post-installation**](./post-installation.md) pour connaître les étapes suivantes recommandées !
