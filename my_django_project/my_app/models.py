from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField(max_length=200, default = "")

    def __str__(self):
        return self.name +" "+ str(self.age)