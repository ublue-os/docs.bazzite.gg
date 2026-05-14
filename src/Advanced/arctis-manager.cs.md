---
title: Installing Arctis Manager
authors:
  - "@elegos"
  - "@ifeign"
  - "@rdamron"
tags:
  - Community
search:
  exclude: true
---

# Instalace Arctis Manager

## Účel
Tato příručka vás provede instalací [**Linux-Arctis-Manager**](https://github.com/elegos/Linux-Arctis-Manager) (v2.0.4+) pomocí Distroboxu. Tato metoda funguje bez vrstvení balíčků nebo dočasného vypnutí kořenového souborového systému pouze pro čtení a zároveň poskytuje správci nezbytný přístup k hardwaru a služby na pozadí. Seznam aktuálně podporovaných zařízení a pokročilou dokumentaci naleznete v propojeném úložišti.

## Instalace 

Pro instalaci spusťte následující skript:

```bash
curl -LsSf https://raw.githubusercontent.com/elegos/Linux-Arctis-Manager/refs/heads/develop/scripts/distrobox.sh | sh
```

!!! note
    
    Pro operační systémy Linux, jako je Bazzite (kořenový souborový systém založený na obrazech / pouze pro čtení), se aplikace chová jako nativní instalace, nikoli jako izolovaný kontejner. Protože Distrobox připojuje vaše `/home`, `/var` a `/etc` přímo, může správce pracovat se systémovými službami a konfiguračními soubory, které potřebuje ke svému fungování.

### Povolit automatické spuštění (volitelné)
Chcete-li ikonu na hlavním panelu spustit automaticky při přihlášení, zkopírujte její položku na ploše do složky automatického spuštění:

```bash
cp ~/.local/share/applications/ArctisManagerSystray.desktop ~/.config/autostart/
```