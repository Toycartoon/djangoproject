from django.db import models

class Data_Model(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text