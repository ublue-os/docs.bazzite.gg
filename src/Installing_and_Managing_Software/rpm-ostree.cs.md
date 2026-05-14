---
title: Package Layering
---

# Vrstvení balíků

## Pomocí `rpm-ostree`

!!! attention

    Nezodpovědné vrstvení balíčků může být **destruktivní** a může zabránit aktualizacím a dalším problémům, dokud nebudou vrstvené balíčky odstraněny.

Nainstalujte [balíčky Fedora Linux](https://packages.fedoraproject.org/) na stávající obraz Bazzite pomocí příkazu terminálu `rpm-ostree`.  Použijte pro balíčky, které nelze nainstalovat z Homebrew nebo spustit uvnitř kontejneru.  Vrstvené balíčky mohou přerušit aktualizace systému, dokud nebudou odstraněny kvůli problémům se závislostmi, protože balíček bude muset být aktualizován se zbytkem obrazu.  To také způsobuje, že aktualizace trvá déle.

### Klíčové poznámky

- Vrstvení balíčků bude **vyžadovat** restartování systému, když dokončí vytváření nového nasazení s balíčky přidanými do vašeho obrazu.
- Tuto metodu použijte jako **poslední možnost** a pro cokoli na "systémové úrovni", protože může pozastavit aktualizace, pokud balíček obsahuje problémy se závislostmi na budoucích aktualizacích, dokud nebude balíček odinstalován.

## Příkazy terminálu související s vrstvením balíků

**Používejte tyto příkazy na vlastní nebezpečí**.

### Balíčky vrstev

```
rpm-ostree install <package>
```

Nainstaluje balíčky Fedory do systému, které zůstanou mezi aktualizacemi, restartujte, aby se instalace použila.

### Odinstalujte vrstvené balíčky

```
rpm-ostree uninstall <package>
```

Odinstaluje všechny vrstvené balíčky přidané do systému, restartujte, aby se odinstalace použila.

### Vyhledejte balíček

```
rpm-ostree search <package>
```

Vyhledá balíčky Fedory, které lze nainstalovat.

### Zobrazit aktuálně vrstvené balíčky

```
rpm-ostree status
```

Tím se vytisknou vrstvené balíčky ve vaší instalaci Bazzite.

## Instalace souborů RPM

Kontejnery Fedora Distrobox by se měly používat pro většinu souborů `.rpm`, ale někdy je třeba je nainstalovat do vašeho hostitele, pokud to s kontejnerem nefunguje správně.

Binární soubory RPM můžete nainstalovat **do svého hostitele** pomocí `rpm-ostree` zadáním:

```
rpm-ostree install <package>.rpm
```

Pro správnou instalaci možná budete muset zkopírovat celou cestu (`/path/to/rpmfile.rpm`).

!!! important

    Nevýhodou instalace místních souborů RPM mimo repozitáře Fedory je, že aktualizace pro konkrétní balíček RPM se nebudou automaticky používat.

## Jak mohu přidat/odebrat úložiště [COPR](https://copr.fedorainfracloud.org)?

!!! warning

    Důrazně se doporučuje **ne** používat úložiště COPR třetích stran, pokud je to možné, takže si uvědomte, že s tím jsou spojena rizika včetně nefunkčních aktualizací, dokud nebudou odstraněny.

=== "Povolit COPR"

    === "DNF5 (Fedora COPR)"

        ```sh
        sudo dnf5 copr enable <USER>/<PROJECT>
        ```

    === "DNF5 (soubor repo)"

        Tato metoda funguje s COPR jinými než Fedora (např.: [Docker](https://docs.docker.com/engine/install/fedora/#set-up-the-repository))

        ```sh
        sudo dnf5 config-manager addrepo --from-repofile=https://url/to/file.repo
        ```

    === "Ručně"

        1. Stáhněte si soubor .repo a uložte jej do `/etc/yum.repos.d/`

        2. Poté nainstalujte balík(y) pomocí `rpm-ostree`

        3. Restartujte

        Pokud zaznamenáte problémy s aktualizací vašeho systému kvůli problémům s podpisem GPG, můžete to vyřešit buď odstraněním úložiště COPR, nebo úpravou souboru změnou `gpgcheck=1` na `gpgcheck=0` (nebo podobným) a jeho uložením **na vlastní riziko**.

=== "Zakázat COPR"

    !!! warning "Předtím se ujistěte, že jste odstranili všechny balíčky nainstalované s COPR."

    === "DNF5 (Fedora COPR)"

        ```sh
        sudo dnf5 copr disable <USER>/<PROJECT>
        ```

    === "DNF5 (soubor repo)"

        Vyjměte `.repo` na `/etc/yum.repos.d/`

    === "Ručně"

        Odstraňte `.repo` na `/etc/yum.repos.d/`

## Jak obnovit výchozí COPR

```sh
# Remove all current repos
sudo rm /etc/yum.repos.d/*

# Now copy the default repo files fro /usr/etc to /etc
sudo cp /usr/etc/yum.repos.d/* /etc/yum.repos.d/
```

## **HLAVNÍ** upozornění pomocí `rpm-ostree`

Vrstvení balíčků může způsobit **vážné následky** včetně:

- Pozastavit aktualizace systému, dokud nebudou balíčky odinstalovány.
- Zabraňte přenastavení na jiné obrazy, dokud nebudou balíčky odinstalovány.
- Konflikt se stávajícími balíčky jako součást obrazu vedoucí k problémům se závislostí.
- Stahování aktualizací trvá déle, protože do systému vrstvíte více balíčků.

Balíčky vrstvení jsou většinou určeny pro **systémové aplikace, knihovny a další závislosti**. Doporučuje se používat Flatpak, Homebrew, kontejnery, AppImage, Waydroid nebo spouštět verzi Windows přes vrstvu kompatibility **před** instalací softwaru s `rpm-ostree`.  Vrstvení balíčků na dočasné časové období je lepší alternativou než ponechání balíčku ve vrstvách na neurčito.

## Jak odstranit **VŠECHNY** vrstvené balíčky

Pokud narazíte na problémy s upgradem kvůli konfliktu vrstvených balíčků, pak buď volitelně odinstalujte konfliktní balíčky, nebo odstraňte všechny vrstvené balíčky pomocí tohoto **příkazu**:

```bash
rpm-ostree reset
```

## Web projektu

https://coreos.github.io/rpm-ostree/