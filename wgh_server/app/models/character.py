# coding=utf8

from tortoise import fields
from tortoise.models import Model

# 定义角色主表
class CharMain(Model):

    char_id = fields.CharField(max_length=64, unique=True)
    bn_id = fields.CharField(max_length=64)
    char_name = fields.CharField(max_length=64)
    char_type = fields.IntField()
    char_equip = fields.IntField()
    char_race = fields.IntField()
    char_camp = fields.IntField()
    char_class = fields.IntField()
    char_create_dt = fields.DatetimeField(auto_now=True, null=True)
    char_update_dt = fields.DatetimeField(auto_now=True, null=True)
    char_stu = fields.IntField()
    char_ext = fields.JSONField(null=True)

    class Meta:
        table = 'wgh_char_main'