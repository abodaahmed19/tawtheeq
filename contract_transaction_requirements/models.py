from django.db import models
from contract_transaction_types.models import ContractTransactionType

class ContractTransactionRequirement(models.Model):
    name  = models.CharField("name", max_length=255)
    type = models.ForeignKey(
        ContractTransactionType,
        on_delete=models.CASCADE,
        related_name='contract_transaction_requirements'
    )
    is_active = models.BooleanField("is_active", default=True)

    class Meta:
        db_table = 'contract_transaction_requirements'

    def __str__(self):
        return self.name
