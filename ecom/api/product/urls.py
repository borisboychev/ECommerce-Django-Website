from django.urls import path, include
from rest_framework import routers

from api.product.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'', ProductViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
