This guide has only been tested on the 2025 Asus Rog Xbox Ally. It MAY also work for the Xbox Ally X and the older Asus Rog Ally/Ally X, but it has NOT been tested on those devices.

## WARNING
WARNING: This will COMPLETELY wipe your device. You will lose Windows and all your games and settings. Please make sure this is what you want to do before proceeding.

## Pre-Installation: Wiping the device

### Prerequisites
1. A Rog Xbox Ally (or possibly Xbox Ally X, Ally X, Ally, etc.)
1. An external keyboard that can connect to the device's USB-C port, either directly or through a USB-A-to-C adapter. You MUST have this in order to use the terminal, which we will need to wipe the drive before Bazzite installation.

### Preparation
1. First make sure you've already downloaded Bazzite and burned it onto a USB drive. If not, follow the instructions on the [download page](https://bazzite.gg/#image-picker).
1. Shut down the device or reboot it.
1. As soon as it starts rebooting (before or as soon as you see the Rog startup logos), hold down the `VOLUME UP` button. Keep holding it until you see a text UI that gives you a choice of boot devices or `ENTER SETUP`.
1. Choose `ENTER SETUP` to access the BIOS.
1. In the BIOS, do the following
  - Disable Secure Boot
  - Disable Fast Boot
  - Set SMA to 4G or 8G instead of Auto
1. Save the settings and exit, which will cause the device to reboot. Hold down the `VOLUME UP` key again and proceed to the next section.

### Wiping the drive
1. At the startup menu, use the control pad to choose the USB drive with Bazzite on it. Push A to boot into it.
1. Wait for the installer to load. At the first UI screen where it asks you to select a language, do NOT select one yet. Instead, plug in your external keyboard.
1. On the keyboard, push CTRL-ALT-F2. This should bring you into a terminal.
1. In the terminal, type the command `fdisk /dev/nvme0n1`.
1. You should see the prompt `Command (m for help):`. Type in `d` (for delete) and push enter.
1. It will ask you which partition to delete, but you can just push enter again to select the highest partition # (probably 5).
1. Do this several more times to delete each partition one by one until fdisk says there are no more partitions left to delete.
1. WARNING: Continuing will WIPE YOUR ENTIRE DEVICE, including Windows and all your games and settings. Be absolutely sure you want to do this before continuing.
1. Type `w` (for write) to finalize your changes. If successful, you'll see the message `Partition table has been altered`.
1. Back at the regular prompt, type `reboot` and push enter. The device will reboot. Hold down the `VOLUME UP` button yet again in order to get back to the boot menu.

### Continuing the Bazzite install.
1. Now you can finally install Bazzite by following the regular installation instructions for handheld PCs, starting at [Step 3](https://docs.bazzite.gg/General/Installation_Guide/Installing_Bazzite_for_Handheld_PCs/#3-installer-setup).
