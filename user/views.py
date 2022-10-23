from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET', 'POST'])
def test(request:Request):
    print('~' * 30)
    print(request.method, request._request.COOKIES, request.headers)
    print(request.data)
    print(request.user, request.user.is_authenticated)
    print(request.auth, '~~~')
    print('~' * 30)
    if request.auth:
        return Response({'views': 'test'})
