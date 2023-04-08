from django.db import models
from django.forms import ImageField
from unicodedata import category

# Create your models here.
CATEGORY = (
    ('Gecko', 'Gecko'),
    ('Frog', 'Frog'),
    ('Fish', 'Fish'),
)

SEX = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unknown', 'Unknown'),
)

class Animal(models.Model):
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    #picture = models.ImageField()
    animal_type = models.CharField(max_length=20, choices=CATEGORY)
    age = models.IntegerField()
    acquire_date = models.DateField()
    cost = models.FloatField()
    sex = models.CharField(max_length=20, choices=SEX)
    mother = models.CharField(max_length=100, null=True)
    father = models.CharField(max_length=100, null=True)
    morph = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Animals'

    def __str__(self):
        return f'{self.common_name}'
