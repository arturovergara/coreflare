from .base import *  # noqa: F403
from .base import env

DEBUG = False
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-@!v7^6er!xca5a@yghoa9i0hj5l!3x7g@%=jlv+#nn!oj7ycv$",
)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# Disable logging console output
LOGGING["root"]["handlers"] = ["null"]  # noqa: F405

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
