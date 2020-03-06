from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Exam(models.Model):
    name = models.CharField(max_length=150)
    total_points = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    duration = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='+')
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='+')
    text = models.CharField(max_length=100, blank=True, null=True)
    is_answer = models.BooleanField(default=False)
    points = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.question} {self.text}"


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='+')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')


class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='+')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    points = models.IntegerField(blank=True, null=True)
