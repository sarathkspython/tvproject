from django.contrib import admin
from . models import Place
from .models import Team
# Register your models here.
admin.site.register(Team)
admin.site.register(Place)
