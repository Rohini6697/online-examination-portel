from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('question_home/',views.question_home,name='question_home'),
    path('instruction/',views.instruction,name='instruction'),
    path('questions/',views.questions,name='questions'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('add_questions/',views.add_questions,name='add_questions'),
    path('candidate_score/',views.candidate_score,name='candidate_score'),
    path('view_questions/',views.view_questions,name='view_questions'),
]
