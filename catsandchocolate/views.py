import string
from typing import Any, Callable
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import request


@api_view(['POST'])
def common_gateway(request: request.Request, req_serializer: type[serializers.Serializer], logic: Callable[[Any], str]):
    req = req_serializer(data=request.data)  # type: ignore

    if not req.is_valid():
        return Response(req.errors, status=400)

    param = req.save()
    return HttpResponse(logic(param).translate({ord(c): None for c in string.whitespace}))
