---
title: Портативні пристрої Ayaneo
---

# Портативні пристрої Ayaneo

!!! disclaimer

    Для роботи сну потрібне оновлення BIOS. Зверніть увагу, що ця вікі може містити застарілу інформацію.

## Відомі проблеми { #known-issues }

- Для переходу в сон потрібне найновіше оновлення BIOS.
  - Повідомляють, що проблеми з контролером після виходу зі сну трапляються непостійно. Схоже, параметр «full initial usb support» у BIOS впливає на те, як часто виникає ця проблема.
- У BIOS немає параметра розміру VRAM, бо у Windows ним керує застосунок AYASPACE.
- RGB-підсвічуванням, можливо, доведеться керувати за допомогою плагіна Decky HueSync.

> Розмір буфера UMA все одно можна змінити за допомогою [Smokeless_UMAF](https://github.com/DavidS95/Smokeless_UMAF), але цей спосіб має свої ризики. Продовжуйте лише **на власний ризик**.

---

## Ayaneo Geek 1S { #ayaneo-geek-1s }

![photo_5875160389711413569_y|663x500, 100%](../../img/Ayaneo_Geek_1S.jpeg)

### Відомі проблеми { #known-issues_1 }

> Див. [тут](#known-issues).

---

## Підтримка e-GPU: { #e-gpu-support }

Використання e-GPU у корпусах Thunderbolt 3, 4 і USB4 через USB4 підтримується частково.

=== "AMD"

    - Автоматичне перемикання під час завантаження за допомогою [all-ways-egpu](https://github.com/ewagner12/all-ways-egpu/tree/main) добре працює зі способами 2 і 3, але спосіб 1, на жаль, не підтримується.
      - Скрипт треба встановлювати за інструкцією [Steam Deck/User Installation](https://github.com/ewagner12/all-ways-egpu/blob/main/README.md#steamosbazziteuser-installation).
    - Відомих проблем із завантаженням із під'єднаною e-GPU немає (відеокарти RDNA 2 точно працюють), і Bazzite за замовчуванням задає потрібні параметри ядра (`amdgpu.ppfeaturemask`).
      - За результатами тестування користувачів, `rpm-ostree kargs --append-if-missing=pci=nommconf` (або редагування командного рядка ядра через `rpm-ostree kargs --editor`) усе одно може знадобитися, бо інакше деякі застосунки можуть працювати гірше.

=== "NVIDIA"
  
    Поки не перевірено, але _може_ працювати з варіантом Bazzite «-deck-nvidia».

---

## Зовнішній ресурс { #external-resource }

Докладніше про цей пристрій і новини — в [оригінальному обговоренні](https://universal-blue.discourse.group/t/ayaneo-geek-1s-2s-linux-bazzite-support-is-already-almost-there-lets-add-them-to-the-officially-supported-devices/1046).

Ayaneo Geek 1S (станом на квітень 2025 року) — єдиний портативний пристрій на Ryzen 7000, який ще не отримав оновлення EC, що збільшує час роботи від батареї. Стежити за цим і повідомляти можна [у цьому обговоренні в Discord](https://discord.com/channels/717181357109018694/1301507866754289745).

---
