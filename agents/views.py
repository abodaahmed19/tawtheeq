from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from helpers.utils import role_required
from .models import Agent

# Agents
@role_required('admin')
def agents(request):
    agents = Agent.objects.all()

    return render(request, 'agents/index.html', {
        'agents': agents
    })

# Create Agent
@role_required('admin')
def agents_create(request):
    name = request.POST.get('name', '')
    if request.method == 'POST':
        name = request.POST.get('name')

        agent = Agent(name=name)
        agent.save()
        messages.success(request, f"تم إنشاء الوكالة {agent.name} بنجاح")
        return redirect('agents')

    return render(request, 'agents/create.html', {
        'name': name
    })

# Edit Agent
@role_required('admin')
def agents_edit(request, agent_id):
    agent = get_object_or_404(Agent, id=agent_id)

    name = agent.name

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        agent.name = name
        agent.save()

        messages.success(request, f"تم تعديل الوكالة {agent.name} بنجاح")
        return redirect('agents')

    return render(request, 'agents/edit.html', {
        'agent': agent,
        'name': name,
    })
