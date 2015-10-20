from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import User, House, Amenity
from snippets.serializers import UserSerializer, HouseSerializer, AmenitySerializer
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.response import Response

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


### VIEWS FOR HOUSES ###
@csrf_exempt
@api_view(['GET'])
def house_list(request, format=None):
    """
    List all Houses
    """
    if request.method == 'GET':
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def new_house(request, format=None):
    """
    Create new house
    """
    if request.method == 'POST':
        serializer = HouseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_house(request, pk):
    """
    Delete existing house
    """
    try:
        house = House.objects.get(pk=pk)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_house(request, pk):
    """
    Update existing house
    """
    try:
        house = House.objects.get(pk=pk)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_house(request, pk):
    """
    Retrieve an existing house
    """
    try:
        house = House.objects.get(pk=pk)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HouseSerializer(amenity)
        return Response(serializer.data)



###USER VIEWS ####

class UserList(generics.ListRetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#GET
class UserDetailRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#DELETE
class UserDetailDestroy(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#POST
class UserDetailCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Upate
class UserDetailUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

###### AMENITIES ####

@csrf_exempt
@api_view(['GET'])
def amenity_list(request, format=None):
    """
    List all Amenities
    """
    if request.method == 'GET':
        amenities = Amenity.objects.all()
        serializer = AmenitySerializer(amenities, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def new_amenity(request, format=None):
    """
    Create new amenity
    """
    if request.method == 'POST':
        serializer = AmenitySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_amenity(request, pk):
    """
    Delete existing amenity
    """
    try:
        amenity = Amenity.objects.get(pk=pk)
    except Amenity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        amenity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_amenity(request, pk):
    """
    Update existing amenity
    """
    try:
        amenity = Amenity.objects.get(pk=pk)
    except Amenity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AmenitySerializer(amenity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_amenity(request, pk):
    """
    Retrieve an existing amenity
    """
    try:
        amenity = Amenity.objects.get(pk=pk)
    except Amenity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AmenitySerializer(amenity)
        return Response(serializer.data)


