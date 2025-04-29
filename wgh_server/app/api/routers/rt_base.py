# coding=utf8

from fastapi import APIRouter, Depends, Query
from fastapi.responses import RedirectResponse

from app.core.config import settings

import requests

# 定义路由
base_rt = APIRouter(prefix='/base', tags=['base'])

# 定义wx验证接口
@base_rt.get('/WeChatAuth')

async def getWeChatAuth():

    appid = settings.WECHAT_APPID
    redirect_uri = 'http://wechat.bearman.xyz/base/wechatAuthCallback'
    state = 'test'

    authorize_url = (
        f"https://open.weixin.qq.com/connect/oauth2/authorize?"
        f"appid={appid}&"
        f"redirect_uri={redirect_uri}&"
        f"response_type=code&"
        f"scope=snsapi_base&"
        f"state={state}#wechat_redirect"
    )
    print(authorize_url)

    return RedirectResponse(url=authorize_url)

@base_rt.get('/WeChatAuthCallback')

async def callbackWeChatAuth(code:str=Query(None)):

    token_url = 'https://api.weixin.qq.com/sns/oauth2/access_token'

    print(settings.WECHAT_APPID)
    print(code)
    print(settings.WECHAT_APPSECRET)

    token_res = requests.get(
        token_url,
        params= {
            'appid': settings.WECHAT_APPID,
            'secret': settings.WEChAT_APPSECRET,
            'code': code,
            'grant_type': 'authorization_code'
        }
    )

    token_data = token_res.json()
    openid = token_data.get('openid')

    return {'openid':openid}