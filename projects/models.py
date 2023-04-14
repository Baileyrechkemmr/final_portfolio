from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    project_image= models.CharField()
    description = models.TextField()

    def __str__(self):
        return self.title