from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def media_filter(path):
    if not path:
        return ""
    return f"/media/{path}"