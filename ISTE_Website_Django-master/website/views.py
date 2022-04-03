from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,Http404

from .models import (
    Board,
    Feedback,
    Event,
    Category,
    Developer
)

from .forms import (
    FooterForm,
    FeedbackForm
)
from django.contrib import messages




import requests



def index(request):
    context={}
    if request.method=="POST":
        feedback=footer_feedback_form(request)
        if feedback==True:
            messages.success(request,"Form saved Successfully",extra_tags="success")
            context['form']=FooterForm()
            return redirect(reverse('website:index'))
        else:
            context['form']=feedback 
    else:
        respose=requests.get('https://blog.istemanipal.com/mobile/blogPosts')
        
        blogs=respose.json()[:5]
        #print(blogs[0]['_id'])

        context['form']=FooterForm()
        context['blogs']=blogs
    number_of_board_members=Board.objects.all().exclude(name__iexact='MC').exclude(name__iexact='WC').count()
    context['number_of_board_members']=number_of_board_members
    return render(request,"website/index.html",context=context)

# Create your views here.
def members_info(request):
    context={}
    if request.method=="POST":
        feedback=footer_feedback_form(request)
        if feedback==True:
            messages.success(request,"Form saved Successfully",extra_tags="success")
            context['form']=FooterForm()
        else:
            context['form']=feedback 
    else:
        context['form']=FooterForm()
    
    members=Board.objects.all().order_by("pk")
    
    try:
        mc=Board.objects.get(name__iexact='MC')
        context['mc']=mc
        members=members.exclude(name__iexact='MC')
    except:
        pass
    try:
        wc=Board.objects.get(name__iexact='WC')
        context['wc']=wc
        members=members.exclude(name__iexact="WC")
    except:
        pass
        

    context['members']=members

    return render(request,"website/members.html",context=context)


def developers(request):
    dev=Developer.objects.all().order_by("pk")
    return render(request,"website/developers.html", {'dev':dev})


def footer_feedback_form(request):
    feedback=FooterForm(request.POST)
    if feedback.is_valid():
        feedback.save()
        return True
    else:
        return feedback


def feedback(request):
    context={}
    if request.method=="POST":
        feedback=FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
            messages.success(request,"Response Recorded Successfully",extra_tags="success")
            context['form']=FeedbackForm()
        else:
            messages.error(request,"Please Check your Inputs",extra_tags="danger")
            context['form']=feedback
    else:
        context['form']=FeedbackForm()
    return render(request,"website/feedback.html",context=context)

def events(request):
    workshops=Event.objects.filter(category__name='Workshop',is_completed=True)
    techweek=Event.objects.filter(category__name='TechWeek',is_completed=True)
    vocational=Event.objects.filter(category__name='Vocational Courses',is_completed=True)
    active=Category.objects.filter(event__is_completed=False).order_by('-start_date').distinct()#|Category.objects.all().order_by('-start_date'))[:1]
    context={}
    if request.method=="POST":
        feedback=footer_feedback_form(request)
        if feedback==True:
            messages.success(request,"Form saved Successfully",extra_tags="success")
            context['form']=FooterForm()
        else:
            context['form']=feedback 
    else:
        context['form']=FooterForm()
    
    context['workshops']=workshops
    context['techweek']=techweek
    context['vocational']=vocational
    context['active']=active

    # test=(Category.objects.filter(event__is_completed=False).order_by('-start_date')|Category.objects.all().order_by('-start_date'))[:1]
    # print(test)
    return render(request,"website/events.html",context=context)

def eventdetails(request,category_slug):
    context={}
    try:
        category=Category.objects.filter(name_slug=category_slug,event__is_completed=False).first()
        events=Event.objects.filter(category__name=category.name,is_completed=False)
    except:
        raise Http404
    context['category']=category
    if events:
        context['events']=events
    return render(request,"website/eventdetails.html",context=context)


def acumen(request):
    context={}
    if request.method=="POST":
        feedback=footer_feedback_form(request)
        if feedback==True:
            messages.success(request,"Form saved Successfully",extra_tags="success")
            context['form']=FooterForm()
        else:
            context['form']=feedback 
    else:
        context['form']=FooterForm()
    return render(request,"website/acumen.html",context=context)



from django.contrib.auth.views import PasswordResetView
def passwordReset(request):
    return render(request,'website/reset.html')


