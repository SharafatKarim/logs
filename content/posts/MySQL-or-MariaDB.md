+++
title = "MySQL-or-MariaDB"
description = "As I'm on archlinux,
let's try to initialize a server, I guess."
+++

As I'm on archlinux,
let's try to initialize a server, I guess.

---

And our beloved wiki!
- [WiKi](https://wiki.archlinux.org/index.php/MariaDB#Installation)

---

## Init
First, go to root,
```bash
su
```
I don't know but it actually works!
   
Then, install the server,
```bash
mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```
Then comes, the real commands,
but first systemd service
```bash
sudo systemctl start mariadb
```
also don't forget to enable it
```bash
sudo systemctl enable mariadb
```

And then perhaps security!
```bash
sudo mariadb-secure-installation
```

# A GUI?
So I guess GUI is available, so should I try?
