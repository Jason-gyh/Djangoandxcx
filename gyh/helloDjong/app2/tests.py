from django.test import TestCase

# Create your tests here.

import yaml
filepath = r'D:\MyDjangos\helloDjong\app2\my_app.yaml'
with open(filepath,'r',encoding='utf-8')as f:
    res = yaml.load(f, Loader=yaml.FullLoader)
    print(res)
