from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone_number=models.CharField(max_length=12)
    password=models.CharField(max_length=50)
    user_type=(
        ("1", "customer"),
        ("2", "provider"),)

class Token(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    token=models.CharField(max_length=200)


class UserCard(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_card=models.CharField(max_length=200)
    last_four_digit=models.CharField(max_length=10)
    expiry_date=models.DateField()


class UserBankAccount(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_bank_account=models.CharField(max_length=50)
    account_name=models.CharField(max_length=50)
    account_number=models.CharField(max_length=50)
