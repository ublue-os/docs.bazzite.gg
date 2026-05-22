---
title: Setting up Sunshine on Bazzite
---

# Setting up Sunshine on Bazzite

## Changes to Sunshine on Bazzite 44

Sunshine has been removed from the base Bazzite image along with the update to Fedora 44.

## Why is This Happening?

The Sunshine package is historically shipped and updated with the image. For a long time, Sunshine did not provide a stable package for Fedora 43 and 44, and this forced Bazzite to use the Sunshine-Beta package instead, causing users to have non-functional streaming after an update numerous times, due to multiple changes to their systemd service name.
Removing Sunshine from the base image allows Sunshine's versions to stay independent of Bazzite updates, avoiding the situation mentioned above.

!!! info "As of 16th May 2026, Sunshine has finally provided an F43 and F44 package. Nevertheless, it is still better for Sunshine's updates to stay independent of Bazzite versions."

## What Should I Do If I am Currently Using Sunshine?

The guide below will walk you through switching to the Sunshine flatpak if you already actively use Sunshine, so that you will continue to have a working stream from your Bazzite Sunshine host when the update occurs.
!!! warning "It is highly recommended that you do this with physical access to your machine, or at least with an ssh connection set up."

1. Open the Bazzite Portal and select **Sunshine**
![Bazzite Portal Menu Preview|400x300](../img/sunshine-bazzite-portal-menu.png)
2. Select **Enable**
![Bazzite Portal Submenu Preview|250x200](../img/sunshine-bazzite-portal-submenu.png)
3. A Terminal Window will appear. Wait for the installation to complete and you will be prompted to input your password to give extra permissions to Sunshine for screen capture and other functionalities.
4. This is a good time to test if your new setup works - Your settings should persist.

## Something Went Wrong, What Should I do?

### The \`brew link\` step did not complete successfully

This is a known issue with homebrew on systems with a symlinked home directory. 
!!! info "Consider trying the new stable or beta Sunshine flatpak by updating Bazzite and reinstalling Sunshine through the Bazzite portal."
![Brew Link Fail Preview|400x200](../img/brew-link-fail.png)
To fix this, manually make the directory for the **Target** that brew is complaining about, or run the following command:
`mkdir -p /home/linuxbrew/.linuxbrew/Cellar/xkeyboard-config/2.47/share/xkeyboard-config-2`
Running the unlink and linking commands may also fix it:
`brew unlink xkeyboard-config; brew link --overwrite xkeyboard-config`

### Is a display connected and turned on? (error 503)

!!! info "Capturing with X11 is not supported. Screen capture is now handled via the compositor of your Desktop Environment (Kwin or Mutter) or via Kernel Mode Setting."
This usually means that the Sunshine executable has trouble capturing the screen. Try other screen capture methods such as XDG Portal, Kwin Screencast, or NvFBC.
You may also try explicitly allowing the `Remote control` option under KDE Settings 🡒 Application Permissions 🡒 Sunshine.

### Error: Couldn't import RGB Image: 00003009 (error -1) 

When checking `systemctl --user status homebrew.sunshine*`, the error `Error: Couldn't import RGB Image: 00003009` is observed, and you are using an Nvidia system.
This is speculated to be some issues related to way Sunshine/CUDA is packaged on homebrew. Possible solutions include:

-    Update Bazzite and reinstall Sunshine as a Flatpak through Bazzite Portal
-    Using **XDG Portal Capture** and trying different encoders.
-    Manually specify the GPU to use for capture if available.
-    Installing the Beta version of Sunshine with alternative means.

!!! info "Help Sunshine fix this if you do find a solution by reporting it upstream!"

## Limitations of Installation through Bazzite Portal

The Bazzite Portal only helps you install and set up the stable Sunshine **flatpak** package. If you want to try a beta package for fixes to your system or due to other purposes, you will need to install it manually. 
!!! info "Bazzite Portal retains the ability to install the **experimental** beta Sunshine **brew** package. However, it is known to have issues related to NvFBC capture and Systray indicator."

## Installing Sunshine Beta

You may try to install Sunshine Beta with alternative ways as listed below, albeit with some limitations and downsides:
!!! warning "Installation of Sunshine via these methods is not officially supported. Please report issues with Sunshine **Beta** to the main Sunshine repository, report issues with packaging to their respective packaging repositories."

=== "Installing the Beta Flatpak manually"

    Sunshine does not provide a Beta repository for their flatpak, nor host them on the flathub-beta repository, so you will need to download the flatpak manually from their [GitHub Releases Page](https://github.com/LizardByte/Sunshine/releases)
    1. Click `Read more` at the bottom of your desired release.
    2. Find and download `sunshine_x86_64.flatpak`(or aarch64 for arm devices). Your downloaded file should be saved to `~/Downloads/`
    3. Run the following commands:
    ```bash
    flatpak install --system ~/Downloads/sunshine_x86_64.flatpak
    flatpak run --command=additional-install.sh dev.lizardbyte.app.Sunshine
    systemctl --user enable --now app-dev.lizardbyte.app.Sunshine
    ```

=== "Layering from the COPR"
    
    This is similar to the situation when sunshine is/was included in the image.
    Layering the Sunshine Beta package from the [official Beta COPR](https://copr.fedorainfracloud.org/coprs/lizardbyte/beta/) by running
    ```bash
    sudo dnf5 copr enable lizardbyte/beta
    rpm-ostree install Sunshine
    ```

=== "Layering a community maintained package"
    
    !!! info "This community package is maintained by pvermeer, and is not officially endorsed, nor packaged by Bazzite."
    Layering the Sunshine/Sunshine-Beta community maintained [package](https://copr.fedorainfracloud.org/coprs/pvermeer/sunshine/) by running
    ```bash
    sudo dnf5 copr enable pvermeer/sunshine
    rpm-ostree install sunshine-beta
    ```
    then `rpm-ostree install sunshine` or `rpm-ostree install sunshine-beta`.
    
=== "Installing the experimental brew package"

    !!! warning "This package is experimental and has known issues related to screen capture and systray indicator."
    Select Yes in Bazzite Portal 🡒 App Install 🡒 Sunshine 🡒 Enable Beta (Brew).
    
If you encounter any other issues, feel free to reach out on the [Bazzite Discord](/community.md)!
