from django.shortcuts import render
from rest_framework import viewsets
from stripe_app.account.serializer import Stripeserializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.db import IntegrityError



class UserViewSet(viewsets.ModelViewSet):
    serializer_class=Stripeserializer

    def get(self,request):
        serializer=self.get_serializer(request.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return Response('similar data',status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    



class login(viewsets.ModelViewSet):
    serializer_class=Stripeserializer

    def post(self,request):
        queryset=User.objects.filter(email=request.data['email'],password=request.data['password']).first()
        if queryset:
            serializer=self.get_serializer(queryset)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response("invalid email and password",status=status.HTTP_400_BAD_REQUEST)
