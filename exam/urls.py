from django.conf.urls import url, include
from . import api, views

urlpatterns = [
    url(r'^exam_list/$', views.ExamListView.as_view(), name='exam_list'),
    url(r'^exam_setup/$', views.ExamSetupView.as_view(), name='exam_setup'),
    url(r'^quiz_list/$', views.QuizView.as_view(), name='quiz_list'),
    url(r'^api/exam_list/$', api.ExamAPI.as_view(), name='exam_api'),
    url(r'^quiz/$', views.ExamView.as_view(), name='quiz'),
    url(r'^api/questions/$', api.QuestionsAPI.as_view(), name='question_api'),
]
