import email
from lib2to3.pgen2 import token
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout

import random
import re


# Create your views here.

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)]+[str(i) for i in range(10)]) for _ in range(length))


@csrf_exempt
def signIn(request):
    if not request.method == 'POST':
        return JsonResponse({'error':'Send a Post Request with Valid Parameter Only'})

    username = request.POST['email']
    password = request.POST['password']
    
    #validation Part
    
    if not re.match("/\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b/gi",username):
        return JsonResponse({'error':'Enter a Valid Email'})
    
    if len(password) < 3:
        return JsonResponse({'error':'Passwords Needs to be at least 3 char long'})

    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
            user_dict = UserModel.objects.filter(email=username).values().first()
            user_dict.pop('password')
            
            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error':'Previous Session Exists!'})
            
            token = generate_session_token()
            user.session_token =token
            user.save()
            login(request,user)
            return JsonResponse({'token':token, 'user':user_dict})
        else:
            return JsonResponse({'error':'Invalid Password'})
        
    except UserModel.DoesNotExist:
        return JsonResponse({'error':'Invalid Email'})
    
    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer
    
    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


def signOut(request,id):
    logout(request)
    
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'Error':'Invalid User ID'})
    
    return JsonResponse ({'success':'Logout Success'})
