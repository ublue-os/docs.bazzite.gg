<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=2413", "fetched_at": "2024-09-03 16:43:19.836067+00:00"}-->
<!-- ANCHOR_END: METADATA -->


!!! disclaimer

    This wiki may contain outdated information.

## Lenovo Legion Go

![legion_go|690x387, 100%](../../img/legion_go.jpeg)

### Optional Tweaks
- Configure the HHD Overlay by opening it with <kbd>Legion R</kbd>
- Adjust the scaling of the UI in the Display Settings

### Workarounds / Known Issues

- Performance overlay might be reporting inaccurate power consumption.
- Adaptive/auto display brightness is currently broken.
  - Manual brightness slider in Steam's UI works without issues.
- BIOS and controller firmware is **recommended** to update in Windows.

### Updating the BIOS without a Windows installation

Read the [tutorial](/Handheld_and_HTPC_edition/update-bios-lenovo-legion-go.md) on how to update the BIOS for the Lenovo Legion Go without a Windows installation.

### BIOS update breaks Secure Boot key

![secure-boot|603x500, 100%](../../img/secure-boot.png)

Read our [Secure Boot guide](/General/Installation_Guide/secure_boot.md#method-b-after-installation-method) to re-enroll the key after a BIOS update if you keep Secure Boot enabled, which is the default for this device.

!!! info

    As of July 2025, external monitors are working just fine. The external display can be set to its respective native resolution and refresh rate.

    ![legion-go-ext-display|690x387, 100%](../../img/legion_go_ext_display.jpeg)

    Without additional fixes, the internal display only offers its native resolution with the correct aspect ratio. Other resolutions can be chosen, but most of the screen will remain empty.

    ![legion-go-resolutions|690x387, 100%](../../img/legion_go_resolutions.png)
    ![legion-go-int-display-alternative-resolution|690x387, 100%](../../img/legion_go_int_display_alternative_resolution.jpg)



If your screen doesn't display the correct output or looks grainy, noisy, or oddly colorful then you will have to **enter a [TTY session](/Handheld_and_HTPC_edition/quirks.md#tty-if-you-cannot-access-desktop-mode) and enter this command**:

```
rm ~/.config/kwin*
```

Alternatively, **ssh into it and enter this command**:

```
mv ~/.config/kwinoutputconfig.json ~/.config/kwinoutputconfig.json.old
```

## External Resource

For more information, check out the [Legion Go Tips and Tricks guide](https://github.com/aarron-lee/legion-go-tricks) which includes useful scripts for this handheld.

## Contributing

This page is a **wiki**, edit it to add any relevant information you may have regarding the handheld and your experience with Bazzite on it. Make sure to follow proper [contributing guidelines](/CONTRIBUTE.md) before adding any edits.

<hr>

**See also**: [Steam Gaming Mode Overview](../Steam_Gaming_Mode.md)

**<-- Back to [Handheld Wiki](./index.md)**
