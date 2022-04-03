from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    building=models.CharField(max_length=20)
    hod=models.CharField(max_length=200,blank=True,null=True)
    
    

    def __str__(self):
        return self.name+"  "+self.building


class Professor(models.Model):
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=200)
    cabin=models.CharField(max_length=50)
    email=models.EmailField(null=True,blank=True)
    phone=models.CharField(max_length=12,null=True,blank=True)
    department=models.ForeignKey(to=Department,on_delete=models.CASCADE)
    time_to_approach=models.CharField(max_length=200)

    class Meta:
        verbose_name="Professors and Projects"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name+"--->"+self.position
    

class Category(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural="Categories"
    def __str__(self):
        return self.name



class Project(models.Model):
    professor=models.ForeignKey(to=Professor,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=65530)
    categories=models.ManyToManyField(to=Category)

    #help_needed=models.BooleanField()

    def __str__(self):
        return self.professor.name+"--->"+self.name
    

