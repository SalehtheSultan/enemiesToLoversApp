# survey/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SurveyForm
from .models import SurveyResponse

@login_required
def survey_take(request):
    try:
        response = SurveyResponse.objects.get(user=request.user)
        return redirect('survey:survey_edit')
    except SurveyResponse.DoesNotExist:
        if request.method == 'POST':
            form = SurveyForm(request.POST)
            if form.is_valid():
                survey = form.save(commit=False)
                survey.user = request.user
                survey.save()
                return redirect('survey:survey_complete')
        else:
            form = SurveyForm()
        return render(request, 'survey/survey.html', {'form': form})

@login_required
def survey_edit(request):
    response = SurveyResponse.objects.get(user=request.user)
    if request.method == 'POST':
        form = SurveyForm(request.POST, instance=response)
        if form.is_valid():
            form.save()
            return redirect('survey:survey_complete')
    else:
        form = SurveyForm(instance=response)
    return render(request, 'survey/survey_edit.html', {'form': form})

@login_required
def survey_complete(request):
    return render(request, 'survey/survey_complete.html')
