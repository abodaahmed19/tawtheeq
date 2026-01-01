import pandas as pd
from django.db import connection
from .models import Department
from agents.models import Agent

def table_exists(table_name):
    return table_name in connection.introspection.table_names()

def create_initial_data(sender, **kwargs):
    if not table_exists("departments") or not table_exists("agents"):
        return

    file_path = "data/departments.xlsx"

    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print("خطأ في قراءة ملف Excel:", e)
        return

    created = {}

    for _ in range(2):
        for _, row in df.iterrows():
            dept_id = row.get("id")
            name = row.get("name")
            parent_id = row.get("parent_id")
            agent_id = row.get("agent_id")

            if pd.isna(name) or pd.isna(agent_id):
                continue

            name = str(name).strip()

            try:
                agent = Agent.objects.get(id=int(agent_id))
            except (Agent.DoesNotExist, ValueError):
                print(f"Agent ID '{agent_id}' غير موجود، تخطي القسم '{name}'")
                continue

            parent_obj = created.get(int(parent_id)) if not pd.isna(parent_id) else None

            dept, _ = Department.objects.get_or_create(
                name=name,
                agent=agent,
                parent=parent_obj
            )

            created[int(dept_id)] = dept
