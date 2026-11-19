---
title: Ayaneo Handhelds
---

# Ayaneo Handhelds

!!! disclaimer

    Sleep functionality requires a BIOS update. Note that this wiki may contain outdated information.

## Known Issues

- Suspending the device requires the latest BIOS update.
  - Reports of controller issues on wake have reported inconsistency. Enabling "full initial usb support" in Bios seems to have an impact on how frequent the issue is.
- VRAM size option is missing from BIOS as it's controlled by AYASPACE application under windows.
- RGB may need to controlled using the HueSync Decky Plugin.

> You can still change the amount of UMA buffer size using [Smokeless_UMAF](https://github.com/DavidS95/Smokeless_UMAF), but this method has its own associated risks. Only proceed **at your own risk**.

---

## Ayaneo Geek 1S

![photo_5875160389711413569_y|663x500, 100%](../../img/Ayaneo_Geek_1S.jpeg)

### Known Issues

> See [here](#known-issues).

---

## e-GPU Support:

Using e-GPU via Thunderbolt 3, 4 and USB4 enclosures over USB4 are partially supported.

=== "AMD"

    - Automatic switch at boot with [all-ways-egpu](https://github.com/ewagner12/all-ways-egpu/tree/main) works fine using method 2 and 3 at boot, however method 1 is unfortunately not supported.
      - The script needs to be installed with [Steam Deck/User Installation](https://github.com/ewagner12/all-ways-egpu/blob/main/README.md#steamosbazziteuser-installation).
    - There are no known issues booting with eGPU attached(RDNA 2 GPUs are a known working configuration) and Bazzite will set the required kernel arguments by default (`amdgpu.ppfeaturemask`).
      - Using `rpm-ostree kargs --append-if-missing=pci=nommconf` (or editing the kernel command line with `rpm-ostree kargs --editor`) may still be needed according to user testing as some applications  may underperform otherwise.

=== "NVIDIA"
  
    Currently untested but _may_ work with the “-deck-nvidia” variant of bazzite.

---

## External Resource

Check out the [original thread](https://universal-blue.discourse.group/t/ayaneo-geek-1s-2s-linux-bazzite-support-is-already-almost-there-lets-add-them-to-the-officially-supported-devices/1046) for more information and updates on this device.

Ayaneo Geek 1S is (as of April 2025) the only Ryzen 7000 handheld which is yet to receive the EC update that increase battery life. You can follow and report [on this discord thread](https://discord.com/channels/717181357109018694/1301507866754289745).

---
