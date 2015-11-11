from django import template

register = template.Library()

@register.filter(name='state_name')
def state_name(actuator, invert=False):
    if actuator.state or (not actuator.state and invert):
        return actuator.type.on_state_name
    else:
        return actuator.type.off_state_name

@register.filter(name="state_icon")
def state_icon(actuator, invert=False):
    if actuator.state or (not actuator.state and invert):
        return actuator.type.on_state_icon
    else:
        return actuator.type.off_state_icon

@register.filter(name="state_color")
def state_color(actuator, invert=False):
    if actuator.state or (not actuator.state and invert):
        return "green"
    else:
        return "red"
