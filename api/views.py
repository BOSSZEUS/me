from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Person, Skill, Quality, Goal, Task
from .serializers import PersonSerializer, SkillSerializer, QualitySerializer, GoalSerializer, TaskSerializer

# BaseViewSet provides a common implementation for the 'get_queryset' method.
class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Requires users to be authenticated

    def get_queryset(self):
        # This method customizes the queryset based on the 'person' query parameter.
        person_id = self.request.query_params.get('person')
        if person_id:
            return self.queryset.filter(person_id=person_id)  # Filter by person_id if provided
        return super().get_queryset()  # Return the default queryset otherwise

# ViewSet for the Person model.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()  # Retrieves all Person objects
    serializer_class = PersonSerializer  # Specifies the serializer class
    permission_classes = [IsAdminUser]  # Only admins can access this view

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
