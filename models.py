from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    progress = models.IntegerField()
    image = models.ImageField(upload_to='courses/')

    def __str__(self):
        return self.name