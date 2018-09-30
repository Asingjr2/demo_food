import factory 

from .models import BaseModel

class BaseModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseModel
        abstract = True
