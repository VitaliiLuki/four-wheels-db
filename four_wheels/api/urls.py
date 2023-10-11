from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views
from .views import CarsViewSet, OptionViewSet

app_name = 'api'


router_v1 = DefaultRouter()
router_v1.register('cars', CarsViewSet, basename='cars')
router_v1.register('options', OptionViewSet, basename='options')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test', views.index),
]
