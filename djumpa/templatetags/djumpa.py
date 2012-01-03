from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def rank(context):
    counter = loopcounter = context['forloop']['counter']
    if context['is_paginated']:
        current_page    = context['page_obj'].number
        per_page        = context['paginator'].per_page
        counter         = loopcounter + (current_page - 1) * per_page
    return counter