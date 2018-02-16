# contactus/urls.py
from django.contrib import admin
from django.conf.urls import url

from contactus import views

app_name = 'contactus'

urlpatterns = [
    url(r'^$',views.emailView, name='email'),

]
