from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30,null=True,blank=True)
    ROLL_CHOICES = (
        ('user','User'),
    )

    role = models.CharField(max_length=10,choices=ROLL_CHOICES,default='user')

    def __str__(self):
        return f"{self.fullname}"
    

class Questions(models.Model):
    question_text = models.CharField(max_length=100,null=True,blank=True)
    option1 = models.CharField(max_length=100,null=True,blank=True)
    option2 = models.CharField(max_length=100,null=True,blank=True)
    option3 = models.CharField(max_length=100,null=True,blank=True)
    option4 = models.CharField(max_length=100,null=True,blank=True)
    ANSWER_CHOICES = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    )

    correct_answer = models.CharField(max_length=10, choices=ANSWER_CHOICES)


    def __str__(self):
        return "{self.question_text} {self.correct_answer}"
