from django.http import JsonResponse
from .models import User, Types, Menu, Basket
from .serializers import UserSerializers, TypesSerializers, MenuSerializers, BasketSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.hashers import make_password
from werkzeug.security import generate_password_hash
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAdminUser
from django.shortcuts import render


import bcrypt

# Function to hash a password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Function to verify a password
def verify_password(hashed_password, input_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)


@api_view(['GET', 'POST'])

def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        hashed_password = hash_password('password')
        serializer1 = UserSerializers(user, many=True)
        return JsonResponse(serializer1.data, safe=False)
    if request.method == 'POST':
        request.data['password'] = generate_password_hash(request.data['password'])
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def types_list(request):
     if request.method == 'GET':
         types = Types.objects.all()
         serializer2 = TypesSerializers(types, many=True)
         return JsonResponse(serializer2.data, safe=False)
     if request.method == 'POST':
        serializer = TypesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

def menu_list(request):
    if request.method == 'GET':
        menu = Menu.objects.all()
        serializer3 = MenuSerializers(menu, many=True)
        return JsonResponse(serializer3.data, safe=False)
    if request.method == 'POST':
        serializer = MenuSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def basket_list(request):
    if request.method == 'GET':
        basket = Basket.objects.all()
        serializer4 = BasketSerializers(basket, many=True)
        return JsonResponse(serializer4.data, safe=False)
    if request.method == 'POST':
        serializer = BasketSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def user_detail(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializers(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        new_password = request.data.get('password')
        if new_password:
            user.password = make_password(new_password)

        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def types_detail(request, id):
    try:
        types=Types.objects.get(pk=id)
    except Types.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = TypesSerializers(types)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TypesSerializers(types, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        types.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def menu_detail(request, id):
    try:
        menu=Menu.objects.get(pk=id)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = MenuSerializers(menu)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MenuSerializers(menu, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def basket_detail(request, id):
    try:
        basket=Basket.objects.get(pk=id)
    except Basket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  

    if request.method == 'GET':
       serializer = BasketSerializers(basket)
       return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BasketSerializers(basket, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        basket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserApi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )
    permission_classes = (IsAdminUser, )

class BasketApi (viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )

class MenuApi (viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )

# connection to html
def home(request):
    return render(request, 'index.html')
def menu(request):
    return render(request, 'menu.html')
def register(request):
    return render(request, 'register.html')