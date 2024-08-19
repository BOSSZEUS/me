from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PersonViewSet, SkillViewSet, QualityViewSet, GoalViewSet, TaskViewSet

# Initialize the DefaultRouter, which automatically generates the URLs for our viewsets.
router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='person')  # Registers the PersonViewSet
router.register(r'skills', SkillViewSet, basename='skill')  # Registers the SkillViewSet
router.register(r'qualities', QualityViewSet, basename='quality')  # Registers the QualityViewSet
router.register(r'goals', GoalViewSet, basename='goal')  # Registers the GoalViewSet
router.register(r'tasks', TaskViewSet, basename='task')  # Registers the TaskViewSet

# URL patterns for the API and JWT authentication.
urlpatterns = [
    path('', include(router.urls)),  # Includes the router-generated URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh endpoint
]
