from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Skill, Quality, Goal, Task

User = get_user_model()  # Use the custom User model with character_name

# ✅ User Serializer (Handles Registration and User Data)
class UserSerializer(serializers.ModelSerializer):
    character_name = serializers.CharField(required=True)  # Require character name on signup
    password = serializers.CharField(write_only=True)  # Hide password in responses

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'character_name']
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password isn't exposed

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)  # Create user with a character name

# ✅ Base Serializer (For Common Fields)
class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'proficiency', 'user']  # Change `person` to `user`

# ✅ Skill Serializer
class SkillSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Skill  # Uses Skill model

# ✅ Quality Serializer (Includes Description)
class QualitySerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Quality
        fields = BaseSerializer.Meta.fields + ['description']  # Adds description field

# ✅ Goal Serializer (Includes Description)
class GoalSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Goal
        fields = BaseSerializer.Meta.fields + ['description']  # Adds description field

# ✅ Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'date_completed', 'user']  # Change `person` to `user`

