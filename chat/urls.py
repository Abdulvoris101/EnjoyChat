from unicodedata import name
from django.urls import path
from .views import chat_list, chat_main, chat_image

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('<slug:slug>/', chat_main, name='chat_main'),
    path('img/image_upload/', chat_image, name="chat_image")
    
]
