---
title: Credits and Donating
---

# Kredity a darování

{% macro contributor(real_name, github, description, sponsor) -%}
    <div style="
    display: inline-flex;
    flex-direction: row;
    gap: 0.5rem;
    align-items: top;
    background-color: #00000066;
    border-radius: 24px;
    padding: 0.3rem;
    padding-right: 0.4rem;
    min-width: 200px;
    width: 100%;
    max-width: 335px;
    line-height: 1.1rem;"
    >
        {% if github %}
            <img
            src="https://github.com/{{ github }}.png?size=60" class="no-lightbox"
            loading="lazy"
            style="max-height:60px;
                border-radius: 24px;"
            >
        {% endif %}
        <div>
            {% if github %}
                <a href="https://github.com/{{ github }}">{{ real_name }}</a>
            {% else %}
                <span>{{ real_name }}</span>
            {% endif %}
            {% if sponsor %}
                <small>
                  <a
                    href="{{ sponsor }}"
                    style="
                      background-color: var(--md-primary-fg-color);
                      color: var(--md-primary-bg-color);
                      border: none;
                      padding: 1px 3px;
                      border-radius: 24px;"
                  >Sponzor</a>
                </small>
            {% endif %}
            <div><small>{{ description or "" }}</small></div>
        </div>
    </div>
{%- endmacro %}

Baví vás používání Bazzite a chcete pomoci udržet jeho vývoj? Zvažte sponzorování projektu a jeho jednotlivých správců a přispěvatelů.

<div class="button-container">
    <a href="https://opencollective.com/bazzite-us" target="_blank" class="sponsor-button">Sponzorujte Bazzite ($ USA)</a>
    <a href="https://opencollective.com/bazzite-eu" target="_blank" class="sponsor-button">Sponzorujte Bazzite (€ Evropa)</a>
</div>

## Správci Bazzite

<div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
{{ contributor("Kyle Gospodnetich", "KyleGospo", "Founder, Image & CI/CD Lead", "https://github.com/sponsors/KyleGospo") }}
{{ contributor("HikariKnight", "HikariKnight", "Virtualizace, skriptování, uživatelská podpora", "https://github.com/sponsors/HikariKnight") }}
{{ contributor("Noel Miller", "noelmiller", "správce komunity, vylepšení instalačního programu, vlastní nástroje pro vytváření obrazů", "https://github.com/sponsors/noelmiller") }}
</div>

## Hlavní přispěvatelé Bazzite

<div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
{{ contributor("Zeglius", "Zeglius", "Skriptování, údržba dokumentace, živý správce ISO", "https://github.com/sponsors/Zeglius") }}
{{ contributor("CheckYourFax", "CheckYourFax", "Podpora komunity, správa hlášení problémů") }}
{{ contributor("Valerie", "valerie-tar-gz", "Správa sociálních sítí, technická podpora") }}
{{ contributor("Amélia", "ameliasvg", "Tvůrce loga a maskota") }}
{{ contributor("Kurt Himebauch", "xXJSONDeruloXx", "Mistr ujust. Správce Decky. Framegen.") }}
{{ contributor("Zacharias Xenakis", "Xarishark", "Portál Bazzite, vylepšení uživatelského prostředí, opravy chyb a překlady") }}
{{ contributor("stellaberrant", "stellaberrant", "Překlady a opravy chyb") }}
{{ contributor("wolfyreload", "wolfyreload", "Vizuální průvodci na YouTube, QA testování") }}
{{ contributor("CharlieBros", "CharlieBros", "Jazykové překlady do španělštiny") }}
{{ contributor("Crono", "EPOCHvoyager", "Nemyslí si o sobě, že je přispěvatel, ale pomáhá s významným testováním", "https://github.com/sponsors/EPOCHvoyager") }}
    
</div>

## Universal Blue

>Zvláštní poděkování patří [**Emeritus** z Universal Blue](https://github.com/ublue-os/main/blob/main/emeritus.md), kteří přispěli v prvních dnech projektu.

<div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
{{ contributor("Jorge Castro", "castrojo", "zakladatel Universal Blue, Bluefin Lead Maintainer, spolutvůrce edice Bazzite DX", "https://github.com/sponsors/castrojo") }}
{{ contributor("Niklas Haiden", "NiHaiden", "Aurora Lead Maintainer, spolutvůrce edice Bazzite DX") }}
{{ contributor("Benjamin Sherman", "bsherman", "uCore Lead Maintainer, správce modulů jádra, správce hlavního obrazu UBlue") }}
{{ contributor("m2", "m2Giles", "Správce modulů jádra, správce hlavního obrazu UBlue. Opravy chyb a vylepšení.") }}
{{ contributor("Tulip Blossom", "tulilirockz", "Bluefin Maintainer, vede rozšíření Wolfi Bluefin. Četné opravy ovlivňující Bazzite.", "https://github.com/sponsors/tulilirockz") }}
{{ contributor("Gareth Widlansky", "gerblesh", "Údržba obrazů") }}
</div>

## Další přispěvatelé

<div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
{{ contributor("RJ Trujillo", "EyeCantCU", "První správce Bazzite. CI/CD pipeline, počáteční podpora alternativního desktopového prostředí a správná podpora Steam Deck. Emeritní.") }}
{{ contributor("Pat Connors", "nicknamenamenick", "Dokumentace") }}
{{ contributor("Aarron Lee", "aarron-lee", "Tvůrce zásuvných modulů Decky pro alternativní kapesní počítače. Poskytl mnoho časných testů, zejména se zařízeními GPD a Legion Go. Emeritní.") }}
{{ contributor("Jan", "Jan200101", "První správce jádra Bazzite prostřednictvím projektu kernel-fsync. Emeritní.") }}
{{ contributor("Sean Srock", "SuperRiderTH", "Animator. Early Ally tester. Creator of Bazzite Boot/Sleep.") }}
{{ contributor("Bouhaa", "BoukeHaarsma23", "První správce ChimeraOS, který poskytl neocenitelné testování s relací herního režimu. Emeritní.") }}
{{ contributor("RoyalOughtness", "RoyalOughtness", "secureblue správce. Poskytuje opravy chyb souvisejících se zabezpečením.", "https://github.com/sponsors/RoyalOughtness") }}
{{ contributor("Jason Nagin", "JasonN3", "Tvůrce neživého instalačního programu a jeho akce sestavení.") }}
{{ contributor("Marco Rodolfi", "RodoMa92", "Opravy chyb a vylepšení") }}
{{ contributor("FiftyDinar", "fiftydinar", "Opravy chyb a vylepšení") }}
{{ contributor("Matthew Schwartz", "matte-schwartz", "Testování a poradenství v herním režimu Steam") }}
{{ contributor("Atapi", "Sterophonick", "Driver Backports") }}
{{ contributor("XYNY", "xynydev", "Infographics & Alternate Custom Tooling") }}
{{ contributor("termdisc", "termdisc", "Technická podpora") }}
{{ contributor("Justin Garrison", "rothgar", "Developer Relations") }}
{{ contributor("Ian Off", "atimeofday", "QA Testing") }}
{{ contributor("Alex Banna", "abanna", "Prototyping") }}
{{ contributor("Tony", "cyrv6737", "Pilot") }}
{{ contributor("Brian Ketelsen", "bketelsen", "Tooling Expert") }}

</div>

>[**Zobrazit úplný seznam přispěvatelů Bazzite v úložišti GitHub**](https://github.com/ublue-os/bazzite/graphs/contributors)

### Projekt Fedora

Bazzite by neexistoval bez [**Fedora Linux**](https://fedoraproject.org/), protože je postaven přímo na něm.  Projekt Fedora nepřijímá peněžní dary, ale oceňuje hardwarové dary a příspěvky do projektu:

- [**Darování hardwaru**](https://fedoraproject.org/wiki/Donations)
- [**Přispívání**](https://fedoraproject.org/wiki/Contribute)

## Software obsažený v Bazzite

Také vám doporučujeme, abyste přispěli na projekty, které se používají v Bazzite, což nám pomáhá udržovat otevřený zdroj udržitelný!

<sub>(*Pokud nám chyběl software, který je součástí Bazzite a je možné jej darovat, pak [**dejte nám prosím vědět**](https://github.com/KyleGospo/docs.bazzite.gg/issues) nebo [**PR a fix**](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/src/donations.md)!*)</sub>

- [**Atuin**](https://github.com/sponsors/atuinsh)
- [**Bazaar**](https://github.com/sponsors/kolunmi)
- [**Blur My Shell**](https://github.com/sponsors/aunetx)
- [**Clapper**](https://liberapay.com/Clapper)
- [**Davincibox**](https://ko-fi.com/akzel94)
- [**Deja Dup**](https://liberapay.com/DejaDup)
- [**Extension Manager**](https://github.com/sponsors/mjakeman)
- [**eza**](https://github.com/sponsors/cafkafk)
- [**fastfetch**](https://github.com/sponsors/LinusDierheimer)
- **fd** ([David Peter](https://github.com/sponsors/sharkdp) a [Tavian Barnes](https://github.com/sponsors/tavianator))
- [**fzf**](https://github.com/sponsors/junegunn)
- [**freedesktop.org**](https://www.freedesktop.org/wiki/#donations)
- [**Gear Lever**](https://ko-fi.com/mijorus)
- [**GNOME**](https://www.gnome.org/donate/)
- [**GNOME themes for Firefox and Thunderbird**](https://www.patreon.com/rafaelmardojai)
- [**Hanabi**](https://ko-fi.com/jeffshee)
- [**Handheld Daemon**](https://github.com/sponsors/antheas)
- [**Homebrew**](https://github.com/Homebrew/brew#donations)
- [**Just Perfection**](https://buymeacoffee.com/justperfection)
- [**KDE**](https://kde.org/donate/)
- [**Logo Menu**](https://github.com/sponsors/Aryan20)
- [**Mozilla**](https://foundation.mozilla.org/en/?form=donate&gad_source=1)
- [**Pika Backup**](https://opencollective.com/pika-backup)
- [**Terra**](https://github.com/sponsors/FyraLabs)
- [**Thunderbird**](https://www.thunderbird.net/en-US/donate/)
- [**Warehouse**](https://ko-fi.com/heliguy)
- [**Waydroid**](https://opencollective.com/waydroid/donate)
- [**xone**](https://www.paypal.com/donate?hosted_button_id=BWUECKFDNY446)
- [**yq**](https://github.com/sponsors/mikefarah)

## Zvláštní poděkování

Bazzite je komunitní úsilí a bez podpory všech by neexistovalo. Níže uvádíme několik lidí, kteří nám na cestě pomohli:

- [amelia.svg](https://bsky.app/profile/ameliasvg.bsky.social) - Za vytvoření našeho loga a celkového brandingu.
- [SuperRiderTH](https://github.com/SuperRiderTH) - Za vytvoření úvodního videa herního režimu Steam.
- [evlaV](https://gitlab.com/evlaV) - Za zpřístupnění kódu Valve a za to, že je [tato osoba](https://xkcd.com/2347/).
- [ChimeraOS](https://chimeraos.org/) - Za gamescope-session a za cennou podporu na cestě.
- [Jovian-NixOS](https://github.com/Jovian-Experiments) - Za podporu s technickými problémy a za vytvoření podobného projektu. Vážně, běž to zkontrolovat. Je to projekt postavený na NixOS.
- [sentry](https://copr.fedorainfracloud.org/coprs/sentry/) - Za pomoc s potřebnými záplatami jádra a za vytvoření [kernel-fsync repo](https://copr.fedorainfracloud.org/coprs/sentry/kernel-fsync/), které nyní používáme.
- [nicknamenamenick](https://github.com/nicknamenamenick) - Za to, že je MVP, který téměř sám spravuje naší dokumentaci a podpůrnou literaturu, a za nespočet případů pomoci uživatelům.
- [Steam Deck Homebrew](https://deckbrew.xyz) - Za to, že navzdory práci navíc podporují jiné distribuce než SteamOS, a zvláštní poděkování patří [PartyWumpus](https://github.com/PartyWumpus) za to, že pro nás zprovoznil Decky Loader se SELinuxem.
- [cyrv6737](https://github.com/cyrv6737) - Za prvotní inspiraci a základ, kterým se stal bazzite-arch.