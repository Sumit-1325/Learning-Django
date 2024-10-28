from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class chaivariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('GR', 'GARLIC'),
        ('KI', 'KIWI'),
        ('PL', 'PLAIN'),
        ('SP', 'SPICY'),
        ('EL', 'ELACHI')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='PL')
    description = models.TextField(default='no description')
    
    def __str__(self):
        return self.name

# One to Many Relationship
class chaiReview(models.Model):
    chai = models.ForeignKey(chaivariety, on_delete=models.CASCADE,related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.user.username} Review for {self.chai.name}'
    
    #Many To Many Relationship

class store(models.Model):
        name = models.CharField(max_length=100)
        location = models.CharField(max_length=100)
        chai_variety = models.ManyToManyField(chaivariety , related_name="store")

        def __str__(self):
         return self.name


#one to one relationship

class chaicertificate(models.Model):
    certificate = models.OneToOneField(chaivariety, on_delete=models.CASCADE,related_name="certificate")
    certificate_no = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
     return f'{self.chai.name} Certificate {self.certificate_no}'