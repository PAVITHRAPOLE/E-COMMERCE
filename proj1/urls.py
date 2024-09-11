"""
URL configuration for proj1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app1.views import index,about,register,contact,login,doregister,logincheck,userhome,adminhome,viewusers,modify,amazon,fashion,success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('about/',about),
    path('register/',register),
    path('login/',login),
    path('contact/',contact),
    path('doregister/',doregister),
    path('logincheck/',logincheck),
    path('userhome/',userhome),
    path('adminhome/',adminhome),
    path('viewusers/',viewusers),
    path('modify/',modify),
    path('amazon/',amazon),
    path('fashion/',fashion),
    path('success/',success)
]
    

