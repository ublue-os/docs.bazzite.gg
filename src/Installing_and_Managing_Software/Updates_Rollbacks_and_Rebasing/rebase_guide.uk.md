---
title: Посібник з перебазування
---

# Посібник з перебазування

## Що таке перебазування?

!!! warning "Перебазування між різними робочими середовищами (наприклад, з KDE Plasma на GNOME) **може спричинити проблеми** й **офіційно не підтримується**. Докладніше можна прочитати [тут](/General/FAQ/#can-i-switch-to-a-different-desktop-environment-on-my-current-installation)."

Перебазування дає змогу перейти на інший **варіант образу** та/або **гілку оновлень** _без_ перевстановлення і без втрати особистих файлів і даних застосунків.

> Для перебазування рекомендуємо використовувати [Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal.md) або [утиліту Bazzite Rollback Helper](./bazzite_rollback_helper.md).

---

## Сценарії перебазування

- Перебазування на конкретні старіші збірки за останні 90 днів, якщо в найновішій збірці Bazzite виникають проблеми.
- Перебазування на інші образи Fedora Atomic Desktop, зокрема на інші образи Bazzite.
  - **Не** перебазовуйтеся між різними робочими середовищами.

---

## Перемикання між образами Bazzite

Для зручності та однозначності:

- **варіант образу** надалі називатимемо **IMAGE**
- **гілку оновлень** надалі називатимемо **TAG**

### Перевірка поточного образу й тегу

Спершу перевірте варіант образу та гілку оновлень своєї системи.

=== "Bazzite Updater"

    У [Bazzite Updater](./bazzite-updater.md) перейдіть до **Other Utilities → System Image Information → Current Image**.

    Ви побачите поточну версію системи у форматі `IMAGE:TAG`.

=== "Bazzite Rollback Helper"

    Щоб побачити поточні **IMAGE** і **TAG**, виконайте таку команду:

    ```bash
    brh current
    ```

=== "Низькорівневі команди"

    ```bash
    rpm-ostree status
    ```

    **Посилання на образ** буде показано в розділі «**Deployments:**» у форматі **повного посилання ostree**, де `<image>` і `<tag>` — це відповідно ваші поточні **IMAGE** і **TAG**:

    ```console
    ● ostree-image-signed:docker://ghcr.io/ublue-os/<image>:<tag>
    ```
    
    !!! example

        ```console
        ● ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:testing
        ```
        
        означає, що:
        
        - **IMAGE** — це `bazzite-deck`
        - **TAG** — це `testing`

---

### Перебазування на інший варіант Bazzite

Перебазування дуже схоже на оновлення (чи радше навпаки), адже Bazzite просто завантажується з нового [завантажувального образу контейнера](/General/terms/?h=bootable+container+image#underlying-technology). Усі наведені нижче команди лише завантажують і готують новий образ, з якого завантажиться система.

!!! tip "Якщо це ще не очевидно: щоб завершити перебазування, після виконання наведених нижче команд потрібно перезавантажитися."

!!! warning "Перебазування між різними робочими середовищами (наприклад, з KDE Plasma на GNOME) **може спричинити проблеми** й **не підтримується**."

=== "Bazzite Portal"

    [Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal.md) має два пункти для зручного перемикання між гілками оновлень `stable` і `testing`.
    
    Просто виберіть **Bazzite Portal → Manage Bazzite → Move to the stable update track/Move to the testing update track**.
    
    !!! info "Для перемикання між варіантами образів Bazzite, як-от `bazzite-nvidia`, використовуйте інші способи."

=== "Bazzite Rollback Helper"

    Введіть ціль перебазування `<target>` в одному з таких форматів:
    
    - Лише гілка оновлень: `TAG`
    - Варіант образу та гілка оновлень: `IMAGE:TAG`
    - Повне посилання ostree: `ostree-image-signed:docker://ghcr.io/ublue-os/IMAGE:TAG`
    
    ```bash
    brh rebase <target>
    ```
    
    !!! example
    
        - Перебазування на `stable` із зазначенням лише гілки оновлень:
        ```bash
        brh rebase stable
        ```
        
        - Перебазування на гілку `testing` образу `bazzite-nvidia` із зазначенням варіанта образу та гілки оновлень:
        ```bash
        brh rebase bazzite-nvidia:testing
        ```
        
        - Перебазування на гілку `stable` образу `bazzite-deck` за **повним посиланням ostree**:
        ```bash
        brh rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:stable
        ```

=== "Низькорівневі команди"

    ```bash
    rpm-ostree rebase <image-ref>
    ```

    Де `<image-ref>` — це **повне посилання ostree**.
    
    !!! example
        
        - Перебазування на гілку `stable` образу `bazzite-deck` за **повним посиланням ostree**:
        ```bash
        rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:stable
        ```

=== "У Steam (лише Bazzite-Deck)"

    В образах Bazzite-Deck гілку можна змінити в ігровому режимі Steam: **Settings → System → OS Update Channel**.

    Якщо ви ввімкнули **advanced update channel**, з'являться додаткові варіанти. Вони відповідають таким гілкам:

    | Канал оновлень Steam | Канал оновлень Bazzite (TAG) |
    | :------------------ | :-------------------------: |
    | Stable | `:stable` |
    | Release Candidate | `:testing` |
    | Beta | `:testing` |
    | Beta Candidate | `:unstable` |
    | Main | `:unstable` |

!!! info

    Якщо ви бачите таке повідомлення:
    
    ```console
    error: Old and new refs are equal: ostree-image-signed:docker://ghcr.io/ublue-os/bazzite:testing
    Rebase failed. Image may not exist or be accessible.
    ```

    Це означає, що варіант образу чи гілка, на які ви намагаєтеся перебазуватися, збігаються з поточними. Просто [оновіться](/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/updating_guide/), щоб отримати найновішу версію поточного образу.

---

## Відмінності між гілками оновлень

=== "Стабільна гілка"

    Це перша з двох гілок для кінцевих користувачів, призначена для тих, хто хоче, щоб усе просто працювало.

    - Стабільна (TAG: `stable`)
    - Гілка за замовчуванням у звичайних інсталяціях Bazzite.
    
    !!! info "Зазвичай стабільні образи оновлюються раз на [два тижні](https://en.wikipedia.org/wiki/Fortnight)."

=== "Тестова гілка"

    Це друга гілка, призначена для досвідчених користувачів, які готові допомагати, тестувати й пробувати нові та експериментальні функції.

    - [Тестова (TAG: `testing`)](https://github.com/ublue-os/bazzite/compare/main...testing)
      - Ранній доступ до майбутніх збірок Bazzite ще до їхнього випуску.
      - Помилки можуть з'являтися часто.
      - Після тестування великого релізу радимо перебазуватися назад на `:stable`.

    !!! info "Тестові образи збираються майже щодня, іноді навіть кілька разів на день."

=== "Нестабільна гілка"

    Ця гілка призначена лише для основних учасників і мейнтейнерів Bazzite і використовується для великих змін, які потребують частого тестування. 
    
    !!! warning "Нестабільна гілка може відставати навіть від оновлень стабільної гілки, оскільки в ній тестують окремі великі зміни і її не збирають за розкладом."

---

## Перемикання гілок оновлень в ігровому режимі Steam
  
> Див. [тут](/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rebase_guide/#__tabbed_2_3).

---

## Перебазування на старіші збірки { #rebasing-to-older-builds }

!!! warning "Після переходу на старішу збірку Bazzite ви не отримуватимете нових оновлень, доки не повернетеся на `:stable`. Тобто до повернення на стабільну гілку не буде й оновлень безпеки."

Так само як і з відкатом до попереднього розгортання Bazzite, можна перебазуватися на конкретну збірку Bazzite, створену протягом останніх 90 днів.  Усі ваші дані залишаться недоторканими.

Однак щоб оновити систему й отримати нові функції та виправлення безпеки, доведеться вручну перебазуватися назад на `:stable`. 

### Перегляд доступних образів

Переглянути список доступних стабільних збірок можна такими способами:

=== "Bazzite Rollback Helper"

    !!! info "Також можна переглянути інші гілки оновлень, вказавши їх у команді `brh list TAG`, або запустити `brh` в інтерактивному режимі."

    ```bash
    brh list
    ```

    !!! example

        Щоб переглянути образи в гілці оновлень `testing`:
        ```bash
        brh list testing
        ```

=== "Через командний рядок"

    Змініть цю команду під себе, замінивши `bazzite` і `stable-`:

    ```bash
    skopeo list-tags docker://ghcr.io/ublue-os/bazzite | grep -E "\bstable-" | sort -rV
    ```

=== "У браузері"

    > Знайти конкретні збірки можна на [сторінці релізів Bazzite на GitHub](https://github.com/ublue-os/bazzite/releases).

---

### Перебазування на конкретну збірку

Щоб перебазуватися на конкретну збірку, достатньо вказати **TAG** у форматі `BRANCH-VERSION.YEARMONTHDAY`

=== "Bazzite Rollback Helper"

    ```bash
    brh rebase VERSION-YEARMONTHDAY
    ```
    
    !!! example
        
        Перебазування на збірку `bazzite-deck` (_Fedora 39_) від **13 січня 2024 року**:
        
        ```bash
        brh rebase bazzite-deck:stable-39.20240113
        ```

        <small>_(Зверніть увагу: ця збірка вже недоступна, бо минуло понад 90 днів, і її наведено лише як приклад для цієї документації.)_</small>
        
        Перебазування на найновішу збірку `bazzite-deck` на Fedora 43, якщо ви вже користуєтеся `bazzite-deck`:
        
        ```bash
        brh rebase stable-43
        ```

=== "Низькорівневі команди"

    ```bash
    rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/IMAGE:VERSION-YEARMONTHDAY
    ```
    
    !!! example
        
        Перебазування на збірку `bazzite-deck` (_Fedora 39_) від **13 січня 2024 року**:
        ```bash
        rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:39-20240113
        ```

        <small>_(Зверніть увагу: ця збірка вже недоступна, бо минуло понад 90 днів, і її наведено лише як приклад для цієї документації.)_</small>

---
