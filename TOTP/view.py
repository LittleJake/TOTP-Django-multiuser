from django.http import *
from django.db import models

def hello(request):
    print(request.META["HTTP_X_APPKEY"])
    return HttpResponse("Hello world !")


def check_code(request, code):
    appkey = request.META["HTTP_X_APPKEY"]

