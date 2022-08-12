from rest_framework import serializers, status

from precision_paint_api.models.work_order import WorkOrder

class WorkOrderSerializer(serializers.ModelSerializer):
    """JSON serializer for work_orders
    """
    class Meta:
        model = WorkOrder
        fields = ('id', 'address', 'description', 'date', 'accepted' )
