from django.db import models

class Estimate(models.Model):
    estimate_date = models.DateField(auto_now_add= True)
    start_date = models.DateField()
    price =models.DecimalField(decimal_places=2, max_digits=10)
    approved = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    work_order = models.ForeignKey('WorkOrder', related_name="estimates", on_delete=models.CASCADE)  
    # need to snake case and take off id and add related names and cascade delete
# going to access workorder and invoice on estimateSerializer  
    