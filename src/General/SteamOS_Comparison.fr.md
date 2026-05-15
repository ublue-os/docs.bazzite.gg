---
title: Comparaison avec SteamOS
---

# Comparaison avec SteamOS

## Qu'est-ce que SteamOS ?

**SteamOS** est un système d'exploitation initialement conçu pour le Steam Deck. SteamOS est un système d'exploitation destiné au client Steam et propose également un environnement de bureau avec **KDE Plasma** qui permet aux utilisateurs, par exemple, d'installer des mods et des émulateurs, mais qui peut s'avérer limité pour une utilisation bureautique.

## Qu'est-ce que Bazzite ?

Bazzite est un système d'exploitation Linux dédié au jeu vidéo et développé par la communauté, intégrant les derniers pilotes Linux et proposant plusieurs variantes (**Desktop (Bazzite)**, **Handheld/HTPC (Bazzite-Deck)** et **Developer eXperience (Bazzite-DX)**). Il est basé sur [**Fedora Linux**](https://fedoraproject.org/fr/) et intègre un [**système de mise à jour atomique**](https://github.com/bootc-dev/bootc), garantissant que la mise à jour précédente est toujours disponible en cas de problème.

Il est également conçu pour une utilisation quotidienne, avec un accent particulier sur le **jeu**, le **multimédia** et le **développement**. ‍ De plus, Bazzite intègre les derniers pilotes, vous pouvez donc être sûr que si votre appareil fonctionne sous Linux, il fonctionnera sous Bazzite. ‍ Bazzite prend en charge les GPU **AMD**, ainsi que les GPU **Nvidia** et **Intel** récents. Bazzite fonctionne également très bien avec les appareils portables **Lenovo**, **Asus**, **Ayn**, **GPD** et **OneXPlayer**.

### Améliorations supplémentaires de Bazzite par rapport à SteamOS

- Excellente prise en charge du **Dual Boot** avec **Windows**.
- Fonctionne sur la **plupart** des appareils portables x86 : Lenovo Legion Go/S, ASUS ROG Ally/X, variantes OneXPlayer F1/G1/X1, GPD Win 4/Mini/Max, Ayn Loki, MSI Claw 1ère génération AI7+/8+, Zotac Zone, Ayaneo Air/Geek/Next, Steam Deck LCD/OLED.
- Prise en charge du réglage du GPU et des ventilateurs des ordinateurs de bureau.
- **Mises à jour indolore**
  - Vous avez toujours accès à la **version précédente** via le bootloader.
  - Pour les appareils portables, Bazzite reviendra automatiquement à la version précédente après 3 démarrages infructueux.
  - Un **historique des mises à jour des 90 derniers jours** est disponible, et vous pouvez facilement revenir à n'importe quelle version à l'aide d'une simple commande ou via Handheld Daemon.
- Intègre les **derniers logiciels disponibles**, notamment le **noyau Linux**, les **pilotes graphiques** et [**Gamescope**](https://github.com/ValveSoftware/gamescope).
- **Logiciels utiles liés aux jeux**, tels que **Lutris, Umu-Launcher, ProtonUp-QT, Protontricks**, et bien d'autres.
- Accès à l'environnement de bureau **GNOME** comme alternative à KDE Plasma.
- Prise en charge native de la **virtualisation** et du **"pass-through GPU"**.
- Les **applications Android** peuvent être installées avec [Waydroid](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md).
- [`ujust`](/Installing_and_Managing_Software/ujust.md) : scripts pratiques permettant de configurer des logiciels et d'effectuer des réglages tels que le démarrage sécurisé, ainsi que d'installer des logiciels supplémentaires.
- Utilise le format de disque **BTRFS** avec **déduplication** et **compression** (SteamOS utilise **Ext4**) et prend en charge le **montage automatique** pour les **disques internes** et les **cartes SD**.

### Utilisation quotidienne

- Les paquets système sont mis à jour régulièrement.
- Wayland est utilisé en mode bureau, ce qui garantit un redimensionnement correct pour les écrans à haute résolution (DPI).
- La plupart des paquets suivent le cycle de vie de Fedora, sauf en cas de bugs, auquel cas le paquet est soit retiré de la distribution, soit corrigé avant Fedora.

### Pour les développeurs

- Accédez à plusieurs gestionnaires de paquets et dépôts dans des conteneurs à l'aide de [Distrobox](https://distrobox.it).
- [Homebrew](https://brew.sh/) est préinstallé pour les paquets en ligne de commande.
- [Layer](/Installing_and_Managing_Software/rpm-ostree.md) des paquets système Fedora qui restent entre les mises à jour du système.
- Consultez la section [Développement](https://dev.bazzite.gg) pour plus d'informations.

### Améliorations en matière de sécurité

Bazzite prend en charge le chiffrement de disque LUKS, le Secure Boot et le déverrouillage du disque chiffré via le TPM. Bazzite intègre également [SELinux (Security Enhanced Linux)](https://www.redhat.com/fr/topics/linux/what-is-selinux), qui est activé et préconfiguré par défaut.

La prise en charge du Secure Boot est également utile pour le Dual Boot avec Windows, car elle est requise par certains logiciels anti-triche. Pour en savoir plus, consultez le [**Guide du Secure Boot**](/General/Installation_Guide/secure_boot.md).
