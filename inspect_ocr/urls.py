from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ImageCreateView

router = DefaultRouter(trailing_slash=False)

router.register(r'images', ImageCreateView, basename='images')

urlpatterns = [
    path(r'', include(router.urls))
]