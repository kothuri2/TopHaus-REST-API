from django.db import models

class User (models.Model):
	time_type = (
        ('D', 'Day'),
        ('M', 'Month'),
        ('Y', 'Year'),
    )
	gender_type = (
    	('Male', 'Male'),
    	('Female', 'Female'),
    	('Other', 'Other'),
    )
	style_type = (
    	('Convertible', 'Convertible'),
    	('Studio', 'Studio'),
    	('Convertible Studio', 'Convertible Studio'),
    	('Alcove Studio', 'Alcove Studio'),
    	('Loft', 'Loft'),
    	('Junior 1-bedroom', 'Junior 1-bedroom'),
    	('Junior 4', 'Junior 4'),
    	('Three-Room', 'Three-Room'),
    	('Two-Bedroom', 'Two-Bedroom'),
    	('Wing Two-Bedroom', 'Wing Two-Bedroom'),
    	('Classic Six', 'Classic Six'),
    	('Duplex or Triplex', 'Duplex or Triplex'),
    	('Garden Apartment', 'Garden Apartment'),
    )
	preferences_type = (
    	('Gym', 'Gym'),
    	('Full Kitchen', 'Full Kitchen'),
    	('TV', 'TV'),
    	('Internet Access', 'Internet Access')
    )
	name = models.CharField(max_length = 40)
	gender = models.CharField(max_length = 10, choices = gender_type)
	budget = models.PositiveIntegerField(default = 0)
	number_of_roommates = models.PositiveIntegerField(default=0)
	style = models.CharField(max_length = 25, choices = style_type)
	location = models.CharField(max_length = 400)
	type_of_time = models.CharField(max_length = 1, choices = time_type)
	length_of_stay = models.PositiveIntegerField()
	preferences = models.CharField(max_length = 200)
	company = models.CharField(max_length = 40)
	avatar = models.ImageField(max_length=None)

	def __str__(self):
		return self.name

class House (models.Model):
	location = models.CharField(max_length = 255)
	exact_cost = models.IntegerField(default = 0)
	number_of_people = models.IntegerField(default = 1)
	style = models.CharField(max_length = 200)
	def __str__(self):
		return self.location

class Amenity(models.Model):
	location = models.CharField(max_length = 255)
	schools = models.CharField(max_length = 255)
	garden_backyard = models.CharField(max_length = 3)
	pool = models.CharField(max_length = 3)
	gym = models.CharField(max_length = 3)
	shopping_mall = models.CharField(max_length = 255)
	houses = models.ManyToManyField(House)
	def __str__(self):
		return self.location