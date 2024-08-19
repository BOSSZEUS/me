from rest_framework import serializers
from .models import Person, Skill, Quality, Goal, Task

# BaseSerializer defines the common fields for Skill, Quality, and Goal serializers.
class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'proficiency', 'person']  # Common fields

# Serializer for the Person model.
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person  # Specifies the model to be serialized
        fields = ['id', 'name']  # Fields to include in the serialized output

# Serializer for the Skill model.
class SkillSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Skill  # Specifies the model to be serialized

# Serializer for the Quality model.
class QualitySerializer(BaseSerializer):
    # description = serializers.CharField(source='description')
    # Additional field for description

    class Meta(BaseSerializer.Meta):
        model = Quality  # Specifies the model to be serialized
        fields = BaseSerializer.Meta.fields + ['description']  # Adds the description field

# Serializer for the Goal model.
class GoalSerializer(BaseSerializer):
    # description = serializers.CharField(source='description')
    # Additional field for description

    class Meta(BaseSerializer.Meta):
        model = Goal  # Specifies the model to be serialized
        fields = BaseSerializer.Meta.fields + ['description']  # Adds the description field

# Serializer for the Task model.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task  # Specifies the model to be serialized
        fields = ['id', 'name', 'date_completed', 'person']  # Fields to include in the serialized output
