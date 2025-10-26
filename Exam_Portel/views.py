from .models import Profile, Questions, Result
from django import forms
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import UserForm

# Create your views here.
def signup(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()


            # role = request.POST.get('role')
            Profile.objects.create(user = user,fullname=form.cleaned_data.get('fullname') ,role='user')
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

    request.session['score'] = 0

    return render(request,'students/instruction.html')

def questions(request,q_no=1):
    total = Questions.objects.count() 

    if q_no > total:
        score = request.session.get('score', 0)
        percentage = (score/total)*100
        student_profile = Profile.objects.get(user=request.user)

        Result.objects.create(
            student = request.user,
            score = score,
            total_questions = total,
            percentage = percentage
        )
        request.session['score'] = 0

        return redirect('result')  
    question = get_object_or_404(Questions,id=q_no)
    if request.method == 'POST':
        selected_option = request.POST.get('answer')
        score = request.session.get('score', 0)

        if selected_option == question.correct_answer:
            score +=1
        request.session['score'] = score
        return redirect('questions', q_no=q_no + 1)


    return render(request, 'students/questions.html', {'question': question, 'current': q_no, 'total': total})


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
    result = Result.objects.all().order_by('-attempt_date')
    # profile = Profile.objects.all()
    # user = request.user

    return render(request,'admin/candidate_score.html',{'result':result})

def view_questions(request):
    questions = Questions.objects.all()

    return render(request,'admin/view_questions.html',{'questions':questions})


def result(request):
    result = Result.objects.filter(student=request.user).order_by('-attempt_date').first()
    return render(request, 'students/result.html', {'result': result})

def view_result(request):
    result = Result.objects.filter(student=request.user).order_by('-attempt_date').first()
    return render(request,'students/view_result.html', {'result': result})


def question_delete(request,id):
    delete_candidate = Questions.objects.get(id=id)
    delete_candidate.delete()
    return redirect('view_questions')


def question_update(request, id):
    question = get_object_or_404(Questions, id=id)

    if request.method == 'POST':
        question.question_text = request.POST.get('question_text')
        question.option1 = request.POST.get('option1')
        question.option2 = request.POST.get('option2')
        question.option3 = request.POST.get('option3')
        question.option4 = request.POST.get('option4')
        question.correct_answer = request.POST.get('correct_answer')
        question.save()

        return redirect('view_questions')  

    return render(request, 'admin/question_update.html', {'question': question})
