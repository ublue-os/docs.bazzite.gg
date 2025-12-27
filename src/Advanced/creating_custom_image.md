<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=43", "fetched_at": "2024-09-03 16:43:11.309087+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## Use Cases

- You want to help **development** by being able to test your contributions prior to submiting to the community.
    - Hardware enablement, experimental features, confirming fixes ahead of merge.
- You want to **swap out applications and other default choices but want to stick close to Bazzite** to get improvements automatically.
    - For example: Bazzite has Waydroid baked into the image, but not setup or running by default.  If you desire to have this package uninstalled, then you could replace it or remove it.
    - You need to layer something like VPN software that has to be on an image but you don't want to maintain your own standalone image. (Deriving off of others is always easier)
    - You want a personal-use image with config and software changes, but also want to benefit from work being completed upstream.

## Recommended Methods

### Option A - Using the Image template

Use the [**official template image**](https://github.com/ublue-os/image-template) to build off of to make your own custom Bazzite preferred over forking the project.

#### Video Guide

https://www.youtube.com/watch?v=IxBl11Zmq5w

### Option B - Forking Bazzite

Sometimes you don't want to make a whole new image from scratch, you just want to change some things without too much extra work by **forking Bazzite**.  It is highly recommended to use the [**Pull application for Github**](https://github.com/apps/pull) to keep your fork in sync.

### Option C - Using BlueBuild

[**BlueBuild**](https://blue-build.org/learn/universal-blue/) is a project that orginally started as a starting point for Universal Blue custom image building and eventually became its own separate project.  All support for Blue-Build images should be directed to the appropriate [communication channels](https://blue-build.org/community/) outside of Universal Blue.
