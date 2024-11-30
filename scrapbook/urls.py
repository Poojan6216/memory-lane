from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline, name='timeline'),  # Timeline view
    path('add/', views.add_memory, name='add_memory'),  # Add new memory
    path('<int:memory_id>/', views.memory_detail, name='memory_detail'),  # View memory details
    #path('my-memory/', views.my_memory, name='my_memory'),  # Ensure this exists
    path('my_memories/', views.my_memories, name='my_memory'),
    path('edit/<int:pk>/', views.edit_memory, name='edit_memory'),
    path('delete/<int:pk>/', views.delete_memory, name='delete_memory'),
]
