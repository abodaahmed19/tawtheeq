from django.db import connection
from .models import ContractTransactionType

def table_exists(table_name):
    return table_name in connection.introspection.table_names()

def create_initial_data(sender, **kwargs):
    if not table_exists("contract_transaction_types"):
        return

    data = [
        (1, "إستلام إبتدائي"),
        (2, "إستلام نهائي"),
        (3, "تسليم موقع"),
        (4, "إيقاف أعمال"),
        (5, "إستئناف أعمال"),
    ]

    for _id, name in data:
        ContractTransactionType.objects.get_or_create(
            id=_id,
            defaults={"name": name}
        )
