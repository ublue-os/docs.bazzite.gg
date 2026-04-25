---
title: "VPN Setup"
---

# Nastavení VPN

## Používání funkčních VPN Flatpaků

Klienti VPN obvykle nejsou nabízeni v obchodě s aplikacemi Bazaar, protože karanténa Flatpak je pro většinu klientů VPN příliš přísná, aby fungovala tak, jak je, což znamená, že nejsou k dispozici v Bazaar. Příklady dobrých VPN klientů dostupných v Bazaar:

- [Mozilla VPN](https://flathub.org/apps/org.mozilla.vpn)
- [ProtonVPN](https://flathub.org/apps/com.protonvpn.www)

## Tailscale

Ve výchozím nastavení je zahrnuta [Tailscale](https://tailscale.com), která poskytuje služby VPN pro případy použití na počítačích i ve vývoji. Než budete pokračovat, přečtěte si tuto [příručku Tailscale](https://blog.6nok.org/tailscale-is-pretty-useful/) pro běžné použití.

- [Používání Tailscale s Mullvad](https://tailscale.com/kb/1258/mullvad-exit-nodes) - Poskytuje to nejlepší hned po vybalení.
  - [Using Tailscale with Docker](https://tailscale.com/kb/1282/docker) - Pro účely vývoje.
  - `ujust toggle-tailscale` odstraní vestavěnou integraci desktopu, pokud chcete použít něco jiného.
  – [kanál YouTube](https://www.youtube.com/@Tailscale) společnosti Tailscale nabízí spoustu skvělých tipů a triků.
- Dobré sítě VPN poskytují konfigurační soubory Wireguard, které lze importovat přímo do NetworkManageru. Další informace naleznete v dokumentaci poskytovatelů VPN.
- Pouze jako poslední možnost [navrstvit VPN pomocí rpm-ostree](/Installing_and_Managing_Software/rpm-ostree/).

## Importujte konfigurační soubory VPN prostřednictvím prostředí Desktop

Tato možnost pro vás může být dost dobrá, pokud nepotřebujete speciální funkce poskytované klientem VPN, jako jsou přepínače zabíjení, rozdělené tunelování a další vlastní funkce, které nejsou součástí protokolu VPN. Takto importované VPN lze libovolně zapínat a vypínat.

=== "KDE Plasma"

    1\. Otevřete Nastavení systému
    2\. Přejděte do části Síť a přejděte do nastavení „Wi-Fi a Internet“.
    3\. Klikněte na tlačítko „+“ ve spodní části

    <img src="/img/vpn_settings.png" alt="Stránka Nastavení v Nastavení sítě" width="600" height="487" />

    4\. Vyberte stažený konfigurační soubor

    <img src="/img/add_vpn.png" alt="Dialogové okno Import konfiguračního souboru VPN" width="400" height="617" />

=== "GNOME"

    1\. Otevřete Nastavení
    2\. Přejděte do části Síť
    3\. Klikněte na tlačítko „+“ v sekci VPN

    <img src="/img/vpn_settings_gnome.png" alt="Stránka Nastavení sítě v GNOME" width="600" height="487" />

    4\. Zvolte "Importovat ze souboru..."

    <img src="/img/add_vpn_file_gnome.png" alt="Dialogové okno Import konfiguračního souboru VPN v GNOME" width="600" height="487" />

    5\. Vyberte stažený konfigurační soubor.