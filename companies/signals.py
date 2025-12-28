import pandas as pd
from django.db import connection
from datetime import datetime
from .models import Company


def table_exists(table_name):
    return table_name in connection.introspection.table_names()


def safe_int(value):

    if pd.isna(value):
        return None
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def safe_date(value):
    if pd.isna(value):
        return None

    if isinstance(value, pd.Timestamp):
        return value.date()

    if isinstance(value, str):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            return None

    return None


def safe_str(value):
    if pd.isna(value):
        return None
    return str(value)


def create_initial_companies(sender, **kwargs):
    if not table_exists("companies"):
        return

    file_path = "data/companies.xlsx"

    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print("خطأ في قراءة ملف Excel:", e)
        return

    for _, row in df.iterrows():
        Company.objects.get_or_create(
            name=safe_str(row.get("name")),
            defaults={
                "cr_number": safe_int(row.get("cr_number")),
                "cr_expiry": safe_date(row.get("cr_expiry")),
                "phone": safe_str(row.get("phone")),
                "mobile": safe_str(row.get("mobile")),
                "email": safe_str(row.get("email")),
                "website": safe_str(row.get("website")),
                "address": safe_str(row.get("address")),
                "type": safe_str(row.get("type")) or "contractor",
            }
        )
