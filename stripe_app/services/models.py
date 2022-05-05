from django.db import models
from stripe_app.account.models import User

class Service(models.Model):
    name=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)

class ProviderService(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)

class CustomerService(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    amount=models.CharField(max_length=50)
