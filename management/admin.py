from django.contrib import admin
from . import models

from unfold.admin import ModelAdmin

# from import_export.admin import


# Register your models here.
@admin.register(models.Customer)
class ProfileAdmin(admin.ModelAdmin):
    """Admin View for Profile"""

    list_display = (
        "mobile_number",
        "full_name",
        "package",
        "account_number",
        "is_notes",
    )
    list_filter = (
        "package",
        "provider",
        "pay_on",
        "online_payment",
        "account_manager",
        "net",
    )


@admin.register(models.Package)
class PackageAdmin(
    admin.ModelAdmin,
):
    """Admin View for Package"""


@admin.register(models.Provider)
class ProviderAdmin(
    admin.ModelAdmin,
):
    """Admin View for Provider"""


@admin.register(models.Payon)
class PayonAdmin(
    admin.ModelAdmin,
):
    """Admin View for Payon"""


@admin.register(models.OnlinePayment)
class OnlinePaymentAdmin(
    admin.ModelAdmin,
):
    """Admin View for OnlinePayment"""


@admin.register(models.Net)
class NetAdmin(
    admin.ModelAdmin,
):
    """Admin View for Net"""


@admin.register(models.AccountManager)
class AccountManagerAdmin(admin.ModelAdmin):
    """Admin View for AccountManager"""
