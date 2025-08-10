# Keyd - a key mapping daemon

## Installation

```bash
sudo pacman -S keyd
```

## Systemd service

```bash
sudo systemctl start keyd
```

> Use `sudo systemctl enable keyd` to start keyd on boot.

## Config

Edit the `/etc/keyd/default.conf` file like,

```
[ids]

*

[main]

leftshift = wakeup

```

> To know the key name and other stuff, use `keyd -h`.
