---
title: "Best Shell Practices"
---

# Best Shell Practices

## Changing the default terminal shell

!!! note

    *The procedure for changing the default terminal on Bazzite is the same as that for [Project Bluefin](https://projectbluefin.io/) since both are based on [Universal Blue](https://universal-blue.org/). These instructions are adapted from the [Project Bluefin docs](https://docs.projectbluefin.io/).*

Bazzite ships [Konsole](https://apps.kde.org/konsole/) as the default terminal. It shows up as Konsole in the menu. It is **strongly recommended** that you [change your shell via the terminal emulator instead of system-wide](https://tim.siosm.fr/blog/2023/12/22/dont-change-defaut-login-shell/). Click on the hamburger menu in the top right, then Settings -> Configure Konsole. Go to Profiles and edit your own profile:

![Konsole Edit Profile](../img/Konsole_Edit_Profile.png)

Then use the "Command" box to add the shell you want to use. `/usr/bin/fish` is included on the image and other shells like ZSH may be installed with Homebrew:

![Konsole Fish Command](../img/Konsole_Fish_Command.png)
