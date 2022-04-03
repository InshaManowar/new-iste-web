from . import views
from django.urls import path,include



app_name="api"
urlpatterns = [
   

    #Event related
    path("category",views.getCategory,name="category"),
    path("event/<slug:category>",views.getEvents,name="events"),

    #authorization
    path("register",views.userRegistration,name="register"),
    path("login",views.CustomLogin.as_view(),name="login"),

    #Interview 
    path('interview/questions',views.get_questions,name="questions"),
    path("interview/submit",views.submit_answer,name="sumbit_answer"),
    path("interview/submitted",views.get_submitted_answers,name="submitted_answers"),
    path("interview/leaderboard/<int:pk>",views.get_leaderboard,name="leaderboard"),

    #Research
    path("research/",include("research.urls")),
]
