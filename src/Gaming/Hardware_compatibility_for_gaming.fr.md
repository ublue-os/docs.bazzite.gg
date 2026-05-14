---
title: Compatibilité matérielle pour le jeu
---

# Compatibilité matérielle pour le jeu

## Configuration minimale requise

- **Architecture**: x86_64
- **Firmware**: UEFI (CSM/Legacy boot [**NON SUPPORTÉ**](../General/FAQ.md#does-bazzite-support-csmlegacy-boot))
- **Processeur (CPU)** : 2GHz quad core ou supérieur
- **Mémoire système (RAM)**: 8GB
- **Carte Graphique (GPU)**: une carte graphique capable d'utiliser Vulkan 1.3 ou supérieure; les CG AMD récentes offrent les meilleures performances
- **Stockage** : 50 Go d'espace libre sur un **disque SSD** interne
  - **Stockage recommandé** : 120 Go d'espace libre sur un **disque SSD** interne
  - **Stockage externe et disques secondaires** : tous les disques doivent être formatés en **BTRFS (SSD)** ou **Ext4 (disques durs [HDD])** (_veuillez sauvegarder les fichiers et reformater après installation_)
- **Réseau** : connexion Internet stable sans limitation de bande passante (_non requise pour l'installation_)
- **Remarques supplémentaires** : certains périphériques ne sont **pas** compatibles avec Bazzite :
  - **Exemple d'adaptateur Wi-Fi** - [liste des adaptateurs Wi-Fi USB **connus pour être compatibles**](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md)

>[**Le site Web "Hardware for Linux"**](https://linux-hardware.org/?view=computers) donne une bonne idée du niveau de prise en charge du matériel des fabricants OEM avec Linux.

### Configuration requise pour le mode jeu Steam

!!! note

    Cette configuration spécifique s'applique uniquement aux [images Bazzite-Deck](/Handheld_and_HTPC_edition/Steam_Gaming_Mode.md) fournies avec tous les téléchargements ISO de Bazzite pour appareils portables.

- Carte graphique AMD récente
  - Série RX 4xx et supérieure
    - Les cartes graphiques intégrées 600M/700M sont également prises en charge
- Les cartes graphiques Intel Arc sont prises en charge avec **quelques restrictions** par rapport au matériel AMD
- La prise en charge des GPU Nvidia est soumise à des [**restrictions importantes**](/Handheld_and_HTPC_edition/quirks/#nvidia-gpu-exclusive-issues-with-steam-gaming-mode) par rapport au GPU AMD, qui échappent au contrôle du dévellopement de Bazzite
- Nécessite un compte [**Steam**](https://store.steampowered.com/)
  - Vous pouvez créer un compte après l'installation si vous n'en avez pas déjà un


>[**Le site Web "Hardware for Linux"**](https://linux-hardware.org/?view=computers) donne une bonne idée du niveau de prise en charge du matériel des fabricants OEM avec Linux.

### Appareils portables compatibles

Le [**Handheld Wiki**](../Handheld_and_HTPC_edition/Handheld_Wiki/index.md) répertorie les appareils portables testés qui prennent correctement en charge le Steam Deck, l'ASUS ROG Ally, la Lenovo Legion Go et d'autres modèles.

<hr>

## Carte graphique compatible avec Vulkan

!!! attention

    Le jeu sous Linux dépend fortement de la compatibilité de votre matériel avec Vulkan.

### Vérifier la version Vulkan de votre carte graphique

Si vous utilisez un appareil équipé d'une carte graphique plus ancienne ou moins puissante qui ne prend pas en charge **Vulkan 1.3 ou ultérieure**, vous devez utiliser des versions plus anciennes de Proton et Wine, telles que **Proton/WINE 6** ou antérieures.  Pour vérifier la version de Vulkan utilisée par votre carte graphique, saisissez la commande suivante dans le **terminal** :

```command
vulkaninfo | grep 'Instance Version'
```

- Si la valeur affichée dans le champ « Vulkan Instance Version: » est inférieure à `1.3` ou si cela ne fonctionne pas du tout, vous risquez de rencontrer des problèmes, notamment une baisse des performances ou des jeux qui ne fonctionnent pas.
- Les appareils anciens peuvent nécessiter le recours à la conversion OpenGL, qui offre des performances moins bonnes, présente des problèmes graphiques, etc.

![Commande Vulkan](https://github.com/user-attachments/assets/ccca14ca-3001-4aa6-bf47-e0dcbdb73936)

>Essayez d'utiliser [**Proton-Sarek**](https://github.com/pythonlover02/Proton-Sarek) si votre matériel peut prendre en charge Vulkan 1.1, mais pas les versions plus récentes. Il peut être installé à l'aide de ProtonPlus.

### Cartes graphiques ne prenant pas en charge Vulkan

Toutefois, si votre carte graphique ne prend pas du tout en charge Vulkan, vous devez utiliser une version plus ancienne de Proton (Proton 3, 4 ou 5) et utiliser cette **option de lancement pour la plupart des jeux Steam** :

```command
PROTON_USE_WINED3D=1 %command%
```

Cela permettra d'utiliser la conversion OpenGL plutôt que Vulkan.

<hr>

## Systèmes de fichiers de stockage

!!! note

    Bazzite montera automatiquement les disques secondaires formatés en Ext4 ou BTRFS par défaut.

**BTRFS est le système de fichiers par défaut et recommandé pour Bazzite**.  Tout disque secondaire sur lequel vous prévoyez de jouer à des jeux doit être **sauvegardé et reformaté en Ext4 ou BTRFS ; toutefois, le disque perdra toutes ses données lors de cette opération**.  Vous pouvez utiliser [**GNOME Disks pour formater les disques de manière appropriée, à vos propres risques**](../Advanced/Auto-Mounting_Secondary_Drives.md).

### Systèmes de fichiers non pris en charge pour les disques secondaires


!!! CRITICAL

    NTFS et exFAT/FAT32 NE SONT PAS PRIS EN CHARGE. CES DEUX SYSTÈMES DE FICHIERS PEUVENT ENTRAÎNER ET ENTRAÎNERONT UNE CORRUPTION DES DONNÉES SOUS LINUX. NE LES UTILISEZ PAS !
    winBTRFS VIA WINDOWS COMPORTE ENCORE DES BUGS ET NE CONSTITUE PAS NON PLUS UNE SOLUTION. 
    
    IL N'EXISTE ACTUELLEMENT AUCUN SYSTÈME DE FICHIERS CROSSPLATEFORME FIABLE POUVANT ÊTRE PARTAGÉ ENTRE WINDOWS ET LINUX.

!!! warning

    Vous perdrez toutes vos données en formatant les disques secondaires internes/externes.
    
!!! info
    
    Pour désactiver l'avertissement NTFS, exécutez `ujust _disable-ntfs-service`. **NE FAITES CELA QUE SI VOUS SAVEZ CE QUE VOUS FAITES. CELA NE PRÉVIENDRA PAS LA PERTE DE DONNÉES, MAIS DÉSACTIVERA UNIQUEMENT L'AVERTISSEMENT.**


#### NTFS

Si vous passez de Windows à Bazzite et que vous prévoyez de jouer sur un disque secondaire sur lequel des jeux sont déjà installés, nous avons le malheur de vous informer que le système de fichiers NTFS n'est **pas pris en charge** pour les jeux sur Bazzite.

Jouer à des jeux à partir d'un disque NTFS entraîne divers problèmes, notamment, mais sans s'y limiter, le **refus de lancement des jeux**, et finira par entraîner une **corruption des données** et une **perte définitive de données** !

#### exFAT et FAT32

FAT32 et exFAT ne sont **pas pris en charge**. Ces deux systèmes de fichiers **ne prennent pas en charge les liens symboliques**, qui sont nécessaires au bon fonctionnement des préfixes Proton.  Cependant, dans certains cas, une carte microSD formatée en exFAT _peut fonctionner_, mais cette méthode n'est pas prise en charge et les dévellopeurs de Bazzite ne prévoient pas de la prendre en charge.

### Partager des jeux avec un Dual Boot Windows

Installez le pilote non officiel [WinBtrfs](https://github.com/maharmstone/btrfs) sur votre installation Windows **à vos propres risques**. Veuillez vous assurer de lire toute la documentation associée à ce projet avant d'installer le pilote sur Windows.

#### Tutoriel vidéo

https://www.youtube.com/watch?v=h6fc-3CCXbA
