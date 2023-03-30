from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Package(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OnlinePayment(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Net(models.Model):
    # relations
    name = models.CharField(max_length=50)
    # fields

    def __str__(self):
        return self.name


class AccountManager(models.Model):
    # relations
    name = models.CharField(max_length=50)
    # fields

    def __str__(self):
        return self.name


class SpecialOffer(models.Model):
    # relations
    name = models.CharField(max_length=50)
    # fields

    def __str__(self):
        return self.name


class Customer(models.Model):
    # relations
    full_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    package = models.ForeignKey(Package, on_delete=models.DO_NOTHING)

    account_number = models.CharField(
        max_length=50, null=True, blank=True, default=None
    )
    provider = models.ForeignKey(
        Provider, on_delete=models.DO_NOTHING, null=True, blank=True, default=None
    )

    online_payment = models.ForeignKey(
        OnlinePayment, on_delete=models.DO_NOTHING, null=True, blank=True, default=None
    )

    mazaya_annual = models.BooleanField(default=False)
    mazaya_annual_start_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True, default=None
    )
    mazaya_annual_end_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True, default=None
    )
    account_manager = models.ForeignKey(
        AccountManager, on_delete=models.DO_NOTHING, null=True, blank=True, default=None
    )
    new_account_number = models.CharField(
        max_length=50, null=True, blank=True, default=None
    )
    actual_bill = models.CharField(max_length=50, null=True, blank=True, default=None)
    total_bill = models.CharField(max_length=50, null=True, blank=True, default=None)
    commission = models.CharField(max_length=50, null=True, blank=True, default=None)
    net = models.ForeignKey(
        Net, on_delete=models.DO_NOTHING, null=True, blank=True, default=None
    )
    rch = models.BooleanField(default=False)
    device_installments = models.BooleanField(default=False)
    installments_start_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True, default=None
    )
    installments_end_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True, default=None
    )
    device_type = models.CharField(max_length=50, null=True, blank=True, default=None)
    installments_phone_number = models.CharField(
        max_length=50, null=True, blank=True, default=None
    )
    suspended = models.BooleanField(default=False)
    activation_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True, default=None
    )
    no_ntra = models.BooleanField(default=False)
    ntra_details = models.CharField(max_length=50, null=True, blank=True, default=None)
    is_notes = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True, default=None)

    special_offer = models.ForeignKey(
        SpecialOffer, on_delete=models.DO_NOTHING, null=True, blank=True, default=None
    )
    lines_to_same_user = models.IntegerField()
    mr_to_account = models.BooleanField(default=False)
    mr_to_corporate = models.BooleanField(default=False)
    new_line = models.BooleanField(default=False)
    pause = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
