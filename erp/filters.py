import django_filters
from erp.models import Client, Product, Order, Invoice

class ClientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')
    document = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'document',]


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name',]


class OrderFilters(django_filters.FilterSet):
    client = django_filters.CharFilter(lookup_expr='icontains')
    product = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['client', 'product',]


class InvoiceFilter(django_filters.FilterSet):
    order = django_filters.CharFilter(lookup_expr='icontains')
    number = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Invoice
        fields = ['order', 'number',]
