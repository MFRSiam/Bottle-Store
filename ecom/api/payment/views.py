from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import braintree


gateway = braintree.BraintreeGateway(
    braintree.Configuration(
    environment=braintree.Environment.Sandbox,
    merchant_id='b82ntpq756jgpww8',
    public_key='bvkcj5hmqdvz3cz7',
    private_key='f908a6e6acb04f14a9bd8e0055b9b5b3'
    )
)

def validate_user_session(id,token):
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False
    
    
@csrf_exempt
def generate_token(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'Error':'Invalid Session,Please Login Again'})
    return JsonResponse({'clientToken':gateway.client_token.generate(),'Success':True})

@csrf_exempt
def process_payment(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'Error':'Invalid Session,Please Login Again'})
    
    nonce_from_the_client = request.POST["paymentMethonNonce"]
    amount_from_the_client = request.POST["amount"]
    
    result = gateway.transaction.sale({
        "amount": amount_from_the_client,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
        "submit_for_settlement": True
        }
    })
    
    if result.is_success:
        return JsonResponse({
            'Success':result.is_success,
            'transaction':{'id':result.transaction.id,'amount':result.transaction.amount}
            })
    else:
        return JsonResponse({'Error':True,'Success':False})