from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


# Create your models here.
class Players(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('CB', 'Center-back'),
        ('LB', 'Left-back'),
        ('RB', 'Right-back'),
        ('CM', 'Central Midfielder'),
        ('CDM', 'Defensive Midfielder'),
        ('CAM', 'Attacking Midfielder'),
        ('ST', 'Striker'),
        ('LW', 'Left Winger'),
        ('RW', 'Right Winger'),
    ]
    name = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    family = models.CharField(validators=[MinLengthValidator(3)], max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(80)])
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    img = models.ImageField(upload_to=r'players/images', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.family}'


