from django import template

register = template.Library()

@register.filter
def select_content(value):
    return value.content