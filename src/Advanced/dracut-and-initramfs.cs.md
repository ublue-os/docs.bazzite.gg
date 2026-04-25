---
title: How to Use Modprobe Options in Bazzite
---

# Jak používat možnosti Modprobe v Bazzite

## Pokud jen plánujete přidat možnosti do modulu, měli byste zvážit použití karg!
Dotknutí se systému initramfs a modprobe zpomalí vaše aktualizace, takže všechny vaše aktualizace budou trvat o několik minut déle. Ve většině případů to, co chcete dělat v modprobe, lze provést pomocí jednoduchých argumentů jádra.

V tomto příkladu umožňuje změnit níže uvedené možnosti modprobe na karg (argument jádra):
```
options hid_apple fnmode=2
```
To by se přeložilo na karg:
```
hid_apple.fnmode=2
```
Chcete-li to přidat do grub, vydáme příkaz:
```
rpm-ostree kargs --append-if-missing="hid_apple.fnmode=2"
```
To vám umožní změnit volbu modulu bez úpravy systému initramfs a je mnohem rychlejší, kdykoli aktualizujete systém, protože argumenty jádra se při každé aktualizaci negenerují.

## Upstream dokumentace o úpravě argumentů jádra

Další informace naleznete v [**upstream dokumentaci Fedory**](https://docs.fedoraproject.org/en-US/fedora-coreos/kernel-args/) k tomuto tématu.