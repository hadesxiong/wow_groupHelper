# coding=utf8

from fastapi import APIRouter, Depends

from app.api.schema.sch_group import *
from app.api.controller.ctrl_group import *

# 定义路由
group_rt = APIRouter(prefix='/group', tags=['group'])

# 定义查询接口
@group_rt.get('/groupQuery',
              response_model=GroupRes,
              response_model_exclude_unset=True)

async def getGroupList(params:GroupQuery = Depends()):

    fltr_parms = {k:v for k,v in params.model_dump().items() if v is not None}

    if fltr_parms.get('group_id'):
        fltr_parms.pop('page_no',None)
        fltr_parms.pop('page_size',None)

    rslt = await get_group_handler(fltr_parms)

    if fltr_parms.get('group_id'):
        return GroupRes(code=200, msg='success', data=rslt[0] if len(rslt)>=1 else None)

    else:
        return GroupRes(code=200, msg='success', data=rslt)