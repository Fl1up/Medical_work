from django.db import models


class Employee(models.Model):
    name_employee = models.CharField(max_length=100, verbose_name="Сотрудник")

    def __str__(self):
        return f"{self.name_employee}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = 'Сотрудники'


class Warehouse(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название склада")
    assigned_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Закрепленный сотрудник")

    def __str__(self):
        return f"{self.name},{self.assigned_employee}"

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = 'Склады'


class Technique(models.Model):
    inventory_number = models.CharField(max_length=100, verbose_name="Инвентарный номер")
    manufacturer = models.CharField(max_length=100, verbose_name="Производитель")
    country_of_manufacture = models.CharField(max_length=100, verbose_name="Страна производителя")
    price = models.IntegerField(verbose_name="Цена")
    model = models.CharField(max_length=100, verbose_name="Модель техники")

    def __str__(self):
        return f"{self.inventory_number},{self.manufacturer},{self.country_of_manufacture},{self.price},{self.model}"

    class Meta:
        verbose_name = "Техника"


class Stock(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="Название склада")
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, verbose_name="Техника")
    quantity = models.IntegerField(verbose_name="Остаток")

    def __str__(self):
        return f"{self.warehouse},{self.technique},{self.quantity}"

    class Meta:
        verbose_name = "Остаток"
        verbose_name_plural = 'Остатки'
