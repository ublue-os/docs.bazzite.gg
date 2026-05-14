---
title: Rebase Guide
---

# Rebase Guide

## What is Rebasing?

!!! warning

    Rebasing between different desktop environments (e.g. KDE Plasma to GNOME) **may cause issues** and is **unsupported**.

Rebasing allows users to switch to a different image **without** having to reinstall and lose personal files and application data.

>[**It is recommended to use the Bazzite Rollback Helper utility**](./bazzite_rollback_helper.md).

## Rebase Scenarios

- Rebase to specific images of older builds within the last 90 days if issues are occurring on the newest build of Bazzite.
- Rebase to other Fedora Atomic Desktop images including other Bazzite images.
  - Do **not** rebase between different desktop environments.

## How do I swap between Bazzite images?

See what channel or build you are on by **entering this command in a host terminal**:

```command
rpm-ostree status
```

Check under "**Deployments:**" and the output should be similar to:
```
 ● ostree-image-signed:docker://ghcr.io/ublue-os/[*image*]:[*channel*]
```

Switch to another Bazzite variant by entering the command for each specific image.

Open the terminal and **enter**:

```
rpm-ostree rebase <image>
```

### **Example**:

!!! warning

    Rebasing between different desktop environments (e.g. KDE Plasma to GNOME) **may cause issues** and is **unsupported**.

```command
rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:stable
```

For rebasing to the KDE Plasma version of the Bazzite-Deck image.

## How do I change the Bazzite's update branch? (Stable, Testing, and Unstable)

There are two update branches intended for end-users:

- Stable (`:stable`)
  - Default branch that's used in normal Bazzite installations.
- [Testing (`:testing`)](https://github.com/ublue-os/bazzite/compare/main...testing)
  - Get a sneak peak of future Bazzite builds before release.
  - Bugs may frequently appear.
  - Encouraged to rebase back to `:stable` after testing a major release.

### The Unstable Branch

This is intended for Bazzite's core contributors and maintainers only and is used for major changes that need frequent testing. The unstable branch can fall behind updates even in the stable branch since it is testing specific major changes and is not something that is built on a schedule.

## Switching Update Branches in Steam Gaming Mode
  
Bazzite-Deck images can switch branches in `Settings > System > OS Update Channel` in Steam Gaming Mode.

If you enabled **advanced update channel**, then additional options will appear. The options map as the following:

```
Stable (:stable)
Release Candidate (:testing)
Beta (:testing)
Beta Candidate (:unstable)
Main (:unstable)
```

###  **Example**:

```command
rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite:testing
```

For the **testing** branch on the AMD/Intel Desktop image.

## Rebasing to older builds

!!! attention

    You will have to rebase back to `:stable` once you want to upgrade to the newest release.

!!! warning

    Switching to older Bazzite builds will not bring new updates until you upgrade back to `:stable` which means there will be no security updates until you rebase back to the stable branch.

Like rolling back to the previous Bazzite deployment, users can also rebase to a specific Bazzite builds that was were built within the last 90 days.  All of your userdata will remain intact, but like how the warning indicates above, you will have to rebase manually back to `:stable` to update the system to receive the newest build.

View the list of available stable builds by **entering**:

```command
skopeo list-tags docker://ghcr.io/ublue-os/bazzite | grep -- "stable-" | sort -rV
```

Rebasing to a specific build requires users to open a host terminal and **enter**:

```command
rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/IMAGE-NAME:VERSION-YEARMONTHDAY
```

**Example**:

```command
rpm-ostree rebase ostree-image-signed:docker://ghcr.io/ublue-os/bazzite-deck:39-20240113
```

For the _Jan. 13th 2024_ `bazzite-deck` (_Fedora 39_) build.

<small>_(Please note that this build is no longer available since it is past the 90 day limit and is only used as an example for this documentation.)_</small>
