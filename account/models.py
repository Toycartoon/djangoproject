from django.db import models

class Data_Model(models.Model):
    uid = models.CharField(max_length=30)
    passwd = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.uid

class Photo(models.Model):
    data = models.ForeignKey(Data_Model, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
