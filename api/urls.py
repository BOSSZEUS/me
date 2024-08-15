from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PersonViewSet, SkillViewSet, QualitiesViewSet, GoalsViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet, basename='person')
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'qualities', QualitiesViewSet, basename='quality')
router.register(r'goals', GoalsViewSet, basename='goal')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),  # Include API routes without a prefix
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain route
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh route
]
