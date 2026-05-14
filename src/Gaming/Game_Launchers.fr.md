---
title: Launchers de jeux
---

# Launchers de jeux

## **Configuration de Steam**

Steam permet de jouer à des jeux Windows sous Linux. Il s'appuie sur un large éventail de projets et de correctifs regroupés dans un module intégré à Steam appelé [**Proton**](https://github.com/ValveSoftware/Proton) pour assurer la compatibilité avec Windows.

### Forcer une version spécifique de Proton/Steam Play Tool

#### Notes importantes

- Les jeux disposant d'un portage Linux seront utilisés par défaut sur les images Desktop.
- Valve sélectionne le launcher par défaut sur les images _Handheld/HTPC_. 
- Certains jeux fonctionnent mieux avec une version spécifique de Proton ou en forçant l'éxécution du portage Linux.

Lancez cette version spécifique en allant dans les **Propriétés** du jeu > **Compatibilité** > **Forcer l'utilisation d'un outil de compatibilité Steam Play spécifique**

#### Images d'exemple
![Cog Icon > Properties|690x284, 75%](../img/Steam_Setup_Cog.png)
![Compatibility tab|690x492, 75%](../img/Steam_Setup_Compat_Tab.png)


## **Jeux hors Steam**

**Il est recommandé d'utiliser [Lutris](https://lutris.net/games?q=&ordering=-popularity&paginate_by=100) pour la _plupart_ des jeux hors Steam**.  Il existe des cas particuliers avec certains launchers et jeux pour lesquels il existe une alternative plus performante que Lutris, mais Lutris reste l'option la plupart du temps la mieux prise en charge pour les jeux PC hors Steam sur Bazzite, sauf dans des cas particuliers.

### Configuration de Lutris

Lutris propose deux méthodes pour jouer à des jeux Windows sur Bazzite : l'utilisation de scripts développés par la communauté ou l'ajout manuel de l'exécutable. Il est **fortement recommandé d'utiliser la méthode manuelle**, car certains scripts sont peu mis à jour.

### Ajouter manuellement un jeu Windows à Lutris

![Add Locally Installed Game|632x496, 75%](../img/Lutris_Setup_Add_Local_Game.png)

![Lutris manually adding games example 1|690x213](../img/Lutris_Setup_Add_Local_Game_1.png)

Toutefois, si votre jeu ne figure pas dans la liste ou ne fonctionne pas avec le script fourni, ajoutez manuellement l'exécutable. Il faudra créer un [**répertoire de préfixe**](./Managing_and_modding_games.md), mais par défaut, le répertoire `~/Games` sera utilisé pour chaque jeu.

### Scripts d'installation de Lutris

![Exemple de programmes d'installation Lutris|623x500, 75%](../img/Lutris_Setup_Installers.png)

Lutris est un logiciel de gestion de jeux qui sert également d'interface WINE pour les jeux Windows. Il est possible d'installer plusieurs jeux et lauchers en recherchant le titre et en utilisant l'un des scripts d'installation.

#### Raccourcis Lutris

![Menu contextuel de Lutris|421x447, 75%](../img/Lutris_Setup_Shortcut.png)

Un clic droit sur un jeu dans Lutris permet de l'ajouter en tant que jeu non-Steam (utile pour le mode de jeu Steam), de créer un raccourci sur le bureau ou un raccourci dans le menu des applications.

## Autres lanceurs de jeux

Bazaar peut installer d'autres launchers comme [**Heroic Games Launcher**](https://flathub.org/fr/apps/com.heroicgameslauncher.hgl) (pour les jeux GOG/Epic/Amazon) ou encore [**Faugus**](https://flathub.org/fr/apps/io.github.Faugus.faugus-launcher).