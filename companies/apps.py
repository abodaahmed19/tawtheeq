from django.apps import AppConfig
from django.db.models.signals import post_migrate

class CompaniesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'companies'

    def ready(self):
        from .signals import create_initial_companies
        post_migrate.connect(create_initial_companies, sender=self)
