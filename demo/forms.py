from django import forms
from django.forms import ModelForm

from .models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "dish_order", "feedback"]
        widgets = {
            "name": forms.TextInput(attrs = {
            "maxLength":"100", 
            "class" : "wide"
            }), 
            "dish_order": forms.TextInput(attrs = {
                "placeholder" : "What did you eat",
                "maxLength":"250", 
                "class" : "wide"
            }), 
            "feedback": forms.Textarea(attrs = {
                "placeholder" : "What did you like",
                "maxLength":"250", 
                "class" : "wide"
            }),
        }
