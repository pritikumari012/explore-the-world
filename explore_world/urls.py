from django.contrib import admin
from django.urls import path, include

from .views import hello_srm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_srm),
    path('', include('travel.urls')),
]