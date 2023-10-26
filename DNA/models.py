from django.db import models 


class User (models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

class Types (models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)
    type_description = models.CharField(max_length=200)


class Menu (models.Model):
    item_id = models.AutoField(primary_key=True)
    type_id = models.IntegerField()
    item_name = models.CharField(max_length=50)
    item_description = models.CharField(max_length=200)
    price = models.IntegerField()


class Basket (models.Model):
    basket_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    user_id = models.IntegerField()
    total = models.IntegerField()

   








