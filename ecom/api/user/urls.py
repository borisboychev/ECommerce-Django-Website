from django.urls import path, include
from rest_framework import routers

from api.user.views import UserViewSet, sign_in, sign_out

router = routers.DefaultRouter()
router.register(r'', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', sign_in, name='sign in'),
    path('logout/<int:id>/', sign_out, name='sign out'),
]
