from django.db import models

class User (models.Model):
	time_type = (
        ('D', 'Day'),
        ('M', 'Month'),
        ('Y', 'Year'),
    )
	name = models.CharField(max_length = 40)
	gender = models.CharField(max_length = 20)
	budget = models.IntegerField(default = 0)
	number_of_roommates = models.IntegerField(default=0)
	style = models.CharField(max_length = 200)
	location = models.CharField(max_length = 400)
	type_of_time = models.CharField(max_length = 1, choices = time_type)
	length_of_stay = models.IntegerField()
	preferences = models.CharField(max_length = 50)
	company = models.CharField(max_length = 40)

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