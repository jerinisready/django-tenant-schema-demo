from django.urls import path

from .views import *

urlpatterns = [
    path('', ClientList.as_view(), name="client-list"),
    path('add-new-news-channel/', ClientCreateView.as_view(), name="client-create-form")
]


