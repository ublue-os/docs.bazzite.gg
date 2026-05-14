---
title: Using Swap for Additional Memory or Hibernation
---

# Použití funkce Swap pro další paměť nebo režim spánku

## Účel

Tato příručka vás provede kroky k vytvoření odkládacího souboru na souborovém systému BTRFS, který lze použít pro další paměť nebo hibernaci.

Obrazy Bazzite-Deck již podporují hibernaci prostřednictvím Handheld Daemon pomocí dynamického odkládacího souboru (`General -> Hibernate`). Kromě toho všechny obrazy Bazzite standardně používají zram k poskytnutí další paměti.

Tuto příručku použijte, pokud chcete místo zram vytvořit trvalý odkládací soubor pro více nekomprimované paměti, nebo pokud chcete používat hibernaci prostřednictvím desktopového prostředí. 

## Vytvořte odkládací soubor

Nejprve vytvořte podsvazek pro odkládací soubor. Tím je zajištěno, že pokud se rozhodnete použít snímky, odkládací soubor v nich nebude zahrnut. Měli byste také opravit kontext SELinux adresáře swapfile.
```bash
sudo btrfs subvolume create /var/swap
sudo semanage fcontext -a -t var_t /var/swap
sudo restorecon /var/swap
```

Poté vytvořte samotný odkládací soubor. V tomto příkladu vytvoříme 26GB odkládací soubor. Opět musíte opravit kontext SELinux samotného odkládacího souboru.
```bash
SIZE=26G
sudo btrfs filesystem mkswapfile --size $SIZE /var/swap/swapfile
sudo semanage fcontext -a -t swapfile_t /var/swap/swapfile
sudo restorecon /var/swap/swapfile
```

Načtěte odkládací soubor a ověřte, zda funguje s:
```bash
sudo swapon /var/swap/swapfile
```

## Přidání do fstab
Nyní musíte přidat svůj odkládací soubor do `/etc/fstab`, aby byl trvalý:
```
sudo cp /etc/fstab /etc/fstab.bak
sudo nano /etc/fstab
```

!!! attention
    Buďte opatrní, když upravujete soubor fstab **jinak se váš systém již nespustí**! V tomto případě lze ke spuštění použít předchozí obraz.

Přidejte následující **řádek kódu** do fstab:

```
/var/swap/swapfile none swap defaults,nofail 0 0
```

## Zakázat zram
Nakonec musíte deaktivovat zram, aby hibernace fungovala správně. Za tímto účelem můžete vynulovat konfigurační soubor zram-generator. To zabrání aktualizacím Bazzite v jeho obnovení.
```
echo "" | sudo tee /etc/systemd/zram-generator.conf
```

Nakonec restartujte zařízení, abyste použili výše provedené změny.

## Vrácení změn a obnovení zram
Chcete-li vrátit změny a obnovit zram, nejprve odstraňte položku odkládacího souboru z `/etc/fstab`. Poté znovu povolte zram zkopírováním původního konfiguračního souboru zpět:
```
sudo cp /usr/etc/systemd/zram-generator.conf /etc/systemd/zram-generator.conf
```