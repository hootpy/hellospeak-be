from django.contrib.postgres.fields import ArrayField
from django.db import models
import uuid


class Conversation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    messages = models.JSONField(default=list)
    topic = ArrayField(models.CharField(max_length=255), default=list)
    level = models.CharField(max_length=255)

    class Meta:
        db_table = "conversation"
