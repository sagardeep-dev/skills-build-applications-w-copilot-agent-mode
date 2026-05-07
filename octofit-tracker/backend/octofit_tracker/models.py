from djongo import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams')
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} - {self.activity_type}"

class Leaderboard(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.team}: {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
