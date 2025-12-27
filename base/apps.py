from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        # Import signals only when the app is ready
        import base.signals  # This safely connects all signals
