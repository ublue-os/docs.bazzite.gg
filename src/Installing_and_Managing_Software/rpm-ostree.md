---
title: Package Layering
---

# Package Layering

## Using `rpm-ostree`

!!! attention

    Layering packages irresponsibly can be **destructive** and may prevent updates as well as other issues until the layered packages are removed.

Install [Fedora Linux packages](https://packages.fedoraproject.org/) on top of the existing Bazzite image by using the `rpm-ostree` terminal command.  Use for packages that cannot be installed from Homebrew or ran inside of a container.  Layered packages can break system upgrades until removed due to dependency issues since the package will have to be updated with the rest of the image.  It also causes upgrades to take longer to run.

### Key Notes

- Layering packages will **require** a system reboot when it finishes creating the new deployment with the package(s) added to your image.
- Use this method as a **last resort** and for anything at a "system-level" only since it can pause updates, if the package contains dependency issues with future upgrades, until the package is uninstalled.

## Terminal Commands Related to Package Layering

**Use these commands at your own risk**.

### Layer Package(s)

```
rpm-ostree install <package>
```

Installs Fedora package(s) to the system that stay between updates, reboot to apply the installation.

### Uninstall Layered Package(s)

```
rpm-ostree uninstall <package>
```

Uninstalls any layered packages added to the system, reboot to apply the uninstallation.

### Search for a Package

```
rpm-ostree search <package>
```

Searches for Fedora packages that can be installed.

### View Currently Layered Packages

```
rpm-ostree status
```

This will output the layered packages in your Bazzite installation.

## Installing RPM Files

Fedora Distrobox containers should be used for most `.rpm` files, but sometimes they need to be installed to your host if it isn't working well with a container.

You can install RPM binaries **to your host** with `rpm-ostree` by entering:

```
rpm-ostree install <package>.rpm
```

You may need to copy the full path (`/path/to/rpmfile.rpm`) for it to install properly.

!!! important

    The downside of installing local RPM files outside of the Fedora repositories is updates for the specific RPM package will not apply automatically.

## How do I add/remove [COPR](https://copr.fedorainfracloud.org) repositories?

!!! warning

    It is highly advised to **not** use third-party COPR repos if possible, so be aware there are risks associated with it including broken updates until removed.

=== "Enable COPR"

    === "DNF5 (Fedora COPR)"

        ```sh
        sudo dnf5 copr enable <USER>/<PROJECT>
        ```

    === "DNF5 (repo file)"

        This method works with COPR other than Fedora's (ex.: [Docker](https://docs.docker.com/engine/install/fedora/#set-up-the-repository))

        ```sh
        sudo dnf5 config-manager addrepo --from-repofile=https://url/to/file.repo
        ```

    === "Manually"

        1. Download the .repo file and save it to `/etc/yum.repos.d/`

        2. Then install the package(s) with `rpm-ostree`

        3. Reboot

        If you experience issues updating your system due to GPG signature issues, then this can be fixed by either removing the COPR repository, or editing the file by changing `gpgcheck=1` to `gpgcheck=0` (or similar) and saving it **at your own risk**.

=== "Disable COPR"

    !!! warning "Ensure to remove any package installed with the COPR beforehand."

    === "DNF5 (Fedora COPR)"

        ```sh
        sudo dnf5 copr disable <USER>/<PROJECT>
        ```

    === "DNF5 (repo file)"

        Remove the `.repo` at `/etc/yum.repos.d/`

    === "Manually"

        Remove the `.repo` at `/etc/yum.repos.d/`

## How to restore default COPRs

```sh
# Remove all current repos
sudo rm /etc/yum.repos.d/*

# Now copy the default repo files fro /usr/etc to /etc
sudo cp /usr/etc/yum.repos.d/* /etc/yum.repos.d/
```

## **MAJOR** caveats using `rpm-ostree`

Layering packages can cause **severe consequences** including:

- Pause system updates until package(s) are uninstalled.
- Prevent rebasing to different images until package(s) are uninstalled.
- Conflict with existing packages as part of the image leading to dependency issues.
- Updates taking longer to download as you layer more packages to your system.

Layering packages are mostly intended for **system-level applications, libraries, and other dependencies**. It is recommended to use Flatpak, Homebrew, containers, AppImage, Waydroid, or running the Windows version through a compatibility layer **before** installing software with `rpm-ostree`.  Layering packages for a temporary time period is the better alternative than keeping a package layered indefinitely.

## How to remove **ALL** layered packages

If you run into issues upgrading due to a layered package conflict, then either optionally uninstall the conflicted package(s) or remove all layered packages with this **command**:

```bash
rpm-ostree reset
```

## Project Website

https://coreos.github.io/rpm-ostree/
