from django.urls import path
from .views import register, UserLoginView, log_out

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout')
]
