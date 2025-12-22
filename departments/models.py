from django.db import models
from agents.models import Agent

class Department(models.Model):
    name = models.CharField("name", max_length=255, null=False, blank=False)
    agent = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE,
        related_name='departments'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE, 
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name
