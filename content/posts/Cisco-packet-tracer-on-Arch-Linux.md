+++
title = "Cisco-packet-tracer-on-Arch-Linux"
description = "- Let's acquire the package from AUR:"
+++

# Cisco packet tracer on Arch Linux

## Installation

- Let's acquire the package from AUR:

  ```bash
  git clone https://aur.archlinux.org/packettracer.git  
  ```

- Log into Cisco Networking Academy (Skills For All / NetAcad) using your Cisco Account. Register an account if you do not have it.

- Go to the following link and download the latest version of Cisco Packet Tracer for Linux (*Packet Tracer 8.2.2 Ubuntu 64bit*),

  - [Cisco Packet Tracer Resource hub](https://www.netacad.com/resources/lab-downloads?courseLang=en-US)

- Move it to the `packettracer` directory.
- Inside the `packettracer` directory, run the following command to build the package:

  ```bash
  makepkg -si
  ```

