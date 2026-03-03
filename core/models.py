from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class Geladeira(models.Model):
    id_geladeira = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    tipo = models.CharField(max_length=150)
    capacidade = models.PositiveIntegerField()

    dono = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='geladeiras'
    )

    class Meta:
        db_table = 'geladeiras'

    def __str__(self):
        return f"{self.tipo} ({self.dono.username})"


class Tipo(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipos'

    def __str__(self):
        return self.nome


class Item(models.Model):
    geladeira = models.ForeignKey(
        Geladeira,
        on_delete=models.CASCADE,
        related_name='itens'
    )

    nome = models.CharField(max_length=150)

    tipo = models.ForeignKey(
        Tipo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='itens'
    )

    validade = models.DateField(null=True, blank=True)

    botado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'itens'

    def __str__(self):
        return self.nome