from .base import *  # noqa: F403
from .base import env

DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-@!v7^6er!xca5a@yghoa9i0hj5l!3x7g@%=jlv+#nn!oj7ycv$",
)

hosts = env(
    "DJANGO_ALLOWED_HOSTS",
    default="coreflare.local localhost host.docker.internal",
)

ALLOWED_HOSTS = hosts.split(" ")

# Tailwind CSS - Hot Reloading
THIRD_PARTY_APPS += ["django_browser_reload"]
MIDDLEWARE += ["django_browser_reload.middleware.BrowserReloadMiddleware"]
