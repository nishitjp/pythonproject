from django.urls import path,include
from .models import Songs
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router=routers.DefaultRouter()
router.register('Songs',views.songlist)

urlpatterns = [
    path('',include(router.urls))
   
]



