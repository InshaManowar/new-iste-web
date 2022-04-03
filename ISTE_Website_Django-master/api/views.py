from django.shortcuts import render
#models
from website.models import Category,Event
from .models import (Question,Answer)
from django.contrib.auth.models import User
#rest api
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from pytz import timezone


#serializers
from .serializers import CategorySerializer,EventSerializer,UserCreationSerializer,QuestionSerializer,AnswerSerializer,SubmittedAnswerSerializer,LeaderboardSerializer



@api_view(['GET'])
def getCategory(request):
    context={}
    category=Category.objects.filter(event__is_completed=False).order_by('-start_date').distinct()
    serializer=CategorySerializer(category,many=True)
    if category:
        context['status']="Found"
    else:
        context['status']="Not Found"
    context['active']=serializer.data

    return Response(context)

@api_view(['GET'])
def getEvents(request,category):
    context={}
    events=Event.objects.filter(category__name_slug=category,is_completed=False)
    serializer=EventSerializer(events,many=True)
    if events.count()==0:
        context['status']="not found"
    else:
        context['status']="found"
    context['events']=serializer.data
    return Response(context)

@api_view(['POST'])
def userRegistration(request):
    serializer=UserCreationSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        user=serializer.save()
        data['status']="successful"
        data['details']={
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email,
            'token':user.auth_token.key,
        }

    else:
        data['status']="error"
        data['errors']=serializer.errors

    return Response(data)


class CustomLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        context={}
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid(raise_exception=False):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            context['status']="successful"
            context['token']=token.key
            context['username']=user.username
            context['email']=user.email
            context['first_name']=user.first_name
            context['last_name']=user.last_name
            
        else:
            context['status']="unsuccessful"
        return Response(context)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_questions(request):
    context={}
    question=Question.objects.all()
    answered=Question.objects.filter(answers__user=request.user)
    question=question.exclude(pk__in=answered)
    serializers=QuestionSerializer(question,many=True)

    context['questions']=serializers.data
    context['status']="successful"
    return Response(context)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def submit_answer(request):
    context={}
    try:
        submission=Answer(user=request.user,question=Question.objects.get(pk=int(request.data.get('pk'))))
    except:
        context['status']="unsuccessful"
        context['errors']="Invalid pk"
        return Response(context)
    serializer=AnswerSerializer(submission,data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            context['status']="successful"
        except:
            context['status']="unsuccessful"
            context['errors']="Cannot submit again"
            return Response(context)
    else:
        context['status']="unsuccessful"
        context['errors']=serializer.errors
    return Response(context)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_submitted_answers(request):
    context={}
    answers=Answer.objects.filter(user=request.user).order_by('points')
    serializer=SubmittedAnswerSerializer(answers,many=True)
    if answers.count()==0:
        context['status']="not found"
    else:
        context['status']="found"
    context['answers']=serializer.data
    return Response(context)


@api_view(['GET'])
def get_leaderboard(request,pk):
    context={}
    leaderboard=Answer.objects.filter(question__pk=pk).exclude(points__isnull=True).order_by('-points')
    seraializer=LeaderboardSerializer(leaderboard,many=True)
    if leaderboard.count()==0:
        context['status']="no answers to show"
    else:
        context['status']="found"
    context['leaderboard']=seraializer.data
    return Response(context)



        