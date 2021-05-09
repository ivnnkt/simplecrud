from django.urls import path, include
from rest_framework.routers import SimpleRouter

from main.views import TaskViewSet

router = SimpleRouter()

router.register(r'todo', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
