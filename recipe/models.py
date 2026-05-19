from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=50)
    instruction = models.TextField()
    time = models.IntegerField()
    level = models.CharField(max_length=10)
    
# model -> makemigrations -> migration file created -> migrate -> database reflect
# table_name : appname_modelname -> recipe_recipe

    def __str__(self):
        return self.name
