#awesome_website/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns =[
    path('', include('myApp.urls')),
    path('admin/', admin.site.urls),
]
