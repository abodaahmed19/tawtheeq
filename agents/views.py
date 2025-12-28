from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from helpers.utils import role_required
from .models import Agent
from departments.models import Department

# Agents
@role_required('admin')
def agents(request):
    array_agents = Agent.objects.all()

    agents = []

    for agent in array_agents:
        departments_count = Department.objects.filter(agent_id=agent.id).count()
        agents.append([
            agent.id,
            agent.name,
            departments_count
        ])

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
