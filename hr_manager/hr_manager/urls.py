"""hr_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from hr.views import homepage
from hr.views import register
from hr.views import login
from hr.views import register_template
from hr.views import login_succes
from hr.views import login_error
from hr.views import login_template
from hr.views import logout
from hr.views import add
from hr.views import addTemplate
from hr.views import see_note
from hr.views import show_note





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('register/',register),
    path('register-template/',register_template),
    path('login-template/',login_template),
    path('login/',login),
    path('login-success/', login_succes),
    path('login-error/', login_error),
    path('logout/',logout),
    path('add-template/',addTemplate),
    path('add/',add),
    path('see-note/',see_note),
    path('show-note/',show_note),


]
