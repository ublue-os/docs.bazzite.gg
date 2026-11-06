---
title: Rebase Guide
---

# Rebase Guide

## What is Rebasing?

!!! warning "Rebasing between different desktop environments (e.g. KDE Plasma to GNOME) **may cause issues** and is **not officially supported**. You may read more about it [here](/General/FAQ/#can-i-switch-to-a-different-desktop-environment-on-my-current-installation)."

Rebasing allows users to switch to a different **Image Flavor** and/or **Update Branch** _without_ having to reinstall and lose personal files and application data.

> It is recommended to use the [Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal.md) or [Bazzite Rollback Helper utility](./bazzite_rollback_helper.md) to rebase.

---

## Rebase Scenarios

- Rebase to specific images of older builds within the last 90 days if issues are occurring on the newest build of Bazzite.
- Rebase to other Fedora Atomic Desktop images including other Bazzite images.
  - Do **not** rebase between different desktop environments.

---

## Swapping Between Bazzite Images

For convenience and disambiguity,

- **Image Flavor** will be referred to as **IMAGE**
- **Update Branch** will be referred to as **TAG**

### Check Current Image Tag

Check the Image Flavor and Update Branch of your system first.

=== "Bazzite Updater"

    In [Bazzite Updater](./bazzite_updater.md), go to **Other Utilities → System Image Information → Current Image**.

    You will see your current system version in the format of `IMAGE:TAG`.

=== "Bazzite Rollback Helper"

    Use the following command to see your current **IMAGE** and **TAG**:

    ```bash
    brh current
    ```

=== "Backend Commands"

    ```bash
    rpm-ostree status
    ```

    Your **image reference** will be shown under "**Deployments:**" and the output will be in the **full ostree ref** format, where `<image>` and `<tag>` are your current **IMAGE** and **TAG** respectively:

    ```console
    ● ostree-image-signed:docker://ghcr.io/ublue-os/<image>:<tag>
    ```
    
    !!! example

        ```console
        ● ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:testing
        ```
        
        means that:
        
        - **IMAGE** is `bazzite-deck`
        - **TAG** is `testing`

---

### Rebasing to Another Bazzite Variant

The process of rebasing is very similar to updating(or rather the other way around), as Bazzite simply boots a new [bootable container image](/General/terms/?h=bootable+container+image#underlying-technology). All of the commands below simply downloads and prepares a new image for the system to boot with.

!!! tip "If it isn't clear already, you need to reboot to complete the rebase after you have completed the commands below."

!!! warning "Rebasing between different desktop environments (e.g. KDE Plasma to GNOME) **may cause issues** and is **unsupported**."

=== "Bazzite Portal"

    [Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal.md) provides two entries to allow easy switching between `stable` and `testing` Update Branches.
    
    Simply select **Bazzite Portal → Manage Bazzite → Move to the stable update track/Move to the testing update track**.
    
    !!! info "For switching between Bazzite Image Flavors such as `bazzite-nvidia`, use other methods."

=== "Bazzite Rollback Helper"

    Input the rebase `<target>` in any one of the following formats:
    
    - Update Branch only: `TAG`
    - Image Flavor and Update Branch: `IMAGE:TAG`
    - Full Ostree Ref: `ostree-image-signed:docker://ghcr.io/ublue-os/IMAGE:TAG`
    
    ```bash
    brh rebase <target>
    ```
    
    !!! example
    
        - Rebasing to `stable` with Update Branch only:
        ```bash
        brh rebase stable
        ```
        
        - Rebasing to `bazzite-nvidia`'s `testing` branch with Image Flavor and Update Branch:
        ```bash
        brh rebase bazzite-nvidia:testing
        ```
        
        - Rebasing to `bazzite-deck`'s `stable` branch with **full ostree ref**:
        ```bash
        brh rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:stable
        ```

=== "Backend Commands"

    ```bash
    rpm-ostree rebase <image-ref>
    ```

    Where `<image-ref>` is the **full ostree ref**.
    
    !!! example
        
        - Rebasing to `bazzite-deck`'s `stable` branch with **full ostree ref**:
        ```bash
        rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:stable
        ```

=== "In Steam (Bazzite-Deck Only)"

    Bazzite-Deck images can switch branches via **Settings → System → OS Update Channel** in Steam Gaming Mode.

    If you have enabled **advanced update channel**, then additional options will appear. The options map as the following:

    | Steam Update Channel| Bazzite Update Channel(TAG) |
    | :------------------ | :-------------------------: |
    | Stable | `:stable` |
    | Release Candidate | `:testing` |
    | Beta | `:testing` |
    | Beta Candidate | `:unstable` |
    | Main | `:unstable` |

!!! info

    If you encounter the following message:
    
    ```console
    error: Old and new refs are equal: ostree-image-signed:docker://ghcr.io/ublue-os/bazzite:testing
    Rebase failed. Image may not exist or be accessible.
    ```

    This means the Image Flavor/Branch you are trying to rebase to is the same as the one you are currently on. Simply [update](/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/updating_guide/) to receive the newest version of your current image.

---

## Differences between Update Branches

=== "The Stable Branch"

    This is the first of two branches intended for end-users, intended for general users looking for a smooth experience.

    - Stable (TAG: `stable`)
    - Default branch that's used in normal Bazzite installations.
    
    !!! info "Typically, stable images are updated every [fortnight](https://en.wikipedia.org/wiki/Fortnight) (i.e. every other week)."

=== "The Testing Branch"

    This is the second branch intended for advanced end-users who are willing to help, test, and try out new and experimental features.

    - [Testing (TAG: `testing`)](https://github.com/ublue-os/bazzite/compare/main...testing)
      - Get a sneak peak of future Bazzite builds before release.
      - Bugs may frequently appear.
      - Users are encouraged to rebase back to `:stable` after testing a major release.

    !!! info "Testing images are built nearly every day, sometimes even multiple times per day."

=== "The Unstable Branch"

    This is intended for Bazzite's core contributors and maintainers only and is used for major changes that need frequent testing. 
    
    !!! warning "The unstable branch can fall behind updates even in the stable branch since it is testing specific major changes and is not something that is built on a schedule."

---

## Switching Update Branches in Steam Gaming Mode
  
> See [here](/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/rebase_guide/#__tabbed_2_3).

---

## Rebasing to older builds

!!! warning "Switching to older Bazzite builds will not bring new updates until you upgrade back to `:stable` which means there will be no security updates until you rebase back to the stable branch."

Like rolling back to the previous Bazzite deployment, users can also rebase to a specific Bazzite builds that was were built within the last 90 days.  All of your userdata will remain intact.

However, you will have to rebase manually back to `:stable` to update the system to receive the features and security patches. 

### Viewing Available Images

You may view the list of available stable builds by using the following methods:

=== "Bazzite Rollback Helper"

    !!! info "You may also list other Update Branches by specifying them with `brh list TAG` or run `brh` interactively."

    ```bash
    brh list
    ```

    !!! example

        To list images in the `testing` Update Branch:
        ```bash
        brh list testing
        ```

=== "Using the Command Line"

    Edit the following command to your liking, replacing `bazzite` and `stable-`:

    ```bash
    skopeo list-tags docker://ghcr.io/ublue-os/bazzite | grep -E "\bstable-" | sort -rV
    ```

=== "View on Browser"

    > Go to Bazzite's [GitHub Releases Page](https://github.com/ublue-os/bazzite/releases) to find specific builds.

---

### Rebasing to a Specific Build

Rebasing to a specific build is as simple as using a **TAG** with a format of `BRANCH-VERSION.YEARMONTHDAY`

=== "Bazzite Rollback Helper"

    ```bash
    brh rebase VERSION-YEARMONTHDAY
    ```
    
    !!! example
        
        Rebasing to `bazzite-deck`'s (_Fedora 39_) build on **13th January, 2024**:
        
        ```bash
        brh rebase bazzite-deck:stable-39.20240113
        ```

        <small>_(Please note that this build is no longer available since it is past the 90 day limit and is only used as an example for this documentation.)_</small>
        
        Rebasing to `bazzite-deck`'s newest Fedora 43 build, if you are already on `bazzite-deck`:
        
        ```bash
        brh rebase stable-43
        ```

=== "Backend Commands"

    ```bash
    rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/IMAGE:VERSION-YEARMONTHDAY
    ```
    
    !!! example
        
        Rebasing to `bazzite-deck`'s (_Fedora 39_) build on **13th January, 2024**:
        ```bash
        rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:39-20240113
        ```

        <small>_(Please note that this build is no longer available since it is past the 90 day limit and is only used as an example for this documentation.)_</small>

---
