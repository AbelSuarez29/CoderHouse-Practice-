from django.urls import path, include
from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name = "index"),
    path("about/", views.about, name="about"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', exit, name= "exit")
]

