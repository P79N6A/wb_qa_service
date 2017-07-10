from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=20)

class AddressBook(models.Model):
    name = models.CharField(max_length=20)
    tel = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    qq=models.CharField(max_length=20)
    group=models.ForeignKey(Group)
