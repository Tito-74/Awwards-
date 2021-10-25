from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.awards, name='awards'),
    path('review/(?P<id>\d+)/', views.review, name='review'),
    path('add/', views.addproject, name='add'),
    path('search/', views.search, name='search'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)