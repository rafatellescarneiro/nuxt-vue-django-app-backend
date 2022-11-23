
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from backend.core.router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token', TokenObtainPairView.as_view(), name="token"),
    path('api/refresh_token', TokenRefreshView.as_view(), name="refresh_token"),
]
