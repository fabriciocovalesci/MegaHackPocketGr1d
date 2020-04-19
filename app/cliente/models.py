from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=50)
    estado_cívil = models.CharField(max_length=200)
    renda_mensal = models.DecimalField(max_digits=5, decimal_places=2)
    qtdade_filhos = models.IntegerField()
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"




