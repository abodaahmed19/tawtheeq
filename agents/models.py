from django.db import models

class Agent(models.Model):
    name = models.CharField("name", max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name
