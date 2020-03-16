from django.shortcuts import render

# Create your views here.

from django.http import *
from .models import totp_user
from .totp import tool

def hello(request):
    print(request.META["HTTP_X_APPKEY"])
    return HttpResponse("Hello world !")


def check_code(request):
    if request.method == 'GET':
        appkey = request.META["HTTP_X_APPKEY"]
        code = str(request.GET.get("code",default=''))
        try:
            query = totp_user.objects.get(appkey=appkey)
        except Exception as e:
            return JsonResponse({"code": 0, "msg": "header X-APPKEY invalid."})

        return JsonResponse({"code": 1, "msg": "ok", "data": {"check": tool.check(query.token, code)}})
    else:
        return JsonResponse({"code": 0,"msg": "method %s is not allow" % request.method})


def create_user(request):
    if request.method == 'GET':
        token = tool.create_token()
        appkey = tool.rand_str()

        totp_user.objects.create(token=token,appkey=appkey)

        context = {}
        context['img'] = tool.make_qr_base64(tool.gen_uri(token))
        context['token'] = token
        context['appkey'] = appkey
        return render(request, 'create_user.html', context)
    else:
        return JsonResponse({"msg": "method %s is not allow" % request.method})
