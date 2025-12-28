from django.db import models

class Company(models.Model):
    name = models.CharField("name", max_length=255)
    cr_number = models.IntegerField("cr_number", null=True, blank=True)
    cr_expiry = models.DateField("cr_expiry", null=True, blank=True)
    phone = models.CharField("phone", max_length=15, null=True, blank=True)
    mobile = models.CharField("mobile", max_length=15, null=True, blank=True)
    email = models.EmailField("email", max_length=255, null=True, blank=True)
    website = models.CharField("website", max_length=255, null=True, blank=True)
    address = models.TextField("address", null=True, blank=True)
    type = models.CharField(
        max_length=20,
        choices= [
            ('contractor', 'Contractor'),
            ('consultant', 'Consultant'),
        ]
    )

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name
