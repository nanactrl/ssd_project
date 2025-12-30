<<<<<<< HEAD
# base/apps.py
from django.apps import AppConfig

class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        import base.signals  # noqa
=======
from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        # Import signals only when the app is ready
        import base.signals  # This safely connects all signals
>>>>>>> d37cbd7bcc9fd181b230781706a15cba0601bf65
