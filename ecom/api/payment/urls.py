from django.urls import path, include
from rest_framework import routers

from api.payment.views import generate_token, process_payment
from api.user.views import UserViewSet, signin, signout

urlpatterns = [
   path('gettoken/<str:id>/<str:token>/', generate_token, name="token generate"),
   path('process/<str:id>/<str:token>/', process_payment, name="process payment"),
]