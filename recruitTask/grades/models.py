from django.db import models
from account.models import Profile


class Task(models.Model):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.title


class Grade(models.Model):
    grade = models.IntegerField(default=0)
    task = models.ForeignKey(Task, related_name='Task', on_delete=models.CASCADE)
    candidate = models.ForeignKey(Profile, related_name='Candidate', on_delete=models.CASCADE)
    recruiter = models.ForeignKey(Profile, related_name='Recruiter', on_delete=models.SET_NULL, null=True)
