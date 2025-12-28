from django import template

register = template.Library()

MAP = {
    "admin": "مسؤول",
    "manager": "مدير",
    "company":"شركة",
    "reviewer": "مراجع",
    "user": "مستخدم",

    "contractor": "مقاول",
    "consultant": "إستشاري"
}

@register.filter
def ar(text):
    if not text:
        return ""
    return MAP.get(text.lower(), text)
