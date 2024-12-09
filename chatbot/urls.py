from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),  # HTTP URL for the chatbot page
]
