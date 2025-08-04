from django.db import models


class Client(models.Model):
    PERSON_TYPE_CHOICES =[
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    ]

    name = models.CharField(max_length=255, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    phone = models.CharField(max_length=20, verbose_name="Telefone")
    document = models.CharField(max_length=20, unique=True, verbose_name="CPF ou CNPJ ")
    person_type = models.CharField(max_length=1, choices=PERSON_TYPE_CHOICES, verbose_name="Tipo de Documento")
    address = models.TextField(blank=True, verbose_name="Endereço")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criando em")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    description = models.TextField(blank=True, verbose_name="Descrição")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    stocker_quatity = models.PositiveIntegerField(verbose_name="Quantidade")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criando em")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name


class Order(models.Model):
    PAYMENT_METHOD_CHOICE = [
        ('cash', 'Dinheiro'),
        ('credit_card', 'Cartão de Crédito'),
        ('boleto', 'Boleto'),
        ('pix', 'Pix'),
    ]

    STATUS_PAYMENT = [
        ('pending', 'Pendente'),
        ('paid', 'Pago'),
        ('canceled', 'Cancelado'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cliente")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criando em")
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICE, verbose_name="Método de Pagamento")
    status = models.CharField(max_length=20, choices=STATUS_PAYMENT, default='Pendente', verbose_name="Status de Pagamento")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"Pedido: {self.id} - {self.client.name} - {self.product.name}"

class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Pedido")
    number = models.CharField(max_length=5, unique=True, verbose_name="Número")
    issue_data = models.DateField(auto_now_add=True, verbose_name="Data de emissão")
    due_data = models.DateField(verbose_name="Data de vencimento")
    sent = models.BooleanField(default=False, verbose_name="Enviado")

    class Meta:
        verbose_name = "Fatura"
        verbose_name_plural = "Faturas"

    def __str__(self):
        return f"Fatura: {self.number}"
    