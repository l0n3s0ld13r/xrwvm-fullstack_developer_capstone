from django.contrib import admin
from .models import CarMake, CarModel

class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Fields to display in the list view
    search_fields = ('name', 'description')  # Fields to search in the admin interface

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')  # Fields to display in the list view
    search_fields = ('name', 'car_make__name')  # Fields to search in the admin interface
    list_filter = ('type', 'year')  # Filters to add to the sidebar

# Register the models with the admin site
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
