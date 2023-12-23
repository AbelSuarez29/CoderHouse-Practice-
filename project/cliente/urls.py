from django.urls import path, include
from . import views

app_name = "cliente"

urlpatterns = [
    path('', views.home, name = "index"),
    path('cliente/', views.cliente_view, name= "cliente"),
    path('accounts/', include('django.contrib.auth.urls')),
]
