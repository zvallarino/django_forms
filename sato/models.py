from django.db import models

# Create your models here.
class PeepsHeKnows(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} is a {self.age} year old {self.sex}'