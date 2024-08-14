from django.db import models
from django.contrib.auth.models import User

DEFAULT_CHAR_MAX_LEN = 200

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=DEFAULT_CHAR_MAX_LEN)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    purchaseDate = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Curso(models.Model):
    name = models.CharField(max_length=DEFAULT_CHAR_MAX_LEN)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Modulo(models.Model):
    name = models.CharField(max_length=DEFAULT_CHAR_MAX_LEN)
    description = models.TextField(null=True, blank=True)
    videoUrl = models.URLField()
    media = models.FileField(upload_to="")                              # Upload to?

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class MatchedBetting(models.Model):
    availivableUntil = models.DateTimeField()

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class SureBetting(models.Model):
    availivableUntil = models.DateTimeField()

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Event(models.Model):
    name = models.CharField(max_length=DEFAULT_CHAR_MAX_LEN)
    matchedBetting = models.BooleanField()
    casaApuesta = models.CharField(max_length=DEFAULT_CHAR_MAX_LEN)
    date = models.DateTimeField()
    cuota = models.DecimalField(max_digits=6, decimal_places=2)       
    liquidez = models.DecimalField(max_digits=6, decimal_places=2)
    mercado = models.CharField(max_length=DEFAULT_CHAR_MAX_LEN)