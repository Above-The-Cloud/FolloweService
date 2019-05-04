import json
import traceback
from decimal import Decimal

from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from train.models import Train


@csrf_exempt
def hello(request):
    return HttpResponse("Hello world ! ")

@csrf_exempt
def rcmd(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    if not {'start','end'}.issubset(set(request.POST.keys())):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'unexpected params!', 'data': request.POST.dict()}))
    try:
        qset=Train.objects.filter(start__contains=request.POST['start'],end__contains=request.POST['end'])
        gomore=[]
        for q in qset:
            row={}
            row['trainno']=q.trainno
            row['start']=q.start
            row['end']=q.end
            row['starttime'] = q.starttime.strftime('%H:%I')
            row['endtime'] = q.endtime.strftime('%H:%I')
            print(type(q.price),q.price)
            row['price']=str(q.price.quantize(Decimal('0')))
            gomore.append(row)
        res['data']['gomore'] = gomore
        res['data']['gorcmd'] = {} if len(gomore)==0 else gomore[0]

        qset = Train.objects.filter(start__contains=request.POST['end'], end__contains=request.POST['start'])
        gomore = []
        for q in qset:
            row = {}
            row['trainno'] = q.trainno
            row['start'] = q.start
            row['end'] = q.end
            row['starttime'] = q.starttime.strftime('%H:%I')
            row['endtime'] = q.endtime.strftime('%H:%I')
            print(type(q.price), q.price)
            row['price'] = str(q.price.quantize(Decimal('0')))
            gomore.append(row)
        res['data']['backmore'] = gomore
        res['data']['backrcmd'] = {} if len(gomore) == 0 else gomore[0]
    except:
        res = {'code': -3, 'msg': '查询失败-3', 'data': []}
        traceback.print_exc()
    return HttpResponse(json.dumps(res))