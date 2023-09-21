
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url

from news6app.views import *

urlpatterns = [
    path('news/<int:pk>/recommend/', NewsView),
    path('news/<int:pk>/', DetailView),
    path('news/', ListView),
]
