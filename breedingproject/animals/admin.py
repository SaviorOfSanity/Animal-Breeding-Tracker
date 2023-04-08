from django.contrib import admin
from .models import Animal
from django.contrib.auth.models import Group

admin.site.site_header = 'Valhalla Rose Admin Dashboard'

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['common_name', 'scientific_name', 'sex', 'animal_type', 'morph',]
    list_filter = ['animal_type', 'common_name', ]



admin.site.register(Animal, AnimalAdmin)

admin.site.unregister(Group)
