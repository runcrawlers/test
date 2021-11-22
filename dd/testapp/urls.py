from django.urls import path
from testapp import views

urlpatterns = [
    path('encode/', views.encode, name='encode'),
]
