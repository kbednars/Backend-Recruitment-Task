from django import forms
from grades.models import Task, Grade
from account.models import Profile


class GradingForm(forms.ModelForm):
    task = forms.ModelChoiceField(required=True, queryset=Task.objects.all())
    candidate = forms.ModelChoiceField(required=True, queryset=Profile.objects.filter(is_recruiter=False))
    grade = forms.IntegerField(required=True, min_value=0, max_value=5)

    class Meta:
        model = Grade
        fields = ('task', 'candidate', 'grade')
