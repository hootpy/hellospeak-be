from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    year = models.IntegerField()

    class Meta:
        db_table = "cars"
