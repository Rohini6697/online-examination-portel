from .models import Profile, Questions
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
           
            if user.is_superuser:
                      return redirect('admin_dashboard')
            else:
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

def admin_dashboard(request):

    return render(request,'admin/admin_dashboard.html')




def add_questions(request):
    message =''
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correct_answer = request.POST.get('correct_answer')

        # Questions.objects.create(question_text=question_text,option1=option1,option2=option2,option3=option3,option4=option4,correct_answer=correct_answer)
        if question_text and option1 and option2 and option3 and option4 and correct_answer:
            Questions.objects.create(question_text=question_text,option1=option1,option2=option2,option3=option3,option4=option4,correct_answer=correct_answer)
            message = 'Question added successfully!'
        else: 
            message = 'Please fill in all fields.'
    return render(request,'admin/add_questions.html',{'message':message})


def candidate_score(request):

    return render(request,'admin/candidate_score.html')

def view_questions(request):
    questions = Questions.objects.all()

    return render(request,'admin/view_questions.html',{'questions':questions})


