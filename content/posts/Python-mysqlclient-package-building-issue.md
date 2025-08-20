+++
title = "Python-mysqlclient-package-building-issue"
description = "While installing a python environment for django, we need a package called, `mysqlclient`, which uses `wheel` to build."
+++

# Python `mysqlclient` package building issue

While installing a python environment for django, we need a package called, `mysqlclient`, which uses `wheel` to build.

> As described in cpanel[1]  
> cPanel, L.L.C. doesn’t develop or ship Python WSGI web applications,... . when using pip install mysqlclient pip try to build mysqlclient package into a wheel but it is not a wheel.

# Alternative approach

So, this library should be installed from the root shell system wide to solve this issue. 

## For Debian/ Ubuntu

```shell
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

## For Red Hat/ CentOS

```shell
sudo yum install python3-devel mysql-devel
```

> If this approach doesn't work, we will really appreciate it if we get `docker` container support or, shell access support in cpannel. 

# References

[1] - https://stackoverflow.com/questions/76430550/error-while-install-mysqlclient-package-cpanel-terminal 

