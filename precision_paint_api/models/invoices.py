from django.db import models

class Invoice(models.Model):
    date_completed = models.DateField(auto_now_add= True)
    amount_owed = models.DecimalField(decimal_places=2, max_digits=10)
    completed = models.BooleanField(default=False)
    work_order = models.ForeignKey('WorkOrder', related_name="invoice", on_delete=models.CASCADE)
    estimate = models.ForeignKey('Estimate', related_name="invoice", on_delete=models.CASCADE)
