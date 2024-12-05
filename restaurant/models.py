from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField(default='Reservation Success')

    def __str__(self):
        return self.name



class Meal(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='meals')
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.f_name


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField(max_length=100, blank=False)

    def __str__(self):
        return self.email
    
class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(default='0796830208')
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.name




