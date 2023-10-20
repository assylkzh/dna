from django.http import JsonResponse
from .models import Hot, Cold, Dessert, Snacks
from .serializers import HotDSerializers, ColdDSerializers, DessertSerializers, SnacksSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets


@api_view(['GET', 'POST'])

def hot_list(request):
    if request.method == 'GET':
        hot_drinks = Hot.objects.all()
        serializer1 = HotDSerializers(hot_drinks, many=True)
        return JsonResponse(serializer1.data, safe=False)
    if request.method == 'POST':
        serializer = HotDSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

def cold_list(request):
     if request.method == 'GET':
         cold_drinks = Cold.objects.all()
         serializer2 = ColdDSerializers(cold_drinks, many=True)
         return JsonResponse(serializer2.data, safe=False)
     if request.method == 'POST':
        serializer = ColdDSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

def dessert_list(request):
    if request.method == 'GET':
        desserts = Dessert.objects.all()
        serializer3 = DessertSerializers(desserts, many=True)
        return JsonResponse(serializer3.data, safe=False)
    if request.method == 'POST':
        serializer = DessertSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def snack_list(request):
    if request.method == 'GET':
        snacks = Snacks.objects.all()
        serializer4 = SnacksSerializers(snacks, many=True)
        return JsonResponse(serializer4.data, safe=False)
    if request.method == 'POST':
        serializer = SnacksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def hot_detail(request, id):
    try:
        hot=Hot.objects.get(pk=id)
    except Hot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
       serializer = HotDSerializers(hot)
       return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HotDSerializers(hot, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        hot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def cold_detail(request, id):
    try:
        cold=Cold.objects.get(pk=id)
    except Cold.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = ColdDSerializers(cold)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ColdDSerializers(cold, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cold.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def dessert_detail(request, id):
    try:
        dessert=Dessert.objects.get(pk=id)
    except Dessert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = DessertSerializers(dessert)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DessertSerializers(dessert, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dessert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def snacks_detail(request, id):
    try:
        snacks=Snacks.objects.get(pk=id)
    except Snacks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  

    if request.method == 'GET':
       serializer = SnacksSerializers(snacks)
       return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SnacksSerializers(snacks, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snacks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ColdDApi(viewsets.ModelViewSet):

    queryset = Cold.objects.all()
    serializer_class = ColdDSerializers