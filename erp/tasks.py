from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_email_task(client_name, client_email, product_name, created_at, payment_method, status):
    subject = 'Confirmação de Pedido'
    message = (
        f"Prezado(a) {client_name},\n\n"
        f"Seu pedido foi registrado com sucesso!\n\n"
        f"Produto: {product_name}\n"
        f"Data: {created_at}\n"
        f"Método de Pagamento: {payment_method}\n"
        f"Status: {status}\n\n"
        f"Obrigado por comprar conosco!"
    )
    send_mail(
        subject,
        message,
        None,  # ou settings.DEFAULT_FROM_EMAIL
        [client_email],
        fail_silently=False,
    )
