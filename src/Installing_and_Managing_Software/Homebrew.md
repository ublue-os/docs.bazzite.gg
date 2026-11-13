---
title: Homebrew
---

# Homebrew

## What is Homebrew?

![Homebrew|332x500, 15%](../img/Homebrew.png)

!!! note

    Any [formula](#formulae-and-casks) that requires root privileges will either need a rootful Distrobox container or has to be layered with `rpm-ostree`.

Homebrew is a package manager that installs packages into their own prefix. It is primarily used for command-line interface (CLI) and terminal user interface (TUI) applications. Homebrew can also install graphical applications using the `--cask` flag, but most are for macOS as support for casks on Linux is still developing. Use the Bold Brew application or the terminal using the command below to install packages.

Install packages in a host terminal with this **terminal command**:

```
brew install <package>
```

!!! note

    For multiple user or atypical setups only: Root privileges (`sudo`) will be required to install Homebrew packages because it uses the `linuxbrew` user to install them.

## Formulae and casks

Homebrew installs two kinds of packages:

- **Formulae** are command-line programs, for example `go` or `node`. They are installed into the Homebrew prefix (`/home/linuxbrew/.linuxbrew`).
- **Casks** are ready-made applications, mostly graphical ones, and fonts. Graphical casks add a shortcut to the application menu. [Bazzite Portal](./Bazzite_Portal.md) installs some applications as casks, for example Visual Studio Code (`visual-studio-code-linux`).

The command above installs formulae. To install a cask, add `--cask`:

```
brew install --cask <cask>
```

!!! note

    Some casks change system files, for example to add a system service. These casks can ask for your password with `sudo` when you install, upgrade or remove them. If an automatic update cannot upgrade such a cask, upgrade it manually in a terminal:

    ```
    brew upgrade --cask <cask>
    ```

    If the password prompt does not appear and the command fails with a `sudo` error, run it like this instead. This makes `sudo` ask for the password in the terminal rather than in a separate window:

    ```
    env -u SUDO_ASKPASS brew upgrade --cask <cask>
    ```

## Bold Brew

![bbrew|3164x2060, 25%](../img/bbrew-installed-screenshot.png)

The [Bold Brew application](https://bold-brew.com/) offers a terminal user interface (TUI) for installing common Homebrew packages.

## Fonts

Homebrew is also used for installing fonts, browse [this page](https://formulae.brew.sh/cask-font/) and install your favorite fonts. They will be copied into `~/.local/share/fonts`

- Microsoft Fonts:

If you need to install Microsoft fonts in order to ensure compatibility with some documents, most of them are in Homebrew.

Be aware that some of these fonts are copyrighted by Microsoft.
Microsoft UK confirmed you are allowed to have them, provided that you own a copy of either:

- Microsoft PowerPoint Viewer (free, retired)
- May include PowerPoint Mobile (free)
- Microsoft Office (Any version, Windows or Mac)

Calibri, Cambria, Candara, Consolas, Constantia and Corbel are included in font-microsoft-office, the others must be installed individually. You can install all of them at once by running the following command in a terminal:

```
brew tap colindean/fonts-nonfree && brew install --cask font-microsoft-office font-microsoft-aptos font-arial font-arial-black font-courier-new font-times-new-roman font-georgia
```

## Project Website

https://brew.sh/
