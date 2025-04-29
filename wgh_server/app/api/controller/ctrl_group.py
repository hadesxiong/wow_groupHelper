# coding=utf8

from datetime import datetime
from fastapi_pagination import Params
from fastapi_pagination.ext.tortoise import paginate
from tortoise.expressions import Q

from app.models.group import GroupMain, MemberMain
from app.utils.query import build_and_query, build_or_exp, get_dict_code
from app.core.error import CustomHTTPException

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