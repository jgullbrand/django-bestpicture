from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'moviedata', views.MovieDataViewSet, base_name="test")

urlpatterns = [
    path("", views.index, name = "index"),
    path("api/", include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
