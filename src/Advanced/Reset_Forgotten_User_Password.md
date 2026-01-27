# Reset Forgotten User Password

!!! important

    This method is only if you forgot your current user password! Changing your current password should be done through the desktop environment.

!!! warning

    Follow this guide **at your own discretion** because you can break your system attempting any of this.

![Edit the command for the latest boot entry|690x351](../img/Edit_the_command_for_the_latest_boot_entry.png)

1. Reboot your device.
2. Press <kbd>Esc</kbd> on the keyboard to reach the GRUB boot menu.
   a. If you press <kbd>Esc</kbd> too many times, you may end up at a `grub>` prompt.
   b. Return to the boot menu by typing `exit` and pressing <kbd>Enter</kbd>
3. Edit the last deployment by presssing <kbd>E</kbd> on your keyboard.

![Boot with init=/bin/bash|689x359](../img/Boot_with_init_bin_bash.jpeg)

Edit the GRUB prompt and append `init=/bin/bash` to the line beginning with `linux`.

![Reboot|689x359](../img/Reset_Password_Reboot.jpeg)

Continue boot process with <kbd>Ctrl</kbd>+<kbd>X</kbd>

Once you are in the GRUB command line:

1. Temporarily mount SELinux

   `mount -t selinuxfs selinuxfs /sys/fs/selinux`

2. Load SELinux policy

   `/sbin/load_policy`

3. Enter your new password (i.e. `passwd bazzite`)

   `passwd [INSERT USERNAME HERE]`

4. Sync

   `sync`

5. Reboot

   `/sbin/reboot -ff`

![Commands|690x334](../img/Reset_Password_Commands.png)

Your user password should now be reset.

> Thanks to [Colin Walters](https://github.com/cgwalters) for the [solution](https://github.com/ublue-os/main/issues/469#issuecomment-1885264886).

## Not Working?

Many users forget steps regarding SELinux because of old habits. If you've created everything but the SELinux steps above, then the file `/etc/shadow` will be unreadable or unreachable by any process.

The good way to check if `/etc/shadow` is in bad SELinux configuration is to execute following command:

`ls -Z /etc/shadow`

![ls -Z /etc/shadow|690x334](../img/Unlabeled_Etc_Shadow.png)

You should also notice _unlabeled_t_ on your side.
You now have to fix the label on `/etc/shadow` with command below:

`restorecon -v /etc/shadow`

And then check result again with `ls -Z /etc/shadow`, which should lead to:

`system_u:object_r:shadow_t:s0   /etc/shadow`

Now the system is ready and you can reboot with `/sbin/reboot -ff`.
