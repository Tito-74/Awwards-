from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.awards, name='awards'),
    path('review/(?P<id>\d+)/', views.review, name='review'),
    path('add/', views.addproject, name='add'),
    path('search/', views.search, name='search'),
    url('api/v1/profile',views.ProfileList.as_view(),name='profileEndpoint'),
    url('api/v1/post',views.ProjectList.as_view(),name='postEndpoint')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)