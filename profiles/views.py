# profiles/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm
from .models import UserProfile

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'profiles/profile_view.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile_view')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'form': form})
