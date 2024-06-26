from django.db import models
import uuid


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True, unique=True)
    score = models.IntegerField(default=0)
    favorite_conversations = models.ManyToManyField("Conversation", related_name="users", blank=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
