from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline, name='timeline'),  # Timeline view
    path('add/', views.add_memory, name='add_memory'),  # Add new memory
    path('<int:memory_id>/', views.memory_detail, name='memory_detail'),  # View memory details
    path('my-memory/', views.my_memory, name='my_memory'),  # Ensure this exists
]
