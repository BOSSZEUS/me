from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):  
    character_name = models.CharField(max_length=100, unique=True)  # In-game character name

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # Unique related_name
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Unique related_name
        blank=True,
    )

    def __str__(self):
        return self.character_name  # Display character name in admin panel

# ✅ Skill Model (Now linked to User instead of Person)
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")  # Link to User
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Rate 1 to 99")

    def __str__(self):
        return self.name

# ✅ Quality Model
class Quality(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="qualities")  # Link to User
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Rate 1 to 99")
    description = models.TextField(help_text="How would you as an individual, use this skill?")

    def __str__(self):
        return self.name

# ✅ Goal Model
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goals")  # Link to User
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Rate 1 to 99")
    description = models.TextField()

    def __str__(self):
        return self.name

# ✅ Task Model
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")  # Link to User
    name = models.CharField(max_length=100)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} completed on {self.date_completed.strftime('%Y-%m-%d %H:%M')}"
