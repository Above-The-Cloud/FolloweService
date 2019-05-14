import json
import traceback

from django.core import serializers
from django.http import HttpResponse
from spot.models import Spot
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def hello(request):
 return HttpResponse("Hello world ! ")

@csrf_exempt
def rcmdSpot(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    if not {'position'}.issubset(set(request.POST.keys())):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'unexpected params!', 'data': request.POST.dict()}))
    try:
        qset = Spot.objects.filter(address__contains=request.POST['position'])
        for x in json.loads(serializers.serialize('json',qset)):
            row=x['fields']
            row['id']=x['pk']
            res['data'].append(row)
        # res['data']=[ x['fields'] for x in json.loads(serializers.serialize('json',qset))]
    except:
        res = {'code': -3, 'msg': '查询失败-3', 'data': []}
        traceback.print_exc()

    return HttpResponse(json.dumps(res))
