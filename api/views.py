from rest_framework import viewsets
from .models import Person, Skill, Qualities, Goals, Task
from .serializers import PersonSerializer, SkillSerializer, QualitiesSerializer, GoalsSerializer, TaskSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        person_id = self.request.query_params.get('person')
        if person_id:
            return Skill.objects.filter(person_id=person_id)
        return super().get_queryset()

class QualitiesViewSet(viewsets.ModelViewSet):
    queryset = Qualities.objects.all()
    serializer_class = QualitiesSerializer
 
    def get_queryset(self):
        person_id = self.request.query_params.get('person')
        if (person_id):
            return Qualities.objects.filter(person_id=person_id)
        return super().get_queryset()

class GoalsViewSet(viewsets.ModelViewSet):
    queryset = Goals.objects.all()
    serializer_class = GoalsSerializer

    def get_queryset(self):
        person_id = self.request.query_params.get('person')
        if (person_id):
            return Goals.objects.filter(person_id=person_id)
        return super().get_queryset()

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        person_id = self.request.query_params.get('person')  
        if person_id:
            return Task.objects.filter(person_id=person_id)
        return super().get_queryset()