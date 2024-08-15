from django.utils import timezone
from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Rate your skill 1 to 99")
    person = models.ForeignKey(Person, related_name='skill', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Qualities(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Rate 1 to 99 how much you utilize this skill per day.")
    description = models.CharField(max_length=250, help_text="How would you as an individual, use this skill?")
    person = models.ForeignKey(Person, related_name='qualities', on_delete=models.CASCADE,  null=True)

    def __str__(self):
        return self.name

class Goals(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Rate of completion, 1 to 99")
    description = models.CharField(max_length=250)
    person = models.ForeignKey(Person, related_name='goals', on_delete=models.CASCADE,  null=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    name = models.CharField(max_length=100)
    date_completed =  models.DateTimeField(default= timezone.now)
    person = models.ForeignKey(Person, related_name='task', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} completed on {self.date_completed.strftime('%Y-%m-%d %H:%M')}"
     