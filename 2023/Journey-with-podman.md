# Journey with podman

## Let's start

### Installation

With pacman, it's easy,

```bash
sudo pacman -S podman
```

### First pull

#### Alpine

```bash
podman pull docker.io/library/alpine
```

#### First run

```bash
podman run -it --rm docker.io/library/alpine
```

##### -it: These are two options combined

- i stands for interactive, and it allows you to interact with the container's stdin.
- t allocates a pseudo-TTY, which enables a terminal inside the container.

So, -it together is often used when you want to run an interactive session inside the container

##### or, perhaps you want to run

```bash
podman run --name test --rm docker.io/library/alpine "cat" /etc/os-release
```

Here's the breakdown of the command:

- podman run: This is the command to run a container with Podman.
- --name test: This option assigns the name "test" to the running container. This allows you to reference the container by this name instead of using its container ID.
- --rm: This option instructs Podman to automatically remove the container when it exits. This is useful for temporary containers.
- docker.io/library/alpine: This is the name of the Docker image from which to create the container. In this case, it's the official Alpine Linux image from Docker Hub.
- "cat" /etc/os-release: This is the command that will be executed within the container. It runs the cat command to display the contents of the /etc/os-release file, which contains information about the operating system.

#### Exited? Want to return?

```bash
docker start -a -i `docker ps -q -l`
```

Explanation:

- docker start start a container (requires name or ID)
- -a attach to container
- -i interactive mode
- docker ps List containers
- -q list only container IDs
- -l list only last created container

#### And then, to list all

And to list all,

```bash
podman images
```

### Getting rid of it?

Just list first,

```bash
podman ps -a
```

and then,

```bash
podman rm <container-id>
```
