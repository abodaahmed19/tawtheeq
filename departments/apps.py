from django.apps import AppConfig
from django.db.models.signals import post_migrate

class DepartmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'departments'

    def ready(self):
        from .signals import create_initial_departments
        post_migrate.connect(create_initial_departments, sender=self)
