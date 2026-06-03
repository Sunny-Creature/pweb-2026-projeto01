from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('characters/', views.personagens, name="personagens"),
    path('about/', views.sobre, name="sobre"),
]