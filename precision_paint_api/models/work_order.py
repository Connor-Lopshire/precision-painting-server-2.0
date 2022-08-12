from django.db import models
from django.contrib.auth.models import User

class WorkOrder(models.Model):
    address = models.CharField( max_length=110)
    description = models.CharField( max_length=110)
    date = models.DateField(auto_now_add= True)
    accepted = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="work_orders", on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.address