from rest_framework import serializers
from snippets.models import User, House, Amenity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'gender', 'budget', 'number_of_roommates', 'style', 'location',
        			'type_of_time', 'length_of_stay', 'preferences', 'company')

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'location', 'exact_cost', 'number_of_people', 'style')

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('id', 'location', 'schools', 'garden_backyard', 'pool', 'gym', 'shopping_mall', )