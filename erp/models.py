from django.db import models


class Client(models.Model):
    PERSON_TYPE_CHOICES =[
        ('F', 'Pessoa Física'),
        ('J', 'Pessoa Jurídica'),
    ]

    name = models.CharField(max_length=255, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="E-mail")
    phone = models.CharField(max_length=20, verbose_name="Telefone")
    document = models.CharField(max_length=20, unique=True, verbose_name="Documento")
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


class Sale(models.Model):
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

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Cleinte")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criando em")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Total")
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICE, verbose_name="Método de Pagamento")
    status = models.CharField(max_length=20, choices=STATUS_PAYMENT, default='Pendente', verbose_name="Status de Pagamento")

    class Meta:
        verbose_name = "Oferta"
        verbose_name_plural = "Ofertas"

    def __str__(self):
        return f"Venda: {self.id} - {self.client.name}"
    

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name="Venda")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    quantity = models.PositiveIntegerField(verbose_name="Quantidade")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    

class Invoice(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name="Venda")
    number = models.CharField(max_length=20, unique=True, verbose_name="Número")
    issue_data = models.DateField(auto_now_add=True, verbose_name="Data de emissão")
    due_data = models.DateField(verbose_name="Data de vencimento")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    sent = models.BooleanField(default=False, verbose_name="Enviado")

    class Meta:
        verbose_name = "Fatura"
        verbose_name_plural = "Faturas"

    def __str__(self):
        return f"Fatura: {self.number}"
    

class Payment(models.Model):
    PAYMENT_METHOD_CHOICE = [
        ('cash', 'Dinheiro'),
        ('credit_card', 'Cartão de Crédito'),
        ('boleto', 'Boleto'),
        ('pix', 'Pix'),
    ]

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, verbose_name="Fatura")
    payment_data = models.DateField(verbose_name="Data de Pagamento")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    method_payment = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICE, verbose_name="Método de Pagamento")
    confirmed = models.BooleanField(default=False, verbose_name="Confirmado")

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def __str__(self):
        return f"Pagamento de {self.amount} em {self.payment_data}"



