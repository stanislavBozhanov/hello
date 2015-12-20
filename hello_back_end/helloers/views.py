from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .helper import friendship_request
from .models import Helloer,Friendship
from .serializers import EventSerializer, HelloerSerializer, FriendshipSerializer


@api_view(['POST'])
def event(request):
    print(request.data)
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        friendship_request()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if (request.data['user'] == 'Viki' and request.data['pass'] == 'Viki') or \
            (request.data['user'] == 'Stenly' and request.data['pass'] == 'Stenly'):
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def profile(request):
    if request.method == 'GET':
        name = request.query_params.get('user')
        user = get_object_or_404(Helloer, name=name)
        serializer = HelloerSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        name = request.query_params.get('user')
        user = get_object_or_404(Helloer, name=name)
        serializer = HelloerSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def friends(request):
    name = request.query_params.get('user')
    user = get_object_or_404(Helloer, name=name)
    friendships = Friendship.objects.filter(user=user.id).first()
    serializer = FriendshipSerializer(friendships)
    return Response(serializer.data, status=status.HTTP_200_OK)
