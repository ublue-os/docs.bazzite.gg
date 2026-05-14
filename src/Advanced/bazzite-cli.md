---
title: bazzite-cli
---

# `bazzite-cli`

## What is `bazzite-cli`?

### List of CLI Tools

Bazzite's opt-in command line experience. `bazzite-cli` comes with command line tools such as:

- [**atuin**](https://github.com/atuinsh/atuin) - A tool for syncing shell history across machines.
- [**bash-preexec**](https://github.com/rcaloras/bash-preexec) - Pre-execution and pre-command hooks for Bash (required by atuin).
- [**bat**](https://github.com/sharkdp/bat) - A `cat` clone with syntax highlighting and Git integration.
- [**chezmoi**](https://www.chezmoi.io/) - A tool to manage dotfiles across multiple machines.
- [**direnv**](https://direnv.net/) - An environment switcher for the shell.
- [**dysk**](https://github.com/Canop/dysk) - A Linux utility to get information on filesystems.
- [**eza**](https://github.com/eza-community/eza) - A modern replacement for the `ls` command.
- [**fd**](https://github.com/sharkdp/fd) - A simple, fast, and user-friendly alternative to `find`.
- [**gh**](https://cli.github.com/) - The official GitHub command-line tool.
- [**glab**](https://gitlab.com/gitlab-org/cli) - The official GitLab command-line tool.
- [**ripgrep**](https://github.com/BurntSushi/ripgrep) - A fast recursive file searcher that respects `.gitignore`.
- [**shellcheck**](https://www.shellcheck.net/) - A static analysis tool for shell scripts.
- [**starship**](https://starship.rs/) - A minimal, blazing-fast, and infinitely customizable prompt for any shell.
- [**stress-ng**](https://github.com/ColinIanKing/stress-ng) - A stress testing tool for Linux.
- [**tealdeer**](https://github.com/dbrgn/tealdeer) - A fast client for simplified `tldr` man pages.
- [**television**](https://github.com/alexpasmantier/television) - A blazingly fast general purpose fuzzy finder TUI.
- [**trash-cli**](https://github.com/andreafrancia/trash-cli) - A command line interface to the freedesktop.org trashcan.
- [**ugrep**](https://github.com/Genivia/ugrep) - A faster, user-friendly `grep` replacement.
- [**yq**](https://github.com/mikefarah/yq) - A command-line processor for YAML, JSON, and XML data.
- [**zoxide**](https://github.com/ajeetdsouza/zoxide) - A smarter `cd` command that learns your habits.

The community may add new tools over time, re-running `ujust bazzite-cli` will install them.

## Using `bazzite-cli` With Alternate Shells

You can enable `bazzite-cli` for fish or zsh by pre-pending an override to the $SHELL variable to the command with:

```
SHELL=fish ujust bazzite-cli
SHELL=zsh ujust bazzite-cli
# Or do it all at once from bash with
ujust bazzite-cli && SHELL=fish ujust bazzite-cli && SHELL=zsh ujust bazzite-cli
```
