from django.urls import path, include
from rest_framework import routers
from erp.views import ClientApiV1Views, ProductApiV1Views, OrderApiV1View, InvoiceApiV1View

router = routers.SimpleRouter()
router.register('client', ClientApiV1Views, basename='client')
router.register('product', ProductApiV1Views, basename='product')
router.register('order', OrderApiV1View, basename='order')
router.register('invoice', InvoiceApiV1View, basename='invoice')

urlpatterns = [
    path('', include(router.urls))
]
