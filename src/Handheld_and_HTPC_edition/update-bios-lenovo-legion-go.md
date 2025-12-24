---
title: How to Update the BIOS on the Lenovo Legion Go from Bazzite (No Windows Required)
search:
  boost: 0.5
---

!!! quote ""

    This was originally a [forum post](https://universal-blue.discourse.group/t/how-to-update-the-bios-on-the-lenovo-legion-go-from-bazzite-no-windows-required/3064) by [Mister Fluffles](https://universal-blue.discourse.group/u/mrfluffles/summary).

!!! warning

    **THIS METHOD HAS ONLY BEEN TESTED ON THE LENOVO LEGION GO**. Please only follow this guide if you are using a Lenovo Legion Go. **PLEASE BE AWARE THAT DOING THIS ON OTHER DEVICES RISKS MAKING A BRICK**

Updating the BIOS on the Legion Go from Bazzite works, and means not needing to keep a pesky Windows partition around for updates. Here's how to do so. (Credit to the [ChimeraOS](https://chimeraos.org/) devs and [aarron-lee](https://github.com/aarron-lee) on github for the original fwupdtool instructions)

Warning: Your battery must be above 25% for the fwupdtool tool to function correctly. In addition, only perform this process when on AC power.

!!! warning

    If you have secure boot enabled, you will need to disable it prior to updating your BIOS. Please see the end of the guide for the steps needed to re-enable it afterwards.

1. Download the BIOS update from Lenovo
2. Use 7z (or file-roller, etc) to extract the contents of the EXE file
3. The file we want is the isflash.bin file. Keep that one, the rest don't matter.
4. Run this command:

```
sudo fwupdtool install-blob isflash.bin
```

Afterwards, select the 'System Firmware' option from the presented menu and after fwupdtool finishes, select 'Y' to reboot.

Let the update run. After the initial update screen, your Legion Go may sit on a black screen for anywhere from 30 seconds to several minutes. **Just wait.** The system will automatically reboot to another 'Updating...' screen after that, and then will wind up in the GRUB menu eventually.

Once you are in the GRUB menu (as the BIOS update has re-enabled secure boot and wipes your custom enrolled keys if you had any, so you won't be able to boot) do the following:

- Reboot back into the BIOS
- Disable Secure Boot
- (Optional) Set UMA back to 'Auto' (or whatever your preferred setting is) as the BIOS update will have set it back to 3gb.
- Save, and reboot. If you don't use Secure Boot at all, you're done. Congrats!

If you do use Secure Boot, you will need to boot back into Bazzite's Desktop mode, and run

```
ujust enroll-secure-boot-key
```

Reboot once more. Follow the normal [MOK enroll process](/General/Installation_Guide/secure_boot.md), and afterwards enable secure boot in the BIOS again, and all should be working.

!!! warning

    Please note that this process has not been tested on Dual-boot systems, as it is presumed that on a dual-boot system you can simply update via Windows.
