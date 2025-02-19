from django.contrib.auth.models import User  # Import Django's built-in User model for authentication.
from django.utils import timezone  # Import timezone utilities to handle date and time operations.
from django.db import models  # Import Django's ORM (Object-Relational Mapper) for defining database models.

# BaseModel serves as an abstract base class for Skill, Quality, and Goal.
# It contains common fields like 'name' and 'proficiency' to avoid code duplication.
class BaseModel(models.Model):
    name = models.CharField(max_length=100)  # Name of the skill, quality, or goal with a max length of 100 characters.
    proficiency = models.IntegerField(help_text="Rate 1 to 99")  # Integer field representing proficiency level (1-99 scale).

    class Meta:
        abstract = True  # This ensures BaseModel is not created as a table in the database; only inherited by other models.

    def __str__(self):
        return self.name  # Returns the name field as the string representation of the object.

# Person model links a Django User instance to additional personal attributes.
class Person(models.Model):
    user = models.OneToOneField(
        User,  # Links each Person instance to a single User instance.
        on_delete=models.CASCADE,  # Deleting the User will also delete the linked Person instance.
        related_name="person"  # Allows reverse access from User to Person via `user.person`.
    )
    name = models.CharField(max_length=100)  # Name field for the person with a max length of 100 characters.

    def __str__(self):
        return self.name  # Returns the person's name as the string representation.

# Skill model represents a specific skill a person possesses, inheriting from BaseModel.
class Skill(BaseModel):
    person = models.ForeignKey(
        Person,  # Establishes a many-to-one relationship with Person.
        related_name='skills',  # Allows access to a person's skills via `person.skills.all()`.
        on_delete=models.CASCADE  # Deleting a person will also delete their associated skills.
    )

# Quality model represents an individual's trait or characteristic, with an added description field.
class Quality(BaseModel):
    description = models.TextField(help_text="How would you as an individual, use this skill?")  # Detailed explanation of the quality.
    person = models.ForeignKey(
        Person,  # Many-to-one relationship linking qualities to a person.
        related_name='qualities',  # Allows access to a person's qualities via `person.qualities.all()`.
        on_delete=models.CASCADE  # Deleting a person removes all their associated qualities.
    )

# Goal model represents a target or objective a person aims to achieve.
class Goal(BaseModel):
    description = models.TextField()  # Text field for a detailed description of the goal.
    person = models.ForeignKey(
        Person,  # Many-to-one relationship linking goals to a person.
        related_name='goals',  # Allows access to a person's goals via `person.goals.all()`.
        on_delete=models.CASCADE  # Deleting a person removes all their associated goals.
    )

# Task model represents a task assigned to a person, with a completion date.
class Task(models.Model):
    name = models.CharField(max_length=100)  # Name of the task with a max length of 100 characters.
    date_completed = models.DateTimeField(default=timezone.now)  # Stores the date and time the task was completed.
    person = models.ForeignKey(
        Person,  # Many-to-one relationship linking tasks to a person.
        related_name='tasks',  # Allows access to a person's tasks via `person.tasks.all()`.
        on_delete=models.CASCADE  # Deleting a person removes all their associated tasks.
    )

    def __str__(self):
        return f"{self.name} completed on {self.date_completed.strftime('%Y-%m-%d %H:%M')}"  # Returns a formatted string representation of the task.
