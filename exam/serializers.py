from rest_framework import serializers
from .models import *


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'
