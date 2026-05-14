[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/bazzite-org/docs.bazzite.gg)

# Přispívání k dokumentaci Bazzite MkDocs

- [Přispíváme k dokumentaci Bazzite MkDocs](#contributing-to-bazzite-mkdocs-documentation)
  - [Úvod](#úvod)
  - [Pokyny pro dokumentaci](#documentation-guidelines)
    - [1. Interní odkazy](#1-interní-linky)
    - [2. Vyhněte se používání záhlaví h1 (`#`) na stránkách](#2-nepoužívejte-na-stránkách-záhlaví-h1)
  - [Co je MkDocs?](#what-is-mkdocs)
  - [Setup MkDocs Tooling](#setup-mkdocs-tooling)
    - [1. Vytvořte soubor markdown, do kterého uložíme náš dokument.](#1-create-the-markdown-file-where-we-new-store-our-document)
    - [2. Nastavte správný název stránky](#2-set-a-proper-page-name)
  - [Přeložit dokumentaci](#translate-documentation)

## Úvod

Toto je průvodce, který vám ukáže, jak napsat dokumentaci pro [operační systém Bazzite](https://bazzite.gg).

## Pokyny k dokumentaci

### 1. Interní odkazy

Nepoužívejte absolutní adresy URL směřující na interní stránky v dokumentaci (https://docs.bazzite.gg).

Místo toho:

- Používejte relativní cesty
  - `./index.md`
  - `../Handheld_and_HTPC_edition/Steam_Gaming_Mode.md`
- Použít absolutní cesty\*
  - `/General/Installation_Guide/Installing_Bazzite_for_Handheld_PCs.md`

<small>\* Absolutní cesty jsou relativní k `docs_dir` deklarovaným v [mkdocs.yml](./mkdocs.yml). V tomto případě `src/`.</small>

### 2. Nepoužívejte na stránkách záhlaví h1 (`#`).

Místo toho použijte záhlaví h2 (`##`).

Pokud opravdu potřebujete, používejte `#` pouze a výhradně pro názvy stránek a pouze jednou na stránku.

## Co je MkDocs?

> _MkDocs je rychlý, jednoduchý a vyloženě nádherný generátor statických stránek, který je zaměřen na tvorbu projektové dokumentace. Zdrojové soubory dokumentace jsou psány v Markdown a konfigurovány pomocí jediného konfiguračního souboru YAML._
>
> Zdroj ~ https://www.mkdocs.org/

**TL;DR**: Je to skvělý nástroj, který nám umožňuje vytvořit dokumentační web se základním [Markdown](https://commonmark.org/help/).

Nezbytnou součástí, která v MkDocs nemůže chybět, je soubor `mkdocs.yml`.

`mkdocs.yml` funguje jako náš hlavní konfigurační soubor. Jedním z jeho hlavních úkolů je konfigurace **Obsahu** a konfigurace překladových souborů.

## Nastavení nástroje MkDocs

> ⚠️ UPOZORNĚNÍ ⚠️
>
> Tento krok je **vyžadován** pro nastavení náhledů výsledných MkDocs.

Chcete-li nainstalovat naše závislosti, spusťte toto:

```sh
bash utils/install-deps.sh
```

<details>
<summary>
<big>Seznam závislostí</big><br>
<sup>Ignorujte, pokud používáte install-deps.sh</sup>
</summary>

- [uv](https://docs.astral.sh/uv/) (lze nainstalovat s Homebrew)
- [Just](https://just.systems/man/en/) (předinstalovaný ve všech obrazech [Universal Blue](https://universal-blue.org/))

</details>

Chcete-li spustit dev-server MkDocs a zobrazit náhled dokumentace Bazzite, spusťte toto:

```sh
just mkdocs serve
```

Budete potřebovat i další nástroje, např.

- Editor kódu kompatibilní s markdown (např.: **Visual Studio Code**)
- **git** (je předinstalovaný ve většině distribucí Linuxu)

### 1. Vytvořte soubor markdown, kam budeme ukládat náš dokument

> ⚠️ UPOZORNĚNÍ
>
> Pamatujte: ⚠️**NEPOUŽÍVEJTE MEZERY V NÁZVU SOUBORU!**⚠️ Mezery v názvech souborů způsobí problémy v budoucnu.
> Místo toho použijte podtržítka `_`

### 2. Nastavte správný název stránky

Pomocí metadat YAML můžete přidat explicitnější názvy stránek (používané názvy karet prohlížeče).

Přidáním tohoto na začátek souboru markdown by se změnil název karty na „Ahoj světe“:

```yaml
---
title: "Hello world"
---
```

## Přeložte dokumentaci

Překlad dokumentace je tak jednoduchý, jak jen může být.
Řekněme, že chceme přeložit `index.md` do španělštiny. Jediné, co byste museli udělat, je vytvořit kopii souboru s názvem `index.es.md` a začít překládat.

Možná nevidíte svůj překlad pomocí `just mkdocs serve`.
Je pravděpodobné, že k tomu budeme muset nakonfigurovat MkDocs.

Otevřete `mkdocs.yml`, vyhledejte pole `languages`, mělo by vypadat nějak takto:

```yaml
languages:
   - locale: en
      default: true
      name: English
      build: true
```

Přidejte svůj jazyk, v našem případě je to španělština:

```yaml
languages:
   - locale: en
      default: true
      name: English
      build: true
   - locale: es
      name: Spanish
      build: true
```

MkDocs by měl v horní liště zobrazit výběr jazyka.