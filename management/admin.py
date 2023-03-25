from django.contrib import admin
from . import models


from import_export.admin import ImportExportMixin


# Register your models here.
@admin.register(models.Customer)
class ProfileAdmin(ImportExportMixin, admin.ModelAdmin):
    """Admin View for Profile"""

    list_display = (
        "mobile_number",
        "full_name",
        "package",
        "account_number",
        "is_notes",
    )
    search_fields = (
        "account_manager__name",
        "online_payment__name",
        "net__name",
    )
    list_filter = (
        "no_ntra",
        "rch",
        "suspended",
        "mr_to_account",
        "mr_to_corporate",
        "mazaya_annual",
        "device_installments",
        "new_line",
        "pause",
    )
    fields = [
        ("full_name", "online_payment"),
        ("mobile_number", "actual_bill"),
        ("package", "total_bill"),
        ("account_number", "commission"),
        ("provider", "activation_date"),
        ("account_manager", "special_offer"),
        ("net", "rch"),
        ("no_ntra", "suspended"),
        ("ntra_details", "lines_to_same_user"),
        ("mr_to_account", "new_account_number"),
        ("mr_to_corporate", "pause", "new_line"),
        ("mazaya_annual"),
        ("mazaya_annual_start_date", "mazaya_annual_end_date"),
        ("device_installments"),
        ("installments_start_date", "installments_end_date"),
        ("installments_phone_number", "device_type"),
        ("is_notes",),
        ("notes",),
    ]


@admin.register(models.Package)
class PackageAdmin(ImportExportMixin, admin.ModelAdmin):
    """Admin View for Package"""


@admin.register(models.Provider)
class ProviderAdmin(ImportExportMixin, admin.ModelAdmin):
    """Admin View for Provider"""


@admin.register(models.OnlinePayment)
class OnlinePaymentAdmin(ImportExportMixin, admin.ModelAdmin):
    """Admin View for OnlinePayment"""


@admin.register(models.Net)
class NetAdmin(ImportExportMixin, admin.ModelAdmin):
    """Admin View for Net"""


@admin.register(models.AccountManager)
class AccountManagerAdmin(ImportExportMixin, admin.ModelAdmin):
    """Admin View for AccountManager"""


@admin.register(models.SpecialOffer)
class SpecialOfferAdmin(ImportExportMixin, admin.ModelAdmin):
    """Admin View for SpecialOffer"""
