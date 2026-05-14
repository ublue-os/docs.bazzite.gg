---
title: Other Handhelds
---

# Other Handhelds

![generic handheld|348x158, 100%](../../img/generic_handheld.jpeg)

## Untested Handhelds

!!! note

    Certain handhelds have been confirmed to boot Bazzite, but are plagued by missing driver support for Linux including missing audio drivers.

Untested handhelds _could work_ with Bazzite, but there may be major issues encountered that are undocumented.  Your mileage may vary with untested hardware. 

Bazzite does **not** have the required setup for other handhelds, so setup will be manually done by the end-user for different functionality if it even works properly on the unsupported device.

### HHD Setup (If Not Enabled By Default on Device)

**Commands for functional HHD**:

```command
systemctl start hhd@yourusername
```

```command
systemctl enable hhd@yourusername
```

!!! important
    Replace `yourusername` with your Bazzite username.
