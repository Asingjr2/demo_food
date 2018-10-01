from django.urls import path

from . import views
from .views import HomeView, AllIngredientsView, FeedbackView, FoodCategoriesView, EventsHomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("categories", FoodCategoriesView.as_view(), name="food_categories"),
    path("all_ingredients", AllIngredientsView.as_view(), name="all_ingredients"), 
    path("feedback", FeedbackView.as_view(), name="feedback"),
    path("events", EventsHomeView.as_view(), name="events"),
]

