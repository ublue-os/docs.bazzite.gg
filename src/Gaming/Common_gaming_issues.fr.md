---
title: Problèmes courants liés aux jeux
---

# Problèmes courants liés aux jeux

### Portage natif sous Linux par rapport à la version Windows

Certains portages sous Linux peuvent avoir des fonctionnalités manquantes ou offrir des performances inférieures à celles de la version Windows exécutée via Proton. Il existe des cas où l'utilisation exclusive du portage natif est votre seule option, voire la plus intéressante.  

Si un jeu natif Linux ne se lance pas, forcez la couche de compatibilité **Legacy Runtime** en accédant aux **propriétés du jeu**, puis en sélectionnant "**Compatibilité**", en cochant "**Forcer l'utilisation d'un outil de compatibilité Steam Play spécifique**" et en le sélectionnant.

### Jeux verrouillés par le DRM Denuvo

Les jeux utilisant le DRM Denuvo considèrent le changement de version de Proton comme une activation du jeu sur un matériel différent, ce qui peut vous empêcher d'accéder au jeu si vous changez de version de Proton plus de 5 fois au cours d'une période de 24 heures.

## Problèmes audio et de contenu personnalisé avec le moteur Source 1

!!! note

    Ceci ne s'applique qu'à certains jeux fonctionnant sur le [moteur Source](https://fr.wikipedia.org/wiki/Source_(moteur_de_jeu)).

!!! attention

    N'essayez **pas** d'appliquer cette solution tant que vous n'avez pas rencontré de problèmes audio ou que vous n'êtes pas confronté au problème mentionné ci-dessous concernant _Left 4 Dead 2_.

Des répliques vocales manquantes ou du contenu personnalisé qui ne se charge pas dans les jeux Source ? SELinux bloque le décodage MP3 et d'autres "middlewares" car il [**exécute la mémoire heap**](https://github.com/ValveSoftware/steam-for-linux/issues/43).

Il a également été confirmé que cela causait des problèmes pour rejoindre et héberger des cartes personnalisées dans _Left 4 Dead 2_.

### Solution aux problèmes liés à l'audio et au contenu personnalisé

!!! warning

    La configuration de SELinux est réservée aux utilisateurs avancés ; une utilisation inappropriée peut endommager d'autres composants de votre configuration et compromettre la sécurité de votre appareil.

Ouvrez un terminal et **exécutez ces 4 commandes à vos propres risques** :

```command
sudo su
```

```command
cd /tmp
```

```command
ausearch -c “hl2_linux” --raw | audit2allow -M my-hl2linux
```

```command
semodule -X 300 -i my-hl2linux.pp
```

Redémarrez votre machine et vérifiez si le jeu Source présente toujours des problèmes.

### Annuler cette modification

**Désactivez ou supprimez le module.**

#### Désactiver la modification

```command
semodule -X 300 -d my-hl2linux
```

##### Supprimer la modification

```command
semodule -X 300 -r my-hl2linux
```

Le fichier `.pp` devrait se trouver dans `/root` si vous voulez le supprimer.

## Les jeux Steam ne se lancent pas

Les jeux Steam peuvent ne pas se lancer pour diverses raisons.

### Récupération des fichiers journaux Steam

Si vous rencontrez des problèmes lors du lancement d'un jeu sur Steam :

1. Ouvrez les propriétés du jeu et **saisissez cette option de lancement** :
   `PROTON_LOG=1 %command%`

2. Lancez le jeu

Un fichier log devrait apparaître dans votre répertoire personnel, nommé d'après le numéro d'identification de l'application du jeu.

### Problèmes d'autorisation sur les disques formatés en NTFS

Assurez-vous que vos jeux ne se trouvent **pas** sur une partition NTFS (Windows). Vous trouverez plus d'informations [**ici**](./Hardware_compatibility_for_gaming.md#unsupported-filesystems-for-secondary-drives).

### Particularités de WINE en mode multi-utilisateurs

!!! note

    Bazzite-Deck ne prend pas en charge les multiples comptes utilisateurs, cette information s'applique uniquement à l'édition Desktop de Bazzite.

Il arrive parfois que les jeux Steam refusent complètement de se lancer sur un compte utilisateur secondaire. Cela peut être dû à la propriété des fichiers de préfixe WINE. Vous pourriez voir une erreur comme celle-ci dans ` ~/.local/share/Steam/logs/console-linux.txt ` sur le compte utilisateur secondaire :

```
wineserver: /SteamLibrary/steamapps/compatdata/377160/pfx is not owned by you
```

Vous pouvez résoudre ce problème en créant un dossier de bibliothèque Steam distinct pour stocker les données de préfixe de Proton, puis en créant un lien symbolique (_symlink_) vers les autres dossiers (comme les données communes des jeux).

```
USER2@bazzite: /mnt/ExtraStuff/USER2SteamLibrary/steamapps$ ls -la
total 32
drwxrwxr-x. 3 USER2 steamplayers 4096 Jan 29 15:19 .
drwxrwsr-x. 3 USER2 steamplayers 4096 Jan 29 16:13 ..
-rwxr-xr-x. 1 USER2 USER2         2287 Jan 29 15:19 appmanifest_377160.acf
lrwxrwxrwx. 1 USER2 USER2           51 Jan 29 15:10 common -> /mnt/ExtraStuff/USER1SteamLibrary/steamapps/common/
drwxr-xr-x. 3 USER2 USER2         4096 Jan 29 15:13 compatdata
lrwxrwxrwx. 1 USER2 USER2           56 Jan 29 15:12 shadercache -> /mnt/ExtraStuff/USER1SteamLibrary/steamapps/shadercache/
lrwxrwxrwx. 1 USER2 USER2           49 Jan 29 15:12 temp
lrwxrwxrwx. 1 USER2 USER2           53 Jan 29 15:12 workshop
```

De la même manière, copiez ou créez des liens symboliques vers les fichiers appmanifest de chaque bibliothèque afin que les jeux s'affichent correctement dans chaque bibliothèque Steam.