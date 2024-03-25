import os

from django.core.asgi import get_asgi_application

from app import create_app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.config.configs")

django_app = get_asgi_application()

app = create_app()
