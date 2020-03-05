from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse
# Create your views here.
import requests
import yaml
from django.conf import settings
from django.views import View
import json
# import myfirstproj.settings 和上边一致
# from helloDjong import settings
import os
from django.shortcuts import render
from utils import responseutil
from utils.responseutil import UtilMixin
from helloDjong import secret_settings
from apptupian.models import gyhUser
# Create your views here.
def image(request):
    if request.method == 'GET':
        filepath = os.path.join(settings.STATIC_ROOT_SELF, '123.jpg')
        f = open(filepath, 'rb')
        # with open(filepath, 'rb') as f:
        # return HttpResponse(content=f.read(),content_type='image/png')
        return FileResponse(f, content_type='image/jpg')
    elif request.method == "POST":
        return HttpResponse('这是post请求')
    else:
        return HttpResponse(request.method + '方法没有实现')

class ImageView(View,UtilMixin):

    def get(self, request):
        filepath = os.path.join(settings.STATIC_ROOT_SELF, '123.jpg')
        f = open(filepath, 'rb')
        # with open(filepath, 'rb') as f:
        # return HttpResponse(content=f.read(),content_type='image/png')
        return FileResponse(f, content_type='image/jpg')
        # return render(request,'upfile.html')

    def post(self, request):
        files1 = request.FILES
        # class 'django.utils.datastructures.MultiValueDict'
        # print(type(files))
        picdir = settings.UPLOAD_PIC_DIR

        for key,value in files1.items():
            filename = os.path.join(picdir,key[-8:])
            UtilMixin.savepic(filename,value.read())

        # return HttpResponse(filename)
        return JsonResponse(UtilMixin.wrapdic({'filename':key[-8:]}))

    def delete(self,request):
        picname = request.GET.get('name')
        picdir = settings.UPLOAD_PIC_DIR
        poc_full_path = os.path.join(picdir,picname)
        if not os.path.exists(poc_full_path):
            return HttpResponse('图片不存在')
        else:
            os.remove(poc_full_path)
            return HttpResponse('图片删除成功')

from utils.responseutil import ResponseMixin
class ImageText(View, ResponseMixin):
    def get(self, request):
        return JsonResponse(data=self.wrap_response({'url': 'xxxxx', 'des': '我很好','code':2002}))

class CookeieTest(View):
# 发送cookie
    def get(self,request):
        # print(dir(request))
        request.session['mykey']='gyh98.521'
        return JsonResponse({'key':'value'})

class CookeieTest2(View):
# 接受cookie
    def get(self,request):
        # request.session 这个是一个字典 可以用items()把内容遍历出来
        # print(dir(request))
        print(request.session['mykey'])
        print(request.session.items())
        return JsonResponse({'key2':'value2'})
# 登录
class authorize(View):
    def get(self,request):
        return self.post(request)
    def post(self,request):
        print(request.body) # b'{"code":"043cZlUH0WI9md2lUGTH0tBuUH0cZlUY"}'
        bodystr = request.body.decode('utf-8')
        bodydict =json.loads(bodystr)
        code = bodydict.get('code')
        nickName = bodydict.get('nickName')
        print(code) # 043yhc890Mj44A1Ob0690Pvc890yhc8Y
        print(nickName)
        appid = secret_settings.appid
        secret = secret_settings.secret
        js_code = code
        url ='https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(appid,secret,js_code)
        res = requests.get(url)
        print(res.text)
        res_dict =json.loads(res.text)
        openid = res_dict.get('openid')
        if not openid:
            return HttpResponse('滚蛋')
        request.session['openid']=openid
        request.session['id_authorized']=True

        # 保存用户信息
        if not gyhUser.objects.filter(openid=openid):
            newuser = gyhUser(openid=openid,nickname=nickName)
            newuser.save()
        return HttpResponse('authorize post OK')