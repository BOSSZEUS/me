from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Person, Skill, Quality, Goal, Task
from .serializers import UserSerializer, PersonSerializer, SkillSerializer, QualitySerializer, GoalSerializer, TaskSerializer

# ✅ User Registration API
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()  # Define the queryset to use for this view
    serializer_class = UserSerializer  # Specify the serializer to use
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

# ✅ Base ViewSet to ensure users can only access their own data
class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_queryset(self):
        """
        Ensure that users can only access objects related to their Person.
        """
        if self.queryset is None:
            raise NotImplementedError("Subclasses of BaseViewSet must define a queryset.")

        # Filter the queryset to only include objects related to the authenticated user
        return self.queryset.filter(person__user=self.request.user)

# ✅ Person ViewSet (Users can only see their own Person)
class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer  # Specify the serializer to use
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_queryset(self):
        """
        A user should only be able to access their own Person object.
        """
        # Filter the queryset to only include the Person object related to the authenticated user
        return Person.objects.filter(user=self.request.user)

# ✅ Skill, Quality, Goal, Task ViewSets (Restricted to User's Person)
class SkillViewSet(BaseViewSet):
    queryset = Skill.objects.all()  # Define the queryset to use for this view
    serializer_class = SkillSerializer  # Specify the serializer to use

class QualityViewSet(BaseViewSet):
    queryset = Quality.objects.all()  # Define the queryset to use for this view
    serializer_class = QualitySerializer  # Specify the serializer to use

class GoalViewSet(BaseViewSet):
    queryset = Goal.objects.all()  # Define the queryset to use for this view
    serializer_class = GoalSerializer  # Specify the serializer to use

class TaskViewSet(BaseViewSet):
    queryset = Task.objects.all()  # Define the queryset to use for this view
    serializer_class = TaskSerializer  # Specify the serializer to use