from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from base.models import BaseModel

# Base	UUID, created, modified
# Ingredient	name, calories, food type (protein, starch/base, topping)
# Dish	name, calories, ingredients, vegatarian
# Flavor/Category	name

FOOD_TYPES = (
    ("Protein" : "protein"), 
    ("Base" : "base"),
    ("Topping" : "topping")
    )

SMOKE_LEVEL = (
    ("Light" : "light"),
    ("Medium" : "medium"),
    ("Heavy" : "heavy")
)


class Ingredient(BaseModel):
    name = models.CharField(max_length=100)
    calories = models.IntegerField(MinValueValidator=0, MaxValueValidator=2000)
    type = models.CharField(choices=FOOD_TYPES default="Topping")

    def __str__(self):
        return "Name: {}, Calories: {}".format(self.name, self.calories)

   # Need to add absolute value for detail page for the ingredient


class Dish(BaseModel):
    name = models.CharField(max_length=200)
    calories = models.IntegerField(MinValueValidator=0, MaxValueValidator=2000)
    gluten_free = models.CharField(max_length=3)
    vegatarian = models.CharField(max_length=3)
    dish_ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True, blank=True)
    smokyn = models.CharField(choices=SMOKE_LEVEL default="Topping")

    # Need to add absolute value for detail page for the ingredient
