from django.urls import path
from . import views


urlpatterns = [
    path('', views.mountain, name='mountain'),
]
