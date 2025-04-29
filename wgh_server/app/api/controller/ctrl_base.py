# coding=utf8

import hashlib

from app.core.config import settings

# 定义wechat_server检验
async def check_wx_server_handler(echo:str, timestamp:str,
    nonce:str, signature:str):
    
    token = settings.WECHAT_TOKEN
    # token,timestamp,nonce进行拼接
    list_obj = [token, timestamp, nonce]
    list_obj.sort()
    list_str = ''.join(list_obj)

    # list_str= ''.join(sorted('{}{}{}'.format(token,timestamp,nonce)))

    # sha1加密
    sha1_obj = hashlib.sha1(list_str.encode('utf-8'))
    hash_code = sha1_obj.hexdigest()

    # 验证请求是否来自微信
    if hash_code == signature:
        return int(echo)
    else:
        return {'result': False}