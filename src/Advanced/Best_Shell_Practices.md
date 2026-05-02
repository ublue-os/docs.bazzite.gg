---
title: "Best Shell Practices"
---

# Best Shell Practices

## Changing the default terminal shell

!!! note

    *The procedure for changing the default terminal on Bazzite is the same as that for [Project Bluefin](https://projectbluefin.io/) since both are based on [Universal Blue](https://universal-blue.org/). These instructions are adapted from the [Project Bluefin docs](https://docs.projectbluefin.io/).*

Bazzite ships [Konsole](https://apps.kde.org/konsole/) as the default terminal. It shows up as `Konsole` in the menu. It is **strongly recommended** that you [change your shell via the terminal emulator instead of system-wide](https://tim.siosm.fr/blog/2023/12/22/dont-change-defaut-login-shell/). Click on the hamburger menu in the top right, then Settings -> Configure Konsole. Go to Profiles and edit your your own profile:

![image](https://github.com/user-attachments/assets/3c751d84-8209-43ec-a204-a429f1b4a814)

Then use the "Command" box to add the shell you want to use. `/usr/bin/fish` is included on the image and other shells like ZSH may be installed with Homebrew:

![image](https://github.com/user-attachments/assets/618f11f9-8f5f-4a8d-8ddf-c839caab05f2)
