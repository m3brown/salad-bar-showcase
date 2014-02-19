from django.db import models

# Create your models here.
class Ingredient(models.Model):
	name = models.CharField(max_length=50)
	serving_size = models.IntegerField(default=0)
	serving_unit = models.CharField(max_length=10)
	calories = models.IntegerField(default=0)
	weight_in_oz = models.DecimalField(max_digits=10, decimal_places=2)
	nutrient_density = models.DecimalField(max_digits=10, decimal_places=2)
