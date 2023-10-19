from django.db import models 

class Hot (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class Cold (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class Dessert (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class Snacks (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
   








