+++
title = "PostgreSQL-with-podman"
description = "```bash"
+++

# PostgreSQL with podman

## Install

```bash
podman run -d \
  --name postgresql \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=tree \
  -e POSTGRES_DB=postgres_db \
  -p 5432:5432 \
  docker.io/library/postgres:latest
```

## Connect

```bash
podman exec -it postgresql psql -U user -d postgres_db
```
