from django.db import models

class Planets(models.Model):
    name = models.CharField(max_length=100)
    population = models.BigIntegerField(null=True, blank=True)
    terrains = models.TextField(null=True, blank=True)   
    climates = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
