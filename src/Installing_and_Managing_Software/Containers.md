---
title: Containers
---

# Containers

## What are containers?

Containers are isolated environments for software to run.  Bazzite utilizes containers in a software context for applications that either run better in a container environment or are not available in the Bazaar app store.

---

## Distrobox

[**Distrobox**](./Distrobox.md) allows users to run minimal versions of other Linux operating systems within their own containerized environment with access to their own package managers and repositories. For example, if some software only provides a downloadable `.deb` or `.rpm` package on their website, it can be installed with its corresponding container.

You may also use various Distrobox GUI to help simply this, such as DistroShelf and Kontainer.

---

## Quadlet

[**Quadlet**](./Quadlet.md) is specifically used for running services like media servers, game servers, etc.  Quadlet is advanced in comparison to other package formats and relies heavily on system-level tooling that is pre-installed on Bazzite. There is no `quadlet` command and requires declaratively creating services with it using systemd units and Podman.

---
