from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(verbose_name=_("Nombre"), max_length = 100)
    price = models.DecimalField(verbose_name=_("Precio"), max_digits = 6, decimal_places = 2)
    
    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(verbose_name=_("Nombre"), max_length = 50)
    ingredients = models.ManyToManyField('pizzas.Ingredient', verbose_name=_("Ingredientes"), related_name = 'pizzas')
    image = models.ImageField(verbose_name=_("Imagen"), null = True, blank = True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.CharField(verbose_name=_("Comentario"), max_length = 140)
    created = models.DateTimeField(verbose_name=_("Fecha Creación"), auto_now_add = True)
    score = models.IntegerField(verbose_name=_("Puntuación"), default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    pizza = models.ForeignKey(Pizza,verbose_name=_("Pizza"), related_name = 'comments')
    def __str__(self):
        return self.text