+++
title = "Django-wsgi"
description = "1. Set STATIC_ROOT to the directory from which you want to serve collected static files:"
+++

# Django + WSGI

## Static files

### Deployment

1. Set STATIC_ROOT to the directory from which you want to serve collected static files:

```python
STATIC_ROOT = "/var/www/example.com/static/"
```

2. Collect static files into STATIC_ROOT:

```bash
python manage.py collectstatic
```

This copies all files from your app/static and other static locations into STATIC_ROOT. Serve the resulting files with your chosen web server (nginx, Apache, CDN, etc.).

## References

- Django static files how-to: <https://docs.djangoproject.com/en/3.2/howto/static-files/>
- Django WSGI deployment: <https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/>

