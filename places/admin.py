from django.contrib import admin
from .models import Type
from .models import Ubication
from .models import Place

admin.site.register(Type)

class UbicationAdmin(admin.ModelAdmin):
    list_display = ('city', 'country', 'note', 'link_maps',)
    ordering = ('country',)
    search_fields = ('city', 'country',)
admin.site.register(Ubication, UbicationAdmin)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'ubication', 'note', 'priority', 'visited',)
    ordering = ('name',)
    search_fields = ('name', 'type__name', 'ubication__city',)
    list_filter = ("priority", "visited",)
admin.site.register(Place, PlaceAdmin)
