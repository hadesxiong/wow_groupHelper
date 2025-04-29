# coding=utf8

from pydantic import BaseModel, Field
from typing import Dict, List, Any

from app.api.schema.sch_base import ResBasic

'''
队伍创建
'''

# 定义组基本信息
class GroupInfo(BaseModel):

    group_name: str | None = Field(default=None, alias='name')
    group_mark: str | None = Field(default=None, alias='mark')
    group_type: int | None = Field(default=None, alias='type')
    group_cap: str | None = Field(default=None, alias='cap')
    group_open: int | None = Field(default=None, alias='open')

    class Config:
        extra = 'forbid'

# 定义查询
class GroupQuery(BaseModel):
    group_id: str | None = Field(default=None, alias='group')
    group_type: int | None = Field(default=None, alias='type')
    group_open: int | None = Field(default=None, alias='open')

    class Oonfig:
        extra = 'forbid'

# 定义动作神情
class GroupAction(BaseModel):

    action_type: str | None = Field(default=None, alias='action')
    group_id: str | None = Field(default=None, alias='group')
    group_data: GroupInfo | None = Field(default=None, alias='data')

# 定义回复
class GroupRes(ResBasic):

    target: str | List[Any] | Dict[str, Any] | None = Field(default=None)
    dt: str | None = Field(default=None)