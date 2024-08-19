from django.utils import timezone
from django.db import models

# BaseModel class defines common fields to be used in Skill, Quality, and Goal models.
class BaseModel(models.Model):
    name = models.CharField(max_length=100)  # Common 'name' field
    proficiency = models.IntegerField(help_text="Rate 1 to 99")  # Common 'proficiency' field

    class Meta:
        abstract = True  # This is an abstract model, meaning it won't be created in the database

    def __str__(self):
        return self.name  # Default string representation for objects of models that inherit this class

# Person model defines an individual person with a name.
class Person(models.Model):
    name = models.CharField(max_length=100)  # Person's name field

    def __str__(self):
        return self.name  # String representation of the Person model

# Skill model defines a skill that a person possesses.
class Skill(BaseModel):
    person = models.ForeignKey(Person, related_name='skills', on_delete=models.CASCADE, null=True)
    # ForeignKey relates a skill to a person. If the person is deleted, the skill is also deleted.

# Quality model defines a personal quality or trait.
class Quality(BaseModel):
    description = models.TextField(help_text="How would you as an individual, use this skill?")
    # Description field provides more details on how the quality is utilized.
    person = models.ForeignKey(Person, related_name='qualities', on_delete=models.CASCADE, null=True)
    # ForeignKey relates a quality to a person. If the person is deleted, the quality is also deleted.

# Goal model defines a goal that a person has set.
class Goal(BaseModel):
    description = models.TextField()  # Description field provides details about the goal.
    person = models.ForeignKey(Person, related_name='goals', on_delete=models.CASCADE, null=True)
    # ForeignKey relates a goal to a person. If the person is deleted, the goal is also deleted.

# Task model defines a task that a person has completed.
class Task(models.Model):
    name = models.CharField(max_length=100)  # Task name field
    date_completed = models.DateTimeField(default=timezone.now)  # Timestamp when the task was completed
    person = models.ForeignKey(Person, related_name='tasks', on_delete=models.CASCADE)
    # ForeignKey relates a task to a person. If the person is deleted, the task is also deleted.

    def __str__(self):
        return f"{self.name} completed on {self.date_completed.strftime('%Y-%m-%d %H:%M')}"
        # String representation of the Task model, showing the task name and completion date.
