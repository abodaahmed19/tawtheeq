from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db import models
from .models import Chat

# Chats
User = get_user_model()

@login_required(login_url='login')
def chats(request):
    users = User.objects.exclude(id=request.user.id).order_by('username')
    return render(request, 'chats.html', {"users": users})

# Send Message
@login_required(login_url='login')
@require_POST
def send_message(request):
    import json
    data = json.loads(request.body)
    receiver_id = data.get("receiver_id")
    content = data.get("content", "").strip()

    if not receiver_id or not content:
        return JsonResponse({"error": "Invalid data"}, status=400)

    chat = Chat.objects.create(
        sender=request.user,
        receiver_id=receiver_id,
        content=content
    )

    return JsonResponse({
        "status": "ok",
        "id": chat.id,
        "sender": chat.sender.name,
        "sender_id": chat.sender.id,
        "message": chat.content,
        "time": chat.created_at.strftime("%H:%M") if chat.created_at else ""
    })


# Poll Messages
@login_required(login_url='login')
def poll_messages(request):
    receiver_id = request.GET.get("receiver_id")
    last_id = int(request.GET.get("last_id", 0))

    if not receiver_id:
        return JsonResponse({"error": "receiver_id required"}, status=400)

    receiver_id = int(receiver_id)

    messages = Chat.get_chat(request.user, User.objects.get(id=receiver_id))
    
    messages = [m for m in messages if m.id > last_id]

    data = [{
        "id": m.id,
        "sender": m.sender.name,
        "sender_id": m.sender.id,
        "message": m.content,
        "time": m.created_at.strftime("%H:%M") if m.created_at else ""
    } for m in messages]

    return JsonResponse({"messages": data})
