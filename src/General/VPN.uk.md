---
title: "Налаштування VPN"
---

# Налаштування VPN

## Робочі VPN-застосунки у Flatpak { #using-functional-vpn-flatpaks }

VPN-клієнтів зазвичай немає в магазині застосунків Bazaar, бо пісочниця Flatpak обмежує можливості, потрібні для їхньої роботи. Проте кілька з них певною мірою працюють:

- [Mozilla VPN](https://flathub.org/apps/org.mozilla.vpn)
- [ProtonVPN](https://flathub.org/apps/com.protonvpn.www) <small>Примітка: неофіційний пакет, зібраний з офіційного застосунку.</small>

## Tailscale { #tailscale }

[Tailscale](https://tailscale.com) входить до системи за замовчуванням і надає VPN-послуги як для звичайного використання, так і для розробки. Перш ніж продовжити, прочитайте [цей посібник із Tailscale](https://blog.6nok.org/tailscale-is-pretty-useful/) про типові сценарії використання.

-   [Tailscale разом із Mullvad](https://tailscale.com/kb/1258/mullvad-exit-nodes) — найзручніший варіант одразу після встановлення.
  -   [Tailscale разом із Docker](https://tailscale.com/kb/1282/docker) — для розробки.
  -   Пункт **Enable Tailscale** у **Bazzite Portal** прибере вбудовану інтеграцію з робочим столом, якщо ви хочете користуватися чимось іншим.
  -   На [YouTube-каналі](https://www.youtube.com/@Tailscale) Tailscale є багато корисних порад і хитрощів.
-   Хороші VPN-сервіси надають файли конфігурації WireGuard, які можна імпортувати безпосередньо в NetworkManager. Докладніше — у документації вашого VPN-провайдера.
-   [Накладайте VPN через rpm-ostree](../Installing_and_Managing_Software/rpm-ostree.md) лише в крайньому разі.

## Імпорт файлів конфігурації VPN через робоче середовище { #import-vpn-configuration-files-through-desktop-environment }

Цього варіанта може бути достатньо, якщо вам не потрібні особливі функції VPN-клієнта, як-от аварійне відключення (kill switch), роздільне тунелювання (split tunneling) та інші функції, яких немає в самому протоколі VPN. Імпортовані так VPN можна вмикати й вимикати будь-коли.

=== "KDE Plasma"

    1. Відкрийте «Системні параметри» (System Settings)
    2. Перейдіть у розділ «Мережа» (Networking) і відкрийте налаштування «Wi-Fi та інтернет» (Wi-Fi & Internet)
    3. Натисніть кнопку «+» внизу

    <img src="/img/vpn_settings.png" alt="Сторінка мережевих налаштувань" width="600" height="487" />

    4. Виберіть завантажений файл конфігурації

    <img src="/img/add_vpn.png" alt="Вікно імпорту файлу конфігурації VPN" width="400" height="617" />

=== "GNOME"

    1. Відкрийте «Параметри» (Settings)
    2. Перейдіть у розділ «Мережа» (Network)
    3. Натисніть кнопку «+» у розділі VPN

    <img src="/img/vpn_settings_gnome.png" alt="Сторінка мережевих налаштувань у GNOME" width="600" height="487" />

    4. Виберіть «Імпортувати з файла…» (Import from file…)

    <img src="/img/add_vpn_file_gnome.png" alt="Вікно імпорту файлу конфігурації VPN у GNOME" width="600" height="487" />

    5. Виберіть завантажений файл конфігурації.
