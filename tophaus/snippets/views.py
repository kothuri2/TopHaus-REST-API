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
import django_filters
from rest_framework import filters

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'GET ALL users': 'http://tophaus.herokuapp.com/users/',
        'POST a new user': 'http://tophaus.herokuapp.com/users/newUser/',
        'GET a User': 'http://tophaus.herokuapp.com/users/getUser/[id]',
        'PUT a User': 'http://tophaus.herokuapp.com/users/updateUser/[id]',
        'REMOVE a User': 'http://tophaus.herokuapp.com/users/deleteUser/[id]',
        'GET Compatible Roommates': 'http://tophaus.herokuapp.com/users/getCompatibleRoommates/[id]',
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

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class HouseFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(name="exact_cost", lookup_type='gte')
    max_price = django_filters.NumberFilter(name="exact_cost", lookup_type='lte')
    class Meta:
        model = House
        fields = ['location', 'style', 'min_price', 'max_price']

### VIEWS FOR HOUSES ###
class HouseList(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = HouseFilter

#GET
class HouseDetailRetrieve(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

#DELETE
class HouseDetailDestroy(generics.DestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

#POST
class HouseDetailCreate(generics.CreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

#PUT
class HouseDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


###USER VIEWS ####

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['location', 'gender', 'company', 'number_of_roommates']

#GET LIST
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserFilter

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

#PUT
class UserDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def get_compatible_roommates(request, pk):
    """
    Retrieve compatible roommates
    """
    try:
        base_user = User.objects.get(pk=pk)
        best_roommates = find_roommates(base_user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(best_roommates, many=True)
        return Response(serializer.data)

def find_roommates(base_user):
    #print(base_user.name)
    users = User.objects.all()
    users_len = len(users)
    sorted_users = []
    for user in users:
        count = 0
        if(base_user.name == user.name or base_user.location != user.location):
            count += 0
        else:
            count += 1
        if(base_user.gender == user.gender):
            count += 1
        if(abs(base_user.budget - user.budget) <= 100):
            count += 1
        if(abs(base_user.number_of_roommates - user.number_of_roommates) <= 2):
            count += 1
        if(base_user.style == user.style):
            count += 1
        if(base_user.company == user.company):
            count += 1
        tuple1 = (user, count)
        #print(user.name)
        sorted_users.append(tuple1)
    sorted_users.sort(key=lambda tup: tup[1], reverse=True)
    #sorted(sorted_users, key=lambda user: user[1])   # sort by age
    del sorted_users[0]
    final_users = []
    for user in sorted_users:
        final_users.append(user[0])
    return final_users


####AMENITIES#####
#GET LIST
class AmenityList(generics.ListAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

#GET
class AmenityDetailRetrieve(generics.RetrieveAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

#DELETE
class AmenityDetailDestroy(generics.DestroyAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

#POST
class AmenityDetailCreate(generics.CreateAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

#Update
class AmenityDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer

