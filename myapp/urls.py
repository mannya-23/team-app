from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TeamMemberViewSet
from .views import team_members_list, add_team_member, edit_team_member

router = DefaultRouter()
router.register(r'teammembers', TeamMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('', team_members_list, name='team_members_list'),
    path('add/', add_team_member, name='add_team_member'),
    path('edit/<int:id>/', edit_team_member, name='edit_team_member'),
    path('delete/<int:id>/', views.delete_team_member, name='delete_team_member'),
]