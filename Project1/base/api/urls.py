from django.urls import path
from . import views

urlpatterns =[
    path('', views.getRouter),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
    
]