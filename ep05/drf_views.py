from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def drf1(request):
    if request.method == 'POST':
        return Response({'message': 'Got some data', 'data': request.data})
    return Response({'message': 'Hello, World'})
