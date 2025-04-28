# coding=utf8

from tortoise import fields
from tortoise.models import Model

# 定义消息记录表
class MsgRecord(Model):

    rec_id = fields.CharField(max_length=64, unique=True)
    rec_batch = fields.CharField(max_length=64)
    msg_tmpl = fields.CharField(max_length=64)
    msg_rcv = fields.CharField(max_length=64)
    msg_data = fields.JSONField(null=True)
    msg_send_dt = fields.DatetimeField(auto_now=True, null=True)
    msg_stu = fields.IntField()
    msg_ext = fields.JSONField(null=True)

    class Meta:
        table = 'wgh_msg_record'