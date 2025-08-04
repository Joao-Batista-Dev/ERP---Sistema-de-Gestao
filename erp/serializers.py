from rest_framework import serializers
from erp.models import Client, Product, Order, Invoice


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone', 'document', 'person_type', 'address', 'created_at',]


class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stocker_quatity', 'created_at',]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'client', 'product', 'created_at', 'payment_method', 'status',]


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'order', 'number', 'issue_data', 'due_data', 'sent',]
