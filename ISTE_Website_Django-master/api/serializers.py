from website.models import (
    Category,
    Event,
    Event_Date
)
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import Question,Mentor,Answer
    

class EventDateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event_Date
        fields=['venue','start_date','end_date','title']

class EventSerializer(serializers.ModelSerializer):
    event_date_set=EventDateSerializer(many=True,read_only=True)
    class Meta:
        model=Event
        fields=['name','description','is_completed','registration_link','event_date_set']

class CategorySerializer(serializers.ModelSerializer):
    events=serializers.SerializerMethodField('get_not_completed')
    class Meta:
        model=Category
        fields=['name','start_date','end_date','poster','name_slug','description','registration_link','events']
    
    def get_not_completed(self,category):
        event=Event.objects.filter(category=category,is_completed=False)
        serializer=EventSerializer(event,many=True)
        return serializer.data

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Token
        fields=['key']

class UserCreationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self):
        user=User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
        )
        password1=self.validated_data['password']
        password2=self.validated_data['password2']
        if password1!=password2:
            raise serializers.ValidationError({'status':"Error",'errors':{'password':['Passwords did not match']}})
        if len(password1)>=8:
            user.set_password(password1)
            user.save()
            return user
        raise serializers.ValidationError({'status':"Error",'errors':{'password':['Password is too short']}})


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mentor
        fields=['name','company','year','brief_description']



class QuestionSerializer(serializers.ModelSerializer):
    mentor=MentorSerializer(many=False,read_only=True)
    category=serializers.StringRelatedField(read_only=True,many=False)
    class Meta:
        model=Question
        fields=['pk','mentor','question','category','expected_answer']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=['answer']
    
class SubmittedAnswerSerializer(serializers.ModelSerializer):
    question=QuestionSerializer(many=False,read_only=True)
    class Meta:
        model=Answer
        fields=['question','answer','points']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','first_name','last_name']

class LeaderboardSerializer(serializers.ModelSerializer):
    user=UserSerializer(many=False,read_only=True)
    class Meta:
        model=Answer
        fields=['user','points']
    