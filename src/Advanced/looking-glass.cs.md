---
title: Looking Glass
---

# Instalace Looking Glass

## ČTĚTE NEJPRVE!
[Looking-Glass](https://looking-glass.io/) je velmi experimentální projekt a není připraven k produkčnímu použití!
To znamená, že zatím neexistují žádné oficiální balíčky pro `looking-glass-client`. <br>
Z tohoto důvodu `looking-glass-client` nezabalujeme ani nezasíláme, poskytujeme pouze funkční konfiguraci a pravidla SELinuxu, aby jej bylo možné použít v Bazzite.
Modul jádra `kvmfr` však zabalíme a připojíme k obrazu systému, jako takový zapíšeme jakýkoli problém s modulem `kvmfr` v Bazzite do našeho nástroje pro sledování problémů Discord nebo Github a nezapomeňte odeslat ping @HikariKnight.

Řekneme vám, že máte problém nahlásit přímo na Looking-Glass, pouze pokud problém nesouvisí s balením a konfigurací modulu `kvmfr`.

## Povolení modulu KVMFR
Modul kvmfr můžete povolit spuštěním tohoto příkazu:

```bash
ujust setup-virtualization kvmfr
```

## Kompilace klienta Looking Glass
Vytvořte distrobox `fedora:latest`, který použijeme ke kompilaci binárního souboru, pomocí následujícího příkazu vytvořte kontejner, na dotaz, jaký obraz použít, vyberte výchozí, protože jsem ověřil, že tato příručka funguje s tímto obrazem pro sestavení.
Tento distrobox musí být vyroben ručně bez příznaku `--nvidia`, který naše ujust automaticky aplikuje pro povolení hardwarové akcelerace, ale výslovně to nechceme, aby se `cmake-data` úspěšně nainstaloval.

!!! note

    Pokud nepoužíváte nejnovější verzi Fedory, změňte prosím `latest` tak, aby odpovídala číslu vaší verze, aby se předešlo problémům s verzováním závislostí.

```bash
distrobox create -i "fedora:latest" -n "tmp-lookingglass"
```
Pokud k tomu chcete použít samostatnou domovskou složku, vytvořte složku, která bude obsahovat tuto domovskou složku kontejnerů, a místo toho spusťte tento příkaz:
```bash
distrobox create -i "fedora:latest" -n "tmp-lookingglass" -H "/path/to/new/home"
```
Vstupte do kontejneru pomocí `distrobox enter tmp-lookingglass`

Postupujte podle [upstream dokumentace](https://looking-glass.io/docs/rc/build/#installing-build-dependencies), můžete najít závislosti sestavení fedory [zde](https://looking-glass.io/wiki/Installation_on_other_distributions) a také budete chtít nainstalovat závislosti uvedené pro uživatele **Pipe.
Protože budeme stavět pro **Wayland** a ne pro X11, budete také potřebovat balíček `libdecor-devel`

Když se dostanete k části pro spuštění `cmake`, použijte příkaz:
```
cmake -DENABLE_WAYLAND=1 -DENABLE_X11=0 -DENABLE_PULSEAUDIO=0 -DENABLE_PIPEWIRE=1 ..
```
Výše uvedený příkaz deaktivuje podporu X11 a Pulseaudio, ale povolí podporu Pipewire a Wayland, tím se vyhnete jakýmkoli problémům, protože Bazzite nedodává závislosti X11 pro `looking-glass`.

Zkopírujte sestavený binární soubor `looking-glass-client` do `/run/host/home/$USER/.local/bin/`
Pokud jste postupovali podle dokumentace k Looking Glass, můžete to provést pomocí následujících příkazů.
```bash
mkdir /run/host/home/$USER/.local/bin
cp ./looking-glass-client /run/host/home/$USER/.local/bin/
```
Otestujte a zjistěte, zda vám binární soubor `looking-glass-client` funguje na hostiteli se spuštěným virtuálním počítačem.

Ukončete kontejner a spusťte níže uvedený příkaz k odstranění kontejneru, který jsme použili k vytvoření klienta Looking-Glass.
```bash
distrobox stop tmp-lookingglass ; distrobox rm tmp-lookingglass
```