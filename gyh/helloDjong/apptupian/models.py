from django.db import models

# Create your models here.

class gyhUser(models.Model):
    openid = models.CharField(max_length=64,unique=True)
    nickname = models.CharField(max_length=64,db_index=True)
    # def __str__(self):
    #     return self.nickname