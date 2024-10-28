# matches/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def matches_view(request):
    # Calculate time remaining until November 18, 2024
    target_date = datetime(2024, 11, 18)
    now = datetime.now()
    time_remaining = target_date - now
    days_remaining = time_remaining.days
    return render(request, 'matches/countdown.html', {'days_remaining': days_remaining})

@login_required
def countdown_view(request):
    return render(request, 'matches/countdown.html')
