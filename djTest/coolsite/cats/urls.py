from djoser import urls
from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

from cats.views import *

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('api/v1/token/', TokenObtainPairView.as_view()),
    path('api/v1/token/refresh/', TokenObtainPairView.as_view()),
    path('api/v1/token/verify/', TokenVerifyView.as_view()),
    path('api/v1/', include(router.urls)),
]
