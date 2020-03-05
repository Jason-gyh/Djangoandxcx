from django.test import TestCase

# Create your tests here.
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] ='helloDjong.settings'
django.setup()

from apptupian.models import gyhUser

# r = gyhUser.objects.filter(nickname__contains='哈')
# print(r)
import random
def ranstr(length):
    CHS = 'easdadsfsgfsdhjyregervdfbrthwergjlgjhlergrngoingirewiotwivlkfnglngqieger'
    salt=''
    for i in range(length):
        salt += random.choice(CHS)
    return salt

# 单个数据添加
# def add_one():
#     # 第一种
#     User = gyhUser(openid='test_nickname',nickname='xxxxxxxxxxx')
#     User.save()
#     # 第二种
#     gyhUser.objects.create(openid='sssssssssss',nickname='hui')
# add_one()

# 多数据添加
# def add_batch():
#     new_user_list = []
#     for i in range(10):
#         openid = ranstr(32)
#         nickname = ranstr(5)
#         user = gyhUser(openid=openid,nickname=nickname)
#         new_user_list.append(user)
#     gyhUser.objects.bulk_create(new_user_list)
# add_batch()
# 精确查询
# def get_one():
#     user = gyhUser.objects.get(openid='test_nickname')
#     print(user)
# get_one()