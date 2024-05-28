+++
title = "A-bit-of-pacman"
description = "A package manager for Arch Linux and its variants."
+++

# A bit of pacman

## Pacman

A package manager for Arch Linux and its variants.

### Installing packages

```bash
sudo pacman -S <package>
```

### Removing packages

```bash
sudo pacman -R <package>
```

### Updating packages

```bash
sudo pacman -Syu
```

### Searching packages

```bash
sudo pacman -Ss <package>
```

### Querying packages

```bash
sudo pacman -Qi <package>
```

### Querying files

```bash
sudo pacman -Ql <package>
```

## Extras

### Database lock file

```bash
sudo rm /var/lib/pacman/db.lck
```

