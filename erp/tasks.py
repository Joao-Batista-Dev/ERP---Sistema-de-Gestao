from celery import shared_task
import time

@shared_task
def send_order_email_task(name, email, product, created_at, payment_method, status):
    time.sleep(3)
    print(f"""
    Pedido de {name} ({email})
    Produto: {product}
    Data: {created_at}
    Pagamento: {payment_method}
    Status: {status}
    """)
