from .models import Profile
from django import forms
from django.contrib.auth import authenticate, login as auth_login

from django.shortcuts import redirect, render

from .forms import UserForm

# Create your views here.
def signup(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()


            role = request.POST.get('role')
            Profile.objects.create(user = user,role = form.cleaned_data['role'])
            return redirect('signin')
    return render(request,'signup.html',{'form':form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            auth_login(request,user)
            return redirect('question_home')
        
    else:
        form = UserForm()

    return render(request,'signin.html')


def question_home(request):

    return render(request,'students/question_home.html')


def instruction(request):

    return render(request,'students/instruction.html')

def questions(request):

    return render(request,'students/questions.html')
