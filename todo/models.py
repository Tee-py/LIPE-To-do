from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    """
    A project table in the database for all longterm projects created
    by a user.
    """
    Title = models.CharField(max_length=30)
    Details = models.TextField()
    Due = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.Title

class Task(models.Model):
    """
    This allows a user to breakdown longterm projects into smaller tasks with durations
    """
    Title = models.CharField(max_length=30)
    Duration = models.CharField(max_length=20)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.Title


class DailyTodo(models.Model):
    """
    A database table for all Daily Todos by the user
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Title = models.CharField(max_length=30)
    Done = models.BooleanField(default=False)
    DateStamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Title