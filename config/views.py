from django.http import JsonResponse
from users.views import RegisterView

def welcome(request):
    return JsonResponse({'message': 'Welcome to the E-Commerce API !!'})