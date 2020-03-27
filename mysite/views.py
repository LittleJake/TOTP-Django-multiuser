from django.shortcuts import render

# Create your views here.
from django.db.utils import *
from django.http import *
from .models import totp_user
from .totp import tool
from time import *

def check_code(request):
    if request.method == 'GET':
        id = request.GET.get("user", default=0)
        try:
            query = totp_user.objects.get(id=id)
            query.update_time = time()
            query.save()
        except Exception as e:
            return JsonResponse({"code": 0, "msg": "Invalid User."})

        code = str(request.GET.get("code", default=''))
        data = {
            "pass": tool.check(query.token, code),
            "time": int(time())
        }

        return JsonResponse({
            "code": 1,
            "msg": "OK",
            "data": data,
            "integrity": tool.check_sum(data, query.secret)
        })
    else:
        return JsonResponse({"code": 0,"msg": "method %s is not allow" % request.method})


def create_user(request):
    if request.method == 'GET':
        ip = get_client_ip(request)
        token = tool.create_token()
        secret = tool.rand_str()
        try:
            user = totp_user.objects.create(token=token,secret=secret,ip=ip,update_time=time())
        except IntegrityError as e:
            return HttpResponse('创建失败，IP重复')

        context = {}
        context['img'] = tool.make_qr_base64(tool.gen_uri(token))
        context['token'] = token
        context['secret'] = secret
        context['id'] = user.id
        context['ip'] = ip
        return render(request, 'create_user.html', context)
    else:
        return JsonResponse({"msg": "method %s is not allow" % request.method})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip