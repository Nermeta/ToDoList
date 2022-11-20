from django.urls import path
from .views import GoalList, GoalCreate


urlpatterns = [
    path("", GoalList.as_view(), name = 'goals'),
    path("goal-create/", GoalCreate.as_view(), name = 'goal-create')
]