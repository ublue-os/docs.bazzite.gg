---
title: Gérer et modifier des jeux
---

# Gérer et modifier des jeux

## Logiciel de compatibilité et gestion des jeux Windows

![Proton Plus|1797x1412, 43%](../img/proton-plus.png)

Les jeux Windows doivent s'exécuter via un **logiciel de compatibilité** (comme Proton) sur Bazzite. Installez et mettez à jour les dernières versions de [GE-Proton](https://github.com/GloriousEggroll/proton-ge-custom), [Luxtorpeda](https://github.com/luxtorpeda-dev/luxtorpeda) et d'autres outils utilisant ProtonPlus.

## Protontricks

![Protontricks|660x500](../img/Protontricks.png)

Certains jeux nécessitent [Protontricks](https://github.com/Matoking/protontricks) (préinstallé) ou [Winetricks](https://github.com/Winetricks/winetricks) (pour les jeux non-Steam, inclus avec Lutris) afin de fonctionner correctement, en installant des DLL Windows dans le préfixe.

## Fichiers cachés dans le gestionnaire de fichiers

!!! note

    Winecfg propose une option permettant d'afficher les fichiers cachés pour les programmes Windows qui utilisent le sélecteur de fichiers.

Les systèmes Linux contiennent des fichiers et des répertoires cachés qui peuvent inclure des fichiers importants liés a vos jeux

**Affichez les fichiers cachés** en cliquant sur le **menu hamburger** (_3 lignes horizontales dans le gestionnaire de fichiers_), en sélectionnant "Afficher les panneaux" puis cocher "Afficher les emplacements cachés" pour voir tous les dossiers et fichiers masqués par défaut.

Ces dossiers et fichiers commencent tous par un `.`


### Qu'est-ce qu'un préfixe Proton (ou Wine) ?

C'est le lien qui assure la cohésion de l'ensemble lorsque vous lancez un jeu via Proton ; il sert également à regrouper tous les fichiers que le jeu créerait en dehors du dossier d'installation.

!!! important

    Le dossier d'installation des **jeux Steam** se trouve généralement à l'emplacement suivant : `.../steamapps/common/<game>`

De nombreux jeux PC créent des fichiers dans des dossiers Windows tels que "Mes documents" ou "AppData", et ces deux dossiers se trouvent dans votre répertoire de préfixe. Ce répertoire de préfixe peut être utile pour modifier vos jeux, sauvegarder vos parties ou gérer vos fichiers de configuration.

![AppID|690x482, 75%](../img/Steam_AppID.png)

Pour les jeux sur Steam, ils se trouvent dans votre dossier `~/.steam/root/steamapps/compatdata/`, suivi de l'**AppID du jeu** :

- Vous trouverez cet identifiant en accédant aux propriétés du jeu sur Steam via **Propriétés** >> **Mises à jour** >> **App ID**
- Continuez vers `.../pfx/drive_c/` et l'emplacement où le jeu se trouve sous Windows.

Pour les jeux non-Steam, vous pouvez définir l'emplacement du dossier racine où vous le souhaitez. Par défaut, Lutris utilise `~/Games` comme dossier principal.

#### Problème avec le préfixe Proton ?

!!! warning

    La suppression d'un préfixe Proton **peut** entraîner la suppression des sauvegardes et des fichiers de configuration !

Ouvrez le dossier du préfixe du jeu et supprimez les données qu'il contient. Veillez à ne pas supprimer le dossier racine `.../compatdata` (ou `~/Games`, ou le dossier personnalisé que vous avez défini, pour les jeux non Steam), car cela supprimerait les données du préfixe pour tous les jeux !

## Modding

**Steam Workshop est la méthode la plus simple pour obtenir des mods**, mais elle n'est pas prise en charge pour tous les titres et nécessite que vous possédiez le jeu sur Steam. Certains gestionnaires de mods disposent de versions pour Linux, comme [r2modman](https://github.com/ebkr/r2modmanPlus).

L'ajout et le remplacement de fichiers de jeu restent possibles tant dans le dossier du jeu que dans le préfixe, mais cela peut nécessiter quelques étapes supplémentaires.  Certains mods nécessitent une variable d'environnement "WINE DLL OVERRIDE" dans les options de lancement de Steam.  Pour les jeux non-Steam, utilisez Lutris pour ouvrir "Wine Configuration" et sélectionnez l'onglet "Libraries" pour ajouter de nouvelles "OVERRIDE". 

### Exemple d'option de lancement avec override de DLL

    **DirectInput8 DLL Override**: 
    `WINEDLLOVERRIDES="dinput8=n,b" %command%`
