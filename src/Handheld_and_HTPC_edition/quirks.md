---
title: Steam Gaming Mode Quirks and Workarounds
---

# Steam Gaming Mode Quirks and Workarounds

## How do I use my microSD card that I used on my Steam Deck running SteamOS?

Open a host terminal and enter this **command**:

```bash
ujust switch-to-ext4
```

---

## How do I specify the correct monitor for Gaming Mode to use? (HTPC only)

In Desktop Mode, open a host terminal and run the following **command** to find your Display Output Name:

=== "KDE"

    ```bash
    kscreen-doctor -o
    ```

=== "GNOME"

    ```bash
    gnome-randr
    ```
    !!! note

        It has been reported that some systems don't properly report the Display Output Name when using gnome-randr. You may run the command below to list the names of all connected outputs without any details, and compare them with the previous command output to find your actual Display Output Name.
    
        ```bash
        grep -r '^connected' /sys/class/drm/*/status | grep -Po 'card.?-\K([^/]*)'
        ```
After finding the correct Display Output Name, you may now create a file to tell Steam Gaming Mode to use your display.

=== "Using the GUI"
    
    In Desktop Mode or Nested Desktop, 
    
    1. Create the directory `~/.config/environment.d` if it does not exist already.
    
    2. Create the file under the aforementioned directory named `10-gamescope-session.conf` if it does not exist already.

    3. Add the following line to the file:
        `OUTPUT_CONNECTOR=DP-1`
    !!! info "Make sure you change `DP-1` to your Display Output!"
    
    4. Save the file, restart, and verify that your device is outputing on the correct display.
    
=== "Using the command line"
    
    Run the following commands to create the file:
    
    !!! info "Make sure you change `DP-1` to your Display Output!"
    
    ```bash
    mkdir -p ~/.config/environment.d
    echo "OUTPUT_CONNECTOR=DP-1" >> ~/.config/environment.d/10-gamescope-session.conf
    ```

---

## Audio output not working (Default Device)

This issue happens usually with HDMI TV audio. Enter Desktop Mode and in system settings, disable devices that do not match the sound output that you are using. 

!!! info "A typical fix is disabling everything except HDMI for your TV audio."

---

## Change physical keyboard layout for Steam Gaming Mode

Steam Gaming Mode has no official way to change the physical keyboard layout and defaults to the US layout. If you want to change the layout, then you may set it globally through an environment variable.

=== "Using the GUI"
    
    In Desktop Mode or Nested Desktop, 
    
    1. Create the directory `~/.config/environment.d` if it does not exist already.
    
    2. Create the file under the aforementioned directory named `10-gamescope-session.conf` if it does not exist already.

    3. Add the following line to the file, replacing `us` with the correct layout.
        `XKB_DEFAULT_LAYOUT=us`
    !!! info 
    
        The layout name is usually a [2-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements),
        Alternatively, you may use one of the following commands to see a list without a description:

        -   `localectl list-x11-keymap-models`
        -   `localectl list-x11-keymap-layouts`
        -   `localectl list-x11-keymap-variants [layout]`
        -   `localectl list-x11-keymap-options`
    
    4. Save the file, restart, and verify that you have the correct keyboard layout.
    
=== "Using the command line"
    
    Run the following commands to create the file, replacing `us` with the correct layout.:
    
    ```bash
    mkdir -p ~/.config/environment.d
    echo "XKB_DEFAULT_LAYOUT=us" >> ~/.config/environment.d/10-gamescope-session.conf
    ```
    
    !!! info 
    
        The layout name is usually a [2-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements),
        Alternatively, you may use one of the following commands to see a list without a description:

        -   `localectl list-x11-keymap-models`
        -   `localectl list-x11-keymap-layouts`
        -   `localectl list-x11-keymap-variants [layout]`
        -   `localectl list-x11-keymap-options`

!!! note 

    This fix will also work in Desktop Mode, including when running Nested Gamescope or when using Nested Desktop, but it has its own quirks: 
    
    -   <kbd>altgr</kbd> + <kbd>2</kbd> to write `@` on the Norwegian layout will still not work, though the basic keyboard layout does work. Fortunately, The <kbd>altgr</kbd> key is not needed for normal typing on the Norwegian layout. 
    -   The <kbd>altgr</kbd> key has been reported to work on the French layout
    -   Your mileage may vary on differing keyboard layouts.

---

## How do I disable certain "Steam Deck" features that conflict with my setup?

**Scenarios where this is desirable**:

-   Keyboard and mouse does not work for a certain game

-   The game’s launcher for adjusting video settings or adding mods does not launch

-   Certain features/graphics options are not available

Open the game's properties on Steam and [**add this launch option**](/Gaming/launch-options-env-variables/#where-to-set-launch-options):

```bash
sd0 %command%
```
> Read more about Launch Options and Environment Variables [here](/Gaming/launch-options-env-variables/)

---

## Why do specific Decky Loader plugins not function on Bazzite?

Some plugins are built specifically for SteamOS or the Steam Deck, and won’t necessarily work on Bazzite or non-Steam-Deck hardware.

-   For example, the [DeckMTP plugin](https://github.com/dafta/DeckMTP) only works on the Steam Deck models and will not work on other hardware.

---

## How do I use SteamDeckGyroDSU on hardware that isn't the Steam Deck?

You typically cannot use SteamDeckGyroDSU outside of the Steam Deck, though you may try disabling Steam Input and it _may_ work depending on your hardware and use case.

---

## How do I specify which GPU that Steam Gaming Mode should use?

Open a TTY session with an **external physical keyboard** using this **keyboard combination**:
   <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>F4</kbd>

!!! info "This feature is superceded by the new [CardWire](https://github.com/OpenGamingCollective/cardwire) GPU Manager in Bazzite-Deck 44."
   
```bash
export-gpu
```

---

## I lost my "Return to Gaming Mode" shortcut

You can restore this shortcut by opening terminal and running:

```bash
ujust restore-gamemode-shortcut
```

---

## Black Screen When Booting into Gaming Mode

If you: 

-   Encounter a black screen after the Bazzite spinner, 
-   Does not have Internet connection,
-   find that it is obvious that Steam is trying and failing to update due to the lack of/ slow Internet;

You may follow the instructions [here](#i-cannot-progress-past-this-screen) to boot into Desktop Mode.

---
 
## I cannot progress past this screen

!!! info "The instructions below are also applicable for [Black Screen When Booting into Gaming Mode](#black-screen-when-booting-into-gaming-mode)."

![If your controller supports Bluetooth, select Next to pair to your Steam Machine.](../img/connect_controller.jpg)

1. Open a TTY session with an **external physical keyboard** using this **keyboard combination**:
    <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>F4</kbd>
2. Login to your user.
3. Enter this command:
```bash
steamos-session-select desktop
```
4. Log into Steam in Desktop mode, and reboot the device.

---

## Stuck on 'Update calculating: Time Remaining'

![Update time remaining](../img/update_calculating_time_remaining.jpg)

Reboot the device.

---

## Steam broke and Gaming Mode is broken too

In scenarios where Steam Gaming Mode refuses to start due to an issue with the Steam client:

Follow the instructions [here](#stuck-at-the-bazzite-logo).

---

## "Something went wrong while displaying this content" Error

This is most likely due to a broken Decky Loader plugin you have installed and can be fixed by uninstalling the broken plugin. 

!!! note "Specific CSS Loader themes may also cause this issue."

---

## Why is VRR not working on my VRR-compatible display?

!!! note "Preliminary support for HDMI 2.1 FRL, VRR, and DSC on AMDGPU is expected to arrive at Linux Kernel version 7.2. This section will be updated accordingly once the updates arrive on Bazzite."

Most of the time this is because the device is connected via HDMI which does not yet support VRR on Linux.

> You may read more about it [here](https://www.phoronix.com/news/HDMI-2.1-OSS-Rejected).

---

## Rainbow Display

![My-Eyes|690x430](../img/hdr-woes.png)

Toggle HDR on and off in the Quick Access Menu.

!!! note "You may need to additionally enable the "Force Composite" option found in the Developer Options, of which [Developer Options] also has to be enabled in the Steam settings beforehand."

---

## Stuck at the Bazzite logo

!!! info "The instructions below are also applicable for [Steam broke and Gaming Mode is broken too](#steam-broke-and-gaming-mode-is-broken-too)."

=== "Desktop Mode Method"

    Open Bazzite Portal → Troubleshoot → Reset Steam installation, then reboot.

=== "TTY Method (_if you cannot enter Desktop Mode_)"

    Access a TTY session with <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>F4</kbd>, login with your Bazzite username and password, then enter this command:
    
    !!! info "The default username and passwords are both `bazzite` if you have not set it during installation."
    
    ```bash
    ujust fix-reset-steam
    ```
    You can then reboot with this command:
    
    ```bash
    systemctl reboot
    ```

=== "Backup Method"

    !!! warning

        Try rebooting your device first before proceeding with the next steps! You may lose your games, saves, and other content if this is done incorrectly.

    Press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>F4</kbd> to enter the TTY and login using your Bazzite username and password, then run the following command.
    
    !!! info "The default username and password are both `bazzite` if you haven't set them during setup."
    
    ```bash
    mv ~/.local/share/Steam ~/.local/share/Steam.bak
    ```

    2.  This command will rename the `Steam` to `Steam.bak`. After restarting Steam, Steam will automatically recreate the `Steam` folder.
    3.   You can move your games from the renamed `Steam.bak` directory to the new `Steam` directory if you had any installed previously on your internal storage.
    4.  You may use <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>F2</kbd> to exit the TTY.

> You may also follow the video guide below：
https://www.youtube.com/watch?v=gE1ff72g2Gk

---

## Nvidia GPU Exclusive Issues with Steam Gaming Mode

- "Enable GPU accelerated rendering in web views (requires restart)" must be enabled in the Steam settings for better performance in the UI.
  - Enabling this option will most likely cause game-breaking graphical artifacts.
- HDR can cause game-breaking graphical artifacts.
