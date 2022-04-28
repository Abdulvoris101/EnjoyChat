
from unicodedata import name
from django.urls import path
from .views import my_profile_views, follow_or_not, profile_view, all_profiles

urlpatterns = [
    path('', my_profile_views, name="my_profile"),
    path('follow_or_not/', follow_or_not, name='follow_or_not'),
    path('<slug:slug>/', profile_view, name='profile'),
    path('all/list/', all_profiles, name='all_profiles')
]
