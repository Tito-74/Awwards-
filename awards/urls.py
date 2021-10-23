from django.urls import path
from . import views

urlpatterns = [
    path('', views.awards, name='awards'),
    path('review/', views.review, name='review'),
    path('add/', views.addproject, name='add'),
    path('search/', views.search, name='search'),
    path('vote/', views.vote, name='vote'),
]