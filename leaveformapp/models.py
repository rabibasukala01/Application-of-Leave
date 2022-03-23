from django.db import models

# Create your models here.


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    roll = models.IntegerField()
    year = models.CharField(max_length=50)
    createdTime = models.CharField(max_length=50)
    createdDate = models.CharField(max_length=50)
    reason = models.TextField()

    def __str__(self):
        return self.fullname
