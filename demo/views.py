from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Ingredient, Dish, Feedback
from .forms import FeedbackForm
from .info import KEY, all_events


class HomeView(TemplateView):
    template_name = "demo/home.html"


class FoodCategoriesView(TemplateView):
    template_name = "demo/food_categories.html"


class EventsHomeView(View):
    def get(self, request):
        locations = all_events
        if "route" not in request.session:
            request.session["origin"] = "Maine" 
            request.session["destination"] = "Chicago"

        embed_url = "https://www.google.com/maps/embed/v1/directions?origin={}&destination={}&key={}".format(request.session["origin"], request.session["destination"], KEY )

        url = "https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&key={}".format(request.session["origin"], request.session["destination"], KEY )

        return render(request, "demo/events.html", {"url":url, "embed_url":embed_url, "locations":locations})

    def post(self, request):
        if "origin" in request.session:
            print("form looks good")
            request.session["origin"] = request.POST["origin"]
            request.session["destination"] = request.POST["destination"]
            request.session["route"] = 1
        if "origin" in request.session:
            print("form does not look good")
        return redirect("/locations")

























class AllIngredientsView(ListView):
    queryset = Ingredient.objects.all()

    def get_queryset(self, *args, **kwargs):
        q_set = Ingredient.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            query = query.lower().capitalize()  # Changed to match DB syntax
            q_set = q_set.filter(
            Q(name__icontains = query) |
            Q(type__icontains = query)  
            )
        return q_set


class FeedbackView(CreateView):
    model = Feedback
    template_name = "demo/feedback_create.html"
    success_url = reverse_lazy("home")
    fields = fields = ["name", "dish_order", "feedback"]

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context["form"] = FeedbackForm()
        return context

    def form(self, form):
        messages.warning(self.request, "Please double check your responses")
        return HttpResponseRedirect(reverse("home"))


