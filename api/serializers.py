from rest_framework import serializers
from .models import Person, Skill, Qualities, Goals, Task

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name']  # Include 'id' field

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency', 'person']

class QualitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualities
        fields = ['id', 'name', 'proficiency', 'description', 'person']

class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = ['id', 'name', 'proficiency', 'description', 'person']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'date_completed', 'person']
