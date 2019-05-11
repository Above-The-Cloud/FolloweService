import json
import traceback

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from guide.models import Guide


@csrf_exempt
def hello(request):
    return HttpResponse("Hello world ! ")

@csrf_exempt
def list(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    if not {'position'}.issubset(set(request.POST.keys())):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'unexpected params!', 'data': request.POST.dict()}))
    try:
        qset = Guide.objects.filter(position__contains=request.POST['position'])
        js=json.loads(serializers.serialize('json',qset))
        data=[x['fields'] for x in js]
        res['data']=data
    except:
        res = {'code': -3, 'msg': '查询失败-3', 'data': []}
        traceback.print_exc()
    return HttpResponse(json.dumps(res))