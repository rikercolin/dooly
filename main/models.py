from django.db import models

# Create your models here.
class ToDo(models.Model):
    username = models.CharField(max_length=150)
    todo_name = models.CharField(max_length=200)
    todo_category = models.CharField(max_length=200, default="none")
    todo_details = models.TextField()
    todo_date_published = models.DateField(auto_now_add=False)
    todo_date_due = models.DateField('Due Date')

    def __str__(self):
        name = self.username + ": " + self.todo_name
        return name
    
