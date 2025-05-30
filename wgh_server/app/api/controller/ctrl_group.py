# coding=utf8

from bson.objectid import ObjectId
from datetime import datetime, timezone, timedelta
from fastapi_pagination import Params
from fastapi_pagination.ext.tortoise import paginate
from tortoise.expressions import Q
from typing import Dict, Any

from app.api.schema.sch_group import GroupInfo
from app.core.error import CustomHTTPException
from app.models.group import GroupMain, MemberMain
from app.utils.query import build_and_query, build_or_exp, get_dict_code


# 查询队伍
async def get_group_handler(filters):

    or_query = Q()

    filter_dict = {
        k:v for k,v in filters.items() \
        if k not in ['page_no','page_size','order_by']
    }

    and_query = build_and_query(filter_dict) if len(filter_dict) > 0 else Q()

    order_dict = {}

    try:
        if filters.get('page_no'):
            group_rslt = await paginate(
                GroupMain.filter(and_query),
                Params(page=filters['page_no'], size=filters['page_size'])
            )

        else:
            group_rslt = await GroupMain.filter(and_query)

        return group_rslt
    
    except:
        raise CustomHTTPException(status_code=400, detail='查询参数错误',err_code=40005)
    
# 增删改茶
async def update_group_handler(
        action_type: str | None = None,
        action_data: GroupInfo | None = None,
        usr_id: str | None = None):
    
    '''
    处理逻辑
    1. 判断三要素是否存在
    2. 根据type判断crud
    '''

    print(action_data)

    if action_type == 'create':

        create_dt = datetime.now(timezone(timedelta(hours=8)))
        action_data.update({
            'group_id': f'group_{ObjectId()}',
            'group_cap': usr_id,
            'group_create_dt': create_dt,
            'group_udpate_dt': create_dt,
            'group_stu': 1
        })

        try:
            group_rslt = await GroupMain.create(**action_data)
            return {
                'id': group_rslt.group_id[6:],
                'dt': create_dt.strftime('%Y-%m-%d %H:%M:%S')
            }
        
        except:
            raise CustomHTTPException(status_code=400, detail='参数错误', err_code=40006)
        
    else:
        raise CustomHTTPException(status_code=400, detail='方式错误', err_code=40007)