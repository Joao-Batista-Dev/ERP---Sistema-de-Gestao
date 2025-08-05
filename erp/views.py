from rest_framework.viewsets import ModelViewSet
from erp.models import Client, Product, Order, Invoice
from erp.serializers import ClientSerializer, ProductSerializer, OrderSerializer, InvoiceSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from erp.filters import ClientFilter, ProductFilter, OrderFilters, InvoiceFilter
from erp.tasks import send_order_email_task


class ClientApiV1Views(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = ClientFilter


class ProductApiV1Views(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = ProductFilter


class OrderApiV1View(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = OrderFilters

    def perform_create(self, serializer):
        order = serializer.save()

        send_order_email_task.delay(
            order.client.name,
            order.client.email,
            order.product.name,
            order.created_at.strftime('%d/%m/%Y %H:%M'),
            order.get_payment_method_display(),
            order.get_status_display(),
        )


class InvoiceApiV1View(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = InvoiceFilter