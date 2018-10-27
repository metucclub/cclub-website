from django import template

register = template.Library()

@register.filter
def iterate_all(value):
    return value.all()