---
title: bazzite-cli
---

# `bazzite-cli`

## Що таке `bazzite-cli`? { #what-is-bazzite-cli }

### Список інструментів командного рядка { #list-of-cli-tools }

Розширений командний рядок Bazzite, який вмикається за бажанням. `bazzite-cli` містить такі інструменти командного рядка:

- [**atuin**](https://github.com/atuinsh/atuin) — синхронізація історії оболонки між комп'ютерами.
- [**bash-preexec**](https://github.com/rcaloras/bash-preexec) — хуки перед виконанням і перед командою для Bash (потрібні для atuin).
- [**bat**](https://github.com/sharkdp/bat) — аналог `cat` із підсвічуванням синтаксису й інтеграцією з Git.
- [**chezmoi**](https://www.chezmoi.io/) — керування dotfiles на кількох комп'ютерах.
- [**direnv**](https://direnv.net/) — перемикач середовища для оболонки.
- [**dysk**](https://github.com/Canop/dysk) — утиліта Linux для отримання інформації про файлові системи.
- [**eza**](https://github.com/eza-community/eza) — сучасна заміна команди `ls`.
- [**fd**](https://github.com/sharkdp/fd) — проста, швидка й зручна альтернатива `find`.
- [**gh**](https://cli.github.com/) — офіційний інструмент командного рядка GitHub.
- [**glab**](https://gitlab.com/gitlab-org/cli) — офіційний інструмент командного рядка GitLab.
- [**ripgrep**](https://github.com/BurntSushi/ripgrep) — швидкий рекурсивний пошук у файлах, який враховує `.gitignore`.
- [**shellcheck**](https://www.shellcheck.net/) — інструмент статичного аналізу скриптів оболонки.
- [**starship**](https://starship.rs/) — мінімалістичне, надзвичайно швидке й гнучко налаштовуване запрошення для будь-якої оболонки.
- [**stress-ng**](https://github.com/ColinIanKing/stress-ng) — інструмент стрес-тестування для Linux.
- [**tealdeer**](https://github.com/dbrgn/tealdeer) — швидкий клієнт для спрощених довідкових сторінок `tldr`.
- [**television**](https://github.com/alexpasmantier/television) — надзвичайно швидкий універсальний нечіткий пошук із текстовим інтерфейсом (TUI).
- [**trash-cli**](https://github.com/andreafrancia/trash-cli) — інтерфейс командного рядка для кошика freedesktop.org.
- [**ugrep**](https://github.com/Genivia/ugrep) — швидша й зручніша заміна `grep`.
- [**yq**](https://github.com/mikefarah/yq) — обробник даних YAML, JSON і XML для командного рядка.
- [**zoxide**](https://github.com/ajeetdsouza/zoxide) — розумніша команда `cd`, яка запам'ятовує ваші звички.

Спільнота з часом може додавати нові інструменти, і повторний запуск `ujust bazzite-cli` встановить їх.

## Використання `bazzite-cli` з іншими оболонками { #using-bazzite-cli-with-alternate-shells }

Щоб увімкнути `bazzite-cli` для fish або zsh, додайте перед командою перевизначення змінної $SHELL:

```
SHELL=fish ujust bazzite-cli
SHELL=zsh ujust bazzite-cli
# Or do it all at once from bash with
ujust bazzite-cli && SHELL=fish ujust bazzite-cli && SHELL=zsh ujust bazzite-cli
```
