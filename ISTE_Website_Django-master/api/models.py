from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver


from rest_framework.authtoken.models import Token

@receiver(post_save,sender=User)
def create_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)



class Mentor(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    company=models.CharField(max_length=100)
    brief_description=models.TextField(max_length=500)

    def __str__(self):
        return self.name+" "+self.company

class Category(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name="Category for Question"
        verbose_name_plural="Categories for Question"
    def __str__(self):
        return self.title

class Question(models.Model):
    mentor=models.ForeignKey(to=Mentor,on_delete=models.CASCADE)
    question=models.TextField(max_length=65000)
    category=models.ForeignKey(to=Category,on_delete=models.SET_NULL,null=True,blank=True)
    #expiry_date=models.DateField(blank=True,null=True)
    expected_answer=models.TextField(max_length=65000,blank=True,null=True)
    #right=models.IntegerField(default=0,blank=True)
    #wrong=models.IntegerField(default=0,blank=True)
    def __str__(self):
        return self.question[0:50]



def hundred_check(value):
    if value>100:
        raise ValidationError("Points must be less than or equal to 100!")

class Answer(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="answers")
    question=models.ForeignKey(to=Question,on_delete=models.CASCADE,related_name="answers")
    answer=models.TextField(max_length=10000)
    points=models.DecimalField(max_digits=4,decimal_places=1,null=True,blank=True,validators=[hundred_check])
    
    def __str__(self):
        return self.user.first_name+"-->"+self.answer[0:50]
    
    class Meta:
        unique_together=['user','question']


