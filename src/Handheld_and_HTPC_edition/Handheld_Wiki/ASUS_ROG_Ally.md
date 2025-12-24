<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=2414", "fetched_at": "2024-09-03 16:43:21.670173+00:00"}-->
<!-- ANCHOR_END: METADATA -->


!!! disclaimer

    This wiki may contain outdated information.

## ASUS ROG Ally / ASUS ROG Ally X

![ally|603x500, 100%](../../img/ally.png)

### General Notes

- Holding the Armoury Crate button (on the side) allows you to switch to Mouse Mode
- Enable the Steam Power Button Handler setting in Handheld Daemon

### Optional Tweaks

- Adjust settings in Handheld Daemon.
- Adjust the scaling of the UI in the Display Settings.

### Workarounds / Known Issues
- Changing A/C power sometimes leads to a stuck TDP.
- Some users report that "Auto UMA" in the bios can cause crashes in some games.
  - If you encounter this, then try setting the VRAM in bios to **4GB** or **8GB**.
- LED indicator is on max brightness by default and cannot be changed on any other operating system outside of Windows.
  - This is tied to the firmware.
  - This also affects when the ally is charging and sleeping.
- The Ally does **not support** button holding for the Steam or QAM buttons.
  - Steam Input's chords do not work by default.
    - Swapping the Start/Select button(s) is a workaround.
- Suspend can break if SMT is disabled
- Fingerprint driver does not work.
- Storage shows duplicate drives.
  - This is a visual bug, do **not** attempt to format this drive!
- Turning on the wake animation when resuming from sleep causes the device to act erratically.
  - No controls outside of Steam.
  - Steam's top and bottom panels missing.

#### CPU Boost?

Disabled by default to prevent excessive power draw to the device.

More information can be found [**here**](https://github.com/aarron-lee/SimpleDeckyTDP/blob/main/README.md#are-there-cpu-boost-controls) about this.

## Contributing

This page and all of the links to each specific handheld are **wikis**, edit it to add any relevant information you may have regarding the handheld and your experience with Bazzite on it. Make sure to follow proper [contributing guidelines](/CONTRIBUTE.md) before adding any edits.

<hr>

**See also**: [Steam Gaming Mode Overview](../Steam_Gaming_Mode.md)

**<-- Back to [Handheld Wiki](./index.md)**
