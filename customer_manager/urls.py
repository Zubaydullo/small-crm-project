"""customer_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.models import Customer
from rest_framework import generics
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path("api/v1/customers", CustomerView.as_view(), name="customer-list")
]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
