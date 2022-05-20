from django.urls import  path
from AppCoder.views import Mama,Hermana,Hermano
from django.contrib import admin

urlpatterns = [

     path('Mama/', Mama),
     path('Hermana/',Hermana),
     path('Hermano/',Hermano),
     #path('Mascota',views.Novia),
     #path('Novia',views.Mascota),

]