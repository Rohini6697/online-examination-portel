from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('question_home/',views.question_home,name='question_home'),
    path('instruction/',views.instruction,name='instruction'),
    path('questions/',views.questions,name='questions'),

]
