---
title: Dépannage de l'installation
---

# Dépannage de l'installation

## Téléchargement de l'ISO

Utilisez un gestionnaire de téléchargement (comme [**Motrix**](https://motrix.app/)) si le téléchargement direct échoue ou est trop lent.

## Disques

Veillez à ne sélectionner que les disques appropriés pour éviter de perdre des données sur les autres, et il est recommandé de retirer tout disque externe avant de continuer.

## Erreur "Failed to open \EFI\BOOT\mmx64.efi - Not Found"

![Failed to open \EFI\BOOT\mmx64.efi - Not Found](../../img/efi-boot-fail.png)

Pour régler ce problème, démarrez à partir du fichier. Accédez à votre UEFI (BIOS), sélectionnez votre partition EFI sur laquelle Bazzite est installé, puis sélectionnez /EFI/fedora/grubx64.efi pour démarrer.
Après cela, votre gestionnaire de démarrage devrait démarrer normalement en affichant « FEDORA » comme option.

## L'installateur ne démarre pas

!!! note

Le nouvel installateur risque de ne pas démarrer si votre BIOS est configuré en mode CSM Legacy plutôt qu'en mode UEFI. Pour en savoir plus, consultez la page [**Configuration système requise pour Bazzite**](../../Gaming/Hardware_compatibility_for_gaming.md#minimum-system-requirements).

Utilisez l'[ISO Legacy](./legacy-install.md) ou essayez la [méthode alternative](./alternate-install-guide.md) pour installer Bazzite.

## Code d'erreur 1

L'erreur « code 1 » est un code d'erreur générique qui s'affiche pendant l'installation lorsqu'aucun message d'erreur plus précis n'est disponible. Cette erreur peut se produire dans plusieurs situations que nous avons identifiées, mais il peut en exister d'autres :

- **Installation Linux existante :** si vous avez déjà installé un autre système Linux sur le même disque, le programme d'installation peut échouer lors de l'installation du bootloader avec une erreur 'bootloader write config'.
  - Cela peut se produire même si l'installation Linux précédente n'est plus fonctionnelle. Ce problème est connu pour se produire à la fois avec les distributions **basées sur Fedora** (Fedora, Fedora Atomic, Bazzite, Nobara, etc.) et **basées sur Ubuntu** (Ubuntu, Mint, PopOS, etc.).
  - **Solution 1 :** Disque séparé : si votre matériel prend en charge plus d'un SSD, installez Bazzite sur un disque différent qui n'a jamais accueilli Linux auparavant.
  - **Solution 2 :** Supprimez manuellement le Linux existant de l'EFI :  [Veuillez consulter les instructions ci-dessous.](#how-to-remove-an-orphaned-copy-of-grub)
  - **Solution 3 :** Supprimez la partition EFI existante sur le disque : si vous ne prévoyez PAS de Dual Boot, utilisez GParted ou Disques pour supprimer l'EFI existant.
    - **Avertissement :** cette opération est **irréversible** et supprimera tous les autres systèmes d'exploitation présents sur le disque, **y compris Windows**
  - **Solution 4 :** Créez une nouvelle partition EFI : vous pouvez utiliser le partitionnement manuel tel que décrit dans le [Guide de partitionnement manuel](./manual_partitioning.md) pour créer une nouvelle partition EFI à côté de celle existante afin d'y parvenir.
  - Avertissement : certains BIOS ne prennent pas en charge une deuxième partition EFI sur le disque.
- **Filesystem incorrecte :** l'utilisation du système de fichiers EXT4 ou de tout autre type de système de fichiers pour la partition racine provoquera cette erreur. Vous devez utiliser BTRFS pour la partition racine.
- **Image ISO corrompue :** assurez-vous que l'image ISO n'est pas corrompue en calculant les checksums.
- **Surchauffe de la clé USB :** utilisez une clé USB 3.0 ou supérieure et branchez-la sur un port USB 3.0 ou supérieur pour éviter toute surchauffe.

## Erreur "Espace insuffisant sur l'appareil"
![Espace insuffisant sur l'appareil](../../img/no_more_space_left.png)

Cette erreur peut s'afficher de manière trompeuse lorsque le système ne dispose pas de suffisamment de RAM pour permettre le fonctionnement du programme d'installation. [**Vous avez besoin d'au moins 8 Go de RAM pour installer Bazzite.**](/General/Installation_Guide/Installing_Bazzite_for_Desktop_or_Laptop_Hardware.md/#minimum-system-requirements)

## Erreur "Bad shim signature, you need to load the kernel first"

![You need to load the kernel first](../../img/you-need-to-load-the-kernel-first.png)

Désactivez le Secure Boot dans le BIOS pour passer cet écran. Si vous souhaitez utiliser le Secure Boot, suivez [le **Guide du Secure Boot** en utilisant la méthode B](/General/Installation_Guide/secure_boot.md).

**Guide video**:

https://www.youtube.com/watch?v=Z_DsWqTuipU

## Erreur "Device is Active" 

Cette erreur se produit lorsque le programme d'installation détecte une partition chiffrée par BitLocker. Deux options s'offrent à vous :

A. **En cas de Dual Boot :** réduisez la partition sous Windows avant l'installation, de manière à libérer suffisamment d'espace pour l'installation de Bazzite.
B. **Bazzite uniquement :** supprimez la partition BitLocker à l'aide d'un outil tel que GParted avant l'installation.

**Vidéo de démonstration** :

https://www.youtube.com/watch?v=FBGLLkIKp-w

### "Error checking storage configuration"

**Regardez cette vidéo pour savoir comment contourner le problème** :

https://www.youtube.com/watch?v=VTnm9EiBdPA


## Erreur : impossible d'allouer le schéma de partition demandé

Cette erreur se produit lors de l'installation sur des disques d'une capacité supérieure à 2 To, lorsque les 2 premiers To (ou plus) sont déjà occupés par une ou plusieurs partitions. L'image ci-dessous illustre le message d'erreur.

![Impossible d'allouer le schéma de partition demandé](../../img/unable-to-allocation-requested-partition-scheme.png)

Il semble que le programme d'installation Anaconda ne puisse créer aucune partition au-delà de la limite des 2 To.

Voici quelques solutions possibles pour résoudre ce problème :

- Installez Bazzite sur un autre périphérique de stockage où Bazzite peut disposer de l'intégralité du disque.
- Si vous utilisez un Dual Bootavec Windows, réduisez la taille de votre partition Windows à moins de 2 To. Si l'outil de gestion des disques de Windows ne permet pas d'effectuer cette opération, envisagez d'utiliser un outil tiers tel que [EaseUS Partition Master](https://www.easeus.com/partition-master/) pour redimensionner les partitions lorsque Windows n'est pas en cours d'exécution.
- Si le disque ne contient aucune donnée importante, vous pouvez supprimer toutes les partitions existantes et relancer le processus d'installation.

<hr>

## Méthode d'installation alternative

!!! note

    **La méthode d'installation alternative permet de télécharger une image ISO plus légère et peut résoudre d'autres problèmes, mais elle présente également des problèmes d'affichage dans le programme d'installation sur la plupart des écrans d'appareils portables**.

Si aucune des erreurs ci-dessus ne correspond à votre problème, ou si vous rencontrez toujours des difficultés pour installer Bazzite, essayez de suivre notre méthode d'installation alternative :

[**Essayez d'installer Bazzite en effectuant un rebase à partir de Fedora Kinoite (KDE Plasma) ou Fedora Silverblue (GNOME)**](/General/Installation_Guide/alternate-install-guide.md).

## Comment supprimer une copie orpheline de GRUB
1. Démarrez dans le programme d'installation de Bazzite (le programme d'installation Legacy ne fonctionnera pas pour cette solution) et ouvrez le menu des applications
   ![](../../img/remove_grub_1.png)
2. Tapez 'disques' et ouvrez l'application Disques
   ![](../../img/remove_grub_2.png)
3. Sélectionnez le disque sur lequel vous souhaitez installer Bazzite
   ![](../../img/remove_grub_3.png)
4. Identifiez votre partition EFI ; elle sera de type FAT et généralement peu volumineuse.
   ![](../../img/remove_grub_5.png)
5. Montez la partition EFI (si elle n'est pas déjà montée) en cliquant sur le bouton 'Play'.
   ![](../../img/remove_grub_6.png)
6. Cliquez sur le texte en bleu à côté de 'mounted at'
   ![](../../img/remove_grub_7.png)
7. Double-cliquez sur le dossier EFI
   ![](../../img/remove_grub_8.png)
8. Identifiez le dossier 'Ubuntu' ou 'Fedora' et déplacez-le vers la corbeille
   ![](../../img/remove_grub_9.png)
!!! warning
    Ne supprimez aucun autre dossier, tel que « Boot », « Dell », « HP » ou « Microsoft », sinon Windows risque de ne pas démarrer correctement !
9. Redémarrez, puis relancez le programme d'installation. Vous pouvez supprimer les partitions créées lors de la première tentative d'installation.
   ![](../../img/remove_grub_10.png)
