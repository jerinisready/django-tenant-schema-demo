from django.urls import reverse_lazy

INTERNAL_IPS = [
    '127.0.0.1',
    '192.168.1.100',
]


LOGIN_URL = reverse_lazy('home:index')

