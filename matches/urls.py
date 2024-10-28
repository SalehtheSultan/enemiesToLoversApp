# matches/urls.py

from django.urls import path
from . import views

app_name = 'matches'

urlpatterns = [
    # Matches Page with Countdown
    path('', views.matches_view, name='matches_view'),
    
    # Countdown Page
    path('countdown/', views.countdown_view, name='countdown'),
    

]

