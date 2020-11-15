from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
import braintree
from django.views.decorators.csrf import csrf_exempt

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="g4dpbrpyffj9b4ds",
        public_key="8swrjmsrbmvgfms9",
        private_key="a52083aa56f84f0895d3174f4a14a68c"
    )
)


def validate_user_session(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({"error": "Invalid session (re-login)"})

    # Generates client token and send it to the frontend
    return JsonResponse({"client_token": gateway.client_token.generate(), 'success': True})


@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({"error": "Invalid session (re-login)"})

    nonce_from_client = request.POST['paymentMethodNonce']
    amount_from_client = request.POST['amount']

    result = gateway.transaction.sale({
        "amount": amount_from_client,
        "payment_method_nonce": nonce_from_client,
        "options": {
            "submit_for_settlement": True
        }
    })

    if result.is_success:
        return JsonResponse({
            "success": result.is_success,
            "transaction": {
                "id": result.transaction.id,
                "amount": result.transaction.amount
            }
        })
    return JsonResponse({"erorr": True, "success": result.is_success})
