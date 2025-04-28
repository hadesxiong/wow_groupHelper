# coding=utf8

from tortoise import fields
from tortoise.models import Model

# 定义队伍表
class GroupMain(Model):

    group_id = fields.CharField(max_length=64, unique=True)
    group_name = fields.CharField(max_length=64)
    group_mark = fields.TextField()
    group_type = fields.IntField()
    group_cap = fields.CharField(max_length=64)
    group_open = fields.IntField()
    group_stu = fields.IntField()
    group_create_dt = fields.DatetimeField(auto_now=True, null=True)
    group_update_dt = fields.DatetimeField(auto_now=True, null=True)
    group_ext = fields.JSONField(null=True)

    class Meta:
        table = 'wgh_group_main'

# 定义队员表
class MemberMain(Model):

    member_id = fields.CharField(max_length=64)
    group_id = fields.CharField(max_length=64)
    char_id = fields.CharField(max_length=64)
    member_type = fields.IntField()
    member_class = fields.IntField()
    member_stu = fields.IntField()
    member_create_dt = fields.DatetimeField(auto_now=True, null=True)
    member_update_dt = fields.DatetimeField(auto_now=True, null=True)
    member_ext = fields.JSONField(null=True)

    class Meta:
        table = 'wgh_member_main'
