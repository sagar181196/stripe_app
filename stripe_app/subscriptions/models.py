from django.db import models
from stripe_app.account.models import User

class Subscription(models.Model):
    subscription_name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subscription_type=(
        ("1", "monthly"),
        ("2", "quarterly"),
        ("3", "yearly"),
    )
    stripe_product=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)

class ProviderSubscription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subscription=models.ForeignKey(Subscription,on_delete=models.CASCADE)

class CustomerSubscription(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subscription=models.ForeignKey(Subscription,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()