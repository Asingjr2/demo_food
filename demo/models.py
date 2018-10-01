from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from base.models import BaseModel

# Base	UUID, created, modified
# Ingredient	name, calories, food type (protein, starch/base, topping)
# Dish	name, calories, ingredients, vegatarian
# Flavor/Category	name

FOOD_TYPES = (
    ("Protein", "protein"), 
    ("Base", "base"),
    ("Topping","topping")
    )

SMOKE_LEVEL = (
    ("Light", "light"),
    ("Medium", "medium"),
    ("Heavy", "heavy")
)


class Ingredient(BaseModel):
    name = models.CharField(max_length=100)
    calories = models.IntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(2000)])
    protein = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    fat = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    fiber = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    carbs = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    type = models.CharField(max_length=100, choices=FOOD_TYPES, default="Topping")

    def __str__(self):
        return "Name: {}, Calories: {}".format(self.name, self.calories)

   # Need to add absolute value for detail page for the ingredient


class Dish(BaseModel):
    name = models.CharField(max_length=200)
    calories = models.IntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(2000)])
    gluten_free = models.CharField(max_length=3)
    vegatarian = models.CharField(max_length=3)
    dish_ingredients = models.ManyToManyField(Ingredient)
    smokyn = models.CharField(max_length=100, choices=SMOKE_LEVEL, default="Topping")

    # Need to add absolute value for detail page for the ingredient

    def __str__(self):
        return "Name: {}, Calories: {}".format(self.name, self.calories)

    class Meta:
        # Double check syntax on below for plural
        verbose_name = "Dishe"


class Feedback(BaseModel):
    name = models.CharField(max_length=250)
    dish_order = models.CharField(max_length=250)
    feedback = models.CharField(max_length=250, default="Liked everything")
    # could_improve = models.CharField(max_length=250, default="Things need work")

    def __str__(self):
        return "Feedback form submitted by {}".format(self.name)
