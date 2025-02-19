from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import Person, Skill, Quality, Goal, Task
from .serializers import PersonSerializer, SkillSerializer, QualitySerializer, GoalSerializer, TaskSerializer

# API view for user registration
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()  # Define the queryset to retrieve all users
    serializer_class = UserSerializer  # Specify the serializer class to handle user data
    permission_classes = [permissions.AllowAny]  # Allow anyone to register without authentication


    # Base ViewSet class to be inherited by other viewsets.
    # This class ensures that only authenticated users can access the data
    # and restricts the data to the logged-in user's related person.
    class BaseViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAuthenticated]  # Only authenticated users can access the viewset

        def get_queryset(self):
            # Override the get_queryset method to filter the queryset
            # to only include objects related to the logged-in user's person.
            return self.queryset.filter(person__user=self.request.user)

# ViewSet for the Person model.
class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Person.objects.filter(user=self.request.user)  # Only return the logged-in user’s Person

# ViewSet for the Skill model.
class SkillViewSet(BaseViewSet):
    queryset = Skill.objects.all()  # Retrieves all Skill objects
    serializer_class = SkillSerializer  # Specifies the serializer class

# ViewSet for the Quality model.
class QualityViewSet(BaseViewSet):
    queryset = Quality.objects.all()  # Retrieves all Quality objects
    serializer_class = QualitySerializer  # Specifies the serializer class

# ViewSet for the Goal model.
class GoalViewSet(BaseViewSet):
    queryset = Goal.objects.all()  # Retrieves all Goal objects
    serializer_class = GoalSerializer  # Specifies the serializer class

# ViewSet for the Task model.
class TaskViewSet(BaseViewSet):
    queryset = Task.objects.all()  # Retrieves all Task objects
    serializer_class = TaskSerializer  # Specifies the serializer class
