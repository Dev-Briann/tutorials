from django.db import models

class SalesRecords(models.Model):
    month = models.IntegerField()
    sales = models.DecimalField(max_digits=5, decimal_places=1)
    expenses = models.DecimalField(max_digits=5, decimal_places=1)