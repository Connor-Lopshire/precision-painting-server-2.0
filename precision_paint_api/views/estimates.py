from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from precision_paint_api.models.estimates import Estimate
from precision_paint_api.models.work_order import WorkOrder
from precision_paint_api.serializers.estimate import EstimateSerializer
from rest_framework import serializers, status
from rest_framework.decorators import action

class EstimateView(ViewSet):
    def list(self, request):
        """ handle get all work_orders.accepted = false 
        """
        # need  
        user=request.auth.user
        if user.is_staff == True: 
            estimates = Estimate.objects.filter(approved=True, completed=False)
        else: 
            estimates = Estimate.objects.filter(approved=True, completed=False, work_order__user=user)
        search_term = request.query_params.get('search_term', None)
        if search_term is not None :
            estimates = estimates.filter(address__contains = search_term)
        serializer = EstimateSerializer(estimates, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        estimate = Estimate.objects.get(pk=pk)
        serializer = EstimateSerializer(estimate)
        return Response(serializer.data)
    def update(self, request, pk):
        """
        put to change accepted = false
        """
        estimate = Estimate.objects.get(pk=pk)
        estimate.approved = request.data["approved"]
        estimate.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def create(self, request):
        """HANDLE POST NEW WorkOrder"""
        work_order = WorkOrder.objects.get(pk=request.data["work_order"])
        estimate = Estimate.objects.create(
        start_date = request.data['start_date'],  
        price = request.data['price'],
        work_order = work_order
        )
        serializer = EstimateSerializer(estimate)
        return Response(serializer.data)
    @action(methods=['get'], detail=False)
    def approve_list(self,request):
        user=request.auth.user
        estimates = Estimate.objects.filter(approved=False, completed=False, work_order__user=user)
        search_term = request.query_params.get('search_term', None)
        if search_term is not None :
            estimates = estimates.filter(address__contains = search_term)
        serializer = EstimateSerializer(estimates, many=True)
        return Response(serializer.data)