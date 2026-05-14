---
title: Ayaneo Handhelds
---

# Ayaneo Handhelds

!!! disclaimer

    Sleep functionality requires a BIOS update.

## Ayaneo Geek 1S

![photo_5875160389711413569_y|663x500, 100%](../../img/Ayaneo_Geek_1S.jpeg)

### Known Issues

- Suspending the device requires the latest BIOS update.
  - Reports of controller issues on wake have reported inconsistency. Enabling "full initial usb support" in Bios seems to have an impact on how frequent the issue is.
- VRAM size option is missing from BIOS as it's controlled by AYASPACE application under windows. You can change the amount of UMA buffer size using [Smokeless_UMAF](https://github.com/DavidS95/Smokeless_UMAF), but this method has its own associated risks.

### Functional HHD

```
sudo systemctl enable --now hhd@$(whoami)
```

### e-GPU Support:

- e-GPU Thunderbolt 3/4 and USB4 enclosures over USB4 are supported.
  - **AMD**:
    - Automatic switch at boot with [all-ways-egpu](https://github.com/ewagner12/all-ways-egpu/tree/main) works fine using method 2 and 3 at boot, unfortunately method 1 is not supported.
      - The script needs to be installed with [Steam Deck/User Installation](https://github.com/ewagner12/all-ways-egpu/blob/main/README.md#steamosbazziteuser-installation).
    - No issue in booting with eGPU attached. Tested on RX 6800 and no kernel parameters are needed since Bazzite is now enabling the needed argument by default (amdgpu .ppfeaturemask).
      - Using `rpm-ostree kargs --append-if-missing=pci=nommconf` (or editing the kernel command line with `rpm-ostree kargs –editor`) is still needed according to my testing because some applications otherwise may underperform.
    - Some AMD cards requires to set a correct limit for GPU and Memory Clocks, this is a known issue that is present also on Desktops. I suggest installing LACT and setting the correct limits for the card.
  - **NVIDIA**: currently untested but _may_ work with the “-nvidia-deck” variant of bazzite.

### External Resource

Check out the [original thread](https://universal-blue.discourse.group/t/ayaneo-geek-1s-2s-linux-bazzite-support-is-already-almost-there-lets-add-them-to-the-officially-supported-devices/1046) for more information and updates on this device.

Ayaneo Geek 1s is (as of April 2025) the only Ryzen 7000 handheld which is yet to receive the EC update that increase battery life. You can follow and report [on this discord thread](https://discord.com/channels/717181357109018694/1301507866754289745).
