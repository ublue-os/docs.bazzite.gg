---
title: Containers
---

# Kontejnery

## Co jsou kontejnery?

Kontejnery jsou izolovaná prostředí pro běh softwaru.  Bazzite využívá kontejnery v softwarovém kontextu pro aplikace, které buď fungují lépe v prostředí kontejnerů, nebo nejsou dostupné v obchodě s aplikacemi Bazaar.

## Distrobox

[**Distrobox**](./Distrobox.md) umožňuje uživatelům spouštět další minimální verze operačních systémů Linux v jejich vlastním kontejnerovém prostředí s přístupem k jejich vlastním úložištím.  Příklady ze skutečného světa zahrnují aplikace, které podporují pouze Linux pro Ubuntu a dodávají soubor `.deb` na své webové stránky.  Kontejner Ubuntu lze vytvořit pomocí DistroShelf a poté lze do kontejneru nainstalovat soubor `.deb` a exportovat jej tak, aby se objevil ve vašich aplikacích.

[**Quadlet**](./Quadlet.md) se specificky používá pro spouštění služeb, jako jsou mediální servery, herní servery atd. Quadlet je ve srovnání s jinými formáty balíčků pokročilý a hodně se spoléhá na nástroje na systémové úrovni, které jsou předinstalované na Bazzite. Neexistuje žádný příkaz `quadlet` a vyžaduje deklarativní vytváření služeb pomocí jednotek systemd a Podman.