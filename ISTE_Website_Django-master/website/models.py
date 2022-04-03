from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver


import os
from PIL import Image
# Create your models here.
class Board(models.Model):
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    image=models.ImageField(upload_to="DPs")
    linkedin = models.CharField(max_length=150, default=None, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    github = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name

class Developer(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="DPs")
    linkedin = models.CharField(max_length=150, default=None, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    github = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name



def between_check(value):
    if not (value<=5 and value>=1):
        raise ValidationError("Rating should be between 1 and 5")

def check_phone(value):
    if value<=999999999:
        raise ValidationError("Number should be atleast 10 digits")


class Feedback(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254,unique=True)
    phone=models.CharField(max_length=12)
    rating=models.IntegerField(validators=[between_check],choices=[
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ])
    message=models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField(null=True,blank=True)
    poster=models.ImageField(upload_to="Posters",null=True,blank=True)
    name_slug=models.SlugField(null=True,blank=True)
    description=models.TextField(max_length=1000,null=True,blank=True)
    registration_link=models.URLField(null=True,blank=True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name



class Event(models.Model):
    category=models.ForeignKey(to=Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    is_completed=models.BooleanField(default=False)
    registration_link=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name

class Event_Date(models.Model):
    title=models.CharField(max_length=100)
    event=models.ForeignKey(to=Event,on_delete=models.CASCADE)
    venue=models.CharField(max_length=100)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.venue+" : "+str(self.start_date)
    
    class Meta:
        verbose_name="Dates of Events"
        verbose_name_plural=verbose_name
        ordering=['start_date']




@receiver(pre_save,sender=Category)
def delete_previous(sender,instance=None,**kwargs):
    if not instance.pk:
        return False
    
    try:
        old_file=sender.objects.get(pk=instance.pk).poster
        if (not old_file) or (old_file==instance.poster):
            return False
    except:
        return False
    os.remove(old_file.path)


@receiver(pre_save,sender=Category)
def make_slug(sender,instance=None,**kwargs):
    instance.name_slug=slugify(instance.name)

@receiver(post_save,sender=Board)
def resize_board_image(sender,instance=None,**kwargs):
    image=Image.open(instance.image.path)
    new_image=image.resize((640,640))
    new_image.save(instance.image.path)


