---
title: Сумісність портативних пристроїв
---

# Сумісність портативних пристроїв

> Це загальніший посібник. Про вирішення проблем читайте в розділі [Особливості ігрового режиму Steam](../quirks.md).

## Можливості як у SteamOS { #steamos-like-functionality }

!!! info

    [Bazzite Deck 44](https://universal-blue.discourse.group/t/bazzites-biggest-update-deck-44-has-launched-happy-birthday-to-universal-blue/12373) використовує [OpenGamepadUI](https://github.com/ShadowBlip/OpenGamepadUI) і [InputPlumber](https://github.com/shadowblip/InputPlumber) для повноцінної підтримки портативних пристроїв.
    
    Раніше це робив Handheld Daemon. Докладніше про це можна дізнатися [тут](https://universal-blue.discourse.group/t/a-brighter-future-for-bazzite/11575).

Образи Bazzite-Deck постачаються з [ігровим режимом Steam](../Steam_Gaming_Mode.md), який відтворює досвід SteamOS. Мета — підтримувати більшість портативних ПК на x86_64 раніше, ніж SteamOS, і з тими самими перевагами, що й настільна версія Bazzite.

---

## Підтримувані портативні пристрої { #supported-handhelds }

!!! info "Цей список неповний, і якщо пристрою в ньому немає, це не обов'язково означає, що Bazzite на ньому не працює."

_Натисніть назву пристрою, щоб переглянути налаштування після встановлення, функції, що працюють, проблеми та способи їх обійти._

- [**Портативні пристрої ASUS**](./ASUS_ROG_Ally.md)
- [**Портативні пристрої Lenovo**](./Lenovo_Legion_Go.md)
- [**Портативні пристрої GPD**](./GPD_Handhelds.md)
- [**Портативні пристрої OneXPlayer**](./OneXPlayer_Handhelds.md)
- [**Портативні пристрої Ayn**](./Ayn_Handhelds.md)
- [**Портативні пристрої Ayaneo**](./Ayaneo_Handhelds.md)
- [**Steam Deck**](./Steam_Deck.md)
- [**Інші портативні пристрої**](./Other_Handhelds.md) 

---

## Керування TDP { #tdp-controls }

![TDP|409x1004, 33%](../../img/TDP.png) ![Профілі живлення OGUI|1920x1200, 30%](../../img/OGUI_Profile.jpg)

Є кілька способів керувати TDP у Bazzite:

!!! info "Якщо в OpenGamepadUI ви бачите повідомлення `TDP managed by Steam`, це означає, що TDP вашого пристрою справді налаштовується через Steam."

!!! tip "Якщо докладних налаштувань TDP не видно, спробуйте вибрати профіль **Performance** → прокрутіть униз і ввімкніть TDP і GPU Clocks. Після цього мають з'явитися докладні налаштування TDP у ватах."

=== "Меню швидкого доступу (QAM) клієнта Steam"

    Якщо TDP вашого пристрою можна налаштовувати через SteamOS Manager, цей параметр буде тут. Якщо його немає, перевірте OpenGamepadUI або скористайтеся іншими способами налаштування TDP вашого пристрою.
    
    !!! info "Як відкрити QAM, дивіться [тут](#how-do-i-open-the-qam)."
    
    - Виберіть **:material-lightning-bolt: піктограму блискавки** й увімкніть розширені параметри (**Advanced**)
    - Після цього TDP можна змінити в окремому розкривному списку TDP.
    - Власне значення TDP можна задати, вибравши **Custom**, прокрутивши вниз і ввімкнувши **Custom TDP**, а потім змінивши значення **повзунком TDP**, що з'явиться.
    
    > [Ці пристрої](https://github.com/ublue-os/bazzite/blob/main/system_files/desktop/shared/usr/libexec/hwsupport/steamos-manager-hardware) за замовчуванням використовують цей спосіб.
  
=== "OpenGamepadUI (OGUI)"

    Це друге місце, де можна знайти керування TDP вашого пристрою. У цьому меню керування TDP забезпечує [PowerStation](https://github.com/ShadowBlip/PowerStation). Якщо ваш пристрій можна налаштувати через QAM у Steam, параметри продуктивності тут можуть бути, а можуть і не бути. Для налаштування пристрою можна користуватися будь-яким із двох способів.

    !!! info "Як відкрити OGUI, дивіться [тут](#how-do-i-open-the-ogui-overlay)."

    > [Ці пристрої](https://github.com/ublue-os/bazzite/blob/main/system_files/desktop/shared/usr/libexec/hwsupport/powerstation-hardware) за замовчуванням використовують цей спосіб.
  
=== "Плагіни Decky"

    Якщо ні QAM у Steam, ні OGUI не дають налаштувати TDP, для цього також можна скористатися плагінами Decky. Але пам'ятайте, що такі плагіни заважатимуть один одному й конфліктуватимуть, якщо ввімкнути кілька одночасно.
    
    !!! tip "Переконайтеся, що працює лише один спосіб керування TDP (зокрема OGUI/PowerStation)!"
    
    - Плагін [SimpleDeckyTDP](https://github.com/aarron-lee/SimpleDeckyTDP) підтримує TDP, відеокарту, регулятор живлення (Power Governor) та інші налаштування.
      - Є також [графічний застосунок](https://github.com/aarron-lee/SimpleDeckyTDP-Desktop), але його треба встановлювати вручну.
    - [PowerControl](https://github.com/mengmeet/PowerControl) підтримує TDP, відеокарту й керування вентиляторами на деяких пристроях.
    - [Panel de Control](https://github.com/Hooandee/panel-de-control) також дає змогу задавати власний TDP, керувати вентиляторами й автоматично підбирати профілі залежно від того, як ви користуєтеся пристроєм.

---

### Як відкрити оверлей OGUI? { #how-do-i-open-the-ogui-overlay }

![Оверлей|690x431, 75%](../../img/OGUI_Overlay.jpg)

Кнопка, яка відкриває OGUI, на різних пристроях різна. <small>_Ми щосили намагалися знайти схожі зображення..._</small>

| Пристрій | Зображення | Назва кнопки | Дія |
| :-: | :-: | :- | :- |
| Серія ROG Ally | :material-microsoft-dynamics-365:/:simple-nucleo: | Кнопка Armory Crate | Довге натискання |
| Серія Xbox Ally | :material-bookshelf:/<kbd>\|\|\\</kbd> | Кнопка бібліотеки (Library) | Довге натискання |
| MSI | :simple-wattpad: | Центральна кнопка M | Довге натискання |
| Ayaneo | **. . .** | Кнопка RC | Натискання |
| OneXPlayer | :simple-atlasos: | Кнопка Guide | Утримуйте Guide і натисніть QAM |
| Інші пристрої | :material-microsoft-xbox:/:material-sony-playstation:/:material-steam: + :material-gamepad-circle-right: | Guide + B | Одне натискання |

!!! note "Зараз OGUI вибірково ввімкнено для пристроїв зі списку дозволених, і він не призначений для HTPC. Якщо на вашому портативному пристрої OGUI не з'являється, створіть звіт про проблему на GitHub!"

!!! tip ":material-microsoft-xbox:/:material-sony-playstation:/:material-steam: + :material-gamepad-circle-right: (Guide + B) — запасний варіант, який працює завжди"

> Інструкції з увімкнення OGUI на непідтримуваних пристроях — [тут](./Other_Handhelds.md#enabling-ogui-on-unsupported-devices). Вмикайте **на власний ризик**.

---

### Як відкрити QAM? { #how-do-i-open-the-qam }

 Кнопка, яка відкриває QAM, на різних пристроях різна. <small>_Ми щосили намагалися знайти схожі зображення..._</small>

| Пристрій | Зображення | Назва кнопки | Дія |
| :-: | :-: | :- | :- |
| Серія ROG Ally | :material-microsoft-dynamics-365:/:simple-nucleo: | Кнопка Armory Crate | Одне натискання |
| Серія Xbox Ally | :material-bookshelf:/<kbd>\|\|\\</kbd> | Кнопка бібліотеки (Library) | Одне натискання |
| Серія Legion Go | :material-tune-variant: | Права кнопка Legion | Одне натискання |
| MSI | :simple-wattpad: | Центральна кнопка M | Одне натискання |
| Ayaneo | _**//**_ | Кнопка користувацької функції (=) | Одне натискання |
| OneXPlayer | `TURBO` | Кнопка Turbo | Одне натискання |
| GPD | :material-microsoft-xbox-controller-menu:/:octicons-home-24: | Кнопка Menu / кнопка Home. | Довге натискання :material-microsoft-xbox-controller-menu:, якщо є лише :material-microsoft-xbox-controller-menu:, інакше одне натискання тієї, що праворуч. |

Також меню швидкого доступу можна відкрити з клавіатури комбінацією <kbd>Ctrl</kbd> + <kbd>2</kbd>.

---

## Про контролер { #controller-information }

На більшості портативних пристроїв, крім Steam Deck, для повної функціональності емулюється контролер DualSense. Налаштування емуляції контролера можна знайти в QAM або OGUI.

!!! info "Як відкрити QAM, дивіться [тут](#how-do-i-open-the-qam)."

!!! warning "Якщо емулювати контролер Xbox, частина функцій працюватиме гірше або не працюватиме зовсім."

!!! note "Якщо є проблеми з гіроскопом, спробуйте вибрати в OGUI ціль емуляції контролера **deck-uhid**. RGB-підсвічуванням пристрою можна керувати за допомогою **плагіна Decky Huesync**."

Якщо на вашому пристрої є задні кнопки (paddles), варто використовувати контролер DualSense Edge або Steam Deck (**крім Ayn Loki**). За замовчуванням це вимкнено, бо деякі ігри неправильно призначають ці кнопки.

Деяким іграм та емуляторам для правильної роботи керування потрібно **вимкнути** введення Steam.

---

### Керування робочим столом { #desktop-controls }

![desktop_controls_step_1|850x722, 75%](../../img/handheld_desktop_control.png)

Розкладки контролера для робочого столу за замовчуванням може не бути, якщо Steam неправильно налаштував контролер вашого портативного пристрою. Це можна виправити в налаштуваннях контролера Steam.

Віртуальну клавіатуру надає екранна клавіатура Steam, яку треба налаштувати в режимі робочого столу. **Типової комбінації для екранної клавіатури Steam немає**, тож її треба призначити на будь-яку зручну кнопку, хоча зазвичай радять :material-gamepad-circle-left:.

!!! tip "Екранну клавіатуру можна налаштувати в **Steam → Налаштування → Контролер → Розкладка для режиму робочого столу** (Steam → Settings → Controller → Desktop Layout)."

Розкладки контролера для робочого столу за замовчуванням може не бути, якщо Steam неправильно налаштував контролер вашого портативного пристрою. Це можна виправити в налаштуваннях контролера Steam.

!!! info "У KDE Plasma 6.7 з'явилася функція керування робочим столом за допомогою контролера. Вона конфліктує зі способом емуляції в Steam, тож вимкніть її або, навпаки, вимкніть емуляцію Steam, якщо хочете користуватися вбудованою підтримкою контролерів у Plasma."

> Докладніше — [тут](../../General/issues_and_resolutions.md#gamepads-and-handheld-joysticks-dont-work-in-desktop-mode).

---

## Налаштування Decky { #decky-setup }

Щоб встановити [Decky Loader](https://decky.xyz), відкрийте термінал хост-системи й введіть:

```bash
ujust setup-decky
```

Decky Loader можна відкрити в QAM з ігрового режиму Steam або режиму Big Picture.

!!! info "Як відкрити QAM, дивіться [тут](#how-do-i-open-the-qam)."

### Плагіни Decky { #decky-plugins }

!!! info "Після оновлення Decky може зламатися або бути видаленим."

Встановлюйте необов'язкові [плагіни Decky](https://plugins.deckbrew.xyz/) для свого портативного пристрою. Якщо з Decky виникають серйозні проблеми, радимо видалити його, перш ніж повідомляти про помилки в Bazzite.

---

## Непідтримувані портативні пристрої { #unsupported-handhelds }

!!! note

    Підтверджено, що деякі портативні пристрої завантажують Bazzite, але на них бракує підтримки драйверів у Linux, зокрема драйверів звуку.

Непідтримувані портативні пристрої _можуть працювати_ з Bazzite, але ви можете зіткнутися з неочікуваними й незадокументованими змінами. Якщо вашого портативного пристрою немає в списку, все одно можете спробувати Bazzite з образом Bazzite-Deck.

На неперевіреному обладнанні результат може відрізнятися. Bazzite **не** застосовує автоматично виправлення, налаштування й зміни на непідтримуваних портативних пристроях, тож різні функції, можливо, доведеться налаштовувати вручну.

!!! note

    Якщо ви вважаєте, що ваш пристрій уже добре підтримується в Linux, можете надіслати PR, щоб Bazzite офіційно його підтримувала.

> Інструкції з увімкнення OGUI на непідтримуваних портативних пристроях — [тут](./Other_Handhelds.md#enabling-ogui-on-unsupported-devices).

---

## Застереження щодо e-GPU: { #e-gpu-caveats }

- Ті самі [вимоги до відеокарти](../../Gaming/Hardware_compatibility_for_gaming.md#steam-gaming-mode-requirements), що й для ігрового режиму Steam, стосуються й e-GPU.
  - Відеокарти Nvidia **не підтримуються**, хоча Bazzite має експериментальний образ `-deck-nvidia`.

> Можете прочитати [**загальний посібник із e-GPU для Linux + скрипт**](https://github.com/ewagner12/all-ways-egpu) і дотримуватися його на власний ризик.

---
