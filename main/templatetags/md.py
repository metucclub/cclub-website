from markdown2 import markdown
from django import template

register = template.Library()

@register.filter
def md(value):
    return markdown(value)

