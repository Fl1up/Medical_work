from django.contrib import admin

from warehouses.models import Employee, Warehouse, Technique, Stock

admin.site.register(Employee)


@admin.register(Warehouse)
class Warehouse(admin.ModelAdmin):
    list_display = ("name", "assigned_employee")  # отображение на дисплее
    list_filter = ("name", "assigned_employee")  # фильтр
    search_fields = ("name", "assigned_employee")  # поля поиска


@admin.register(Technique)
class Warehouse(admin.ModelAdmin):
    list_display = (
    "inventory_number", "manufacturer", "country_of_manufacture", "price", "model")  # отображение на дисплее
    list_filter = ("inventory_number", "manufacturer", "country_of_manufacture", "price", "model")  # фильтр
    search_fields = ("inventory_number", "manufacturer", "country_of_manufacture", "price", "model")  # поля поиска


@admin.register(Stock)
class Warehouse(admin.ModelAdmin):
    list_display = ("warehouse", "technique", "quantity")  # отображение на дисплее
    list_filter = ("warehouse", "technique", "quantity")  # фильтр
    search_fields = ("warehouse", "technique", "quantity")  # поля поиска
