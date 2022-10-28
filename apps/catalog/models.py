from django.db import models


class Category(models.Model):
    icon = models.CharField(verbose_name='Иконка', max_length=25)
    name = models.CharField(verbose_name='Название', max_length=50)
    slug = models.SlugField(verbose_name='Slug', max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name='Описание', )
    price = models.IntegerField(verbose_name='Цена', )
    image = models.ImageField(verbose_name='Изображениe', upload_to='static/img/dishes/', null=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return f'{self.category.name} --- {self.name}'

# Create your models here.
