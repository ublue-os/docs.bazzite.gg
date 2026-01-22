---
title: Credits and Donating
---

# Credits and Donating

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
                  >Sponsor</a>
                </small>
            {% endif %}
            <div><small>{{ description or "" }}</small></div>
        </div>
    </div>
{%- endmacro %}

Enjoy using Bazzite and want to help sustain its development? Consider sponsoring the project and its individual maintainers and contributors.

<div class="button-container">
    <a href="https://opencollective.com/bazzite-us" target="_blank" class="sponsor-button">Sponsor Bazzite ($ USA)</a>
    <a href="https://opencollective.com/bazzite-eu" target="_blank" class="sponsor-button">Sponsor Bazzite (€ Europe)</a>
</div>

## Bazzite Maintainers

<div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
{{ contributor("Kyle Gospodnetich", "KyleGospo", "Founder, Image & CI/CD Lead", "https://github.com/sponsors/KyleGospo") }}
{{ contributor("HikariKnight", "HikariKnight", "Virtualization, Scripting, User Support", "https://github.com/sponsors/HikariKnight") }}
{{ contributor("Noel Miller", "noelmiller", "Community Manager, Installer Enhancements, Custom Image Tooling", "https://github.com/sponsors/noelmiller") }}
</div>

## Bazzite Core Contributors

<div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
{{ contributor("Zeglius", "Zeglius", "Scripting, Documentation Maintenance, Live ISOs Maintainer", "https://github.com/sponsors/Zeglius") }}
{{ contributor("CheckYourFax", "CheckYourFax", "Community Support, Issue Wrangling") }}
{{ contributor("Valerie", "valerie-tar-gz", "Social Media Manager, Technical Support") }}
{{ contributor("Amélia", "ameliasvg", "Logo and Mascot Creator") }}
{{ contributor("Kurt Himebauch", "xXJSONDeruloXx", "ujust Extraordinaire. Decky wrangler. Framegen.") }}
{{ contributor("wolfyreload", "wolfyreload", "Visual Guides on Youtube. Major tester.") }}
{{ contributor("CharlieBros", "CharlieBros", "Language Translations on Spanish") }}
{{ contributor("Crono", "EPOCHvoyager", "Does not think of himself as a contributor but helps a lot with significant testing", "https://github.com/sponsors/EPOCHvoyager") }}

</div>

## Universal Blue

>Special thanks to Universal Blue's [**Emeritus**](https://github.com/ublue-os/main/blob/main/emeritus.md) who has contributed in the early days of the project.

<div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
{{ contributor("Jorge Castro", "castrojo", "Universal Blue founder, Bluefin Lead Maintainer, Co-creator of Bazzite DX edition", "https://github.com/sponsors/castrojo") }}
{{ contributor("Niklas Haiden", "NiHaiden", "Aurora Lead Maintainer, Co-creator of Bazzite DX edition") }}
{{ contributor("Benjamin Sherman", "bsherman", "uCore Lead Maintainer, Kernel modules maintainer, UBlue Main image maintainer") }}
{{ contributor("m2", "m2Giles", "Kernel modules maintainer, UBlue Main image maintainer. Bug Fixes & Enhancements.") }}
{{ contributor("Tulip Blossom", "tulilirockz", "Bluefin Maintainer, Leads Wolfi Bluefin expansion. Numerous fixes affecting Bazzite.", "https://github.com/sponsors/tulilirockz") }}
{{ contributor("Gareth Widlansky", "gerblesh", "Image Maintenance") }}
</div>

## Other Contributors

<div style="display: flex; flex-wrap: wrap; gap: 0.4rem;">
{{ contributor("RJ Trujillo", "EyeCantCU", "Early Maintainer of Bazzite. CI/CD Pipelines, Initial Alternate Desktop Environment Support, and proper Steam Deck support. Emeritus.") }}
{{ contributor("Aarron Lee", "aarron-lee", "Decky plugin creator for alternate handhelds. Provided a lot of early testing, especially with GPD and Legion Go devices. Emeritus.") }}
{{ contributor("Jan", "Jan200101", "Early Kernel maintainer of Bazzite through the kernel-fsync project. Emeritus.") }}
{{ contributor("Sean Srock", "SuperRiderTH", "Animator. Early Ally tester. Creator of Bazzite Boot/Sleep animations.") }}
{{ contributor("Bouhaa", "BoukeHaarsma23", "Early ChimeraOS maintainer that provided invaluable testing with gamemode session. Emeritus.") }}
{{ contributor("RoyalOughtness", "RoyalOughtness", "secureblue maintainer. Provides bug fixes related to security.", "https://github.com/sponsors/RoyalOughtness") }}
{{ contributor("Jason Nagin", "JasonN3", "Creator of the non-Live Installer and its build action.") }}
{{ contributor("Marco Rodolfi", "RodoMa92", "Bug Fixes & Enhancements") }}
{{ contributor("FiftyDinar", "fiftydinar", "Bug Fixes & Enhancements") }}
{{ contributor("Matthew Schwartz", "matte-schwartz", "Steam Gaming Mode Testing & Consulting") }}
{{ contributor("Atapi", "Sterophonick", "Driver Backports") }}
{{ contributor("XYNY", "xynydev", "Infographics & Alternate Custom Tooling") }}
{{ contributor("termdisc", "termdisc", "Technical Support") }}
{{ contributor("Justin Garrison", "rothgar", "Developer Relations") }}
{{ contributor("Ian Off", "atimeofday", "QA Testing") }}
{{ contributor("Alex Banna", "abanna", "Prototyping") }}
{{ contributor("Tony", "cyrv6737", "Pilot") }}
{{ contributor("Brian Ketelsen", "bketelsen", "Tooling Expert") }}
</div>

>[**View the full list of Bazzite contributors in the Gitub repository**](https://github.com/ublue-os/bazzite/graphs/contributors)

### Fedora Project

Bazzite would not exist without [**Fedora Linux**](https://fedoraproject.org/) since it is built directly on top of it.  The Fedora Project does not take monetary donations, but values hardware donations and contributions to the project:

- [**Donating Hardware**](https://fedoraproject.org/wiki/Donations)
- [**Contributing**](https://fedoraproject.org/wiki/Contribute)

## Software Included in Bazzite

We also encourage you to donate to the projects that are used in Bazzite which helps us keep open source sustainable!

<sub>(*If we missed software that is part of Bazzite and can be donated to, then [**please let us know**](https://github.com/KyleGospo/docs.bazzite.gg/issues) or [**PR a fix**](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/src/donations.md)!*)</sub>

- [**Atuin**](https://github.com/sponsors/atuinsh)
- [**Bazaar**](https://github.com/sponsors/kolunmi)
- [**Blur My Shell**](https://github.com/sponsors/aunetx)
- [**Clapper**](https://liberapay.com/Clapper)
- [**Davincibox**](https://ko-fi.com/akzel94)
- [**Deja Dup**](https://liberapay.com/DejaDup)
- [**Extensions Manager**](https://github.com/sponsors/mjakeman)
- [**eza**](https://github.com/sponsors/cafkafk)
- [**fastfetch**](https://github.com/sponsors/LinusDierheimer)
- **fd** ([David Peter](https://github.com/sponsors/sharkdp) and [Tavian Barnes](https://github.com/sponsors/tavianator))
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

## Special Thanks

Bazzite is a community effort and wouldn't exist without everyone's support. Below are some of the people who've helped us along the way:

- [amelia.svg](https://bsky.app/profile/ameliasvg.bsky.social) - For creating our logo and overall branding.
- [SuperRiderTH](https://github.com/SuperRiderTH) - For creating our Steam game mode startup video.
- [evlaV](https://gitlab.com/evlaV) - For making Valve's code available and for being [this person](https://xkcd.com/2347/).
- [ChimeraOS](https://chimeraos.org/) - For gamescope-session and for valuable support along the way.
- [Jovian-NixOS](https://github.com/Jovian-Experiments) - For supporting us with technical issues and for creating a similar project. Seriously, go check it out. It's our Nix-based cousin.
- [sentry](https://copr.fedorainfracloud.org/coprs/sentry/) - For assistance with needed kernel patches and for creating the [kernel-fsync repo](https://copr.fedorainfracloud.org/coprs/sentry/kernel-fsync/) we now use.
- [nicknamenamenick](https://github.com/nicknamenamenick) - For being the MVP nearly single-handedly upkeeping our documentation and support literature, and countless cases of helping users.
- [Steam Deck Homebrew](https://deckbrew.xyz) - For choosing to support distributions other than SteamOS despite the extra work, and a special thanks to [PartyWumpus](https://github.com/PartyWumpus) for getting Decky Loader working with SELinux for us.
- [cyrv6737](https://github.com/cyrv6737) - For the initial inspiration and the base that became bazzite-arch.
