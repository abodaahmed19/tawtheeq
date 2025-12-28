from django.db import connection
from .models import Agent

def table_exists(table_name):
    return table_name in connection.introspection.table_names()

def create_initial_data(sender, **kwargs):
    if not table_exists("agents"):
        return

    data = [
        "وكالة المشاريع",
        "وكالة التعمير والمشاريع",
        "وكالة الخدمات"
    ]

    for name in data:
        Agent.objects.get_or_create(name=name)
