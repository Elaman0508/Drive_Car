from django.db import models


class Car(models.Model):
    price = models.IntegerField(default=0)
    title = models.CharField(max_length=15)
    body = models.CharField(max_length=25)
    engine = models.CharField(max_length=20)
    transmission = models.CharField(max_length=30)
    wheel = models.CharField(max_length=10)
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    volume = models.FloatField(default=0)
    states = models.CharField(max_length=20)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Review(models.Model):
    car = models.ForeignKey(Car, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.name} for {self.car.title}'


class Characteristic(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year_of_manufacture = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/')
    views = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.brand




