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


class Payon(models.Model):
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


class Customer(models.Model):
    # relations
    full_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    pay_on = models.ForeignKey(Payon, on_delete=models.CASCADE)
    online_payment = models.ForeignKey(OnlinePayment, on_delete=models.CASCADE)
    mazaya_annual = models.BooleanField()
    mazaya_annual_start_date = models.DateField(auto_now=False, auto_now_add=False)
    mazaya_annual_end_date = models.DateField(auto_now=False, auto_now_add=False)
    account_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    mr = models.BooleanField()
    new_account_number = models.CharField(max_length=50)
    actual_bill = models.CharField(max_length=50)
    total_bill = models.CharField(max_length=50)
    commission = models.CharField(max_length=50)
    net = models.ForeignKey(Net, on_delete=models.CASCADE)
    rch = models.BooleanField()
    rch = models.BooleanField()
    device_installments = models.BooleanField()
    installments_start_date = models.DateField(auto_now=False, auto_now_add=False)
    installments_end_date = models.DateField(auto_now=False, auto_now_add=False)
    device_type = models.CharField(max_length=50)
    installments_phone_number = models.CharField(max_length=50)
    pause = models.BooleanField()
    suspended = models.BooleanField()
    ntra = models.CharField(max_length=50)
    is_notes = models.BooleanField()
    notes = models.TextField()

    def __str__(self):
        return self.full_name
