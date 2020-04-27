from django.shortcuts import render
from django.urls import reverse_lazy

from apps.customer.models import Client
from django.views.generic import ListView, CreateView


class ClientList(ListView):
    queryset = Client.objects.exclude(schema_name='public')


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client-list')




