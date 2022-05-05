from pyexpat import model
from rest_framework import serializers
from stripe_app.account.models import User

class Stripeserializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['first_name','last_name','email','phone_number','password']
