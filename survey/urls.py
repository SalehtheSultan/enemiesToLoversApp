# survey/urls.py

from django.urls import path
from . import views

app_name = 'survey'

urlpatterns = [
    # Take Survey
    path('take/', views.survey_take, name='survey_take'),
    
    # Edit Survey Responses
    path('edit/', views.survey_edit, name='survey_edit'),
    
    # Survey Completion
    path('complete/', views.survey_complete, name='survey_complete'),
]
