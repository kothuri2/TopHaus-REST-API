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

#GET LISTd
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

