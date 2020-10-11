from .models import Grade
from account.models import Profile
from rest_framework import generics
from .forms import GradingForm
from django.views.generic import TemplateView
from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse


class CadidatesView(View):
    def get(self, request):
        data = []
        candidatesProfiles = Profile.objects.filter(is_recruiter=False)
        for candidate in candidatesProfiles:
            grades = Grade.objects.filter(candidate=candidate)
            gradeList = []
            for grade in grades:
                gradeList += [grade.grade]
            data += [{
                'pk': candidate.pk,
                'full_name': candidate.user.first_name + " " + candidate.user.last_name,
                'avg_grade': 0.0 if len(gradeList)==0 else sum(gradeList)/len(gradeList),
                'grades': gradeList
            }]
        return JsonResponse({'data': data}, safe=False)


class GradingView(TemplateView):
    template_name = 'grade.html'

    def get(self, request):
        return render(request, self.template_name, {'form': GradingForm})

    def post(self, request):
        form = GradingForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            if not Grade.objects.filter(candidate=grade.candidate, task=grade.task).exists():
                grade.recruiter = Profile.objects.filter(user=request.user).first()
                grade.save()
                return render(request, self.template_name, {'form': GradingForm})
            else:
                messages.info(request, 'This task has been already graded for this candidate.')
                return render(request, self.template_name, {'form': form})
