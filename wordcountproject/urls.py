
from django.contrib import admin
from django.urls import path
from WordcountApp import views


urlpatterns = [
    path("",views.home, name="home"),
    path("count/", views.count, name = "count"),
    path('admin/', admin.site.urls),
]
