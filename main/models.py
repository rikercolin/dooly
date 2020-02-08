from django.db import models

# Create your models here.
class ToDo(models.Model):
    username = models.CharField(max_length=150)
    label = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default="none")
    details = models.TextField()
    #date_published = models.DateField(auto_now=True)
    #date_due = models.DateField(blank=True, null=True)

    def __str__(self):
        name = self.username + ": " + self.label
        return name

