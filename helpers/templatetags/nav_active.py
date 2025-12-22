from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, names):
    request = context['request']
    current = request.resolver_match.url_name

    name_list = names.split(',')
    return 'active-page' if current in name_list else ''
