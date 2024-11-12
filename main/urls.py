from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'car', CarListViewSet, basename='car')
router.register(r'reviews', ReviewViewSet)
router.register(r'ReviewViewSet', CharacteristicViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('cars/', CarModelCreateView.as_view(), name='cars')
]
