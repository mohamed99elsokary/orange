from django.contrib import admin
from . import models

from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(models.Customer)
class ProfileAdmin(ModelAdmin, ImportExportModelAdmin):
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
class PackageAdmin(ModelAdmin, ImportExportModelAdmin):
    """Admin View for Package"""


@admin.register(models.Provider)
class ProviderAdmin(ModelAdmin, ImportExportModelAdmin):
    """Admin View for Provider"""


@admin.register(models.Payon)
class PayonAdmin(ModelAdmin, ImportExportModelAdmin):
    """Admin View for Payon"""


@admin.register(models.OnlinePayment)
class OnlinePaymentAdmin(ModelAdmin, ImportExportModelAdmin):
    """Admin View for OnlinePayment"""


@admin.register(models.Net)
class NetAdmin(ModelAdmin, ImportExportModelAdmin):
    """Admin View for Net"""
