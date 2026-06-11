from django.db import models

# Create your models here.


class Formdata(models.Model):
    username = models.CharField(max_length=100)
    useremail = models.EmailField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.username
