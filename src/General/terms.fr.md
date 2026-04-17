---
title: Dictionnaire et terminologie
---

# Dictionnaire et terminologie

## Général

- **[Linux pour ordinateurs de bureau](https://www.ubuntudocs.com/bdesktop/)** : Une famille de systèmes d'exploitation qui partagent des mêmes logiciels de base, notamment le [noyau Linux](https://www.kernel.org/), [systemd](https://systemd.io/) et les [utilitaires GNU](https://www.gnu.org/software/coreutils/).
- **[Environnement de bureau](https://fr.wikipedia.org/wiki/Environnement_de_bureau)** : L'interface utilisateur graphique (UI) et l'expérience utilisateur (UX) pour le mode Bureau/images de bureau de Bazzite. Également appelé *DE*.
- **[Fedora Linux](https://fedoraproject.org/fr/)** : un système d'exploitation Linux de pointe qui propose une nouvelle version majeure tous les 6 mois.
- **[Fedora Atomic Desktop](https://fedoraproject.org/fr/atomic-desktops/)** : une version expérimentale de Fedora Linux conçue pour être aussi fiable et réplicable que possible. 2 des variantes les plus populaires sont connues sous les noms de [Fedora Silverblue](https://fedoraproject.org/fr/atomic-desktops/silverblue/) et [Fedora Kinoite](https://fedoraproject.org/fr/atomic-desktops/kinoite/) en raison des environnements de bureau spécifiques qu'elles utilisent (GNOME et KDE Plasma respectivement).
- ["**Immutable**"](https://blog.verbum.org/2020/08/22/immutable-%E2%86%92-reprovisionable-anti-hysteresis/) : terme utilisé pour désigner les systèmes d'exploitation Linux qui ne suivent pas la structure traditionnelle du système de fichiers, dans laquelle chaque fichier peut être supprimé par l'utilisateur disposant des privilèges root.  La réalité est plus [nuancée dans le cas de Bazzite](https://docs.fedoraproject.org/fr/atomic-desktops/technical-information/#filesystem-layout), et est souvent considérée à tort comme "immutable" du point de vue de la communauté Linux au sens large.  L'équipe Bazzite ne décrit **pas** Bazzite comme un système d'exploitation "immutable".
- [**Open Gaming Collective (OGC)**](https://github.com/OpenGamingCollective) : un groupe de travail destiné aux organisations et aux particuliers souhaitant fournir un cadre collaboratif pour les modifications des différents composants de jeux, qui profitera à tous les projets Linux axés sur le jeu.

## Images Bazzite-Deck

- **[Steam Deck](https://store.steampowered.com/steamdeck)** : la console portable de Valve qui utilise son propre système d'exploitation, basé sur Linux et articulé autour du [client Steam](https://store.steampowered.com/about/download).
- **[SteamOS](https://www.steamdeck.com/en/software)** : le système d'exploitation Linux de Valve basé sur [Arch Linux](https://archlinux.org/) qui fait fonctionner la Steam Deck.
- **[Gamescope](https://github.com/ValveSoftware/gamescope)** : micro-compositeur développé pour SteamOS.  Il permet notamment la mise à l'échelle, le filtrage, la limitation de la fréquence d'images et la prise en charge du HDR.
- **[Mode Jeu Steam](https://github.com/KyleGospo/gamescope-session)** : session qui exécute l'interface utilisateur du mode Big Picture de Steam au sein de Gamescope.  Également appelé *Mode Jeu*.

## Logiciels

- **[Proton](https://github.com/ValveSoftware/Proton)** : Couche de compatibilité axée sur le jeu vidéo, maintenue par Valve, permettant d'exécuter des jeux Windows à l'aide de [WINE](https://www.winehq.org/), [DXVK](https://github.com/doitsujin/dxvk), [VKD3D](https://github.com/HansKristian-Work/vkd3d-proton) et d'autres composants.
- [**Vulkan**](https://www.vulkan.org/) : API graphique multiplateforme et open source dérivée de Mantle d'AMD, conçue comme une alternative à DirectX, exclusive à Windows.
- [**OpenGL**](https://www.opengl.org/) : API graphique héritée utilisée lorsque Vulkan n'est pas disponible.
- **[Flatpak](https://flatpak.org/)** : applications universelles pour Linux.  Le dépôt par défaut provient de [Flathub](https://flathub.org/fr).
- [**Conteneurs**](https://www.redhat.com/fr/topics/containers) - Environnements isolés pour les logiciels.

## Technologies associées

- **[OSTree/libostree](https://ostreedev.github.io/ostree/introduction/)** : Système de mise à jour utilisé par Bazzite, permettant de revenir à des mises à jour précédentes ou de rebaser complètement le système sur d'autres images.
- **[Handheld Daemon (HHD)](https://github.com/hhd-dev/hhd)** : logiciel d'activation matérielle pour appareils portables offrant des fonctionnalités sur les contrôleurs, de gestion de l'alimentation, de RGB, et plus encore.
- **[Universal Blue](https://ublue.it)** : collectif Open Source spécialisé dans les images Fedora personnalisées.
- **[Image de conteneur amorçable](https://docs.fedoraproject.org/fr/bootc/getting-started/)** : logiciels et services regroupés dans un conteneur qui s'exécute par-dessus un système d'exploitation existant (comme Fedora) afin de fournir un système d'exploitation spécialisé.  Également appelé [*image personnalisée*](../Advanced/creating_custom_image.md).
- **[Natif Cloud](https://aws.amazon.com/what-is/cloud-native/)** : Création et déploiement automatisés de logiciels. Offre des fonctionnalités telles que les mises à jour en direct, plusieurs images recevant les mêmes mises à jour en amont, etc.  Dans le cas de Bazzite, chaque mise à jour est effectuée sur [Github](https://github.com/ublue-os/bazzite/).