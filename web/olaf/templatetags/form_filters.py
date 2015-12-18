from django import template

register = template.Library()

@register.filter(name='add_error_class')
def add_error_class(errors):
    if len(errors) > 0:
        return "is-invalid"

@register.filter(name="display_errors")
def display_errors(errors):
    if len(errors) > 0:
        return ", ".join(errors)
