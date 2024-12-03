# Podman linking

Here's a short guide,
- <https://discussion.fedoraproject.org/t/how-to-link-a-container-podman/77108>

## Tldr;

I think the simplest is to run the two containers in the same pod. Something like:

```bash
podman pod create -n logicaldoc -p 8080:8080
podman run <other flags> --pod logicaldoc mysql:8.0
podman run <other flags> --pod logicaldoc logicaldoc/logicaldoc-ce
```
