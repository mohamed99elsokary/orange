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
        "full_name",
        "mobile_number",
        "package__name",
        "account_number__exact",
        "provider__name",
        "account_manager__name",
        "online_payment__name",
        "actual_bill",
        "total_bill",
        "commission",
        "net__name",
        "lines_to_same_user",
        "activation_date",
        "user__username",
        "registration_date",
    )
    list_filter = (
        "no_ntra",
        "rch",
        "suspended",
        "mr_to_account",
        "mr_to_corporate",
        "new_line",
        "pause",
        "device_installments",
        "mazaya_annual",
        "is_notes",
        "is_important_notes",
        "is_special",
        "smart_payment",
    )
    fields = [
        ("full_name", "online_payment"),
        ("mobile_number", "actual_bill"),
        ("package", "total_bill"),
        ("account_number", "commission"),
        ("provider", "user"),
        ("account_manager", "activation_date"),
        ("is_special", "special_offer"),
        ("is_net", "net"),
        ("no_ntra", "suspended", "registration_date"),
        ("ntra_details", "lines_to_same_user"),
        ("rch", "notional_id"),
        ("mr_to_account", "new_account_number"),
        ("mr_to_corporate", "new_line", "pause"),
        ("mazaya_annual"),
        ("device_installments"),
        ("smart_payment",),
        ("bills_payment"),
        ("is_notes", "is_important_notes"),
        ("notes"),
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
