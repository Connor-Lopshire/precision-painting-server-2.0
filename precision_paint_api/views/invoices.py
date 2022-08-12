from precision_paint_api.models.estimates import Estimate
from precision_paint_api.models.invoices import Invoice
from precision_paint_api.models.work_order import WorkOrder
from precision_paint_api.serializers.invoice import InvoiceSerializer
from precision_paint_api.serializers.work_order import WorkOrderSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet

from precision_paint_api.views import estimates
class InvoiceView(ViewSet):
    def list(self, request):
        """ handle get all work_orders.accepted = false 
        """
        # need  
        user=request.auth.user
        if user.is_staff == True: 
            invoices = Invoice.objects.filter( completed=False)
        else: 
            invoices = Invoice.objects.filter(completed=False, work_order__user=user)
        search_term = request.query_params.get('search_term', None)
        if search_term is not None :
            invoices = invoices.filter(address__contains = search_term)
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        invoice = Invoice.objects.get(pk=pk)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)
    def update(self, request, pk):
        """
        put to change accepted = false
        """
        invoice = Invoice.objects.get(pk=pk)
        invoice.completed = request.data["completed"]
        invoice.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def create(self, request):
        """HANDLE POST NEW WorkOrder"""
        estimate = Estimate.objects.get(pk=request.data["estimate"])

        invoice = Invoice.objects.create(
        amount_owed = request.data['amount_owed'],  
        work_order = estimate.work_order,
        estimate = estimate
        )
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)