from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AgentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agents'

    def ready(self):
        from .signals import create_initial_data
        post_migrate.connect(create_initial_data, sender=self)
