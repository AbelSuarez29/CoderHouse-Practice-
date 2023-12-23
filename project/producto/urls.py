from django.urls import path, include
from . import views

app_name = "producto"

urlpatterns = [
    path('', views.home, name = "index"),
    path('accounts/', include('django.contrib.auth.urls')),
]
