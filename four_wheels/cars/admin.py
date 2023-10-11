from django.contrib import admin

from .models import Car, CarModel, Option


class OptionInline(admin.TabularInline):
    model = Car.options.through


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_model', 'year_of_manufacture')
    list_filter = ('price', 'mileage', 'transmission_type',
                   'engine_type', 'number_of_owners')
    inlines = [
        OptionInline
    ]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'option_name',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_name',)
