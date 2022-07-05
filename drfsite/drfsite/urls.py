
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from auto.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth', include('rest_framework.urls')),
    path('api/v1/auto/', AutoAPIList.as_view()),
    path('api/v1/auto/<int:pk>/', AutoAPIUpdate.as_view()),
    path('api/v1/autodelete/<int:pk>/', AutoAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
