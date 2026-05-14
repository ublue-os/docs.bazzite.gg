---
title: Guide d'installation alternative
---

# Guide d'installation alternative

!!! warning

    Cette méthode peut poser des problèmes d'évolution avec le programme d'installation selon le matériel utilisé, en particulier s'il s'agit d'une console PC.

## Rebasage à partir d'une image Desktop Fedora Atomic

Si vous rencontrez des difficultés pour installer notre ISO ou si votre disque de démarrage a une capacité trop faible pour Bazzite, téléchargez [Fedora Kinoite (**KDE Plasma**)](https://fedoraproject.org/atomic-desktops/kinoite/) ou [Fedora Silverblue (**GNOME**)] (https://fedoraproject.org/atomic-desktops/silverblue/) en fonction de l'environnement de bureau que vous préférez.

1. La procédure d'installation est similaire à celle de Bazzite et utilise le même installateur avec les mêmes instructions, mais **ne** créez **pas** de compte root si cette option est proposée dans l'installateur.

2. Une fois l'installation terminée, vous ne serez pas sur Bazzite tant que vous n'aurez pas saisi la commande disponible sur notre site web, qui apparaît dans la section [« **Utilisateurs existants de Fedora Atomic Desktop** »](https://download.bazzite.gg) lorsque le téléchargement est prêt, ou en vous référant à la [liste complète des images dans la FAQ](/General/FAQ/#bazzite-image-chart-example).

3. Ouvrez le terminal et saisissez cette commande. Notez bien que ce processus ne dispose d'**aucun information de progression** et peut prendre beaucoup de temps.

4. Redémarrez une fois le rebase terminé. Bazzite devrait alors être installé. Votre nom d'utilisateur et votre mot de passe seront transférés de la version en amont de Fedora Atomic Desktop vers Bazzite.

5. Il vous manquera également **les apps par défaut de Flatpak, jusqu'à ce que vous les installiez à l'aide de la commande `ujust`** ci-dessous.

## Instructions relatives au Secure Boot lors du rebasage à partir d'images Fedora Atomic Desktop

Rebasage depuis Fedora Silverblue, Fedora Kinoite, etc. vers Bazzite.

Si vous effectuez un rebasage à partir d'une image Fedora Atomic Desktop et que vous utilisez Secure Boot, suivez les instructions fournies dans le [**fichier README de Bazzite**](https://github.com/ublue-os/bazzite/blob/main/README.md#secure-boot).

## Installer les applications Flatpak par défaut

Ouvrez le terminal et **saisissez cette commande** :

```command
ujust _install-system-flatpaks
```

Sélectionnez le dépôt "**Flathub**".  Si le système vous demande de choisir entre "Système" et "Utilisateur", sélectionnez "**Système**", car il s'agit du dépôt par défaut pour Bazzite.

> **Cette commande installe :**
>
> - [Applications Flatpak pour les images **KDE Plasma**](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/kinoite/usr/share/ublue-os/bazzite/flatpak/install)
> - [Applications Flatpak pour les images **GNOME**](https://github.com/ublue-os/bazzite/blob/9f6f5e143b7545d06803e70e7723997400bd8b88/system_files/desktop/silverblue/usr/share/ublue-os/bazzite/flatpak/install)

### Supprimer le dépôt Fedora Flatpak

Veuillez supprimer le dépôt Fedora Flatpak à l'aide de l'application Warehouse. Cela **ne** supprimera **pas** les données utilisateur.

## Rebasage vers une image signée

Une fois que tout est correctement configuré, vous devez effectuer un rebasage de l'**image non signée** vers l'**image signée** pour des raisons de sécurité. Pour ce faire, **entrez cette commande** dans votre terminal :

```command
ujust verify-image
``` 
Une fois la commande exécutée, redémarrez votre appareil.

## Tutoriel vidéo

https://www.youtube.com/watch?v=0NKEfVvdiOs
