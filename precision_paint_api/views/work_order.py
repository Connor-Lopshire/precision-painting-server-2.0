from precision_paint_api.models.work_order import WorkOrder
from precision_paint_api.serializers.work_order import WorkOrderSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet



class WorkOrderView(ViewSet):
    def list(self, request):
        """ handle get all work_orders.accepted = false 
        """
        # need  
        user=request.auth.user
        if user.is_staff == True: 
            work_orders = WorkOrder.objects.filter(accepted=False)
        else: 
            work_orders = WorkOrder.objects.filter(accepted=False, user=user )
        search_term = request.query_params.get('search_term', None)
        if search_term is not None :
            work_orders = work_orders.filter(address__contains = search_term)
        serializer = WorkOrderSerializer(work_orders, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        work_order = WorkOrder.objects.get(pk=pk)
        serializer = WorkOrderSerializer(work_order)
        return Response(serializer.data)
    def update(self, request, pk):
        """
        put to change accepted = false
        """
        work_order = WorkOrder.objects.get(pk=pk)
        work_order.accepted = request.data["accepted"]
        work_order.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def create(self, request):
        """HANDLE POST NEW WorkOrder"""
        user = request.auth.user
        work_order = WorkOrder.objects.create(
        address = request.data['address'],  
        description = request.data['description'],
        user =  user
        )
        serializer = WorkOrderSerializer(work_order)
        return Response(serializer.data)