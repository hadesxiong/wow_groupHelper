# coding=utf8

from tortoise import fields
from tortoise.models import Model

# 定义用户主标
class UserMain(Model):

    usr_id = fields.CharField(max_length=64, unique=True)
    usr_uid = fields.CharField(max_length=64, unique=True)
    usr_unionid = fields.CharField(max_length=64)
    usr_openid = fields.CharField(max_length=64, unique=True)
    usr_create_dt = fields.DatetimeField(auto_now=True, null=True)
    usr_update_dt = fields.DatetimeField(auto_now=True, null=True)
    usr_stu = fields.IntField(null=True)
    usr_ext = fields.JSONField(null=True)

    class Meta:
        table = 'wgh_user_main'

# 定义BN用户信息表
class UserBattlleNet(Model):

    usr_uid = fields.CharField(max_length=64)
    bn_id = fields.CharField(max_length=64, unique=True)
    usr_openid = fields.CharField(max_length=64)
    bn_tag = fields.CharField(max_length=64)
    bn_create_dt = fields.DatetimeField(auto_now=True, null=True)
    bn_update_dt = fields.DatetimeField(auto_now=True, null=True)
    bn_stu = fields.IntField(null=True)
    bn_ext = fields.JSONField(null=True)

    class Meta:
        table = 'wgh_user_battlenet'