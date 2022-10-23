#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@project : mengma46
@File    : exceptions.py
@Author  : anyu967
@Date    : 2022/10/16 19:23
"""

from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework.response import Response


class MagBaseException(APIException):
    code = 10000    # 0表示成功
    message = "未知异常，请联系管理员"

    @classmethod       # 类方法
    def get_message(cls):
        return {'code': cls.code, 'message': cls.message}


class NotFound(MagBaseException):
    code = 1000
    message = "找不到数据"


class InvalidUsernameOrPassword(MagBaseException):
    code = 1
    message = "用户名或密码错误，请重新登录"


class InvalidToken(MagBaseException):
    code = 5
    message = '登录无效，请重新登录'


exc_map = {
    # 'DRF异常名': 异常类
    # 'DoseNotExist': NotFound
    "InvalidToken": InvalidToken,
    "AuthenticationFailed": InvalidUsernameOrPassword,
}


def global_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response
    response = exception_handler(exc, context)
    print('+' * 30)
    print(type(exc), exc, '##########')
    print(response, '++++++++++++')

    # Now add the HTTP status code to the response
    # if response is not None:
    #     # response.data['status_code'] = response.status_code
    #     message = exc_map.get(exc.__class__.__name__, MagBaseException).get_message()
    #     return Response({'message': '平安无事'})
    if isinstance(exc, MagBaseException):
        message = exc.get_message()
    else:
        message = exc_map.get(exc.__class__.__name__, MagBaseException).get_message()
    # message = exc_map.get(exc.__class__.__name__, MagBaseException).get_message()
    return Response(message, status=200)
