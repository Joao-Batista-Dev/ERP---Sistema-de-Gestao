from rest_framework.viewsets import ModelViewSet
from erp.models import Client, Product, Order, Invoice
from erp.serializers import ClientSerializer, ProductSerializer, OrderSerializer, InvoiceSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class ClientApiV1Views(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated,]
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['name', 'email', 'phone', 'document',]


class ProductApiV1Views(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,]


class OrderApiV1View(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]


class InvoiceApiV1View(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated,]