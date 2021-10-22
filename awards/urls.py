from django.urls import path
from . import views

urlpatterns = [
    path('', views.awards, name='awards'),
    path('review/<str:pk>/', views.review, name='review'),
    path('add/', views.addproject, name='add'),
    path('search/', views.search_category, name='search'),
]