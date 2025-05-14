from django.urls import path
from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'api/movies', api.MovieModelViewSet, basename="movies")

urlpatterns = [
    
]

urlpatterns += router.urls