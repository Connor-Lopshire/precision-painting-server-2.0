from rest_framework import serializers, status
from precision_paint_api.models.estimates import Estimate
from precision_paint_api.models.invoices import Invoice

from precision_paint_api.models.work_order import WorkOrder
from precision_paint_api.serializers.work_order import WorkOrderSerializer

class InvoiceSerializer(serializers.ModelSerializer):
    """JSON serializer for work_orders
    """
    work_order = WorkOrderSerializer()
    class Meta:
        model = Invoice
        fields = ('id', 'date_completed', 'amount_owed',  'completed', 'work_order')
    
