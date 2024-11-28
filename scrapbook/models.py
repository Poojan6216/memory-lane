from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL

class Memory(models.Model):
    MEMORY_TYPES = [
        ('photo', 'Photo'),
        ('video', 'Video'),
        ('note', 'Note'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    memory_type = models.CharField(max_length=10, choices=MEMORY_TYPES)
    media_file = models.FileField(upload_to='memories/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='memories')
    #shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shared_memories', blank=True)  # New Field

    def __str__(self):
        return self.title

class SharedAccess(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, related_name='shared_with')
    shared_with = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shared_memories')

    def __str__(self):
        return f"{self.memory.title} shared with {self.shared_with.username}"
