from django.contrib import admin
from django.urls import path
from.views import hello_srm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_srm),
]