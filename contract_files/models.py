from django.db import models

class ContractFile(models.Model):
    name = models.CharField("name", max_length=255, null=True, blank=True)
    path = models.TextField("path")
    status = models.CharField(
        max_length=20,
        choices= [
            ('under_review', 'Under Review'),
            ('unacceptable', 'Unacceptable'),
            ('certified', 'Certified'),
        ]
    )

    class Meta:
        db_table = 'contract_files'

    def __str__(self):
        return self.name
