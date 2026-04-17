---
title: Comparaison avec Fedora Atomic Desktop
---

# Comparaison avec Fedora Atomic Desktop

## Qu'est-ce que Bazzite ?

Bazzite est une image personnalisée de [**Fedora Kinoite (images KDE Plasma)**](https://fedoraproject.org/fr/atomic-desktops/kinoite/) ou [**Fedora Silverblue (images GNOME)**](https://fedoraproject.org/fr/atomic-desktops/silverblue/) qui font partie de la [**famille Fedora Atomic Desktop**](https://fedoraproject.org/fr/atomic-desktops/) et qui a été modifiée afin d'offrir une expérience conviviale dès l'installation, en mettant l'accent sur les jeux sur PC.

## Principales différences

Voici une liste des fonctionnalités incluses dans Bazzite qui diffèrent des systèmes d'exploitation Fedora Atomic :

### Moins de configuration après l'installation

- Meilleure prise en charge matérielle dès l'installation, du matériel PC jusqu'aux périphériques.
- Codecs multimédia avec prise en charge complète de l'encodage et du décodage vidéo dès l'installation.
- Logiciels de jeux préinstallés, tels que Steam et Lutris.
- Suppression du dépôt Fedora Flatpak au profit du dépôt [**System Flathub**](https://flathub.org/) afin d'avoir accès à davantage d'applications par défaut.

### Facilité d'utilisation

- Scripts [**`ujust`**](/Installing_and_Managing_Software/ujust/) pratiques, fournis par les mainteneurs et contributeurs du projet.
- Le mode jeu Steam est configuré par défaut et démarre automatiquement sur les [**images Bazzite-Deck**](/Handheld_and_HTPC_edition/Steam_Gaming_Mode/) destinées aux console portable et de salon. 

### Conçu pour les développeurs

- Homebrew est le gestionnaire de paquets recommandé pour les outils en ligne de commande.
- Les conteneurs Distrobox permettent d'accéder à d'autres gestionnaires de paquets pour Linux, destinés à des applications spécifiques ou à des environnements de développement.
- [**Variante Bazzite-DX**](https://dev.bazzite.gg/) : l'image Bazzite de référence pour le développement logiciel.

### Autres améliorations

- Prise en charge des applications Android avec [**Waydroid**](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md).
- Firefox n'est plus inclus dans l'image, au profit de la version Flatpak.
  - Firefox peut désormais être désinstallé, car il ne fait plus partie de l'image
  - Il peut également recevoir des mises à jour plus rapidement, car il ne dépend pas des mises à jour du système pour se mettre à jour.
- Les disques secondaires formatés en BTRFS ou Ext4 seront automatiquement montés.
- Améliorations apportées aux environnements de bureau, notamment des extensions GNOME préinstallées et des thèmes KDE Plasma.
- Rollback vers des versions antérieures de Bazzite datant de moins de 90 jours.