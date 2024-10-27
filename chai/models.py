from django.db import models
from django.utils import timezone


# Create your models here.

class chaivariety(models.Model):         #chaivariety creates structure for database
    CHAI_TYPE_CHOICES = [
        ('ML','MASALA'),
        ('GR','GARLIC') ,
        ('KI','KIWI'),
        ('PL','PLAIN'),
        ('SP','SPICY'),
        ('EL','ELACHI')
    ]

    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now) #date_added
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='PL')
    description = models.TextField(default='no description')
    def __str__(self):
        return self.name