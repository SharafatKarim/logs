As I'm on archlinux,
let's try to initialize a server, I guess.


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

And then perhaps security!
```bash
sudo mariadb-secure-installation
```

# A GUI?

So I guess GUI is available, so should I try?