---
title: bazzite-cli
---

# `bazzite-cli`

## Co je `bazzite-cli`?

### Seznam nástrojů CLI

Možnost přihlášení do příkazového řádku Bazzite. `bazzite-cli` přichází s nástroji příkazového řádku, jako jsou:

- [**atuin**](https://github.com/atuinsh/atuin) – Nástroj pro synchronizaci historie prostředí mezi počítači.
– [**bash-preexec**](https://github.com/rcaloras/bash-preexec) – Háčky před spuštěním a před příkazy pro Bash (vyžaduje atuin).
- [**bat**](https://github.com/sharkdp/bat) - Klon `cat` se zvýrazněním syntaxe a integrací Git.
- [**chezmoi**](https://www.chezmoi.io/) – Nástroj pro správu souborů dot na více počítačích.
- [**direnv**](https://direnv.net/) - Přepínač prostředí pro shell.
- [**dysk**](https://github.com/Canop/dysk) – Nástroj pro Linux k získání informací o souborových systémech.
- [**eza**](https://github.com/eza-community/eza) - Moderní náhrada za příkaz `ls`.
- [**fd**](https://github.com/sharkdp/fd) – Jednoduchá, rychlá a uživatelsky přívětivá alternativa k `find`.
- [**gh**](https://cli.github.com/) - Oficiální nástroj příkazového řádku GitHub.
– [**glab**](https://gitlab.com/gitlab-org/cli) – Oficiální nástroj příkazového řádku GitLab.
- [**ripgrep**](https://github.com/BurntSushi/ripgrep) - Rychlý rekurzivní vyhledávač souborů, který respektuje `.gitignore`.
– [**shellcheck**](https://www.shellcheck.net/) – Nástroj pro statickou analýzu skriptů shellu.
- [**starship**](https://starship.rs/) – Minimální, bleskově rychlá a nekonečně přizpůsobitelná výzva pro jakýkoli shell.
- [**stress-ng**](https://github.com/ColinIanKing/stress-ng) – Nástroj pro zátěžové testování pro Linux.
- [**tealdeer**](https://github.com/dbrgn/tealdeer) - Rychlý klient pro zjednodušené manuálové stránky `tldr`.
– [**television**](https://github.com/alexpasmantier/television) – Ohromně rychlý univerzální fuzzy vyhledávač TUI.
- [**trash-cli**](https://github.com/andreafrancia/trash-cli) - Rozhraní příkazového řádku do koše freedesktop.org.
- [**ugrep**](https://github.com/Genivia/ugrep) - Rychlejší a uživatelsky přívětivá náhrada za `grep`.
– [**yq**](https://github.com/mikefarah/yq) – Procesor příkazového řádku pro data YAML, JSON a XML.
- [**zoxide**](https://github.com/ajeetdsouza/zoxide) - Chytřejší příkaz `cd`, který se naučí vaše návyky.

Komunita může časem přidat nové nástroje, opětovné spuštění `ujust bazzite-cli` je nainstaluje.

## Použití `bazzite-cli` s alternativními shelly

`bazzite-cli` pro fish nebo zsh můžete povolit tak, že před příkazem předpíšete přepsání proměnné $SHELL pomocí:

```
SHELL=fish ujust bazzite-cli
SHELL=zsh ujust bazzite-cli
# Or do it all at once from bash with
ujust bazzite-cli && SHELL=fish ujust bazzite-cli && SHELL=zsh ujust bazzite-cli
```