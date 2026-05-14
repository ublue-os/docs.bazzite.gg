---
title: Options de lancement et variables d'environnement
---

# Options de lancement et variables d'environnement

## Preface

Jouer à des jeux sous Linux est aujourd'hui bien plus intuitif qu'il y a quelques années. Il existe, tout de même,encore des options de lancement et des configurations avancées qui peuvent être utilisées depuis Bazzite. Ce guide montre des exemples de réglages avancés pouvant être effectués sur une installation Bazzite.

## Modèles de configuration pour DXVK, MangoHud et vkBasalt

![Modèle|690x334, 50%](../img/DXVK_Mango_VkBasalt_templ.png)

Les utilisateurs de Bazzite peuvent utiliser des modèles pour certains des outils préinstallés, accessibles en cliquant avec le bouton droit n'importe où dans le gestionnaire de fichiers. Il existe également des applications telles que [**Mango Juice**](https://flathub.org/fr/apps/io.github.radiolamp.mangojuice) qui permettent de configurer MangoHUD de manière graphique.

## Options de lancement et raccourcis Steam

Les options de lancement Steam vous permettent de transmettre des variables d'environnement, des arguments et des commandes au démarrage de vos jeux. Bazzite propose plusieurs raccourcis et améliorations afin de faciliter l'utilisation des options de lancement courantes, en particulier sur les appareils mobiles.

### Modèles courants d'options de lancement

La plupart des options de lancement Steam suivent ce modèle : `ENVIRONMENT_VARIABLES commande_ou_script %command%`

- `%command%` représente l'exécutable du jeu et doit être inclus
- Les variables d'environnement doivent être placées avant `%command%`
- Les arguments supplémentaires peuvent être placés après `%command%`

**Exemples :**
```
PROTON_LOG=1 %command%                    # Activer les logs Proton
SteamDeck=0 %command%                     # Désactiver le mode Steam Deck
PROTON_ENABLE_NGX_UPDATER=1 %command%     # Activer les mises à jour DLSS
```

### Raccourcis d'options de lancement de Bazzite

Bazzite propose plusieurs raccourcis pour simplifier les options de lancement courantes :

#### Pour le contrôle du mode Steam Deck
- **`sd0 %command%`** - Abréviation de `SteamDeck=0 %command%`
  - Désactive les fonctionnalités spécifiques à Steam Deck susceptibles d'entrer en conflit avec votre configuration
  - Exemple : Expedition 33 masque la plupart des paramètres graphiques à moins que vous ne définissiez `SteamDeck=0`, et force les paramètres les plus bas.

#### Pour les utilisateurs NVIDIA (dlss-swapper)
- **`dlss-swapper %command%`** - Active les derniers préréglages DLSS avec le programme de mise à jour NGX
  - Remplace : `PROTON_ENABLE_NGX_UPDATER=1 DXVK_NVAPI_DRS_SETTINGS=NGX_DLSS_SR_OVERRIDE=on, NGX_DLSS_RR_OVERRIDE=on,NGX_DLSS_FG_OVERRIDE=on,NGX_DLSS_SR_OVERRIDE_RENDER_PRESET_SELECTION=render_preset_latest,NGX_DLSS_RR_OVERRIDE_RENDER_PRESET_SELECTION=render_preset_latest %command%`
- **`dlss-swapper-dll %command%`** - Identique à ci-dessus, mais ignore le programme de mise à jour NGX

#### Où définir les options de lancement

1. Cliquez avec le bouton droit sur le jeu dans la bibliothèque Steam
2. Sélectionnez **Propriétés...**
3. Dans l'onglet Général, repérez le champ **Options de lancement**
4. Saisissez vos options de lancement

![Fenêtre Options de lancement|833x594, 75%](../img/Steam_Launch_Options.png)

## Problèmes liés à la limitation du taux de rafraîchissement

Lorsque vous utilisez Gamescope, les limites de taux de rafraîchissement peuvent être appliquées de plusieurs façons. Malheureusement, toutes les méthodes ne fonctionnent pas pour tous les environnements, tous les jeux ou toutes les configurations matérielles.

De nombreuses irrégularités peuvent être observées, en particulier lors de l'application de limites de taux de rafraîchissement en mode bureau.

Les tableaux ci-dessous montrent le comportement des différentes méthodes de limitation du taux de rafraîchissement.

### Mode Jeu Steam (session en mode Jeu Steam)

| Méthode | Étapes de configuration | V-Sync requis ? | Modif. de la limite sans redémarrer le jeu ? | Latence | Recommandation | Remarques |
|---|---|---|---|---|---|---|
| **Limiteur de FPS Gamescope** | Utilisez **Menu d'accès rapide > Performances > Limite de fréquence d'images** | Non | Oui | Moyenne | **Recommandé** | Active automatiquement le V-Sync au niveau du pilote dès que la limite de fréquence d'images est activée. Cela entraîne une latence supplémentaire. |
| **MangoAPP (intégré)** | N/A - ne fonctionne pas du tout. | - | - | - | – | Les paramètres de limitation de fréquence d'images de MangoAPP sont ignorés en mode jeu/mode deck. Utilisez plutôt le curseur ou MangoHUD externe. |
| **MangoHUD (externe)** | **Options de lancement :** `MANGOHUD=1 %command%` | Non | Oui | Bof | – | Définissez `fps_limit=0,30,60,120...` (0 = pas de limite) dans MangoHud.conf. Peut entrer en conflit avec MangoAPP. |
| **Limiteur de fréquence d'images en temps réel DXVK/VKD3D** | **DXVK (D3D8/9/10/11) :** `DXVK_FRAME_RATE={fps} %command%`<br>**VKD3D-Proton (D3D12) :** `VKD3D_FRAME_RATE={fps} %command%` | Non | Non | Optimal | – | S'applique uniquement aux titres DXVK/VKD3D (aucun effet sur OpenGL natif ou Vulkan natif). |


### Mode Bureau (session de bureau GNOME / KDE Plasma)

| Méthode | Étapes de configuration | V-Sync requis ? | Modif. de la limite sans redémarrer le jeu ? | Latence | Recommandation | Remarques |
|---|---|---|---|---|---|---|
| **Limiteur de FPS Gamescope** | **Options de lancement** : `gamescope -r {fps} -- %command%` / `--framerate-limit {fps}` | Oui | Oui | Moyen | – | Utilisez `gamescopectl debug_set_fps_limit {fps}` pour modifier la valeur du limiteur en direct sans redémarrer. |
| **MangoAPP (intégré)** | **Options de lancement :** `gamescope --mangoapp -- %command%` | Oui | Oui | Bof | – | Les limites ne sont parfois pas efficaces. Définissez `fps_limit=0,30,60,120...` (0 = pas de limite) dans MangoHud.conf (ou via `MANGOHUD_CONFIG=...`). Ajoutez `show_fps_limit` au préréglage pour l'afficher en jeu. Modifiez avec `ShiftL+F1`. |
| **MangoHUD (externe)** | **Options de lancement :** `MANGOHUD=1 gamescope -- %command%` | Non | Oui | Bof | **Recommandé** | Les limites sont presque toujours effectives. Définissez `fps_limit=0,30,60,120...` (0 = pas de limite) dans MangoHud.conf (ou via `MANGOHUD_CONFIG=...`). Ajoutez `show_fps_limit` au préréglage pour l'afficher en jeu. Modifiez-le avec `ShiftL+F1`. |
| **Limiteur de fréquence d'images en temps réel DXVK/VKD3D** | **DXVK (D3D8/9/10/11) :** `DXVK_FRAME_RATE={fps} %command%`<br>**VKD3D-Proton (D3D12) :** `VKD3D_FRAME_RATE={fps} %command%` | Non | Non | Optimal | – | Limites au niveau du processus/de l'API ; excellent timing, mais vous devez redémarrer pour modifier le paramètre. |


Si votre limiteur de fréquence d'images ne fonctionne pas, les étapes suivantes peuvent souvent vous aider :

1. Désactivez la synchronisation adaptative/VRR ou supprimez le paramètre `--adaptive-sync` de vos arguments Gamescope.
2. Activez la synchronisation verticale (vsync) dans le jeu.

## Gestion avancée des options de lancement pour ScopeBuddy

Pour les utilisateurs qui souhaitent une gestion plus complexe des options de lancement, consultez la **[documentation ScopeBuddy](../Advanced/scopebuddy.md)** pour une gestion encore plus avancée des options de lancement de Gamescope.
