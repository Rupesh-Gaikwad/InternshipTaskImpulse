from django.db import models

# Create your models here.

class StudentTask(models.Model):
    ''' tasks to be performed by students '''
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    email = models.EmailField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
