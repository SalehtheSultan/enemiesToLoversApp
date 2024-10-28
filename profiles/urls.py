# profiles/urls.py

from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    # View and Edit Profile
    path('view/', views.profile_view, name='profile_view'),
    path('edit/', views.profile_edit, name='profile_edit'),

]
