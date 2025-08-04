from rest_framework.viewsets import ModelViewSet
from erp.models import Client, Product, Order, Invoice
from erp.serializers import ClientSerializer, ProductSerializer, OrderSerializer, InvoiceSerializer


class ClientApiV1Views(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductApiV1Views(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderApiV1View(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class InvoiceApiV1View(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer