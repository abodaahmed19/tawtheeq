from django import template

register = template.Library()

@register.filter
def initials(value):
    if not value:
        return ""
    parts = value.strip().split()
    if len(parts) == 1:
        return parts[0][0] * 2
    return parts[0][0] + ' ' + parts[-1][0]


