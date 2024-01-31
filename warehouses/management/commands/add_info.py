from django.core.management.base import BaseCommand
from warehouses.models import Warehouse, Technique, Stock, Employee
import random
import matplotlib.pyplot as plt
import numpy as np
from django.contrib.auth.models import User

country_manufacturers = ["Германия", "Венгрия", "Россия", "Китай"]
manufacturers = ["Альянс", "Омега", "Альфа", "Каскад", "Вега"]
model = ["v1", "v2", "v4", "a2", "d4", "g5", "h5", "2d"]
name_employee = ["Игорь", "Вася", "Андрей", "Таня", "Антон"]


class Command(BaseCommand):
    def handle(self, *args, **options):
        Warehouse.objects.all().delete()
        Technique.objects.all().delete()
        Stock.objects.all().delete()
        Employee.objects.all().delete()

        for name in name_employee:
            Employee.objects.create(name_employee=name)

        for technique in range(100):
            Technique.objects.create(
                inventory_number=f'ИППЕ № - {technique}',
                manufacturer=f'Производитель - {random.choice(manufacturers)}',
                country_of_manufacture=f'Страна - {random.choice(country_manufacturers)}',
                price=random.randint(10, 1000),
                model=f'Модель - {random.choice(model)}'
            )

        for warehouse in range(5):
            assigned_employee = Employee.objects.order_by('?').first()
            warehouse = Warehouse.objects.create(name=f"Склад №-{warehouse}", assigned_employee=assigned_employee)

            quantity_tech = Technique.objects.all()
            for quantity_technical in quantity_tech:
                quantity = random.randint(0, 100)
                Stock.objects.create(warehouse=warehouse,
                                     technique=quantity_technical,
                                     quantity=quantity)

        warehouse_inventory = {}
        quantity_total = {}
        for warehouse in Warehouse.objects.all():
            inventory = {}
            total = 0
            for stock in Stock.objects.filter(warehouse=warehouse):
                inventory[stock.technique.inventory_number] = stock.quantity
                total += stock.quantity
                quantity_total[stock.technique.inventory_number] = quantity_total.get(stock.technique.inventory_number,
                                                                                      0) + stock.quantity
            warehouse_inventory[warehouse.name] = inventory
            warehouse_inventory[warehouse.name]["Total"] = total

        technique_inventory = sorted(quantity_total.items(), key=lambda x: x[1], reverse=True)
        labels, values = zip(*technique_inventory)
        indexes = np.arange(len(labels))
        plt.bar(indexes, values)
        plt.xticks(indexes, labels, rotation='vertical')
        plt.title('Гистограмма частот общих остатков по единицам техники')

        plt.savefig('histogram.png', bbox_inches='tight')
