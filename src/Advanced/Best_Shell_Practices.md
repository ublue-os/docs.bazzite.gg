---
title: "Best Shell Practices"
---

# Best Shell Practices

## Changing the default terminal shell

!!! note

    *The procedure for changing the default terminal on Bazzite is the same as that for [Project Bluefin](https://projectbluefin.io/) since both are based on [Universal Blue](https://universal-blue.org/). These instructions are adapted from the [Project Bluefin docs](https://docs.projectbluefin.io/).*

Bazzite ships [Konsole](https://apps.kde.org/konsole/) as the default terminal. It shows up as `Konsole` in the menu. It is **strongly recommended** that you [change your shell via the terminal emulator instead of system-wide](https://tim.siosm.fr/blog/2023/12/22/dont-change-defaut-login-shell/). Click on the Terminal settings and edit your profile:

![image](https://github.com/user-attachments/assets/2c122205-dbd8-41e6-8b7b-4f536c3b69e9)

Then select "Use Custom Command" and add the shell you want to use. `/usr/bin/fish` is included on the image and other shells like ZSH may be installed with Homebrew:

![image](../img/ptyxis-custom-command.png)
