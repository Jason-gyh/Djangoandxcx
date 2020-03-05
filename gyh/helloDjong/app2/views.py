from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse
# Create your views here.
import requests
import yaml
import os
from helloDjong import settings
from django.views import View
def hellojuhe(request):
    url ="http://apis.juhe.cn/xzpd/query?men=%E6%B0%B4%E7%93%B6&women=%E6%91%A9%E7%BE%AF&key=53bb9075aab043eb32ad1d7943624cd6"
    res = requests.get(url)
    if res.status_code == 200:
        return HttpResponse(res.text)
    else:
        return HttpResponse('没有找到数据')
# def apps(request):
#     return JsonResponse(['微信','支付宝','钉钉'],safe=False)
def apps(request):
    filepath = r'D:\MyDjangos\helloDjong\app2\my_app.yaml'
    with open(filepath, 'r', encoding='utf-8')as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
    return JsonResponse(res,safe=False)
