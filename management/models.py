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
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AccountManager(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SpecialOffer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Customer(models.Model):
    # relations
    full_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    account_number = models.CharField(max_length=50)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    online_payment = models.ForeignKey(OnlinePayment, on_delete=models.CASCADE)

    mazaya_annual = models.BooleanField(default=False)
    account_manager = models.ForeignKey(
        AccountManager, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    new_account_number = models.CharField(
        max_length=50, null=True, blank=True, default=None
    )
    actual_bill = models.CharField(max_length=50)
    total_bill = models.CharField(max_length=50)
    commission = models.CharField(max_length=50)
    net = models.ForeignKey(
        Net, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    is_net = models.BooleanField(default=False)
    notional_id = models.CharField(max_length=50, null=True, blank=True, default=None)
    rch = models.BooleanField(default=False)
    device_installments = models.BooleanField(default=False)
    suspended = models.BooleanField(default=False)
    activation_date = models.CharField(
        max_length=50, null=True, blank=True, default=None
    )
    no_ntra = models.BooleanField(default=False)
    ntra_details = models.CharField(max_length=50, null=True, blank=True, default=None)
    is_notes = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True, default=None)
    smart_payment = models.BooleanField(default=False)
    bills_payment = models.TextField(null=True, blank=True, default=None)
    is_important_notes = models.BooleanField(default=False)
    special_offer = models.ForeignKey(
        SpecialOffer, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    lines_to_same_user = models.IntegerField(null=True, blank=True)
    mr_to_account = models.BooleanField(default=False)
    mr_to_corporate = models.BooleanField(default=False)
    new_line = models.BooleanField(default=False)
    pause = models.BooleanField(default=False)
    registration_date = models.CharField(
        max_length=50, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.full_name
