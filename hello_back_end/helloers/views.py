from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import HelloerProfile
from .serializers import EventSerializer, HellowerProfileSerializer


@api_view(['POST'])
def event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if (request.data['user'] == 'viki' and request.data['pass'] == 'viki') or \
            (request.data['user'] == 'stenly' and request.data['pass'] == 'stenly'):
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profile(request):
        name = request.query_params.get('user')
        user = get_object_or_404(HelloerProfile, name=name)
        serializer = HellowerProfileSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
