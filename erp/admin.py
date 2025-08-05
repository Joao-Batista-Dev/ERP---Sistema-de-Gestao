from django.contrib import admin
from erp.models import Client, Product, Order, Invoice


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'document', 'person_type', 'address', 'created_at',]
    search_fields = ['id', 'name', 'email', 'document', 'person_type', 'address',]
    list_display_links = ['id', 'name', 'email',]
    list_filter = ['id', 'name', 'email',]
    ordering = '-id',


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'stocker_quatity', 'created_at',]
    search_fields = ['id', 'name',]
    list_display_links = ['id', 'name',]
    list_filter = ['id', 'name',]
    ordering = '-id',


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'product', 'created_at', 'payment_method', 'status',]
    search_fields = ['id', 'client', 'product',]
    list_display_links = ['id', 'client', 'product',]
    list_filter = ['id', 'client', 'product',]
    ordering = '-id',


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'number', 'issue_data', 'due_data', 'sent',]
    search_fields = ['id', 'order', 'number', 'issue_data', 'due_data', 'sent',]
    list_display_links = ['order', 'number',]
    list_filter = ['id', 'order', 'number', 'issue_data', 'due_data', 'sent',]
    list_editable = ['sent',]
    ordering = '-id',