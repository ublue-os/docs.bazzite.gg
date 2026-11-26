---
title: "Backup"
---

# Backup

 There are a few user friendly tools that can handle backing these files up, these tools are available in the Bazaar as flatpaks and are quick and easy to setup. 

## 3-2-1 Rule

For backups the "golden rule" is the 3-2-1 rule:

- Backups in three (3) places
- Two (2) copies on-site
- One (1) off-site

This means there should be three copies of your data at any point, two copies should be local and one should be in a remote location (in case of a fire damaing the first two copies).

## User Files

These files include photos (like of your family) and documents (such as tax forms), this would include things that would be very difficult if not impossible to recreate. Some common locations to backup include:

- /home/*username*/Documents
- /home/*username*/Music
- /home/*username*/Pictures

Another location is where user installed Flatpaks store their data:

- /home/.var/app/*flatkak-name*

### Pika Backup

[Pika Backup](https://flathub.org/en/apps/org.gnome.World.PikaBackup) is great for multiple locations including on-site, off-site and external/internal drive to store the data.

### Deja Dup

[Deja Dup](https://flathub.org/en/apps/org.gnome.DejaDup) is great for a single location such as on-site, off-site and external/internal drive to store the data.

## Test Often

It is also recommended to test restoring your data with your backups, this makes sure that they can be used when needed and that all of the data is intact.
