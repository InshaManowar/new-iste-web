"""iste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include


from django.contrib.auth.views import PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView

from website.forms import CustomPasswordResetConfirm

from . import settings
urlpatterns = [
    path('admin/',admin.site.urls),
    path("",include("website.urls")),
    path("api/",include("api.urls")),

    #Password Reset
       path("password-reset/confirm/<uidb64>/<token>/",PasswordResetConfirmView.as_view(template_name="website/reset_confirm.html",form_class=CustomPasswordResetConfirm),
    name="password_reset_confirm"),
    
    path("password-rest/sent/",PasswordResetDoneView.as_view(template_name="website/reset_sent.html"),name="password_reset_done"),
    
    path("password-reset/complete/",PasswordResetCompleteView.as_view(template_name="website/reset_complete.html"),
        name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)