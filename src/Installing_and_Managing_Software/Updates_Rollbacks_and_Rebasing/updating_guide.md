---
title: Update Guide
---

# Update Guide

![System Updates|200x200, 100%](../../img/System_Updates.png)

## Updating Bazzite

!!! attention

    Bazzite needs at least 3% free storage on its installation drive to update properly.

Bazzite updates its own customizations, Fedora’s upstream packages, graphics drivers, and all software installed via Bazaar.

=== "Desktop Images"

    Bazzite Desktop **automatically checks** for updates daily and installs them during idle periods, such as when you're not gaming or running intensive tasks.
    
    - There is a check in-place to only update the image when your CPU, battery, and RAM usage meets certain requirements.

    Updates will be downloaded in the background and will **apply on the next reboot** and should contain the newest build of Bazzite. You may also check for and update manually by using [**Bazzite Updater**](./bazzite_updater.md).

    !!! info "Typically, stable images are updated every [fortnight](https://en.wikipedia.org/wiki/Fortnight) (i.e. every other week)."

=== "Bazzite-Deck Images"

    Automatic updates are **disabled** by default on Bazzite Deck Images.

    - Updates can be managed in Steam Gaming Mode **manually** by the user.
    - Open **Steam Menu → Settings → System → Check for Updates → Apply**
      - Alternatively, you may also use [**Bazzite Updater**](./bazzite_updater.md).
      - Simply **Reboot** to apply system upgrades.

=== "Terminal Command"

    You may use the following command to update if you are:
    
    - Stuck without a graphical session 
    - Connected via `ssh`
    - In a `tty`.

    ```bash
    ujust update
    ```
    
    !!! note "If you are having troubles with the system, seek help by reaching out to us via the [Bazzite Discord server](/community/#discord-no-discord-account)"

---

## Do I have to reboot immediately after every system update?

**No**, but the **system upgrade will not apply until the next reboot**. User-installed applications from Bazaar **can be upgraded without rebooting**.

- **Desktop images**: While your device is running, newer updates will still download in the background once a day, and will be waiting to be applied until the device is rebooted.
- **Bazzite-Deck images**: Updates will be checked daily and can be downloaded and installed at your leisure similar to how SteamOS handles upgrades.

---

## How do I view the changelog for each update?

Changelogs can be viewed in [Bazzite Updater](./bazzite_updater.md#viewing-changelogs) or [GitHub Releases](https://github.com/ublue-os/bazzite/releases).

!!! tip "Make sure to take note of your **current image version** and branch when viewing. A lot of releases are for the **testing** branch only."

Alternatively, you may also view the **differences in packages** between the current and pending image by using the following command:

```bash
rpm-ostree db diff
```

Additionally, you may also view the **security advisory information** via the following command:

```bash
rpm-ostree status -a
```

---

## Metered / Limited Network Connections & Data Caps

!!! note

    This is an unsupported configuration since updates are expected to be running daily for both the operating system and applications.

Open the System Settings of your desktop environment and turn on the setting relating to a metered connection (Data caps or incur charges).  This setting will **pause** automatic updates for Bazzite.

---
