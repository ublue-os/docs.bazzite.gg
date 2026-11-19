---
title: GPD Handhelds
---

# GPD Handhelds

!!! disclaimer

    This wiki may contain outdated information.

## General Information & Tweaks

- Adjust RGB with Steam Gaming Mode or via Huesync Decky Plugin.
- GPD devices typically have a physical switch that can be toggled to enable a separate desktop/mouse mode.

---

## General Issues

- Devices using the Ryzen 7 6800U or any of its derivatives requires the fingerprint scanner to be disabled to have working suspend-resume.
- Devices using the Ryzen 7 7840U, or any of its derivatives (2023-2025) have partially working suspend-resume, where the device is forced into hibernation after a 5% battery drain. This issue is tracked [here](https://gitlab.freedesktop.org/drm/amd/-/issues/3154).
- Back buttons may need to be manually remapped before they are usable.
  - Manually remap back buttons using the QAM, which is now handled by [OpenGamepadUI.](https://github.com/ShadowBlip/OpenGamepadUI)
- Games can sometimes default to 800p resolution.
  - Manually change the resolution per game in the game's **Properties → General → Maximum Game Resolution** to either **Native** or other higher resolutions.

---

## GPD Win 4

![gpdwin4|690x328, 100%](../../img/gpdwin4.jpeg)

### Optional Tweaks

> See [General Information & Tweaks](#general-information-tweaks)

### Known Issues

> See [General Issues](#general-issues)

---

## GPD Win Max 2

![placeholder_gpdwinmax2|407x312, 100%](../../img/GPD_Win_Max_2.png)

### Optional Tweaks

- Recommended **Display** settings in Steam Gaming Mode:
  - **Use Native Color Temperature**: Enabled

> See [General Information & Tweaks](#general-information-tweaks)

### Known Issues

- If the OS is installed on an m.2 2230 SSD in the secondary drive slot, it can cause suspend issues.
  - The OS should be only installed onto the primary internal SSD.
- Gyroscope is non-functional.

> See [General Issues](#general-issues)

---

### External Resource

For more information, check out the [GPD Win Tips and Tricks guide](https://github.com/aarron-lee/gpd-win-tricks) which includes useful scripts for GPD handhelds.

---
