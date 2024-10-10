from django.db import models

# Create your models here.

class past_values(models.Model):
    id = models.AutoField(primary_key=True)
    text1 = models.IntegerField()
    text2 = models.IntegerField()
    val = models.IntegerField()
    