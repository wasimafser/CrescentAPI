from django.shortcuts import render, redirect
from django.views import View
from django.forms import inlineformset_factory

from .models import *
from .forms import *

# Create your views here.


class ExamListView(View):
    template_name = 'exam/exam_list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ExamSetupView(View):
    template_name = 'exam/exam_setup.html'
    active_exams = Exam.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        questionform = QuestionForm(request.GET or None)
        answerformset = AnswerFormSet(queryset=Answer.objects.none())
        return render(request, self.template_name, {'questionform': questionform, 'answerformset': answerformset, 'active_exams': self.active_exams})

    def post(self, request, *args, **kwargs):
        questionform = QuestionForm(request.POST)
        answerformset = AnswerFormSet(request.POST)
        print(questionform.is_valid(), answerformset.is_valid())
        if questionform.is_valid() and answerformset.is_valid():
            question = questionform.save()
            for form in answerformset:
                answer = form.save(commit=False)
                answer.question = question
                answer.save()
            return redirect('exam_setup')
        return render(request, self.template_name, {'questionform': questionform, 'answerformset': answerformset, 'active_exams': self.active_exams})


class QuizView(View):
    template_name = 'exam/quiz_form.html'
    active_exams = Exam.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        questionform = QuestionForm(request.GET or None)
        answerformset = AnswerFormSet(queryset=Answer.objects.none())
        return render(request, self.template_name,
                      {'questionform': questionform, 'answerformset': answerformset, 'active_exams': self.active_exams})

    def post(self, request, *args, **kwargs):
        questionform = QuestionForm(request.POST)
        answerformset = AnswerFormSet(request.POST)
        if questionform.is_valid() and answerformset.is_valid():
            question = questionform.save()
            for form in answerformset:
                answer = form.save(commit=False)
                answer.question = question
                answer.save()
            return redirect('exam_setup')
        return render(request, self.template_name,
                      {'questionform': questionform, 'answerformset': answerformset, 'active_exams': self.active_exams})


class ExamView(View):
    template_name = 'exam/quiz.html'

    def get(self, request, *args, **kwargs):
        exams = Exam.objects.all()
        context = {
            'exams': exams
        }
        return render(request, self.template_name, context)
