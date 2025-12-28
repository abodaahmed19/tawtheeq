from django.db import models
from contracts.models import Contract

class ContractSuspensionPeriod(models.Model):
    from_date = models.DateField("from_date")
    to_date  = models.DateField("to_date", null=True, blank=True)
    reason  = models.CharField("reason", max_length=255, null=True, blank=True)
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name='suspension_periods'
    )

    class Meta:
        db_table = 'contract_suspension_periods'

    def __str__(self):
        return f"{self.contract.number} suspended from {self.from_date} to {self.to_date or 'ongoing'}"

    @property
    def duration_days(self):
        if self.to_date:
            return (self.to_date - self.from_date).days
        return None