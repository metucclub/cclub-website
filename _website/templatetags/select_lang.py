from django import template
from django.utils import translation

register = template.Library()

@register.filter
def select_lang(value):
    return value.select_lang(translation.get_language())

@register.filter
def select_lang_all(value):
    lang = translation.get_language()

    for item in value:
        item.select_lang(lang)

    return value
