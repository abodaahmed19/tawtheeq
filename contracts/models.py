from django.db import models
from departments.models import Department
from companies.models import Company
from datetime import timedelta

class Contract(models.Model):
    number = models.CharField("number", max_length=100)
    name = models.CharField("name", max_length=255)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='contracts'
    )
    amount = models.DecimalField("amount", max_digits=20, decimal_places=2)
    signing_date = models.DateField("date_signing")
    site_handover_date  = models.DateField("date_receipt_site", null=True, blank=True)
    actual_start_date  = models.DateField("date_handover_site", null=True, blank=True)
    duration = models.IntegerField("duration", null=True, blank=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='contracts'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('expired', 'Expired'),
            ('suspended', 'Suspended'),
        ],
        default='active'
    )
    is_suspended = models.BooleanField("is_suspended", default=False)
    percent10 = models.BooleanField("percent10", default=False)

    class Meta:
        db_table = 'contracts'

    def __str__(self):
        return f"{self.number} - {self.name}"

    @property
    def end_date(self):
        if self.date_start_actual and self.duration:
            return self.date_start_actual + timedelta(days=self.duration)
        return None

    @property
    def percent10_amount(self):
        return self.amount * 0.10

    @property
    def total_amount(self):
        if self.percent10:
            return self.amount + self.percent10_amount
        return self.amount
    
    @property
    def total_suspension_days(self):
        total_days = 0
        for period in self.suspension_periods.all():
            start = period.from_date
            end = period.to_date or date.today()
            total_days += (end - start).days
        return total_days
