---
title: Configuration après installation
---

# Configuration après installation

## Configuration au premier démarrage

![Rollbacks|690x402, 50%](../../img/GRUB_Menu.png)

Au premier démarrage, un écran s'affichera pour vous indiquer votre déploiement actuel et le dernier en date. Si vous rencontrez des problèmes, sachez que le menu GRUB vous permet de revenir en arrière sur les déploiements Bazzite.

Pour en savoir plus, consultez la [**documentation sur les mises à jour, rollbacks et le rebase**](../../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md).

## Configuration du mode jeu Steam (images Bazzite-Deck uniquement)

![Configuration du mode jeu|1920x1080, 50%](../../img/deck-edition.png)

Si vous avez choisi d'utiliser le mode jeu Steam avant de télécharger l'ISO, vous vous trouverez alors sur la version Bazzite-Deck.  Une fois toutes les étapes ci-dessus terminées, votre prochain démarrage se fera en mode jeu Steam, ce qui nécessite une configuration supplémentaire pour Steam.

Consultez la [**documentation Bazzite-Deck**](../../Handheld_and_HTPC_edition/index.md) pour plus d'informations sur les images HTPC/Portable.

## Configurer les paramètres système

Il est important de configurer les paramètres système lors du premier démarrage afin de personnaliser votre bureau, surtout si vous constatez que le réglage de l'échelle n'est pas correct lors de votre premier démarrage. Ouvrez l'application des paramètres système dans la session de bureau pour commencer à configurer les paramètres.

### Paramètres de mise à l'échelle

![Paramètres d'affichage (KDE Plasma)|690x370, 75 %](../../img/KDE_Display_Settings.png)
**_Application Configuration du système de KDE Plasma_**

![Paramètres d'affichage (GNOME)|690x344, 75%](../../img/GNOME_Display_Settings.png)
**_Application Paramètres de GNOME_**

Réglez les paramètres système selon vos préférences.

### Modification du mot de passe par défaut
<sub> (Si celui-ci n'a pas été modifié dans le programme d'installation ISO "Legacy") </sub>

![Modification du mot de passe dans KDE Plasma|584x500, 75 %](../../img/change-pass.png)

Modifiez-le dans les paramètres du mode Bureau, sous la catégorie "Utilisateurs".

## Configuration après l'installation en Dual Boot

!!! note

    Cela ne concerne que les utilisateurs de Bazzite qui ont configuré un Dual Bootzzzzzzzzzzzzz avec Windows.

Pour afficher vos installations Windows et Bazzite dans le menu GRUB et pouvoir choisir entre les deux au démarrage, saisissez cette **commande dans le terminal** :

```
ujust regenerate-grub
```

### Bazzite en tant que démarrage par défaut

Si l'`OS Boot Manager` a défini `Windows Boot Manager` comme démarrage par défaut, cela peut entraîner un démarrage direct sous Windows après l'installation, au lieu de Bazzite. Vous devrez peut-être corriger cela dans les paramètres de votre BIOS.

Notez que le menu GRUB pourrait ne pas s'afficher. Dans ce cas, appuyez frénétiquement sur la touche <kbd>↓</kbd> au démarrage.

### Démarrer Windows depuis Steam

Ajoutez un script dans Steam permettant de démarrer Windows.

```
ujust setup-boot-windows-steam
```

### Étendre la capacité de stockage dans un environnement Windows Dual Boot

!!! note

    Ceci est destiné à servir de référence ultérieure après avoir utilisé le Dual Boot pendant un certain temps.

**Regardez ce tutoriel vidéo pour savoir comment étendre la capacité de stockage** :

https://www.youtube.com/watch?v=uy8mi1pAj8E

<hr>

## Étapes suivantes

### Configurer votre système à l'aide de l'application Portail Bazzite

![bazzite-portal|997x785, 50%](../../img/bazzite-portal.png)

Découvrez le portail Bazzite, qui permet d'effectuer la maintenance du système, d'installer un certain nombre d'apps supplémentaires et de configurer les paramètres avancés du système.

### Installer des programmes supplémentaires via la boutique d'apps Bazaar

![Capture d'écran de la boutique d'apps Bazaar|1649x1274, 50 %](../../img/Bazaar.png)

Installez des programmes supplémentaires pour Bazzite dans la boutique d'apps Bazaar. C'est là que vous trouverez la plupart de vos apps, mais si vous avez besoin d'une app qui n'y figure pas, consultez la section [**Installation et gestion des applications**](../../Installing_and_Managing_Software/index.md).

<hr>

## Prêt à jouer

**Vous avez maintenant installé Bazzite !**

Commencez à jouer en consultant notre [**Guide du jeu**](../../Gaming/index.md) qui couvre les points suivants :

- Installation et configuration de **Steam** et **Proton** pour la compatibilité des jeux Windows
- La configuration de **Lutris** et d'autres lanceurs de jeux (Epic Games, GOG, Amazon Games, etc.)
- La gestion et le mod des jeux
- Le dépannage des problèmes courants liés aux jeux

Profitez bien de Bazzite et n'oubliez pas de [**signaler tout bug**](../../General/reporting_bugs.md) que vous rencontrez afin qu'il puisse être corrigé dès que possible.
