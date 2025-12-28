from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse # for a JSON response
# Create your views here.
@api_view(['GET'])
def checkpoint(request, format = None): # return 'OK' if url pattern is correct
    if request.method == "GET":
        return Response( data = {'status': 'OK user'})
        #for a JSON response, use below
        # return JsonResponse(data = {'status': 'OK user'})