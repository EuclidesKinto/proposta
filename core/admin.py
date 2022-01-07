from django import forms
from django.contrib import admin
from .models import Customer, Proposal
from django.utils.html import format_html
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Avg


class ProposalAdmin(admin.ModelAdmin):
    list_display = ["customer", "date", "paid", "value"]
    search_fields = ["customer__name"]
    list_per_page = 30
    save_on_top = True


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Customer, CustomerAdmin)
