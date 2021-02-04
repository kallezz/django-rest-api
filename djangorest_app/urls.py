from django.urls import path, include
from rest_framework import routers
from .viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include('api.urls')),
    path('api/auth/', include('rest_framework.urls'))
]
