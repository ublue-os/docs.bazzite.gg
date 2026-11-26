---
title: "Osvědčené postupy pro shell"
---

# Osvědčené postupy pro shell

## Změna výchozího shellu terminálu

!!! note

    *Postup pro změnu výchozího terminálu na Bazzite je stejný jako u [Project Bluefin](https://projectbluefin.io/), protože oba jsou založeny na [Universal Blue](https://universal-blue.org/). Tyto pokyny jsou převzaty z [dokumentů projektu Bluefin](https://docs.projectbluefin.io/).*

Bazzite dodává [Konsole](https://apps.kde.org/konsole/) jako výchozí terminál. V nabídce se zobrazí jako `Konsole`. **Důrazně doporučujeme**, abyste [změnili svůj shell prostřednictvím emulátoru terminálu místo celosystémového](https://tim.siosm.fr/blog/2023/12/22/dont-change-defaut-login-shell/). Klikněte na hamburger menu vpravo nahoře, poté Nastavení -> Konfigurovat Konsole. Přejděte na Profily a upravte svůj profil:

![Konsole Edit Profile](../img/Konsole_Edit_Profile.png)

Poté použijte pole "Příkaz" pro přidání shellu, který chcete použít. `/usr/bin/fish` je součástí obrazu a další shelly jako ZSH lze nainstalovat s Homebrew:

![Konsole Fish Command](../img/Konsole_Fish_Command.png)