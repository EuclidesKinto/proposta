from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Sum, Avg
from localflavor.br.br_states import STATE_CHOICES
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList


class Customer(models.Model):
    name = models.CharField("Nome", max_length=150)

    def __str__(self):
        return self.name


class Proposal(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cpf = models.CharField("CPF", max_length=14, blank=True)
    cnpj = models.CharField("CNPJ", max_length=18, blank=True)
    end = models.CharField("Endereço", max_length=200, blank=True)
    district = models.CharField("Bairro", max_length=100, blank=True)
    city = models.CharField("Cidade", max_length=100, blank=True)
    state = models.CharField(null=True, max_length=2, blank=True, choices=STATE_CHOICES)
    date = models.DateField("Data de Emissão")
    VALIDADE_CHOICES = (
        ("Quinze", "15 (Quinze)"),
        ("Trinta", "30 (Trinta)"),
        ("Sessenta", "60 (Sessenta)"),
    )
    validate = models.CharField(
        "Validade", blank=True, max_length=200, choices=VALIDADE_CHOICES
    )
    value = models.DecimalField("Valor a pagar", max_digits=8, decimal_places=2)
    CATEGORY_CHOICES = (
        ("Atrasado", "Atrasado"),
        ("A Vencer", "A Vencer"),
        ("Pago", "Pago"),
    )
    situation = models.CharField("Situação", max_length=200, choices=CATEGORY_CHOICES)
    paid = models.BooleanField("Pago", default=False)

    class Meta:
        verbose_name = "Proposta"
        verbose_name_plural = "Propostas"
