from django.urls import path,include
from . import views


app_name="research"
urlpatterns=[
    path("professors",views.getProfessors,name="professors"),
]