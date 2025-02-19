+++
title = "A-moment-with-php"
description = "Let's install with,"
+++

# A Moment With PHP

## Installation

Let's install with,

```bash
sudo pamcan -S php
```

Then a bit of config like described in Archlinux,

```bash
sudo nano /etc/php/php.ini
```

Changes are,

```ini
date.timezone = Asia/Dhaka
extension=mysqli
extension=pdo_mysql
```

## Running

To run a php file, we can use,

```bash
php file.php
```

To serve a php server, we can use,

```bash
php -S localhost:8000
```

> Get the full article with,
>
> - <https://www.php.net/manual/en/features.commandline.webserver.php>

## DB

For MySQL, we can use `PDO` like,

```php
<?php
$servername = "127.0.0.1";
$username = "root";
$password = "tree";

try {
    $conn = new PDO("mysql:host=$servername;dbname=university", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully";
}
catch(PDOException $e)
{
    echo "Connection failed: " . $e->getMessage();
}
?>
```

