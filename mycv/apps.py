from django.apps import AppConfig


class MycvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mycv'

    def ready(self):
        import users.signals
