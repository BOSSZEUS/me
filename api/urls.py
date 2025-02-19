from django.urls import path, include  # Import Django's URL handling modules
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView  # Import JWT authentication views
from .views import CreateUserView, PersonViewSet, SkillViewSet, QualityViewSet, GoalViewSet, TaskViewSet  # Import custom views
from rest_framework.routers import DefaultRouter  # Import DefaultRouter for automatic URL routing

# Initialize a DefaultRouter to handle viewset routing
router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='person')  # Register PersonViewSet with a URL prefix 'persons'
router.register(r'skills', SkillViewSet, basename='skill')  # Register SkillViewSet with a URL prefix 'skills'
router.register(r'qualities', QualityViewSet, basename='quality')  # Register QualityViewSet with a URL prefix 'qualities'
router.register(r'goals', GoalViewSet, basename='goal')  # Register GoalViewSet with a URL prefix 'goals'
router.register(r'tasks', TaskViewSet, basename='task')  # Register TaskViewSet with a URL prefix 'tasks'

# Define URL patterns for the API
urlpatterns = [
    path('', include(router.urls)),  # Include all router-generated URLs
    path('register/', CreateUserView.as_view(), name='register'),  # User registration endpoint
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token generation endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh endpoint
]
