from django.contrib import admin
from erp.models import Client, Product, Sale, SaleItem, Invoice, Payment


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'document', 'person_type', 'address', 'created_at',]
    search_fields = ['id', 'name', 'email', 'document', 'person_type', 'address',]
    list_filter = ['id', 'name', 'email',]
    ordering = '-id',


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'stocker_quatity', 'created_at',]
    search_fields = ['id', 'name',]
    list_filter = ['id', 'name',]
    ordering = '-id',


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'created_at', 'total_amount', 'payment_method', 'status',]
    search_fields = ['id', 'client',]
    list_filter = ['id', 'client',]
    ordering = '-id',


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'sale', 'product', 'quantity', 'unit_price',]
    search_fields = ['id', 'sale', 'product',]
    list_filter = ['id', 'sale', 'product',]
    ordering = '-id',


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'sale', 'number', 'issue_data', 'due_data', 'amount', 'sent',]
    search_fields = ['id', 'sale', 'issue_data', 'due_data', 'sent',]
    list_filter = ['id', 'sale', 'issue_data', 'due_data', 'sent',]
    ordering = '-id',


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice', 'payment_data', 'amount', 'method_payment', 'confirmed',]
    search_fields = ['id', 'invoice', 'payment_data', 'method_payment', 'confirmed',]
    list_filter = ['id', 'invoice', 'payment_data', 'method_payment', 'confirmed',]
    ordering = '-id',







