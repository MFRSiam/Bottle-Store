from unicodedata import name
from django import urls
from rest_framework import routers
from django.urls import path,include

from . import views



router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('login/',views.signIn,name='signin'),
    path('logout/<int:id>',views.signOut,name='signout'),
    path('',include(router.urls))
]