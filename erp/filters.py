import django_filters
from erp.models import Client, Product, Order, Invoice

class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'document',]


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['name',]


class OrderFilters(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = ['client', 'product',]


class InvoiceFilter(django_filters.FilterSet):
    class Meta:
        model = Invoice
        fields = ['order', 'number',]
