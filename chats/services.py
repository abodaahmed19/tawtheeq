from .models import Chat
from django.db.models import Count

def get_or_create_chat(user1, user2):
    chat = Chat.objects.annotate(
        count=Count("users")
    ).filter(
        users=user1
    ).filter(
        users=user2
    ).filter(
        count=2
    ).first()

    if not chat:
        chat = chat.objects.create()
        chat.users.add(user1, user2)

    return chat
