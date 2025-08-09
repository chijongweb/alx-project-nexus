from django.http import JsonResponse

def welcome(request):
    return JsonResponse({
        'message': 'Welcome to the E-Commerce API !!',
        'swagger_url': '/swagger/',
        'docs_url': '/docs/'
    })