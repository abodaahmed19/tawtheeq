from django.db import models
from contracts.models import Contract
from contract_transaction_types.models import ContractTransactionType

class ContractTransaction(models.Model):
    date = models.DateField("date")
    incoming_number = models.TextField("incoming_number", max_length=255, null=True, blank=True)
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='contract_transactions'
    )
    type = models.ForeignKey(
        ContractTransactionType,
        on_delete=models.CASCADE,
        related_name='contract_transactions'
    )
    extract_number = models.TextField("extract_number", max_length=255, null=True, blank=True)
    subject = models.TextField("subject", null=True, blank=True)
    is_documented = models.BooleanField("is_documented", default=False)
    documentation_number = models.TextField("documentation_number", max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'contract_transactions'

    def __str__(self):
        return self.contract.name
