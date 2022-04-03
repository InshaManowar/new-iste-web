from . import views
from django.urls import path
from django.contrib.auth.views import PasswordResetView

from .forms import CustomPasswordResetForm

app_name="website"


urlpatterns = [
    path("",views.index,name="index"),
    path("events",views.events,name="events"),
    path("event/<slug:category_slug>",views.eventdetails,name="eventdetails"),
    path("acumen",views.acumen,name="acumen"),
    path("members",views.members_info,name="members"),
    path("developers",views.developers,name="developers"),
    path("feedback",views.feedback,name="feedback"),

    #Password Reset
    path("reset",PasswordResetView.as_view(template_name="website/reset.html",form_class=CustomPasswordResetForm),name="reset"),
    
 

]
