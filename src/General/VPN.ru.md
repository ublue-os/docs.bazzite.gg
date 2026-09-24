---
title: "Настройка VPN"
---

# Настройка VPN

## Если вы в России

Если вы в России, то про блокировки, ТСПУ и прочие прелести вам, скорее всего, рассказывать не надо.

В таких случаях удобнее держать под рукой портативные VPN-клиенты, поддерживающие популярные протоколы типа VLESS. Их проще попробовать, проще заменить и не нужно глубоко встраивать в систему.

Можно попробовать:

- [**AmneziaVPN**](https://github.com/amnezia-vpn/amnezia-client/releases/latest)
- [**Throne**](https://github.com/throneproj/Throne/releases/latest)
- [**Nekoray**](https://github.com/MatsuriDayo/nekoray/releases/latest) <small>Проект заброшен, но старые релизы все еще могут пригодиться.</small>
- [**v2RayN**](https://github.com/2dust/v2rayN/releases/latest)

Если у AmneziaVPN отваливается сервис, посмотрите [этот комментарий с обходным решением](https://github.com/amnezia-vpn/amnezia-client/issues/1925#issuecomment-3392023066).

Скачивайте релизы только со страниц проектов и обращайте внимание на то, что именно запускаете. Рекомендуется держать в запасе ещё пару клиентов: в России один и тот же клиент спокойно может работать у одного провайдера и перестать работать у другого.

## Использование рабочих VPN Flatpak

VPN-клиенты обычно не предлагаются в магазине приложений Bazaar: песочница Flatpak слишком строгая, поэтому большинство VPN-клиентов не может работать как есть, а значит, их нельзя установить через Bazaar. Однако в Bazaar доступны хорошие VPN-клиенты, например:

- [Mozilla VPN](https://flathub.org/apps/org.mozilla.vpn)
- [ProtonVPN](https://flathub.org/apps/com.protonvpn.www) <small>Примечание: неофициальный пакет, собранный из официального приложения.</small>

## Tailscale

[Tailscale](https://tailscale.com) включен по умолчанию и предоставляет VPN-сервисы как для обычного использования на рабочем столе, так и для разработки. Перед продолжением прочитайте [руководство по Tailscale](https://blog.6nok.org/tailscale-is-pretty-useful/) с типичными сценариями использования.

-   [Tailscale с Mullvad](https://tailscale.com/kb/1258/mullvad-exit-nodes) - дает лучший опыт из коробки.
  -   [Tailscale с Docker](https://tailscale.com/kb/1282/docker) - для разработки.
  -   Параметр **Enable Tailscale** в **Bazzite Portal** удалит встроенную интеграцию с рабочим столом, если вы предпочитаете использовать что-то другое.
  -   На [YouTube-канале](https://www.youtube.com/@Tailscale) Tailscale много полезных советов и приемов.
-   Хорошие VPN должны предоставлять файлы конфигурации Wireguard, которые можно импортировать напрямую в NetworkManager. Подробности ищите в документации своего VPN-провайдера.
-   [Наслаивайте VPN через rpm-ostree](/Installing_and_Managing_Software/rpm-ostree/) только в крайнем случае.

## Импорт файлов конфигурации VPN через окружение рабочего стола

Этот вариант может вам подойти, если вам не нужны особые функции VPN-клиента, такие как kill-switch, split tunneling и другие пользовательские возможности, не встроенные в VPN-протокол. VPN, импортированные таким способом, можно включать и выключать в любой момент.

=== "KDE Plasma"

    1. Откройте System Settings
    2. Перейдите в раздел Networking и откройте настройки "Wi-Fi & Internet"
    3. Нажмите кнопку "+" внизу

    <img src="/img/vpn_settings.png" alt="Страница сетевых настроек" width="600" height="487" />

    4. Выберите загруженный файл конфигурации

    <img src="/img/add_vpn.png" alt="Окно импорта файла конфигурации VPN" width="400" height="617" />

=== "GNOME"

    1. Откройте Settings
    2. Перейдите в раздел Network
    3. Нажмите кнопку "+" в разделе VPN

    <img src="/img/vpn_settings_gnome.png" alt="Страница сетевых настроек в GNOME" width="600" height="487" />

    4. Выберите "Import From file..."

    <img src="/img/add_vpn_file_gnome.png" alt="Окно импорта файла конфигурации VPN в GNOME" width="600" height="487" />

    5. Выберите загруженный файл конфигурации.
