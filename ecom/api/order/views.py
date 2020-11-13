from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.order.models import Order
from api.order.serializers import OrderSerializer

# Create your views here.
from rest_framework import viewsets


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)

        # Checks if user session token is equal to passed token
        if user.session_token == token:
            return True
        return False

    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def add(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Session has expired (re-login)'})

    if request.method == "POST":
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']

        total_products = len(products.split(', '))[:-1]

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'})

        order = Order(user=user,
                      product_names=products,
                      total_products=total_products,
                      transaction_id=transaction_id,
                      total_amount=amount)

        order.save()
        return JsonResponse({'success': True, 'error': False, 'msg': 'Order placed successfully'})
