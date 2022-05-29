from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adopt/<str:pk>', views.adopt, name='adopt'),
    path('photos/new/', views.new_photo, name='new_photo')
]