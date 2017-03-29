from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

import views


urlpatterns = [
    # acquire and refresh JWT token
    url(r'^auth/login', obtain_jwt_token, name='user-login'),
    url(r'^auth/api-token-refresh/', refresh_jwt_token),

    # dummy point
    url(r'^protected', views.ProtectedView.as_view(), name='protected'),
]
