---
title: Booting Into Rescue and Emergency Modes
---

# Booting Into Rescue and Emergency Modes

## Preface

Fedora already has a built-in mechanism (provided by `systemd`) for booting into rescue/emergency modes.

However, Fedora (and thus Universal Blue systems), do not set a `root` password during install. Thus, when the emergency or rescue mode is reached, the user is shown the error:

```
Cannot open access to console, the root account is locked.
```

??? note "We've improved the situation for all _Universal Blue_ derivatives using inspiration from _Fedora CoreOS_."

    Now, when booting to [emergency](#booting-to-emergency-mode-2) or [rescue](#booting-to-rescue-mode-3) mode with a locked root account, the user is instead presented a more standard prompt:

```
Press Enter for maintenance
(or press Control-D to continue):
```

At this point, pressing <kbd>Enter</kbd> will drop the user into the appropriate root shell. SELinux will also be active in this mode (unless it has been disabled by other configuration), so this is a good mode to use if needing to reset your password, etc.

See below for more details:

---

## Booting to Emergency Mode

Emergency mode provides the most minimal environment possible and allows you to repair your system even in situations when the system is unable to enter rescue mode. In emergency mode, the system mounts the `root` file system only for reading, does not attempt to mount any other local file systems, does not activate network interfaces, and only starts few essential services.

1. Press <kbd>Esc</kbd> on the keyboard to reach the GRUB boot menu.
   a. If you press <kbd>Esc</kbd> too many times, you may end up at a `grub>` prompt.
   b. Return to the boot menu by typing `exit` and pressing <kbd>Enter</kbd>
2. Select the desired deployment (the top entry is generally correct) and edit by pressing <kbd>E</kbd> on the keyboard.
3. Arrow down to the line starting with `linux` and press <kbd>Ctrl</kbd>+<kbd>E</kbd> to reach the end of the line.
4. Add the word `emergency` to the end of the line.
   a. Ensure there is a space between `emergency` and the pre-existing text.
   b. Equivalent parameters `-b` and `systemd.unit=emergency.target` may be added instead of `emergency`.
5. Press <kbd>Ctrl</kbd>+<kbd>X</kbd> to boot the system.

---

## Booting to Rescue Mode

Rescue mode provides a convenient single-user environment and allows you to repair your system in situations when it is unable to complete a normal booting process. In rescue mode, the system attempts to mount all local file systems and start some important system services, but it does not activate network interfaces or allow more users to be logged into the system at the same time. In Fedora, rescue mode is equivalent to single user mode.

1. Press <kbd>Esc</kbd> on the keyboard to reach the GRUB boot menu.
   a. If you press <kbd>Esc</kbd> too many times, you may end up at a `grub>` prompt.
   b. Return to the boot menu by typing `exit` and pressing <kbd>Enter</kbd>
2. Select the desired deployment (the top entry is generally correct) and edit by pressing <kbd>E</kbd> on the keyboard.
3. Arrow down to the line starting with `linux` and press <kbd>Ctrl</kbd>+<kbd>E</kbd> to reach the end of the line.
4. Add the word `single` to the end of the line.
   a. Ensure there is a space between `single` and the pre-existing text.
   b. Equivalent parameters `1`, `s`, `S`, and `systemd.unit=rescue.target` may be added instead of `single`.
5. Press <kbd>Ctrl</kbd>+<kbd>X</kbd> to boot the system.

---

## Root shell with no password! How can this be secure?

This improvement is implemented such that a user must have the ability to edit the kernel command line. If your bootloader (eg, GRUB) is configured with a password preventing users from modifying the kernel command line, bypassing the password for a locked root account will not be enabled. This is especially important since `emergency` mode can be reached when a filesystem check fails at boot time, not just when specified on the kernel command line.

Given this safeguard, this improved rescue & emergency method is just as secure as setting `init=/bin/bash`, etc. Plus, it is less likely a user will damage SELinux labels using this method.

---

## Reset Forgotten User Password

Forgot the user password to login?  Read the [Fedora Documentation](https://docs.fedoraproject.org/en-US/fedora-silverblue/troubleshooting/#_resetting_passwords_in_rescue_mode) on this topic.  Please remember that the default password for all new Bazzite installations is "**bazzite**" if you did not set one during the installation setup.
