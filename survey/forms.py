# survey/forms.py

from django import forms
from .models import SurveyResponse, Interest

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['age', 'gender', 'looking_for', 'interests']
        widgets = {
            'gender': forms.RadioSelect(),
            'looking_for': forms.RadioSelect(),
            'interests': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        self.fields['interests'].queryset = Interest.objects.all()
