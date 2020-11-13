from django.urls import path, include
from rest_framework import routers

from api.user.views import UserViewSet, signin, signout

router = routers.DefaultRouter()
router.register(r'', UserViewSet)
urlpatterns = [
    path('login/', signin, name='signin'),
    path('logout/<int:id>/', signout, name='signout'),
    path('', include(router.urls)),
]
