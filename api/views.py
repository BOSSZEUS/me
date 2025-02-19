from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Skill, Quality, Goal, Task
from .serializers import UserSerializer, SkillSerializer, QualitySerializer, GoalSerializer, TaskSerializer

User = get_user_model()  # Use the custom User model with `character_name`

# ✅ User Registration API
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

# ✅ Base ViewSet to ensure users can only access their own data
class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def get_queryset(self):
        """
        Ensure that users can only access objects related to their own account.
        """
        if self.queryset is None:
            raise NotImplementedError("Subclasses of BaseViewSet must define a queryset.")

        return self.queryset.filter(user=self.request.user)  # Filter by authenticated user

# ✅ Skill, Quality, Goal, Task ViewSets (Restricted to User)
class SkillViewSet(BaseViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class QualityViewSet(BaseViewSet):
    queryset = Quality.objects.all()
    serializer_class = QualitySerializer

class GoalViewSet(BaseViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class TaskViewSet(BaseViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
