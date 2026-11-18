---
title: Як використовувати параметри modprobe у Bazzite
---

# Як використовувати параметри modprobe у Bazzite

## Якщо ви плануєте лише додати параметри для модуля, варто скористатися параметром ядра (karg)! { #if-you-just-plan-to-add-options-to-a-module-then-you-should-consider-using-a-karg }
Якщо змінювати initramfs і modprobe, оновлення сповільняться: кожне з них триватиме на кілька хвилин довше. Здебільшого те, що ви хочете зробити через modprobe, можна зробити простими параметрами ядра.

Для прикладу перетворімо такий параметр modprobe на karg (параметр ядра):
```
options hid_apple fnmode=2
```
Він відповідає такому параметру ядра:
```
hid_apple.fnmode=2
```
Щоб додати його в GRUB, виконайте команду:
```
rpm-ostree kargs --append-if-missing="hid_apple.fnmode=2"
```
Так можна змінити параметр модуля, не редагуючи initramfs, і оновлення системи відбуватимуться набагато швидше, бо параметри ядра не генеруються заново під час кожного оновлення.

## Документація першоджерела про зміну параметрів ядра { #upstream-documentation-on-modifying-kernel-arguments }

Докладніше про це — у [**документації Fedora**](https://docs.fedoraproject.org/en-US/fedora-coreos/kernel-args/).
