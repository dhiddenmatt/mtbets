from django.contrib import admin
from .models import Product, Curso, MatchedBetting, SureBetting, Event

# Register your models here.
myModels = [Product, Curso, MatchedBetting, SureBetting, Event]

for model in myModels:
    admin.site.register(model)