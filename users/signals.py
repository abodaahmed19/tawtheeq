from django.db import connection
from .models import User

def table_exists(table_name):
    return table_name in connection.introspection.table_names()

def create_default_user(sender, **kwargs):
    if not table_exists("users"):
        return

    user, created = User.objects.get_or_create(
        id=1,
        defaults={
            "username": "admin",
            "email": "mail@abodaahmed19.com",
            "is_superuser": True,
            "is_staff": True,
            "name": "عبداللطيف احمد",
            "role": "admin",
        }
    )

    if created:
        user.set_password("123123")
        user.save()
