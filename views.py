from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FavoriteBook
from .serializers import FavoriteBookSerializer


@api_view(['GET'])
def apiOverview(request):
    api_badic_urls={
        'List':'/Favoritebook-list/',
         'Detail view':'/Favoritebook-details/',
        'Create':'/Favoriebook-create/',
        'Update':'/FavoriteBook-update/<str-pk>/',
        'Delete':'/Favoritebook-delete/<str-pk>/'

    }
    return Response(api_badic_urls)
@api_view(['GET'])
def favoritebookList(request):
    favoritebooks=FavoriteBook.object.all()
    serializer=FavoriteBookSerializer(favoritebooks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def favoritebookDetail(request,pk):
    favoritebooks=FavoriteBook.objects.get(id-pk)
    serializer=FavoriteBookSerializer(favoritebooks,many=False)
    return  Response(serializer.data)
@api_view(['post'])
def favoritebookCreate(request):
    serializer=FavoriteBookSerializer(data=request.data)
    if  serializer.isvalid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def favoritebookUpdate(request,pk):
    favoritebook = FavoriteBook.objects.get(id - pk)
    serializer = FavoriteBookSerializer(instance=favoritebook,data=request.data)
    if serializer.isvalid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def favoritebookUpdate(request,pk):
    favoritebook = FavoriteBook.objects.get(id - pk)
    favoritebook.delete()

    return Response('item succesfully deleted')
