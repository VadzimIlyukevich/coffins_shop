from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class CoffinManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def get_all_coffins(self):
        qs = list(self.get_queryset().annotate().values())
        return qs


class qwerty(models.Model):
    pass


class FormManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def get_all_form(self):
        qs = list(self.get_queryset().annotate().values())
        return qs


class FormOfCoffin(models.Model):
    name_of_form = models.CharField(max_length=255, verbose_name='Название модели')
    slug = models.SlugField(unique=True)
    price = models.PositiveIntegerField(verbose_name='Стоимость')
    material = models.CharField(max_length=255, verbose_name='Материал')
    color_coffin = models.CharField(max_length=255, verbose_name='Цвет дерева')
    image = models.ImageField(upload_to="forms/")

    def __str__(self):
        return self.name_of_form

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"


class Coffin(models.Model):
    category_form_coffin = models.ForeignKey(FormOfCoffin, verbose_name='Модели гробов', on_delete=models.CASCADE)
    coffin_name = models.CharField(max_length=255, verbose_name='Название гроба')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="coffins/")
    coffin_description = models.CharField(max_length=255, verbose_name='Описание гроба')
    package_service = models.CharField(max_length=255, verbose_name='Пакет')

    class Meta:
        verbose_name = "Гроб"
        verbose_name_plural = "Гробы"

    def __str__(self):
        return self.coffin_name


class Request(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField()
    service = models.TextField(max_length=20, verbose_name='Похороны/кремация')
    date_of_funeral = models.DateField(verbose_name='Дата похорон')
    price_of_funeral = models.CharField(max_length=20, verbose_name='Приблизительная сумма расходов')
    about = models.TextField(verbose_name='Коммантарий', blank=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return "{}".format(self.full_name)
