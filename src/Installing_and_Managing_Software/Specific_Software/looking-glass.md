---
title: Looking Glass
---

## READ FIRST!
[Looking-Glass](https://looking-glass.io/) is a very experimental project and is not ready for production use!
This means there are no official packages for `looking-glass-client` yet. <br>
For this reason we do not package or ship `looking-glass-client`, we only provide a working configuration and SELinux rules so that it can be used in Bazzite.
We do however package the `kvmfr` kernel module and include it with the system image, as such file any issue with the `kvmfr` module in Bazzite to our discord or github issue tracker and ping @HikariKnight in the issue.

We will only tell you to file an issue with Looking-Glass directly if the issue is not related to the packaging and configuration of the `kvmfr` module.

## Enabling the kvmfr module
You can enable the kvmfr module by running this command:

```bash
ujust setup-virtualization kvmfr
```

## Compiling Looking-Glass client
Create a `fedora:latest` distrobox that we will use to compile the binary, use the following command to make the container, when asked about what image to use, select the default one as I have verified this guide works with that image for building.
This distrobox has to be made manually without the `--nvidia` flag which our ujust automatically applies to enable hardware acceleration, however we explicitly do not want it in order to make `cmake-data` successfully install.

!!! note

    If you are not using the latest Fedora version, please change `latest` to match your version number, this is to avoid dependency versioning issues.

```bash
distrobox create -i "fedora:latest" -n "tmp-lookingglass"
```
If you want to use a separate home folder for this then make a folder to contain this containers home folder and run this command instead:
```bash
distrobox create -i "fedora:latest" -n "tmp-lookingglass" -H "/path/to/new/home"
```
Enter the container with `distrobox enter tmp-lookingglass`

Follow [upstream documentation](https://looking-glass.io/docs/rc/build/#installing-build-dependencies), you can find the fedora build dependencies [here](https://looking-glass.io/wiki/Installation_on_other_distributions) and you will also want to install the dependencies mentioned for **PipeWire users**.
Since we will be building for **Wayland** and not X11 you will also need the package `libdecor-devel`

When you get to the part for running `cmake`, use the command:
```
cmake -DENABLE_WAYLAND=1 -DENABLE_X11=0 -DENABLE_PULSEAUDIO=0 -DENABLE_PIPEWIRE=1 ..
```
The above command will disable X11 support and Pulseaudio support, but enable Pipewire and Wayland support, this will avoid any issues as we do not ship the X11 dependencies for `looking-glass`.

Copy the built `looking-glass-client` binary to `/run/host/home/$USER/.local/bin/`
You can do that using the following commands if you followed the looking-glass documentation.
```bash
mkdir /run/host/home/$USER/.local/bin
cp ./looking-glass-client /run/host/home/$USER/.local/bin/
```
7. Test and see if `looking-glass-client` binary works for you on the host with your VM running.
8. Exit the container and run the below command to remove the container we used to build the Looking-Glass client.
```bash
distrobox stop tmp_lookingglass ; distrobox rm tmp_lookingglass
```
