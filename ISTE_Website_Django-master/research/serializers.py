from .models import (
    Professor,
    Project,
    Department,
    Category
)
from rest_framework import serializers

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['name','building','hod']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name']

class ProjectSerializer(serializers.ModelSerializer):
    categories=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Project
        fields=['name','description','categories']

class ProfessorSerializer(serializers.ModelSerializer):
    department=DepartmentSerializer(many=False,read_only=True)
    project_set=ProjectSerializer(many=True,read_only=True)
    class Meta:
        model=Professor
        fields=['name','position','cabin','email','phone','department','time_to_approach','project_set']
