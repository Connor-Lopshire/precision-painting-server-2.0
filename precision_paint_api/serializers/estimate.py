from rest_framework import serializers, status
from precision_paint_api.models.estimates import Estimate

from precision_paint_api.models.work_order import WorkOrder
from precision_paint_api.serializers.invoice import InvoiceSerializer
from precision_paint_api.serializers.work_order import WorkOrderSerializer

class EstimateSerializer(serializers.ModelSerializer):
    """JSON serializer for work_orders
    """
    work_order = WorkOrderSerializer()
    class Meta:
        model = Estimate
        fields = ('id', 'estimate_date', 'start_date', 'price', 'approved', 'completed', 'work_order')
    
