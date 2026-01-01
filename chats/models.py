from django.db import models
from django.conf import settings
from django.utils import timezone
import pytz

def sa_now():
    return timezone.now().astimezone(pytz.timezone('Asia/Riyadh'))


class Chat(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="sender", on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="receiver", on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=sa_now, editable=False)

    class Meta:
        db_table = 'chats'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.content[:20]}"
    
    @staticmethod
    def get_chat(user1, user2):
        return Chat.objects.filter(
            models.Q(sender=user1, receiver=user2) |
            models.Q(sender=user2, receiver=user1)
        ).order_by('created_at')
