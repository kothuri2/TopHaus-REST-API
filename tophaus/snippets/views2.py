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


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'GET ALL users': 'http://tophaus.herokuapp.com/users/',
        'POST a new user': 'http://tophaus.herokuapp.com/users/newUser/',
        'GET a User': 'http://tophaus.herokuapp.com/users/getUser/[id]',
        'PUT a User': 'http://tophaus.herokuapp.com/users/updateUser/[id]',
        'REMOVE a User': 'http://tophaus.herokuapp.com/users/deleteUser/[id]',
        'GET ALL houses': 'http://tophaus.herokuapp.com/houses/',
        'POST a new house': 'http://tophaus.herokuapp.com/houses/newHouse/',
        'GET a house': 'http://tophaus.herokuapp.com/houses/getHouse/[id]',
        'PUT a house': 'http://tophaus.herokuapp.com/houses/updateHouse/[id]',
        'REMOVE a house': 'http://tophaus.herokuapp.com/houses/deleteHouse/[id]',
        'GET ALL Amenities': 'http://tophaus.herokuapp.com/amenities/',
        'POST a new amenity': 'http://tophaus.herokuapp.com/amenities/newAmenity/',
        'GET a amenity': 'http://tophaus.herokuapp.com/amenities/getAmenity/[id]',
        'PUT a amenity': 'http://tophaus.herokuapp.com/amenities/updateAmenity/[id]',
        'REMOVE a amenity': 'http://tophaus.herokuapp.com/amenities/deleteAmenity/[id]',
    })

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

@csrf_exempt
@api_view(['GET'])
def user_list(request, format=None):
    """
    List all Users
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def new_user(request, format=None):
    """
    Create new User
    """
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, pk):
    """
    Delete existing User
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_user(request, pk):
    """
    Update existing user
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user(request, pk):
    """
    Retrieve an existing user
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

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


