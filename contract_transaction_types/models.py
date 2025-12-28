from django.db import models

class ContractTransactionType(models.Model):
    name  = models.CharField("name", max_length=255)
    is_active = models.BooleanField("is_active", default=True)

    class Meta:
        db_table = 'contract_transaction_types'

    def __str__(self):
        return self.name
