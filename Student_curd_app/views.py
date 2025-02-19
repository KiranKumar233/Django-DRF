from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# read

@api_view(['GET'])
def Studentlist(request):
    Studentobj = StudentList.objects.all() # queryset
    serializer=StudentSerializer( Studentobj,many=True)
    return Response(serializer.data)

# Create.
@api_view(['POST'])
def post_Studentlist(request):
    Studentobj = StudentList.objects.all() # queryset
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
         serializer.save()
    return Response(serializer.data)

# update

@api_view(['POST'])
def update_Studentlist(request,id):
    Studentobj = StudentList.objects.get(id=id) # queryset
    serializer=StudentSerializer(instance=Studentobj, data=request.data)
    if serializer.is_valid():
         serializer.save()
    return Response(serializer.data)

# delete

@api_view(['DELETE'])
def delete_Studentlist(request,id):
    Studentobj = StudentList.objects.get(id=id) # queryset
    Studentobj.delete()
    return Response("Student is deleted")
